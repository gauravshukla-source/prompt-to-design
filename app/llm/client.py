"""
Provider-agnostic LLM client.
Supports:
  - Vertex AI via google.genai / vertexai SDK (Application Default Credentials - ADC)
  - Google Gemini API key (via google.generativeai or google.genai)

Configured via environment variables in .env:
  LLM_PROVIDER=vertex_ai   # or gemini_api
  GOOGLE_CLOUD_PROJECT=architecture-diagram-500204
  GCP_LOCATION=us-central1
  GEMINI_MODEL=gemini-2.5-flash
  GEMINI_API_KEY=...        # only if LLM_PROVIDER=gemini_api
"""
import os
import json
import logging
from typing import Any

logger = logging.getLogger(__name__)

# Models prioritized from newest/most capable down to universal fallbacks
_MODEL_FALLBACKS = [
    "gemini-2.5-flash",
    "gemini-2.0-flash",
    "gemini-1.5-flash",
    "gemini-1.5-pro",
]


def _get_model_name() -> str:
    configured = os.getenv("GEMINI_MODEL", "gemini-2.5-flash").strip()
    if not configured or "3.8" in configured:
        return "gemini-2.5-flash"
    return configured


def _get_provider() -> str:
    return os.getenv("LLM_PROVIDER", "vertex_ai").strip().lower()


def generate_json(prompt: str, schema_hint: str = "") -> dict[str, Any] | list[Any]:
    """
    Call the configured LLM and return parsed JSON.
    Raises RuntimeError on failure.
    """
    provider = _get_provider()
    full_prompt = (
        f"{prompt}\n\n"
        f"{'Schema hint: ' + schema_hint if schema_hint else ''}\n\n"
        "Return ONLY valid JSON. No markdown, no explanation, no code fences."
    )

    if provider == "gemini_api":
        return _call_gemini_api(full_prompt)
    else:
        return _call_vertex(full_prompt)


def _call_vertex(prompt: str) -> dict | list:
    """Call Vertex AI using ADC (Application Default Credentials) with automated model fallback."""
    project = os.getenv("GOOGLE_CLOUD_PROJECT", "").strip()
    location = os.getenv("GCP_LOCATION", "us-central1").strip()
    primary_model = _get_model_name()

    models_to_try = [primary_model] + [m for m in _MODEL_FALLBACKS if m != primary_model]
    errors = []

    # Attempt 1: Try google.genai SDK (new unified SDK)
    try:
        from google import genai
        client = genai.Client(
            vertexai=True,
            project=project or None,
            location=location or "us-central1",
        )
        for model in models_to_try:
            try:
                response = client.models.generate_content(
                    model=model,
                    contents=prompt,
                )
                if response and response.text:
                    logger.info("Vertex AI generation succeeded using model: %s", model)
                    return _parse_json_response(response.text)
            except Exception as exc:
                errors.append(f"google.genai [{model}]: {exc}")
                continue
    except ImportError:
        pass
    except Exception as exc:
        errors.append(f"google.genai init: {exc}")

    # Attempt 2: Try vertexai SDK (google-cloud-aiplatform)
    try:
        import vertexai
        from vertexai.generative_models import GenerativeModel
        vertexai.init(project=project or None, location=location or "us-central1")
        for model in models_to_try:
            try:
                gm = GenerativeModel(model)
                response = gm.generate_content(prompt)
                if response and response.text:
                    logger.info("Vertex AI (vertexai SDK) generation succeeded using model: %s", model)
                    return _parse_json_response(response.text)
            except Exception as exc:
                errors.append(f"vertexai [{model}]: {exc}")
                continue
    except ImportError:
        pass
    except Exception as exc:
        errors.append(f"vertexai init: {exc}")

    # Attempt 3: If API key is present as fallback, try google.generativeai
    api_key = os.getenv("GEMINI_API_KEY", "").strip()
    if api_key:
        try:
            return _call_gemini_api(prompt)
        except Exception as exc:
            errors.append(f"api_key fallback: {exc}")

    raise RuntimeError("All Vertex AI model attempts failed: " + "; ".join(errors))


def _call_gemini_api(prompt: str) -> dict | list:
    """Call Google Gemini API using an API key with automated model fallback."""
    api_key = os.getenv("GEMINI_API_KEY", "").strip()
    if not api_key:
        raise RuntimeError("GEMINI_API_KEY not configured in environment")

    primary_model = _get_model_name()
    models_to_try = [primary_model] + [m for m in _MODEL_FALLBACKS if m != primary_model]
    errors = []

    try:
        from google import genai
        client = genai.Client(api_key=api_key)
        for model in models_to_try:
            try:
                response = client.models.generate_content(model=model, contents=prompt)
                if response and response.text:
                    logger.info("Gemini API generation succeeded using model: %s", model)
                    return _parse_json_response(response.text)
            except Exception as exc:
                errors.append(f"genai [{model}]: {exc}")
                continue
    except (ImportError, Exception):
        pass

    import google.generativeai as legacy_genai
    legacy_genai.configure(api_key=api_key)
    for model in models_to_try:
        try:
            gm = legacy_genai.GenerativeModel(model)
            response = gm.generate_content(prompt)
            if response and response.text:
                logger.info("Gemini API (legacy) generation succeeded using model: %s", model)
                return _parse_json_response(response.text)
        except Exception as exc:
            errors.append(f"legacy_genai [{model}]: {exc}")
            continue

    raise RuntimeError("Gemini API calls failed: " + "; ".join(errors))


def _parse_json_response(text: str) -> dict | list:
    """Extract and parse JSON from model response text."""
    text = text.strip()
    # Strip markdown code fences if present
    if "```" in text:
        lines = text.splitlines()
        extracted = []
        inside = False
        for line in lines:
            if line.strip().startswith("```"):
                inside = not inside
                continue
            if inside:
                extracted.append(line)
        if extracted:
            text = "\n".join(extracted).strip()

    # Find first '[' or '{'
    start_bracket = text.find("[")
    start_brace = text.find("{")

    if start_bracket != -1 and (start_brace == -1 or start_bracket < start_brace):
        end_bracket = text.rfind("]")
        if end_bracket != -1:
            text = text[start_bracket : end_bracket + 1]
    elif start_brace != -1:
        end_brace = text.rfind("}")
        if end_brace != -1:
            text = text[start_brace : end_brace + 1]

    return json.loads(text)


def is_available() -> bool:
    """Check if LLM is configured and reachable."""
    try:
        generate_json("Reply with: {\"status\": \"ok\"}")
        return True
    except Exception:
        return False

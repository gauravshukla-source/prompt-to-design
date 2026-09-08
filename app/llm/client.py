class LLMClient:
    """Provider-agnostic extension point.

    Keep provider/model selection outside architecture business logic.
    A Vertex AI / Gemini adapter can implement generate_structured() here.
    """

    def generate_structured(self, prompt: str, schema: dict) -> dict:
        raise NotImplementedError(
            "No LLM provider configured. The deterministic foundation and tests "
            "run without an external model."
        )

import { renderGraph } from "./canvas.js";
import { renderValidation } from "./inspector.js";

const prompt = document.getElementById("prompt");
const viewpoint = document.getElementById("viewpoint");
const generate = document.getElementById("generate");
const status = document.getElementById("status");

function errorToMessage(error) {
  if (error instanceof Error) return error.message || "Unexpected error";
  if (typeof error === "string") return error;

  if (error && typeof error === "object") {
    if (typeof error.detail === "string") return error.detail;
    if (typeof error.message === "string") return error.message;

    try {
      return JSON.stringify(error);
    } catch (_) {
      return "Unexpected error object";
    }
  }

  return "Unexpected error";
}

function responseErrorToMessage(data) {
  if (!data) return "Generation failed";

  if (typeof data.detail === "string") return data.detail;
  if (typeof data.message === "string") return data.message;

  if (data.detail && typeof data.detail === "object") {
    try {
      return JSON.stringify(data.detail);
    } catch (_) {
      return "Generation failed";
    }
  }

  try {
    return JSON.stringify(data);
  } catch (_) {
    return "Generation failed";
  }
}

generate.addEventListener("click", async () => {
  const promptText = prompt?.value?.trim();

  if (!promptText) {
    status.textContent = "Please enter an architecture prompt.";
    return;
  }

  generate.disabled = true;
  status.textContent = "Generating...";

  try {
    const payload = {
      prompt: promptText,
      viewpoint: viewpoint?.value || null,
    };

    const response = await fetch("/api/generate", {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify(payload),
    });

    let data;

    try {
      data = await response.json();
    } catch (_) {
      throw new Error(
        `Server returned an invalid response (HTTP ${response.status})`
      );
    }

    if (!response.ok) {
      throw new Error(responseErrorToMessage(data));
    }

    if (!data || typeof data !== "object") {
      throw new Error("Server returned an empty or invalid result.");
    }

    if (!data.graph || typeof data.graph !== "object") {
      throw new Error("Generation result does not contain a graph.");
    }

    console.debug("Architecture generation result:", data);

    try {
      renderGraph(data.graph);
    } catch (renderError) {
      console.error("Graph rendering failed:", renderError, data.graph);
      throw new Error(`Graph rendering failed: ${errorToMessage(renderError)}`);
    }

    try {
      if (typeof renderValidation === "function") {
        renderValidation(data.analysis || {});
      }
    } catch (validationError) {
      console.error(
        "Validation rendering failed:",
        validationError,
        data.analysis
      );

      status.textContent =
        "Architecture generated, but validation display failed.";
      return;
    }

    const validation = data.analysis?.validation;

    status.textContent =
      validation?.valid === false
        ? "Generated with validation issues"
        : "Generated";
  } catch (error) {
    const message = errorToMessage(error);

    console.error("Generation error:", error);

    status.textContent = `Error: ${message}`;
  } finally {
    generate.disabled = false;
  }
});

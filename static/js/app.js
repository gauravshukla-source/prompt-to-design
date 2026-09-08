import { renderGraph } from "./canvas.js";
import { renderValidation } from "./inspector.js";

const prompt = document.getElementById("prompt");
const viewpoint = document.getElementById("viewpoint");
const generate = document.getElementById("generate");
const status = document.getElementById("status");

generate.addEventListener("click", async () => {
  status.textContent = "Generating...";

  try {
    const payload = {
      prompt: prompt.value.trim(),
      viewpoint: viewpoint.value || null,
    };

    const response = await fetch("/api/generate", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify(payload),
    });

    const data = await response.json();

    if (!response.ok) {
      throw new Error(data.detail || "Generation failed");
    }

    renderGraph(data.graph);
    renderValidation(data.analysis);
    status.textContent = data.analysis.validation.valid
      ? "Generated"
      : "Generated with validation issues";
  } catch (error) {
    console.error(error);
    status.textContent = `Error: ${error.message}`;
  }
});

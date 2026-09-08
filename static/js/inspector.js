export function renderValidation(analysis) {
  document.getElementById("validation").textContent =
    JSON.stringify(analysis, null, 2);
}

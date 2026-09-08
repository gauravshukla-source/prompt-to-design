from app.agents.orchestrator import ArchitectureOrchestrator
from app.agents.intent_agent import IntentAgent
from app.agents.extraction_agent import ExtractionAgent
from app.extraction.prompt_coverage import PromptCoverage


def test_web_application_semantically_matches_react_frontend():
    prompt = (
        "Create an architecture for a web application where users access "
        "a React frontend through the internet. The frontend communicates "
        "with a backend API, which stores application data in a PostgreSQL database."
    )
    model, analysis = ArchitectureOrchestrator().generate(prompt)
    assert analysis["validation"]["valid"]
    assert "Web Application" in analysis["extraction"]["matched_concepts"]
    assert "Web Application" not in analysis["extraction"]["missing_concepts"]


def test_database_semantically_matches_postgresql():
    prompt = "Users access a React frontend which calls a backend API and stores data in PostgreSQL database."
    model = ExtractionAgent().extract(prompt, IntentAgent().analyze(prompt))
    coverage = PromptCoverage().evaluate(prompt, model)
    assert "PostgreSQL Database" in coverage.matched


def test_coverage_missing_is_warning_not_generation_blocker():
    prompt = "Create an architecture for users accessing a web application through a backend API and database."
    model, analysis = ArchitectureOrchestrator().generate(prompt)
    assert analysis["validation"]["valid"]

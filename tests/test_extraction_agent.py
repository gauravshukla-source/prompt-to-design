from app.agents.intent_agent import IntentAgent
from app.agents.extraction_agent import ExtractionAgent

def test_web_application_extraction():
    prompt='Create an architecture for a web application where users access a React frontend through the internet. The frontend communicates with a backend API, which stores application data in a PostgreSQL database.'
    model=ExtractionAgent().extract(prompt,IntentAgent().analyze(prompt))
    names={e.name for e in model.elements}
    assert {'Users','React Frontend','Backend API','PostgreSQL Database'} <= names
    assert len(model.relationships) >= 2

def test_microservices_extraction():
    prompt='Create an architecture where a mobile application and web application access backend microservices through an API Gateway. The microservices communicate with a Redis cache and a MongoDB database.'
    model=ExtractionAgent().extract(prompt,IntentAgent().analyze(prompt))
    names={e.name for e in model.elements}
    assert {'Mobile Application','Web Application','API Gateway','Backend Microservices','Redis Cache','MongoDB Database'} <= names
    assert len(model.relationships) >= 5

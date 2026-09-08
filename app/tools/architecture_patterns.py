PATTERNS = {
    "hybrid_cloud": {
        "domains": ["on_premises", "cloud"],
        "layout": "domain_horizontal",
        "required_concepts": ["application", "vpn", "api", "database"],
    },
    "iam": {
        "layout": "layered_vertical",
        "layers": [
            "users",
            "identity_source",
            "identity_provider",
            "iga",
            "target_systems",
        ],
    },
    "microservices": {
        "layout": "layered_horizontal",
        "layers": ["client", "gateway", "services", "data_or_events"],
    },
    "event_driven": {
        "layout": "event_hub",
        "layers": ["producer", "broker", "consumer"],
    },
    "security": {
        "layout": "security_layers",
        "layers": ["user", "control", "application", "data"],
    },
}

def get_pattern(architecture_type: str) -> dict:
    return PATTERNS.get(architecture_type, {"layout": "layered"})

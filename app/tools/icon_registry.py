ICON_REGISTRY = {
    "user": "user.svg",
    "application": "application.svg",
    "api": "api.svg",
    "api_gateway": "api-gateway.svg",
    "database": "database.svg",
    "vpn": "vpn.svg",
    "identity_source": "identity.svg",
    "identity_provider": "identity.svg",
    "iga": "iga.svg",
    "pam": "pam.svg",
    "target_system": "target.svg",
    "service": "service.svg",
    "message_broker": "broker.svg",
    "load_balancer": "load-balancer.svg",
}

def get_icon(element_type: str) -> str:
    return ICON_REGISTRY.get(element_type, "generic.svg")

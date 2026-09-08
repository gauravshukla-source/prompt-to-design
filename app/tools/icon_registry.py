ICON_REGISTRY = {
    "user": "/static/icons/enterprise/user.svg",
    "application": "/static/icons/enterprise/web-application.svg",
    "api": "/static/icons/integration/api.svg",
    "api_gateway": "/static/icons/integration/api.svg",
    "database": "/static/icons/databases/database.svg",
    "vpn": "/static/icons/security/vpn.svg",
    "identity_source": "/static/icons/identity/directory.svg",
    "identity_provider": "/static/icons/identity/identity-provider.svg",
    "iga": "/static/icons/identity/identity-governance.svg",
    "pam": "/static/icons/identity/pam.svg",
    "target_system": "/static/icons/enterprise/external-system.svg",
    "service": "/static/icons/_fallback/generic-service.svg",
    "message_broker": "/static/icons/integration/message-queue.svg",
    "load_balancer": "/static/icons/azure/load-balancer.svg",
    "generic": "/static/icons/_fallback/generic-service.svg",
}

def get_icon(element_type: str) -> str:
    return ICON_REGISTRY.get(element_type, ICON_REGISTRY["generic"])

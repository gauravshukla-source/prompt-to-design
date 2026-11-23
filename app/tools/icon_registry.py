"""
Icon registry — maps element type strings, technology names, and component names to static SVG paths.
Priority: technology match > name match > element type match > fallback.
"""

# Element-type to default icon path
TYPE_ICONS: dict[str, str] = {
    "user": "/static/icons/enterprise/user.svg",
    "application": "/static/icons/enterprise/web-application.svg",
    "api": "/static/icons/integration/api.svg",
    "api_gateway": "/static/icons/integration/api-gateway.svg",
    "database": "/static/icons/databases/database.svg",
    "storage": "/static/icons/databases/data-store.svg",
    "compute": "/static/icons/enterprise/server.svg",
    "vpn": "/static/icons/security/vpn.svg",
    "connectivity": "/static/icons/security/vpn.svg",
    "identity_source": "/static/icons/identity/directory.svg",
    "identity_provider": "/static/icons/identity/identity-provider.svg",
    "iga": "/static/icons/identity/identity-governance.svg",
    "pam": "/static/icons/identity/pam.svg",
    "target_system": "/static/icons/enterprise/external-system.svg",
    "service": "/static/icons/_fallback/generic-service.svg",
    "message_broker": "/static/icons/integration/message-queue.svg",
    "load_balancer": "/static/icons/azure/load-balancer.svg",
    "security": "/static/icons/security/firewall.svg",
    "generic": "/static/icons/_fallback/generic-service.svg",
}

# Technology/Product name (lowercase) to specific branded icon path
TECHNOLOGY_ICONS: dict[str, str] = {
    # Identity & Access Governance
    "saviynt": "/static/icons/identity/saviynt.svg",
    "saviynt iga": "/static/icons/identity/saviynt.svg",
    "entra id": "/static/icons/identity/entra-id.svg",
    "microsoft entra id": "/static/icons/identity/entra-id.svg",
    "microsoft entra": "/static/icons/identity/entra-id.svg",
    "active directory": "/static/icons/identity/active-directory.svg",
    "okta": "/static/icons/identity/okta.svg",
    "cyberark": "/static/icons/identity/cyberark.svg",
    "ping identity": "/static/icons/identity/ping-identity.svg",
    "ldap": "/static/icons/identity/ldap.svg",

    # AWS Cloud
    "amazon rds": "/static/icons/aws/rds.svg",
    "rds": "/static/icons/aws/rds.svg",
    "aurora": "/static/icons/aws/aurora.svg",
    "dynamodb": "/static/icons/aws/dynamodb.svg",
    "s3": "/static/icons/aws/s3.svg",
    "amazon s3": "/static/icons/aws/s3.svg",
    "lambda": "/static/icons/aws/lambda.svg",
    "aws lambda": "/static/icons/aws/lambda.svg",
    "ecs": "/static/icons/aws/ecs.svg",
    "eks": "/static/icons/aws/eks.svg",
    "fargate": "/static/icons/aws/fargate.svg",
    "ec2": "/static/icons/aws/ec2.svg",
    "cloudfront": "/static/icons/aws/cloudfront.svg",
    "aws api gateway": "/static/icons/aws/api-gateway.svg",
    "cognito": "/static/icons/aws/cognito.svg",
    "sns": "/static/icons/aws/sns.svg",
    "sqs": "/static/icons/aws/sqs.svg",
    "eventbridge": "/static/icons/aws/eventbridge.svg",
    "step functions": "/static/icons/aws/step-functions.svg",
    "cloudwatch": "/static/icons/aws/cloudwatch.svg",
    "cloudtrail": "/static/icons/aws/cloudtrail.svg",
    "elasticache": "/static/icons/aws/elasticache.svg",
    "redshift": "/static/icons/aws/redshift.svg",
    "direct connect": "/static/icons/aws/direct-connect.svg",
    "transit gateway": "/static/icons/aws/transit-gateway.svg",

    # Azure Cloud
    "azure sql": "/static/icons/azure/sql-database.svg",
    "azure app service": "/static/icons/azure/app-service.svg",
    "azure functions": "/static/icons/azure/functions.svg",
    "azure kubernetes service": "/static/icons/azure/aks.svg",
    "aks": "/static/icons/azure/aks.svg",
    "azure blob storage": "/static/icons/azure/blob-storage.svg",
    "cosmos db": "/static/icons/azure/cosmos-db.svg",
    "azure service bus": "/static/icons/azure/service-bus.svg",
    "azure event hubs": "/static/icons/azure/event-hubs.svg",
    "azure event grid": "/static/icons/azure/event-grid.svg",
    "azure api management": "/static/icons/azure/api-management.svg",
    "azure load balancer": "/static/icons/azure/load-balancer.svg",
    "azure front door": "/static/icons/azure/front-door.svg",
    "application gateway": "/static/icons/azure/application-gateway.svg",
    "azure key vault": "/static/icons/azure/key-vault.svg",
    "defender for cloud": "/static/icons/azure/defender-for-cloud.svg",
    "azure vm": "/static/icons/azure/virtual-machine.svg",
    "azure container apps": "/static/icons/azure/container-apps.svg",
    "expressroute": "/static/icons/azure/expressroute.svg",
    "logic apps": "/static/icons/azure/logic-apps.svg",

    # Google Cloud
    "cloud run": "/static/icons/gcp/cloud-run.svg",
    "gke": "/static/icons/gcp/gke.svg",
    "cloud sql": "/static/icons/gcp/cloud-sql.svg",
    "bigquery": "/static/icons/gcp/bigquery.svg",
    "cloud storage": "/static/icons/gcp/cloud-storage.svg",
    "pub/sub": "/static/icons/gcp/pubsub.svg",
    "pubsub": "/static/icons/gcp/pubsub.svg",
    "cloud functions": "/static/icons/gcp/cloud-functions.svg",
    "compute engine": "/static/icons/gcp/compute-engine.svg",
    "cloud armor": "/static/icons/gcp/cloud-armor.svg",
    "apigee": "/static/icons/gcp/apigee.svg",
    "cloud kms": "/static/icons/gcp/cloud-kms.svg",
    "spanner": "/static/icons/gcp/spanner.svg",
    "firestore": "/static/icons/gcp/firestore.svg",
    "app engine": "/static/icons/gcp/app-engine.svg",

    # Databases & Caches
    "postgresql": "/static/icons/databases/postgresql.svg",
    "postgres": "/static/icons/databases/postgresql.svg",
    "mysql": "/static/icons/databases/mysql.svg",
    "mongodb": "/static/icons/databases/mongodb.svg",
    "redis": "/static/icons/databases/redis.svg",
    "redis cache": "/static/icons/databases/redis.svg",
    "elasticsearch": "/static/icons/databases/elasticsearch.svg",
    "opensearch": "/static/icons/databases/opensearch.svg",
    "cassandra": "/static/icons/databases/cassandra.svg",
    "neo4j": "/static/icons/databases/neo4j.svg",
    "oracle": "/static/icons/databases/oracle-database.svg",
    "sql server": "/static/icons/databases/sql-server.svg",
    "mariadb": "/static/icons/databases/mariadb.svg",

    # Messaging & Streaming
    "kafka": "/static/icons/integration/kafka.svg",
    "apache kafka": "/static/icons/integration/kafka.svg",
    "rabbitmq": "/static/icons/integration/rabbitmq.svg",
    "ibm mq": "/static/icons/integration/ibm-mq.svg",

    # Infrastructure & Containers
    "kubernetes": "/static/icons/enterprise/kubernetes.svg",
    "k8s": "/static/icons/enterprise/kubernetes.svg",
    "docker": "/static/icons/enterprise/docker.svg",
    "istio": "/static/icons/enterprise/istio.svg",

    # Security & Network
    "waf": "/static/icons/security/waf.svg",
    "firewall": "/static/icons/security/firewall.svg",
    "zero trust": "/static/icons/security/zero-trust.svg",
    "siem": "/static/icons/security/siem.svg",
    "bastion host": "/static/icons/security/bastion-host.svg",
    "vpn": "/static/icons/security/vpn.svg",
}

_FALLBACK = "/static/icons/_fallback/generic-service.svg"


def get_icon(element_type: str, technology: str | None = None, name: str | None = None) -> str:
    """
    Return the best icon path for a given element.
    Priority: technology match > name match > element type match > fallback.
    """
    # 1. Exact technology match
    if technology:
        tech_key = technology.lower().strip()
        if tech_key in TECHNOLOGY_ICONS:
            return TECHNOLOGY_ICONS[tech_key]

    # 2. Match against name (exact or substring)
    if name:
        name_key = name.lower().strip()
        if name_key in TECHNOLOGY_ICONS:
            return TECHNOLOGY_ICONS[name_key]
        for key, path in TECHNOLOGY_ICONS.items():
            if key in name_key:
                return path

    # 3. Fall back to element type
    type_key = (element_type or "generic").lower().strip()
    return TYPE_ICONS.get(type_key, _FALLBACK)

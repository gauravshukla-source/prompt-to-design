// Full-color, brand-accurate icons matching industry-standard architecture diagrams
// (AWS Architecture Center / Azure docs / GCP reference arch style)
const SVG_ICONS = {
    // ── AWS (orange #FF9900) ───────────────────────────────────────────
    'aws-api-gateway': `<svg viewBox="0 0 40 40" xmlns="http://www.w3.org/2000/svg"><rect width="40" height="40" rx="8" fill="#FF9900"/><text x="20" y="22" text-anchor="middle" font-size="9" font-family="Arial" font-weight="bold" fill="white">API GW</text><path d="M9 28 Q20 24 31 28" stroke="white" stroke-width="1.5" fill="none" opacity="0.8"/><path d="M9 12 Q20 8 31 12" stroke="white" stroke-width="1.5" fill="none" opacity="0.8"/></svg>`,
    'aws-rds': `<svg viewBox="0 0 40 40" xmlns="http://www.w3.org/2000/svg"><rect width="40" height="40" rx="8" fill="#3b48cc"/><ellipse cx="20" cy="12" rx="11" ry="4" fill="#7986E7"/><path d="M9 12 v14 c0 2.2 4.9 4 11 4 s11-1.8 11-4 V12" fill="#3b48cc"/><ellipse cx="20" cy="12" rx="11" ry="4" fill="#7986E7"/><path d="M9 19 c0 2.2 4.9 4 11 4 s11-1.8 11-4" stroke="#7986E7" stroke-width="1.2" fill="none"/><text x="20" y="35" text-anchor="middle" font-size="8" font-family="Arial" font-weight="bold" fill="white">RDS</text></svg>`,
    'aws-ecs': `<svg viewBox="0 0 40 40" xmlns="http://www.w3.org/2000/svg"><rect width="40" height="40" rx="8" fill="#FF9900"/><rect x="8" y="9" width="24" height="9" rx="2" fill="white" opacity="0.9"/><rect x="8" y="21" width="24" height="9" rx="2" fill="white" opacity="0.9"/><circle cx="12" cy="13.5" r="1.5" fill="#FF9900"/><circle cx="12" cy="25.5" r="1.5" fill="#FF9900"/><text x="20" y="38" text-anchor="middle" font-size="7" font-family="Arial" font-weight="bold" fill="white">ECS</text></svg>`,
    'aws-s3': `<svg viewBox="0 0 40 40" xmlns="http://www.w3.org/2000/svg"><rect width="40" height="40" rx="8" fill="#3F8624"/><path d="M20 8 L30 14 L30 26 L20 32 L10 26 L10 14 Z" fill="#5DA832" stroke="white" stroke-width="0.5"/><path d="M20 8 L30 14 L20 20 L10 14 Z" fill="#7BC952"/><path d="M20 20 L30 14 L30 26 L20 32 Z" fill="#4A9E2A"/><text x="20" y="38" text-anchor="middle" font-size="9" font-family="Arial" font-weight="bold" fill="white">S3</text></svg>`,
    'aws-lambda': `<svg viewBox="0 0 40 40" xmlns="http://www.w3.org/2000/svg"><rect width="40" height="40" rx="8" fill="#FF9900"/><text x="15" y="30" font-size="26" font-family="Georgia,serif" font-style="italic" font-weight="bold" fill="white">λ</text></svg>`,
    'aws-ec2': `<svg viewBox="0 0 40 40" xmlns="http://www.w3.org/2000/svg"><rect width="40" height="40" rx="8" fill="#FF9900"/><rect x="9" y="9" width="22" height="16" rx="2" fill="white" opacity="0.9"/><rect x="12" y="12" width="16" height="10" rx="1" fill="#FF9900"/><rect x="13" y="27" width="5" height="3" fill="white" opacity="0.8"/><rect x="22" y="27" width="5" height="3" fill="white" opacity="0.8"/><text x="20" y="38" text-anchor="middle" font-size="7" font-family="Arial" font-weight="bold" fill="white">EC2</text></svg>`,
    'aws-alb': `<svg viewBox="0 0 40 40" xmlns="http://www.w3.org/2000/svg"><rect width="40" height="40" rx="8" fill="#8C4FFF"/><circle cx="10" cy="20" r="4" fill="white" opacity="0.9"/><circle cx="30" cy="13" r="3" fill="white" opacity="0.7"/><circle cx="30" cy="27" r="3" fill="white" opacity="0.7"/><line x1="14" y1="19" x2="27" y2="14" stroke="white" stroke-width="2"/><line x1="14" y1="21" x2="27" y2="26" stroke="white" stroke-width="2"/><text x="20" y="38" text-anchor="middle" font-size="7" font-family="Arial" font-weight="bold" fill="white">ALB</text></svg>`,
    'aws-cloudfront': `<svg viewBox="0 0 40 40" xmlns="http://www.w3.org/2000/svg"><rect width="40" height="40" rx="8" fill="#8C4FFF"/><circle cx="20" cy="17" r="9" stroke="white" stroke-width="1.5" fill="none"/><ellipse cx="20" cy="17" rx="4" ry="9" stroke="white" stroke-width="1.2" fill="none"/><line x1="11" y1="17" x2="29" y2="17" stroke="white" stroke-width="1.2"/><text x="20" y="37" text-anchor="middle" font-size="6" font-family="Arial" font-weight="bold" fill="white">CloudFront</text></svg>`,

    // ── Azure (blue #0072C6) ───────────────────────────────────────────
    'azure-sql': `<svg viewBox="0 0 40 40" xmlns="http://www.w3.org/2000/svg"><rect width="40" height="40" rx="8" fill="#0072C6"/><ellipse cx="20" cy="12" rx="11" ry="4" fill="#50A0E0"/><path d="M9 12 v14 c0 2.2 4.9 4 11 4 s11-1.8 11-4 V12" fill="#0072C6"/><ellipse cx="20" cy="12" rx="11" ry="4" fill="#50A0E0"/><path d="M9 19 c0 2.2 4.9 4 11 4 s11-1.8 11-4" stroke="#50A0E0" stroke-width="1.2" fill="none"/><text x="20" y="35" text-anchor="middle" font-size="8" font-family="Arial" font-weight="bold" fill="white">SQL</text></svg>`,
    'azure-app-service': `<svg viewBox="0 0 40 40" xmlns="http://www.w3.org/2000/svg"><rect width="40" height="40" rx="8" fill="#0072C6"/><rect x="8" y="9" width="24" height="16" rx="2" stroke="white" stroke-width="1.5" fill="white" opacity="0.1"/><line x1="14" y1="28" x2="26" y2="28" stroke="white" stroke-width="2"/><line x1="18" y1="25" x2="18" y2="28" stroke="white" stroke-width="2"/><line x1="22" y1="25" x2="22" y2="28" stroke="white" stroke-width="2"/><text x="20" y="37" text-anchor="middle" font-size="5.5" font-family="Arial" font-weight="bold" fill="white">App Service</text></svg>`,
    'azure-vm': `<svg viewBox="0 0 40 40" xmlns="http://www.w3.org/2000/svg"><rect width="40" height="40" rx="8" fill="#0072C6"/><rect x="8" y="9" width="24" height="17" rx="2" stroke="white" stroke-width="1.5" fill="white" opacity="0.1"/><circle cx="13" cy="17" r="3" fill="white" opacity="0.9"/><rect x="18" y="14" width="11" height="2" rx="1" fill="white" opacity="0.7"/><rect x="18" y="18" width="8" height="2" rx="1" fill="white" opacity="0.5"/><text x="20" y="37" text-anchor="middle" font-size="7" font-family="Arial" font-weight="bold" fill="white">Azure VM</text></svg>`,
    'azure-api-management': `<svg viewBox="0 0 40 40" xmlns="http://www.w3.org/2000/svg"><rect width="40" height="40" rx="8" fill="#0072C6"/><path d="M12 20 Q20 12 28 20 Q20 28 12 20 Z" fill="white" opacity="0.2"/><path d="M12 20 Q20 12 28 20 Q20 28 12 20 Z" stroke="white" stroke-width="1.5" fill="none"/><text x="20" y="37" text-anchor="middle" font-size="5.5" font-family="Arial" font-weight="bold" fill="white">API Mgmt</text></svg>`,
    'azure-active-directory': `<svg viewBox="0 0 40 40" xmlns="http://www.w3.org/2000/svg"><rect width="40" height="40" rx="8" fill="#0072C6"/><path d="M20 9 L28 14 L28 22 L20 27 L12 22 L12 14 Z" stroke="white" stroke-width="1.5" fill="white" opacity="0.1"/><circle cx="20" cy="18" r="3.5" fill="white"/><text x="20" y="37" text-anchor="middle" font-size="5.5" font-family="Arial" font-weight="bold" fill="white">Entra ID</text></svg>`,
    'active-directory': `<svg viewBox="0 0 40 40" xmlns="http://www.w3.org/2000/svg"><rect width="40" height="40" rx="8" fill="#0072C6"/><path d="M20 9 L28 14 L28 22 L20 27 L12 22 L12 14 Z" stroke="white" stroke-width="1.5" fill="white" opacity="0.1"/><circle cx="20" cy="16" r="4" fill="white" opacity="0.9"/><path d="M12 27 Q20 23 28 27" stroke="white" stroke-width="1.8" fill="none"/><text x="20" y="37" text-anchor="middle" font-size="5.5" font-family="Arial" font-weight="bold" fill="white">Active Dir</text></svg>`,
    'azure-functions': `<svg viewBox="0 0 40 40" xmlns="http://www.w3.org/2000/svg"><rect width="40" height="40" rx="8" fill="#0072C6"/><text x="18" y="30" font-size="22" font-family="Georgia,serif" font-style="italic" font-weight="bold" fill="white">ƒ</text></svg>`,
    'azure-service-bus': `<svg viewBox="0 0 40 40" xmlns="http://www.w3.org/2000/svg"><rect width="40" height="40" rx="8" fill="#0072C6"/><rect x="9" y="14" width="22" height="12" rx="2" stroke="white" stroke-width="1.5" fill="white" opacity="0.1"/><path d="M15 20 L25 20 M22 17 L25 20 L22 23" stroke="white" stroke-width="1.5" fill="none" stroke-linecap="round"/><text x="20" y="37" text-anchor="middle" font-size="5.5" font-family="Arial" font-weight="bold" fill="white">Service Bus</text></svg>`,

    // ── GCP (Google colors) ────────────────────────────────────────────
    'gcp-cloud-run': `<svg viewBox="0 0 40 40" xmlns="http://www.w3.org/2000/svg"><rect width="40" height="40" rx="8" fill="#4285F4"/><polygon points="20,9 30,15 30,25 20,31 10,25 10,15" stroke="white" stroke-width="1.5" fill="white" opacity="0.15"/><text x="20" y="23" text-anchor="middle" font-size="9" font-family="Arial" font-weight="bold" fill="white">CR</text><text x="20" y="37" text-anchor="middle" font-size="5.5" font-family="Arial" font-weight="bold" fill="white">Cloud Run</text></svg>`,
    'gcp-gcs': `<svg viewBox="0 0 40 40" xmlns="http://www.w3.org/2000/svg"><rect width="40" height="40" rx="8" fill="#1a73e8"/><path d="M20 9 L30 14 L20 19 L10 14 Z" fill="#FBBC04"/><path d="M10 14 L10 26 L20 31 L20 19 Z" fill="#34A853"/><path d="M20 19 L20 31 L30 26 L30 14 Z" fill="#EA4335" opacity="0.85"/><text x="20" y="38" text-anchor="middle" font-size="7" font-family="Arial" font-weight="bold" fill="white">GCS</text></svg>`,
    'gcp-bigquery': `<svg viewBox="0 0 40 40" xmlns="http://www.w3.org/2000/svg"><rect width="40" height="40" rx="8" fill="#4285F4"/><circle cx="19" cy="17" r="8" stroke="white" stroke-width="1.5" fill="white" opacity="0.1"/><path d="M25 23 L29 27" stroke="white" stroke-width="2.5" stroke-linecap="round"/><text x="20" y="37" text-anchor="middle" font-size="5.5" font-family="Arial" font-weight="bold" fill="white">BigQuery</text></svg>`,
    'gcp-pubsub': `<svg viewBox="0 0 40 40" xmlns="http://www.w3.org/2000/svg"><rect width="40" height="40" rx="8" fill="#EA4335"/><circle cx="20" cy="16" r="5" fill="white" opacity="0.9"/><circle cx="10" cy="25" r="3" fill="white" opacity="0.7"/><circle cx="30" cy="25" r="3" fill="white" opacity="0.7"/><line x1="15" y1="19" x2="12" y2="23" stroke="white" stroke-width="1.5"/><line x1="25" y1="19" x2="28" y2="23" stroke="white" stroke-width="1.5"/><text x="20" y="37" text-anchor="middle" font-size="5.5" font-family="Arial" font-weight="bold" fill="white">Pub/Sub</text></svg>`,

    // ── Identity / IAM ─────────────────────────────────────────────────
    'saviynt-iga': `<svg viewBox="0 0 40 40" xmlns="http://www.w3.org/2000/svg"><rect width="40" height="40" rx="8" fill="#1a56db"/><path d="M20 10 L27 15 L27 23 L20 28 L13 23 L13 15 Z" stroke="white" stroke-width="1.5" fill="white" opacity="0.15"/><circle cx="20" cy="19" r="3.5" fill="white"/><text x="20" y="37" text-anchor="middle" font-size="5.5" font-family="Arial" font-weight="bold" fill="white">Saviynt</text></svg>`,
    'microsoft-graph': `<svg viewBox="0 0 40 40" xmlns="http://www.w3.org/2000/svg"><rect width="40" height="40" rx="8" fill="#0078d4"/><rect x="9" y="9" width="10" height="10" rx="1" fill="#ea3a2f"/><rect x="21" y="9" width="10" height="10" rx="1" fill="#fbb034"/><rect x="9" y="21" width="10" height="10" rx="1" fill="#1aac68"/><rect x="21" y="21" width="10" height="10" rx="1" fill="#0078d4" opacity="0.7"/><text x="20" y="38" text-anchor="middle" font-size="5" font-family="Arial" font-weight="bold" fill="white">MS Graph</text></svg>`,
    'okta': `<svg viewBox="0 0 40 40" xmlns="http://www.w3.org/2000/svg"><rect width="40" height="40" rx="8" fill="#007DC1"/><circle cx="20" cy="18" r="8" stroke="white" stroke-width="2" fill="none"/><circle cx="20" cy="18" r="3" fill="white"/><text x="20" y="37" text-anchor="middle" font-size="8" font-family="Arial" font-weight="bold" fill="white">Okta</text></svg>`,
    'ldap': `<svg viewBox="0 0 40 40" xmlns="http://www.w3.org/2000/svg"><rect width="40" height="40" rx="8" fill="#6d28d9"/><path d="M20 10 L20 19 M20 19 L13 26 M20 19 L27 26" stroke="white" stroke-width="2" stroke-linecap="round"/><circle cx="20" cy="10" r="3" fill="white"/><circle cx="13" cy="26" r="3" fill="white" opacity="0.8"/><circle cx="27" cy="26" r="3" fill="white" opacity="0.8"/><text x="20" y="38" text-anchor="middle" font-size="7" font-family="Arial" font-weight="bold" fill="white">LDAP</text></svg>`,

    // ── Messaging / Integration ────────────────────────────────────────
    'kubernetes': `<svg viewBox="0 0 40 40" xmlns="http://www.w3.org/2000/svg"><rect width="40" height="40" rx="8" fill="#326CE5"/><polygon points="20,9 30,15 30,25 20,31 10,25 10,15" stroke="white" stroke-width="1.5" fill="white" opacity="0.1"/><circle cx="20" cy="20" r="4" fill="white" opacity="0.9"/><line x1="20" y1="9" x2="20" y2="16" stroke="white" stroke-width="1.5"/><line x1="20" y1="24" x2="20" y2="31" stroke="white" stroke-width="1.5"/><line x1="10" y1="15" x2="16" y2="19" stroke="white" stroke-width="1.5"/><line x1="24" y1="21" x2="30" y2="25" stroke="white" stroke-width="1.5"/><line x1="30" y1="15" x2="24" y2="19" stroke="white" stroke-width="1.5"/><line x1="16" y1="21" x2="10" y2="25" stroke="white" stroke-width="1.5"/><text x="20" y="37" text-anchor="middle" font-size="5.5" font-family="Arial" font-weight="bold" fill="white">K8s</text></svg>`,
    'kafka': `<svg viewBox="0 0 40 40" xmlns="http://www.w3.org/2000/svg"><rect width="40" height="40" rx="8" fill="#231F20"/><circle cx="20" cy="16" r="4" fill="white" opacity="0.9"/><circle cx="11" cy="27" r="3" fill="white" opacity="0.7"/><circle cx="29" cy="27" r="3" fill="white" opacity="0.7"/><line x1="17" y1="19" x2="13" y2="25" stroke="white" stroke-width="1.5"/><line x1="23" y1="19" x2="27" y2="25" stroke="white" stroke-width="1.5"/><text x="20" y="38" text-anchor="middle" font-size="7" font-family="Arial" font-weight="bold" fill="white">Kafka</text></svg>`,
    'rabbitmq': `<svg viewBox="0 0 40 40" xmlns="http://www.w3.org/2000/svg"><rect width="40" height="40" rx="8" fill="#FF6600"/><rect x="9" y="12" width="22" height="16" rx="3" stroke="white" stroke-width="1.5" fill="white" opacity="0.1"/><rect x="12" y="16" width="5" height="8" rx="1" fill="white" opacity="0.8"/><rect x="20" y="16" width="5" height="5" rx="1" fill="white" opacity="0.8"/><text x="20" y="37" text-anchor="middle" font-size="5.5" font-family="Arial" font-weight="bold" fill="white">RabbitMQ</text></svg>`,
    'load-balancer': `<svg viewBox="0 0 40 40" xmlns="http://www.w3.org/2000/svg"><rect width="40" height="40" rx="8" fill="#7c3aed"/><circle cx="10" cy="20" r="4" fill="white" opacity="0.9"/><circle cx="30" cy="13" r="3" fill="white" opacity="0.7"/><circle cx="30" cy="27" r="3" fill="white" opacity="0.7"/><line x1="14" y1="19" x2="27" y2="14" stroke="white" stroke-width="1.5"/><line x1="14" y1="21" x2="27" y2="26" stroke="white" stroke-width="1.5"/><text x="20" y="38" text-anchor="middle" font-size="5.5" font-family="Arial" font-weight="bold" fill="white">Load Bal</text></svg>`,

    // ── Generic / Infrastructure ────────────────────────────────────────
    'database': `<svg viewBox="0 0 40 40" xmlns="http://www.w3.org/2000/svg"><rect width="40" height="40" rx="8" fill="#6d28d9"/><ellipse cx="20" cy="12" rx="10" ry="4" fill="#A78BFA"/><path d="M10 12 v16 c0 2.2 4.5 4 10 4 s10-1.8 10-4 V12" fill="#6d28d9"/><ellipse cx="20" cy="12" rx="10" ry="4" fill="#A78BFA"/><path d="M10 20 c0 2.2 4.5 4 10 4 s10-1.8 10-4" stroke="#A78BFA" stroke-width="1.2" fill="none"/><text x="20" y="37" text-anchor="middle" font-size="6" font-family="Arial" font-weight="bold" fill="white">Database</text></svg>`,
    'server': `<svg viewBox="0 0 40 40" xmlns="http://www.w3.org/2000/svg"><rect width="40" height="40" rx="8" fill="#475569"/><rect x="8" y="10" width="24" height="8" rx="2" stroke="white" stroke-width="1.2" fill="white" opacity="0.1"/><rect x="8" y="21" width="24" height="8" rx="2" stroke="white" stroke-width="1.2" fill="white" opacity="0.1"/><circle cx="12" cy="14" r="1.5" fill="#22c55e"/><circle cx="12" cy="25" r="1.5" fill="#22c55e"/><text x="20" y="38" text-anchor="middle" font-size="7" font-family="Arial" font-weight="bold" fill="white">Server</text></svg>`,
    'client': `<svg viewBox="0 0 40 40" xmlns="http://www.w3.org/2000/svg"><rect width="40" height="40" rx="8" fill="#0ea5e9"/><rect x="8" y="9" width="24" height="16" rx="2" stroke="white" stroke-width="1.5" fill="white" opacity="0.1"/><rect x="11" y="12" width="18" height="10" rx="1" fill="white" opacity="0.15"/><line x1="14" y1="28" x2="26" y2="28" stroke="white" stroke-width="2"/><line x1="20" y1="25" x2="20" y2="28" stroke="white" stroke-width="2"/><text x="20" y="38" text-anchor="middle" font-size="7" font-family="Arial" font-weight="bold" fill="white">Client</text></svg>`,
    'user': `<svg viewBox="0 0 40 40" xmlns="http://www.w3.org/2000/svg"><rect width="40" height="40" rx="8" fill="#64748b"/><circle cx="20" cy="13" r="6" fill="white" opacity="0.9"/><path d="M8 31 Q20 24 32 31" stroke="white" stroke-width="2" fill="none"/></svg>`,
    'dns': `<svg viewBox="0 0 40 40" xmlns="http://www.w3.org/2000/svg"><rect width="40" height="40" rx="8" fill="#059669"/><circle cx="20" cy="17" r="9" stroke="white" stroke-width="1.5" fill="none"/><line x1="11" y1="17" x2="29" y2="17" stroke="white" stroke-width="1.2"/><path d="M20 8 Q24 12 24 17 Q24 22 20 26 Q16 22 16 17 Q16 12 20 8" stroke="white" stroke-width="1.2" fill="none"/><text x="20" y="37" text-anchor="middle" font-size="8" font-family="Arial" font-weight="bold" fill="white">DNS</text></svg>`,
    'router': `<svg viewBox="0 0 40 40" xmlns="http://www.w3.org/2000/svg"><rect width="40" height="40" rx="8" fill="#d97706"/><rect x="8" y="16" width="24" height="8" rx="2" stroke="white" stroke-width="1.5" fill="white" opacity="0.1"/><circle cx="14" cy="20" r="2" fill="white" opacity="0.8"/><circle cx="20" cy="20" r="2" fill="white" opacity="0.8"/><circle cx="26" cy="20" r="2" fill="white" opacity="0.8"/><path d="M20 16 L17 10 M20 16 L23 10" stroke="white" stroke-width="1.5" fill="none"/><text x="20" y="37" text-anchor="middle" font-size="7" font-family="Arial" font-weight="bold" fill="white">Router</text></svg>`,
    'firewall': `<svg viewBox="0 0 40 40" xmlns="http://www.w3.org/2000/svg"><rect width="40" height="40" rx="8" fill="#dc2626"/><rect x="8" y="8" width="24" height="24" rx="2" stroke="white" stroke-width="1.5" fill="white" opacity="0.05"/><line x1="20" y1="8" x2="20" y2="32" stroke="white" stroke-width="1.5" opacity="0.5"/><line x1="8" y1="16" x2="32" y2="16" stroke="white" stroke-width="1.5" opacity="0.5"/><line x1="8" y1="24" x2="32" y2="24" stroke="white" stroke-width="1.5" opacity="0.5"/><text x="20" y="38" text-anchor="middle" font-size="6" font-family="Arial" font-weight="bold" fill="white">Firewall</text></svg>`,
    'cog': `<svg viewBox="0 0 40 40" xmlns="http://www.w3.org/2000/svg"><rect width="40" height="40" rx="8" fill="#475569"/><circle cx="20" cy="18" r="5" stroke="white" stroke-width="1.5" fill="white" opacity="0.1"/><circle cx="20" cy="18" r="2.5" fill="white" opacity="0.9"/><path d="M20 9 L20 12 M20 24 L20 27 M9 18 L12 18 M28 18 L31 18 M12.1 11.1 L14.2 13.2 M25.8 22.8 L27.9 24.9 M27.9 11.1 L25.8 13.2 M14.2 22.8 L12.1 24.9" stroke="white" stroke-width="1.5" fill="none" stroke-linecap="round"/><text x="20" y="37" text-anchor="middle" font-size="7" font-family="Arial" font-weight="bold" fill="white">Service</text></svg>`
};

// Convert SVG strings to Data URIs for Cytoscape
function getIconUri(iconName) {
    if (SVG_ICONS[iconName]) {
        return 'data:image/svg+xml;utf8,' + encodeURIComponent(SVG_ICONS[iconName]);
    }
    return null;
}


// State management
let cy = null;
let currentProjectId = "";
let currentDiagramId = "";
let currentVersion = 1;
let customIcons = [];
let officialIcons = [];

// Initialize Page
document.addEventListener("DOMContentLoaded", () => {
    lucide.createIcons();
    initTabs();
    initAuthStatus();
    initCanvas();
    loadProjects();
    loadCustomIcons();
    loadOfficialIcons().then(() => { populateToolbox(); populateInspectorIconSelect(); });
    setupFormListeners();
    setupSelectionListeners();
});

// Tab navigation logic
function initTabs() {
    const tabChat = document.getElementById("tab-chat");
    const tabIcons = document.getElementById("tab-icons");
    const panelChat = document.getElementById("panel-chat");
    const panelIcons = document.getElementById("panel-icons");

    const tabInspector = document.getElementById("tab-inspector");
    const tabToolbox = document.getElementById("tab-toolbox");
    const panelInspector = document.getElementById("panel-inspector");
    const panelToolbox = document.getElementById("panel-toolbox");

    tabChat.addEventListener("click", () => {
        tabChat.classList.add("border-brand-500", "text-white");
        tabChat.classList.remove("border-transparent", "text-slate-400");
        tabIcons.classList.remove("border-brand-500", "text-white");
        tabIcons.classList.add("border-transparent", "text-slate-400");
        panelChat.classList.remove("hidden");
        panelIcons.classList.add("hidden");
    });

    tabIcons.addEventListener("click", () => {
        tabIcons.classList.add("border-brand-500", "text-white");
        tabIcons.classList.remove("border-transparent", "text-slate-400");
        tabChat.classList.remove("border-brand-500", "text-white");
        tabChat.classList.add("border-transparent", "text-slate-400");
        panelIcons.classList.remove("hidden");
        panelChat.classList.add("hidden");
    });

    tabInspector.addEventListener("click", () => {
        tabInspector.classList.add("border-brand-500", "text-white");
        tabInspector.classList.remove("border-transparent", "text-slate-400");
        tabToolbox.classList.remove("border-brand-500", "text-white");
        tabToolbox.classList.add("border-transparent", "text-slate-400");
        panelInspector.classList.remove("hidden");
        panelToolbox.classList.add("hidden");
    });

    tabToolbox.addEventListener("click", () => {
        tabToolbox.classList.add("border-brand-500", "text-white");
        tabToolbox.classList.remove("border-transparent", "text-slate-400");
        tabInspector.classList.remove("border-brand-500", "text-white");
        tabInspector.classList.add("border-transparent", "text-slate-400");
        panelToolbox.classList.remove("hidden");
        panelInspector.classList.add("hidden");
    });
}

// Authentication & ADC status management
async function initAuthStatus() {
    const dot = document.getElementById("auth-status-dot");
    const text = document.getElementById("auth-status-text");
    if (!dot || !text) return;

    try {
        const res = await fetch("/api/auth/status");
        if (res.ok) {
            const data = await res.json();
            if (data.authenticated) {
                dot.className = "w-2 h-2 rounded-full bg-emerald-400";
                text.innerText = `Vertex AI (${data.location})`;
                text.title = `Project: ${data.project} | Mode: ${data.auth_mode}`;
            } else {
                dot.className = "w-2 h-2 rounded-full bg-amber-400";
                text.innerText = "ADC Pending";
                text.title = data.message;
            }
        }
    } catch (e) {
        dot.className = "w-2 h-2 rounded-full bg-rose-400";
        text.innerText = "Auth Error";
    }
}

// Initialize Cytoscape canvas
function initCanvas() {
    cy = cytoscape({
        container: document.getElementById('cy'),
        style: [
            {
                selector: 'node',
                style: {
                    'label': 'data(label)',
                    'color': '#cbd5e1',
                    'font-size': '10px',
                    'font-family': 'Inter, sans-serif',
                    'text-valign': 'bottom',
                    'text-margin-y': '6px',
                    'background-color': '#1c1c1e',
                    'border-width': '2px',
                    'border-color': '#3a3a3c',
                    'width': '56px',
                    'height': '56px',
                    'shape': 'roundrectangle',
                    'background-image': 'data(icon_url)',
                    'background-fit': 'contain',
                    'background-width': '65%',
                    'background-height': '65%',
                    'text-wrap': 'wrap',
                    'text-max-width': '110px',
                    'text-outline-width': 2,
                    'text-outline-color': '#0c0c0e',
                    'transition-property': 'background-color, border-color',
                    'transition-duration': '0.2s'
                }
            },
            {
                selector: 'node:selected',
                style: {
                    'border-color': '#0070f3',
                    'border-width': '3px',
                    'background-color': '#2c2c2e'
                }
            },
            {
                selector: 'node[type="group"]',
                style: {
                    'label': 'data(label)',
                    'text-valign': 'top',
                    'text-halign': 'center',
                    'text-margin-y': '-10px',
                    'background-color': 'rgba(255, 255, 255, 0.02)',
                    'border-style': 'dashed',
                    'border-width': '1.5px',
                    'border-color': '#4a4a4c',
                    'shape': 'roundrectangle',
                    'padding': '24px',
                    'background-image': 'none'
                }
            },
            {
                selector: 'node[type="group"]:selected',
                style: {
                    'border-color': '#0070f3',
                    'border-width': '2px',
                    'background-color': 'rgba(0, 112, 243, 0.05)'
                }
            },
            {
                selector: 'edge',
                style: {
                    'label': 'data(label)',
                    'font-size': '9px',
                    'font-family': 'Inter, sans-serif',
                    'color': '#94a3b8',
                    'width': 2,
                    'line-color': '#4a4a4c',
                    'target-arrow-color': '#4a4a4c',
                    'target-arrow-shape': 'triangle',
                    'curve-style': 'taxi',
                    'taxi-direction': 'rightward',
                    'taxi-turn': '50%',
                    'taxi-turn-min-distance': 28,
                    'taxi-radius': 8,
                    'source-endpoint': 'outside-to-node-or-label',
                    'target-endpoint': 'outside-to-node-or-label',
                    'text-background-opacity': 0.85,
                    'text-background-color': '#0c0c0e',
                    'text-background-padding': '3px',
                    'text-background-shape': 'roundrectangle'
                }
            },
            { selector: 'edge[kind = "async"]', style: { 'line-style': 'dashed', 'line-dash-pattern': [8, 5], 'target-arrow-shape': 'triangle' } },
            { selector: 'edge[kind = "auth"]', style: { 'line-style': 'dotted', 'target-arrow-shape': 'diamond', 'width': 2 } },
            { selector: 'edge[kind = "observability"]', style: { 'line-style': 'dashed', 'line-dash-pattern': [3, 4], 'target-arrow-shape': 'vee' } },
            { selector: 'edge[direction = "bidirectional"]', style: { 'source-arrow-shape': 'triangle' } },
            { selector: 'edge[encrypted = true]', style: { 'line-color': '#2f855a', 'target-arrow-color': '#2f855a' } },
            { selector: 'node[category = "identity"]', style: { 'border-color': '#6b46c1' } },
            { selector: 'node[category = "security"]', style: { 'border-color': '#c53030' } },
            {
                selector: 'edge:selected',
                style: {
                    'line-color': '#0070f3',
                    'target-arrow-color': '#0070f3',
                    'width': 3
                }
            }
        ],
        layout: {
            name: 'preset'
        }
    });

    // Hide/show empty state based on elements
    cy.on('add remove', () => {
        const emptyState = document.getElementById("empty-state");
        if (cy.elements().length > 0) {
            emptyState.classList.add("hidden");
        } else {
            emptyState.classList.remove("hidden");
        }
        updateParentSelectOptions();
    });
}

// Canvas Helpers
function canvasZoomIn() { cy.zoom(cy.zoom() * 1.2); }
function canvasZoomOut() { cy.zoom(cy.zoom() * 0.8); }
function canvasFit() { cy.fit(); }
// Deterministic architecture layout. Avoids compound-node overlap and makes connectivity readable.
function canvasAutoLayout() {
    // Phase 2 semantic layout: stable layers + barycentric ordering to reduce crossings.
    const categoryLayer = { external:0, user:0, client:0, edge:1, network:1, gateway:1,
        security:1, application:2, compute:2, service:2, general:2, integration:3,
        messaging:3, data:4, database:4, storage:4, identity:5, observability:6 };
    const leaves = cy.nodes().filter(n => n.data('type') !== 'group');
    const layerOf = n => {
        const v = Number(n.data('layer'));
        return Number.isFinite(v) ? v : (categoryLayer[n.data('category')] ?? 2);
    };
    const buckets = new Map();
    leaves.forEach(n => { const l = layerOf(n); if (!buckets.has(l)) buckets.set(l, []); buckets.get(l).push(n); });
    const layers = [...buckets.keys()].sort((a,b)=>a-b);
    // Initial deterministic order, then two sweeps based on connected neighbor positions.
    layers.forEach(l => buckets.get(l).sort((a,b)=>String(a.data('label')).localeCompare(String(b.data('label')))));
    for (let pass=0; pass<3; pass++) {
        const index = new Map();
        layers.forEach(l => buckets.get(l).forEach((n,i)=>index.set(n.id(),i)));
        layers.forEach(l => buckets.get(l).sort((a,b) => neighborScore(a,index) - neighborScore(b,index) || String(a.data('label')).localeCompare(String(b.data('label')))));
    }
    const xGap = 265, yGap = 135, baseX = 130, centerY = 330;
    layers.forEach((l, li) => {
        const list = buckets.get(l); const startY = centerY - ((list.length-1)*yGap)/2;
        list.forEach((n,i) => n.position({x: baseX + li*xGap, y: startY+i*yGap}));
    });
    // Compound boundaries automatically wrap children; do not manually move groups.
    cy.nodes('[type = "group"]').forEach(g => {
        g.style({'padding':'38px', 'text-margin-y':'-18px'});
    });
    // Route secondary side dependencies vertically where possible.
    cy.edges().forEach(e => {
        const sL = layerOf(e.source()), tL = layerOf(e.target());
        e.data('sameLayer', sL === tL);
    });
    cy.fit(cy.elements(), 90);
}
function neighborScore(node, index) {
    const neighbors = node.connectedEdges().map(e => e.source().id() === node.id() ? e.target() : e.source())
        .filter(n => n && n.data('type') !== 'group');
    if (!neighbors.length) return Number.MAX_SAFE_INTEGER / 2;
    const scores = neighbors.map(n => index.get(n.id())).filter(v => Number.isFinite(v));
    return scores.length ? scores.reduce((a,b)=>a+b,0)/scores.length : Number.MAX_SAFE_INTEGER/2;
}

// Architecture quality summary for the UI and future API integrations.
function getArchitectureDiagnostics() {
    const nodes = cy.nodes().filter(n => n.data('type') !== 'group');
    const edges = cy.edges();
    const warnings = [];
    if (nodes.length > 20) warnings.push('High node count: consider splitting the architecture into views.');
    const unlabeled = edges.filter(e => !e.data('label')).length;
    if (unlabeled) warnings.push(`${unlabeled} connector(s) have no protocol or flow label.`);
    const dangling = edges.filter(e => !e.source().length || !e.target().length).length;
    if (dangling) warnings.push(`${dangling} dangling connector(s) detected.`);
    return { nodes:nodes.length, edges:edges.length, boundaries:cy.nodes('[type = "group"]').length, warnings };
}

// Project Logic
async function loadProjects() {
    try {
        const res = await fetch("/api/projects");
        const projects = await res.json();
        const selector = document.getElementById("project-selector");
        selector.innerHTML = "";
        
        if (projects.length === 0) {
            // Auto create default project
            const createRes = await fetch("/api/projects", {
                method: "POST",
                headers: { "Content-Type": "application/json" },
                body: JSON.stringify({ name: "My Sandbox" })
            });
            const defaultProj = await createRes.json();
            projects.push(defaultProj);
        }
        
        projects.forEach(p => {
            const opt = document.createElement("option");
            opt.value = p.id;
            opt.textContent = p.name;
            selector.appendChild(opt);
        });
        
        currentProjectId = projects[0].id;
        selector.value = currentProjectId;
        
        selector.addEventListener("change", (e) => {
            currentProjectId = e.target.value;
            loadProjectDiagrams();
        });
        
        loadProjectDiagrams();
    } catch (e) {
        console.error("Error loading projects", e);
    }
}

const btnNewProj = document.getElementById("btn-new-project");
btnNewProj.addEventListener("click", () => {
    document.getElementById("new-project-modal").classList.remove("hidden");
});

function closeNewProjectModal() {
    document.getElementById("new-project-modal").classList.add("hidden");
}

async function createNewProject() {
    const input = document.getElementById("new-project-name");
    const name = input.value.trim();
    if (!name) return;
    
    try {
        const res = await fetch("/api/projects", {
            method: "POST",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify({ name })
        });
        const project = await res.json();
        
        const selector = document.getElementById("project-selector");
        const opt = document.createElement("option");
        opt.value = project.id;
        opt.textContent = project.name;
        selector.appendChild(opt);
        selector.value = project.id;
        currentProjectId = project.id;
        
        closeNewProjectModal();
        input.value = "";
        cy.elements().remove();
        currentDiagramId = "";
        currentVersion = 1;
    } catch (e) {
        console.error("Error creating project", e);
    }
}

async function loadProjectDiagrams() {
    try {
        const res = await fetch(`/api/projects/${currentProjectId}/diagrams`);
        const diagrams = await res.json();
        if (diagrams.length > 0) {
            // Load latest diagram version
            loadDiagram(diagrams[0].id);
        } else {
            cy.elements().remove();
            currentDiagramId = "";
            currentVersion = 1;
        }
    } catch (e) {
        console.error("Error loading diagrams", e);
    }
}

async function loadDiagram(diagramId) {
    try {
        const res = await fetch(`/api/diagrams/${diagramId}`);
        const diagram = await res.json();
        currentDiagramId = diagram.id;
        currentVersion = diagram.version;
        
        renderTopology(diagram.topology_json);
    } catch (e) {
        console.error("Error loading diagram", e);
    }
}

// Convert our DSL schema to Cytoscape format and render
function renderTopology(dsl) {
    cy.elements().remove();
    
    const elements = [];
    
    // Add groups
    if (dsl.groups) {
        dsl.groups.forEach(g => {
            elements.push({
                data: {
                    id: g.id,
                    label: g.label,
                    type: 'group',
                    group_type: g.type,
                    provider: g.provider || 'generic',
                    zone: g.zone || ''
                }
            });
        });
    }
    
    // Add nodes
    if (dsl.nodes) {
        dsl.nodes.forEach(n => {
            let iconUrl = resolveIconUrl(n.data.icon, n.data.provider, n.data.category);
            
            elements.push({
                data: {
                    id: n.id,
                    label: n.data.label,
                    parent: n.parentId || undefined,
                    type: n.type,
                    icon: n.data.icon,
                    icon_url: iconUrl,
                    category: n.data.category,
                    layer: n.data.layer,
                    provider: n.data.provider,
                    description: n.data.description,
                    properties: n.data.properties
                }
            });
        });
    }
    
    // Add edges
    if (dsl.edges) {
        dsl.edges.forEach(e => {
            elements.push({
                data: {
                    id: e.id,
                    source: e.source,
                    target: e.target,
                    label: e.label || (e.data?.protocol || ''),
                    protocol: e.data?.protocol,
                    encrypted: e.data?.encrypted || false,
                    direction: e.data?.direction || 'forward',
                    kind: e.data?.kind || 'sync'
                }
            });
        });
    }
    
    cy.add(elements);
    canvasAutoLayout();
    console.info("Architecture diagnostics", getArchitectureDiagnostics());
}

// Generate topology back to DSL format for storage / refinement
function exportTopologyJSON() {
    const nodes = [];
    const groups = [];
    const edges = [];
    
    cy.nodes().forEach(ele => {
        if (ele.data('type') === 'group') {
            groups.push({
                id: ele.id(),
                label: ele.data('label'),
                type: ele.data('group_type') || 'generic',
                provider: ele.data('provider') || 'generic',
                zone: ele.data('zone') || null
            });
        } else {
            nodes.push({
                id: ele.id(),
                type: ele.data('type') || 'cloudIcon',
                parentId: ele.data('parent') || null,
                data: {
                    label: ele.data('label'),
                    icon: ele.data('icon') || 'server',
                    category: ele.data('category') || 'general',
                    description: ele.data('description') || '',
                    layer: ele.data('layer'),
                    provider: ele.data('provider') || 'generic',
                    properties: ele.data('properties') || {}
                }
            });
        }
    });
    
    cy.edges().forEach(ele => {
        edges.push({
            id: ele.id(),
            source: ele.source().id(),
            target: ele.target().id(),
            label: ele.data('label') || '',
            data: {
                protocol: ele.data('protocol') || '',
                encrypted: ele.data('encrypted') || false,
                direction: ele.data('direction') || 'forward',
                kind: ele.data('kind') || 'sync'
            }
        });
    });
    
    return {
        diagramType: "architecture",
        groups,
        nodes,
        edges
    };
}

// Save diagram to DB
const btnSave = document.getElementById("btn-save");
btnSave.addEventListener("click", async () => {
    if (!currentProjectId) {
        alert("Please create or select a project first.");
        return;
    }
    
    const topology = exportTopologyJSON();
    if (topology.nodes.length === 0 && topology.groups.length === 0) {
        alert("Cannot save an empty diagram.");
        return;
    }
    
    const diagramId = currentDiagramId || Math.random().toString(36).substring(2, 15);
    const payload = {
        id: diagramId,
        project_id: currentProjectId,
        topology_json: topology,
        version: currentVersion
    };
    
    try {
        const res = await fetch("/api/diagrams", {
            method: "POST",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify(payload)
        });
        if (res.ok) {
            currentDiagramId = diagramId;
            alert("Diagram saved successfully!");
        }
    } catch (e) {
        console.error(e);
        alert("Failed to save diagram.");
    }
});

// Custom Icons Ingestion Logic
async function loadOfficialIcons() {
    try {
        const res = await fetch('/api/icon-library');
        if (!res.ok) throw new Error('Icon library unavailable');
        const payload = await res.json();
        officialIcons = payload.icons || [];
        console.info(`Loaded ${officialIcons.length} registered architecture icons`);
    } catch (e) {
        console.warn('Official icon library unavailable; using embedded fallbacks.', e);
        officialIcons = [];
    }
}

function getRegisteredIcon(iconName, provider = null, category = null) {
    const key = String(iconName || '').toLowerCase().replace(/[^a-z0-9]+/g, '-').replace(/^-|-$/g, '');
    return officialIcons.find(i => i.id === key || i.slug === key || (provider && i.provider === provider && i.slug === key))
        || officialIcons.find(i => (i.aliases || []).some(a => String(a).toLowerCase() === String(iconName).toLowerCase()) && (!provider || i.provider === provider))
        || null;
}

function resolveIconUrl(iconName, provider = null, category = null) {
    const registered = getRegisteredIcon(iconName, provider, category);
    if (registered) return registered.assetStatus === 'available' ? registered.path : (registered.fallbackPath || '/static/icons/_fallback/generic-service.svg');
    const embedded = getIconUri(iconName);
    if (embedded) return embedded;
    const custom = customIcons.find(ci => ci.tag === iconName);
    if (custom) return custom.url;
    return '/static/icons/_fallback/generic-service.svg';
}

async function loadCustomIcons() {
    try {
        const res = await fetch("/api/icons");
        customIcons = await res.json();
        renderCustomIconList();
        populateInspectorIconSelect();
    } catch (e) {
        console.error(e);
    }
}

function renderCustomIconList() {
    const list = document.getElementById("icon-list");
    list.innerHTML = "";
    
    if (customIcons.length === 0) {
        list.innerHTML = `<p class="text-xs text-slate-500 text-center py-4">No custom icons uploaded yet.</p>`;
        return;
    }
    
    customIcons.forEach(i => {
        const item = document.createElement("div");
        item.className = "flex items-center justify-between bg-dark-900 border border-dark-50 p-2.5 rounded-lg";
        item.innerHTML = `
            <div class="flex items-center gap-2">
                <img src="${i.url}" class="w-8 h-8 object-contain bg-dark-100 p-1.5 rounded" />
                <div>
                    <div class="text-xs font-bold text-white">${i.tag}</div>
                    <div class="text-[9px] text-slate-400">${i.description}</div>
                </div>
            </div>
            <button onclick="deleteCustomIcon('${i.id}')" class="p-1 hover:bg-red-500/10 rounded text-red-500 hover:text-red-400 transition-colors">
                <i data-lucide="trash-2" class="w-4 h-4"></i>
            </button>
        `;
        list.appendChild(item);
    });
    lucide.createIcons();
}

async function deleteCustomIcon(iconId) {
    if (!confirm("Are you sure you want to delete this custom icon?")) return;
    try {
        const res = await fetch(`/api/icons/${iconId}`, { method: "DELETE" });
        if (res.ok) {
            loadCustomIcons();
        }
    } catch (e) {
        console.error(e);
    }
}

// Generate & Refine Agent Integration
const btnGen = document.getElementById("btn-generate");
const promptInput = document.getElementById("prompt-input");
const loader = document.getElementById("loader");

btnGen.addEventListener("click", async () => {
    const prompt = promptInput.value.trim();
    if (!prompt) return;
    
    loader.classList.remove("hidden");
    
    const isNew = cy.elements().length === 0;
    const url = isNew ? "/api/generate" : "/api/refine";
    const payload = isNew ? { prompt } : { prompt, current_diagram: exportTopologyJSON() };
    
    // Add user message to log
    appendChatMessage(prompt, "user");
    promptInput.value = "";
    
    try {
        const res = await fetch(url, {
            method: "POST",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify(payload)
        });
        
        if (res.ok) {
            const data = await res.json();
            renderTopology(data);
            appendChatMessage("I have generated/refined the diagram matching your instructions. Let me know if you need any further modifications!", "bot");
            if (!isNew) {
                currentVersion += 1;
            }
        } else {
            const err = await res.json();
            appendChatMessage(`Error: ${err.detail || 'Failed to design diagram'}`, "bot");
        }
    } catch (e) {
        console.error(e);
        appendChatMessage("Network error occurred while calling the architect agent.", "bot");
    } finally {
        loader.classList.add("hidden");
    }
});

function appendChatMessage(text, sender) {
    const list = document.getElementById("chat-messages");
    const item = document.createElement("div");
    
    if (sender === "user") {
        item.className = "bg-brand-500/10 border border-brand-500/20 rounded-xl p-3.5 text-xs text-slate-300 ml-8";
        item.innerHTML = `
            <div class="flex items-center gap-2 mb-1">
                <span class="font-semibold text-white">You</span>
            </div>
            <p class="leading-relaxed">${text}</p>
        `;
    } else {
        item.className = "bg-dark-100/50 border border-dark-50 rounded-xl p-3.5 text-xs text-slate-300 mr-8";
        item.innerHTML = `
            <div class="flex items-center gap-2 mb-1.5">
                <span class="bg-brand-500/20 text-brand-500 p-1 rounded-md">
                    <i data-lucide="bot" class="w-3.5 h-3.5"></i>
                </span>
                <span class="font-semibold text-white">Gemini Architect</span>
            </div>
            <p class="leading-relaxed">${text}</p>
        `;
    }
    list.appendChild(item);
    list.scrollTop = list.scrollHeight;
    lucide.createIcons();
}

// Form Upload for Custom Icon
function setupFormListeners() {
    const form = document.getElementById("icon-upload-form");
    form.addEventListener("submit", async (e) => {
        e.preventDefault();
        
        const tag = document.getElementById("icon-tag").value.trim();
        const description = document.getElementById("icon-desc").value.trim();
        const fileInput = document.getElementById("icon-file");
        
        if (!fileInput.files.length) return;
        
        const formData = new FormData();
        formData.append("tag", tag);
        formData.append("description", description);
        formData.append("file", fileInput.files[0]);
        
        try {
            const res = await fetch("/api/icons/upload", {
                method: "POST",
                body: formData
            });
            if (res.ok) {
                form.reset();
                loadCustomIcons();
                alert("Icon uploaded successfully!");
            } else {
                const err = await res.json();
                alert(`Upload failed: ${err.detail}`);
            }
        } catch (e) {
            console.error(e);
            alert("Error uploading file.");
        }
    });
}

// Manual Editor/Toolbox and Inspector Logic
function populateToolbox() {
    const list = document.getElementById("toolbox-node-list");
    list.innerHTML = "";
    
    // Add standard icons to toolbox
    Object.keys(SVG_ICONS).forEach(key => {
        const item = document.createElement("button");
        item.onclick = () => addCanvasNode(key);
        item.className = "bg-dark-900/50 hover:bg-dark-900 border border-dark-50 hover:border-brand-500 p-2.5 rounded-lg text-left transition-all flex items-center gap-2";
        
        // Inline SVG preview
        const svgContainer = document.createElement("div");
        svgContainer.className = "w-6 h-6 flex-shrink-0 bg-dark-100 p-1 rounded";
        svgContainer.innerHTML = SVG_ICONS[key];
        
        const nameText = document.createElement("div");
        nameText.className = "text-[10px] font-semibold text-slate-300 truncate";
        nameText.textContent = key.replace("aws-", "").replace("azure-", "").replace("gcp-", "").toUpperCase();
        
        item.appendChild(svgContainer);
        item.appendChild(nameText);
        list.appendChild(item);
    });
}

function populateInspectorIconSelect() {
    const select = document.getElementById("inspect-node-icon");
    select.innerHTML = "";
    
    // Registered architecture icons (official asset paths when installed, fallback otherwise)
    const optGroupOfficial = document.createElement("optgroup");
    optGroupOfficial.label = "Architecture Icon Library";
    officialIcons.forEach(i => {
        const opt = document.createElement("option"); opt.value = i.id; opt.textContent = `${i.provider.toUpperCase()} — ${i.label}${i.assetStatus === 'missing' ? ' (fallback until asset installed)' : ''}`; optGroupOfficial.appendChild(opt);
    });
    select.appendChild(optGroupOfficial);
    // Embedded fallback icons
    const optGroupStd = document.createElement("optgroup");
    optGroupStd.label = "Embedded Fallback Icons";
    Object.keys(SVG_ICONS).forEach(key => {
        const opt = document.createElement("option");
        opt.value = key;
        opt.textContent = key;
        optGroupStd.appendChild(opt);
    });
    select.appendChild(optGroupStd);
    
    // Add custom icons
    if (customIcons.length > 0) {
        const optGroupCust = document.createElement("optgroup");
        optGroupCust.label = "Custom Icons";
        customIcons.forEach(i => {
            const opt = document.createElement("option");
            opt.value = i.tag;
            opt.textContent = i.tag;
            optGroupCust.appendChild(opt);
        });
        select.appendChild(optGroupCust);
    }
}

// Add Node Manually
function addCanvasNode(iconName) {
    const id = "node_" + Math.random().toString(36).substring(2, 10);
    const parent = document.getElementById("inspect-node-parent").value || undefined;
    
    let iconUrl = resolveIconUrl(iconName);
    
    cy.add({
        data: {
            id,
            label: iconName.replace("aws-", "").replace("azure-", "").replace("gcp-", "").toUpperCase(),
            parent,
            type: 'cloudIcon',
            icon: iconName,
            icon_url: iconUrl,
            category: 'general',
            description: ''
        },
        position: {
            x: cy.width() / 2 + (Math.random() - 0.5) * 50,
            y: cy.height() / 2 + (Math.random() - 0.5) * 50
        }
    });
}

// Add Boundary Group Manually
function addCanvasGroup(groupType, label) {
    const id = "group_" + Math.random().toString(36).substring(2, 10);
    cy.add({
        data: {
            id,
            label,
            type: 'group',
            group_type: groupType
        }
    });
}

// Update parent list selectors in the property inspector
function updateParentSelectOptions() {
    const select = document.getElementById("inspect-node-parent");
    const currentVal = select.value;
    select.innerHTML = '<option value="">None (Root level)</option>';
    
    cy.nodes().forEach(ele => {
        if (ele.data('type') === 'group') {
            const opt = document.createElement("option");
            opt.value = ele.id();
            opt.textContent = ele.data('label');
            select.appendChild(opt);
        }
    });
    
    select.value = currentVal;
}

// Selection handling
let selectedElement = null;

function setupSelectionListeners() {
    cy.on('select', 'node', (evt) => {
        selectedElement = evt.target;
        showNodeInspector(selectedElement);
        
        // If exactly two nodes are selected, show option to connect
        const selectedNodes = cy.nodes(':selected');
        if (selectedNodes.length === 2) {
            showConnectionInspector(selectedNodes[0], selectedNodes[1]);
        }
    });
    
    cy.on('unselect', 'node', () => {
        selectedElement = null;
        hideInspectors();
    });

    cy.on('select', 'edge', (evt) => {
        selectedElement = evt.target;
        showEdgeInspector(selectedElement);
    });

    cy.on('unselect', 'edge', () => {
        selectedElement = null;
        hideInspectors();
    });
}

function hideInspectors() {
    document.getElementById("no-selection").classList.remove("hidden");
    document.getElementById("node-inspector").classList.add("hidden");
    document.getElementById("edge-inspector").classList.add("hidden");
}

function showNodeInspector(node) {
    document.getElementById("no-selection").classList.add("hidden");
    document.getElementById("edge-inspector").classList.add("hidden");
    
    const form = document.getElementById("node-inspector");
    form.classList.remove("hidden");
    
    document.getElementById("inspect-node-label").value = node.data('label') || '';
    document.getElementById("inspect-node-icon").value = node.data('icon') || 'server';
    document.getElementById("inspect-node-parent").value = node.data('parent') || '';
    document.getElementById("inspect-node-desc").value = node.data('description') || '';
}

function showEdgeInspector(edge) {
    document.getElementById("no-selection").classList.add("hidden");
    document.getElementById("node-inspector").classList.add("hidden");
    
    const form = document.getElementById("edge-inspector");
    form.classList.remove("hidden");
    
    document.getElementById("inspect-edge-label").value = edge.data('label') || '';
    document.getElementById("inspect-edge-protocol").value = edge.data('protocol') || '';
    document.getElementById("inspect-edge-encrypted").checked = edge.data('encrypted') || false;
}

// Helper to show inline connect details
function showConnectionInspector(nodeA, nodeB) {
    document.getElementById("no-selection").classList.add("hidden");
    document.getElementById("node-inspector").classList.add("hidden");
    
    const form = document.getElementById("edge-inspector");
    form.classList.remove("hidden");
    
    // Setup for connection creation
    document.getElementById("inspect-edge-label").value = `Link from ${nodeA.data('label')} to ${nodeB.data('label')}`;
    document.getElementById("inspect-edge-protocol").value = 'HTTPS';
    document.getElementById("inspect-edge-encrypted").checked = true;
    
    // Change Apply button action to create connection instead
    const applyBtn = form.querySelector("button[onclick='updateSelectedEdge()']");
    applyBtn.setAttribute("onclick", `createConnectionBetween('${nodeA.id()}', '${nodeB.id()}')`);
    applyBtn.querySelector("span") ? applyBtn.querySelector("span").textContent = "Create Link" : applyBtn.textContent = "Create Link";
}

function createConnectionBetween(sourceId, targetId) {
    const label = document.getElementById("inspect-edge-label").value.trim();
    const protocol = document.getElementById("inspect-edge-protocol").value.trim();
    const encrypted = document.getElementById("inspect-edge-encrypted").checked;
    
    const id = `edge_${sourceId}_${targetId}_${Math.random().toString(36).substring(2, 5)}`;
    
    cy.add({
        data: {
            id,
            source: sourceId,
            target: targetId,
            label: label || protocol,
            protocol,
            encrypted
        }
    });
    
    // Reset apply button
    const form = document.getElementById("edge-inspector");
    const applyBtn = form.querySelector("button[onclick^='createConnectionBetween']");
    applyBtn.setAttribute("onclick", "updateSelectedEdge()");
    applyBtn.textContent = "Apply Changes";
    
    cy.elements().unselect();
}

// Apply updates
function updateSelectedNode() {
    if (!selectedElement) return;
    
    const label = document.getElementById("inspect-node-label").value.trim();
    const icon = document.getElementById("inspect-node-icon").value;
    const parent = document.getElementById("inspect-node-parent").value || undefined;
    const desc = document.getElementById("inspect-node-desc").value.trim();
    
    let iconUrl = resolveIconUrl(icon, selectedElement.data("provider"), selectedElement.data("category"));
    
    selectedElement.data({
        label,
        icon,
        parent,
        icon_url: iconUrl,
        description: desc
    });
    
    cy.elements().unselect();
}

function updateSelectedEdge() {
    if (!selectedElement) return;
    
    const label = document.getElementById("inspect-edge-label").value.trim();
    const protocol = document.getElementById("inspect-edge-protocol").value.trim();
    const encrypted = document.getElementById("inspect-edge-encrypted").checked;
    
    selectedElement.data({
        label: label || protocol,
        protocol,
        encrypted
    });
    
    cy.elements().unselect();
}

function deleteSelectedElement() {
    if (!selectedElement) return;
    if (confirm("Are you sure you want to delete this element?")) {
        cy.remove(selectedElement);
        hideInspectors();
    }
}

// Export Diagram to local assets
function exportDiagram(format) {
    if (cy.elements().length === 0) {
        alert("Nothing to export.");
        return;
    }
    
    if (format === 'json') {
        const topology = exportTopologyJSON();
        const dataStr = "data:text/json;charset=utf-8," + encodeURIComponent(JSON.stringify(topology, null, 2));
        const dlAnchor = document.createElement('a');
        dlAnchor.setAttribute("href", dataStr);
        dlAnchor.setAttribute("download", `diagram_${currentDiagramId || 'draft'}.json`);
        document.body.appendChild(dlAnchor);
        dlAnchor.click();
        dlAnchor.remove();
    } else if (format === 'png') {
        const pngContent = cy.png({ output: 'blob', bg: '#0c0c0e', scale: 2 });
        const dlAnchor = document.createElement('a');
        dlAnchor.setAttribute("href", URL.createObjectURL(pngContent));
        dlAnchor.setAttribute("download", `diagram_${currentDiagramId || 'draft'}.png`);
        document.body.appendChild(dlAnchor);
        dlAnchor.click();
        dlAnchor.remove();
    } else if (format === 'svg') {
        alert("SVG export is partially supported via raw vector mapping. Recommend exporting high-resolution PNG or raw JSON topology.");
    }
}

/* ========================= PHASE 3 ARCHITECTURE STUDIO =========================
   The overrides below preserve the existing UI while upgrading layout, routing,
   multi-view projection, linting, legend generation and SVG/PDF export.
*/
let phase3FullTopology = null;
let phase3ActiveView = 'logical';

const PHASE3_LAYER = { external:0,user:0,client:0,saas:0,edge:1,network:1,gateway:1,
    application:2,compute:2,service:2,general:2,integration:3,messaging:3,
    data:4,database:4,storage:4,identity:5,security:5,observability:6 };

function phase3Layer(node) {
    const v = Number(node.data('layer'));
    return Number.isFinite(v) ? v : (PHASE3_LAYER[node.data('category')] ?? 2);
}
function phase3PortPair(source, target) {
    const a = phase3Layer(source), b = phase3Layer(target);
    if (a === b) return ['south', 'north'];
    return b > a ? ['east', 'west'] : ['west', 'east'];
}
function phase3OrderLayers(leaves, layers) {
    const buckets = new Map(layers.map(l => [l, []]));
    leaves.forEach(n => buckets.get(phase3Layer(n)).push(n));
    layers.forEach(l => buckets.get(l).sort((a,b)=>String(a.data('label')).localeCompare(String(b.data('label')))));
    for (let pass=0; pass<6; pass++) {
        const order = new Map(); layers.forEach(l=>buckets.get(l).forEach((n,i)=>order.set(n.id(), i)));
        const sweep = pass % 2 ? [...layers].reverse() : layers;
        sweep.forEach(l => buckets.get(l).sort((a,b)=>phase3Barycenter(a,order)-phase3Barycenter(b,order) || String(a.data('label')).localeCompare(String(b.data('label')))));
    }
    return buckets;
}
function phase3Barycenter(node, order) {
    const vals = node.connectedEdges().map(e=> e.source().id()===node.id()?e.target():e.source()).filter(Boolean)
      .map(n=>order.get(n.id())).filter(Number.isFinite);
    return vals.length ? vals.reduce((a,b)=>a+b,0)/vals.length : 99999;
}

function initCanvas() {
    cy = cytoscape({
        container: document.getElementById('cy'),
        style: [
            { selector:'node', style:{
                'label':'data(label)','color':'#dbe4ee','font-size':'10px','font-family':'Inter, Arial, sans-serif',
                'text-valign':'bottom','text-margin-y':'7px','background-color':'#18212f','border-width':'2px','border-color':'#526274',
                'width':'66px','height':'66px','shape':'roundrectangle','background-image':'data(icon_url)','background-fit':'contain',
                'background-width':'70%','background-height':'70%','text-wrap':'wrap','text-max-width':'125px',
                'text-outline-width':2,'text-outline-color':'#0b111a','transition-property':'border-color, background-color','transition-duration':'0.2s'}},
            { selector:'node:selected', style:{'border-color':'#38bdf8','border-width':'3px','background-color':'#223044'}},
            { selector:'node[type="group"]', style:{'label':'data(label)','text-valign':'top','text-halign':'left','text-margin-x':'12px','text-margin-y':'-14px',
                'font-size':'12px','font-weight':'600','color':'#cbd5e1','background-color':'rgba(30,41,59,0.08)','border-style':'dashed','border-width':'1.5px',
                'border-color':'#64748b','shape':'roundrectangle','padding':'34px','background-image':'none'}},
            { selector:'node[type="group"][zone = "public"]', style:{'border-color':'#22c55e','background-color':'rgba(34,197,94,0.04)'}},
            { selector:'node[type="group"][zone = "private"]', style:{'border-color':'#38bdf8','background-color':'rgba(56,189,248,0.04)'}},
            { selector:'node[category = "security"]', style:{'border-color':'#fb7185'}},
            { selector:'node[category = "identity"]', style:{'border-color':'#a78bfa'}},
            { selector:'node[category = "observability"]', style:{'border-color':'#22c55e'}},
            { selector:'edge', style:{'label':'data(label)','font-size':'9px','font-family':'Inter, Arial, sans-serif','color':'#cbd5e1','width':2,
                'line-color':'#64748b','target-arrow-color':'#64748b','target-arrow-shape':'triangle','curve-style':'taxi',
                'taxi-direction':'rightward','taxi-turn':'45%','taxi-turn-min-distance':32,'taxi-radius':8,
                'text-background-opacity':0.92,'text-background-color':'#0b111a','text-background-padding':'3px','text-background-shape':'roundrectangle'}},
            { selector:'edge.route-vertical', style:{'taxi-direction':'downward'}},
            { selector:'edge[kind = "async"]', style:{'line-style':'dashed','line-dash-pattern':[8,5],'target-arrow-shape':'triangle','line-color':'#f59e0b','target-arrow-color':'#f59e0b'}},
            { selector:'edge[kind = "auth"]', style:{'line-style':'dotted','target-arrow-shape':'diamond','line-color':'#a78bfa','target-arrow-color':'#a78bfa'}},
            { selector:'edge[kind = "observability"]', style:{'line-style':'dashed','line-dash-pattern':[3,4],'target-arrow-shape':'vee','line-color':'#22c55e','target-arrow-color':'#22c55e'}},
            { selector:'edge[kind = "data"]', style:{'line-color':'#38bdf8','target-arrow-color':'#38bdf8'}},
            { selector:'edge[direction = "bidirectional"]', style:{'source-arrow-shape':'triangle','source-arrow-color':'#64748b'}},
            { selector:'edge[encrypted = true]', style:{'line-color':'#10b981','target-arrow-color':'#10b981'}},
            { selector:'edge:selected', style:{'line-color':'#38bdf8','target-arrow-color':'#38bdf8','width':3}}
        ], layout:{name:'preset'}
    });
    cy.on('add remove', () => { const empty=document.getElementById('empty-state'); if(empty) empty.classList.toggle('hidden', cy.elements().length>0); updateParentSelectOptions(); });
    cy.on('render resize', phase3RenderLegend);
}

function canvasAutoLayout() {
    const leaves = cy.nodes().filter(n=>n.data('type')!=='group');
    if (!leaves.length) return;
    const primary = leaves.filter(n=>!['identity','observability'].includes(n.data('category')));
    const allLayers = [...new Set(primary.map(phase3Layer))].sort((a,b)=>a-b);
    const buckets = phase3OrderLayers(primary, allLayers);
    const xGap=285, yGap=145, baseX=150, centerY=370;
    allLayers.forEach((l, li)=>{
        const list=buckets.get(l)||[]; const start=centerY-((list.length-1)*yGap)/2;
        list.forEach((n,i)=>n.position({x:baseX+li*xGap,y:start+i*yGap}));
    });
    // Side rails: identity and observability should not cross the primary request path.
    const maxX = baseX + Math.max(0,allLayers.length-1)*xGap;
    leaves.filter(n=>n.data('category')==='identity').forEach((n,i)=>n.position({x:Math.min(maxX,baseX+xGap*2),y:90+i*115}));
    leaves.filter(n=>n.data('category')==='observability').forEach((n,i)=>n.position({x:Math.min(maxX,baseX+xGap*3),y:650+i*115}));
    cy.edges().forEach(e=>{
        const [sp,tp]=phase3PortPair(e.source(),e.target());
        if (!e.data('sourcePort') || e.data('sourcePort')==='auto') e.data('sourcePort',sp);
        if (!e.data('targetPort') || e.data('targetPort')==='auto') e.data('targetPort',tp);
        e.toggleClass('route-vertical', ['north','south'].includes(e.data('sourcePort')) || ['north','south'].includes(e.data('targetPort')));
    });
    cy.nodes('[type = "group"]').style({'padding':'42px','text-margin-y':'-20px'});
    cy.fit(cy.elements(), 100);
    phase3RenderLegend();
}

function renderTopology(dsl, preserveFull = false) {
    if (!preserveFull) phase3FullTopology = JSON.parse(JSON.stringify(dsl));
    cy.elements().remove(); const elements=[];
    (dsl.groups||[]).forEach(g=>elements.push({data:{id:g.id,label:g.label,type:'group',group_type:g.type,provider:g.provider||'generic',zone:g.zone||''}}));
    (dsl.nodes||[]).forEach(n=>{
        let iconUrl=getIconUri(n.data.icon); if(!iconUrl){const c=customIcons.find(ci=>ci.tag===n.data.icon); if(c) iconUrl=c.url;}
        elements.push({data:{id:n.id,label:n.data.label,parent:n.parentId||undefined,type:n.type,icon:n.data.icon,icon_url:iconUrl||getIconUri('server'),category:n.data.category,layer:n.data.layer,provider:n.data.provider,description:n.data.description,properties:n.data.properties}});
    });
    (dsl.edges||[]).forEach(e=>{
        const d=e.data||{}; elements.push({data:{id:e.id,source:e.source,target:e.target,label:e.label||d.protocol||'',protocol:d.protocol||'',encrypted:!!d.encrypted,direction:d.direction||'forward',kind:d.kind||'sync',sourcePort:d.sourcePort||'auto',targetPort:d.targetPort||'auto'}});
    });
    cy.add(elements); canvasAutoLayout(); console.info('Phase 3 diagnostics',getArchitectureDiagnostics());
}

async function setArchitectureView(view) {
    if (!phase3FullTopology) return alert('Generate or load an architecture first.');
    const res=await fetch('/api/architecture/view',{method:'POST',headers:{'Content-Type':'application/json'},body:JSON.stringify({diagram:phase3FullTopology,view})});
    if(!res.ok) return alert('Unable to generate architecture view.');
    phase3ActiveView=view; renderTopology(await res.json(), true);
}
async function runArchitectureLint() {
    const topology=exportTopologyJSON();
    const res=await fetch('/api/architecture/lint',{method:'POST',headers:{'Content-Type':'application/json'},body:JSON.stringify({diagram:topology})});
    if(!res.ok) return alert('Architecture linting failed.');
    const out=await res.json(), l=out.lint;
    const lines=[`Architecture Score: ${l.score}/100 (${l.grade})`,...l.findings.map(f=>`${f.severity.toUpperCase()}: ${f.message}`)];
    alert(lines.join('\n\n')); return out;
}

function phase3RenderLegend() {
    if(!cy || !cy.container()) return;
    const parent=cy.container().parentElement; if(!parent) return;
    let legend=parent.querySelector('.phase3-legend');
    if(!legend){ legend=document.createElement('div'); legend.className='phase3-legend'; legend.style.cssText='position:absolute;left:14px;bottom:14px;z-index:5;background:rgba(11,17,26,.92);border:1px solid #334155;border-radius:10px;padding:10px 12px;color:#cbd5e1;font:10px Inter,Arial;box-shadow:0 8px 30px rgba(0,0,0,.25);'; parent.style.position='relative'; parent.appendChild(legend); }
    legend.innerHTML='<b style="display:block;margin-bottom:6px">Architecture Legend</b><span>→ Sync</span> &nbsp; <span style="color:#f59e0b">- - Async</span> &nbsp; <span style="color:#a78bfa">·· Auth</span> &nbsp; <span style="color:#10b981">→ Encrypted</span><br><span style="color:#94a3b8">View: '+phase3ActiveView+'</span>';
}

function phase3Escape(s){return String(s??'').replace(/[&<>"']/g,c=>({'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;',"'":'&apos;'}[c]));}
function phase3SvgDataUri(uri){ return uri && uri.startsWith('data:image') ? uri : ''; }
function buildArchitectureSVG() {
    const bb=cy.elements().boundingBox({includeLabels:true}); const pad=80; const w=Math.max(800,bb.w+pad*2), h=Math.max(500,bb.h+pad*2), ox=pad-bb.x, oy=pad-bb.y;
    const marker='<defs><marker id="arrow" markerWidth="8" markerHeight="8" refX="7" refY="4" orient="auto"><path d="M0,0 L8,4 L0,8 z" fill="#64748b"/></marker></defs>';
    let body='<rect width="100%" height="100%" fill="#0b111a"/>';
    cy.nodes('[type = "group"]').forEach(g=>{const b=g.boundingBox({includeLabels:true}); body+=`<rect x="${b.x+ox}" y="${b.y+oy}" width="${b.w}" height="${b.h}" rx="14" fill="none" stroke="#64748b" stroke-dasharray="6 4"/><text x="${b.x+ox+12}" y="${b.y+oy+18}" fill="#cbd5e1" font-family="Inter,Arial" font-size="12" font-weight="600">${phase3Escape(g.data('label'))}</text>`;});
    cy.edges().forEach(e=>{const s=e.source().position(),t=e.target().position();const dx=t.x-s.x,dy=t.y-s.y;let d; if(Math.abs(dx)>=Math.abs(dy)){const mx=(s.x+t.x)/2; d=`M ${s.x+ox} ${s.y+oy} L ${mx+ox} ${s.y+oy} L ${mx+ox} ${t.y+oy} L ${t.x+ox} ${t.y+oy}`;}else{const my=(s.y+t.y)/2; d=`M ${s.x+ox} ${s.y+oy} L ${s.x+ox} ${my+oy} L ${t.x+ox} ${my+oy} L ${t.x+ox} ${t.y+oy}`;} const color=e.data('encrypted')?'#10b981':e.data('kind')==='async'?'#f59e0b':e.data('kind')==='auth'?'#a78bfa':'#64748b'; const dash=e.data('kind')==='async'?'stroke-dasharray="8 5"':e.data('kind')==='auth'?'stroke-dasharray="2 4"':''; body+=`<path d="${d}" fill="none" stroke="${color}" stroke-width="2" ${dash} marker-end="url(#arrow)"/>`; const label=e.data('label'); if(label) body+=`<text x="${(s.x+t.x)/2+ox}" y="${(s.y+t.y)/2+oy-6}" fill="#cbd5e1" font-family="Inter,Arial" font-size="9" text-anchor="middle">${phase3Escape(label)}</text>`;});
    cy.nodes().filter(n=>n.data('type')!=='group').forEach(n=>{const p=n.position(),size=66,x=p.x-size/2+ox,y=p.y-size/2+oy,uri=phase3SvgDataUri(n.data('icon_url')); body+=`<rect x="${x}" y="${y}" width="${size}" height="${size}" rx="10" fill="#18212f" stroke="#526274" stroke-width="2"/>`; if(uri) body+=`<image href="${uri}" x="${x+10}" y="${y+8}" width="46" height="46"/>`; body+=`<text x="${p.x+ox}" y="${y+80}" fill="#dbe4ee" font-family="Inter,Arial" font-size="10" text-anchor="middle">${phase3Escape(n.data('label'))}</text>`;});
    body+=`<text x="24" y="30" fill="#e2e8f0" font-family="Inter,Arial" font-size="18" font-weight="700">Architecture Diagram — ${phase3Escape(phase3ActiveView)}</text>`;
    return `<svg xmlns="http://www.w3.org/2000/svg" width="${w}" height="${h}" viewBox="0 0 ${w} ${h}">${marker}${body}</svg>`;
}
function phase3Download(name, content, type){const a=document.createElement('a');a.href=URL.createObjectURL(new Blob([content],{type}));a.download=name;document.body.appendChild(a);a.click();a.remove();setTimeout(()=>URL.revokeObjectURL(a.href),1000);}
function exportDiagram(format) {
    if(cy.elements().length===0) return alert('Nothing to export.');
    if(format==='json'){const t=exportTopologyJSON();return phase3Download(`diagram_${currentDiagramId||'draft'}.json`,JSON.stringify(t,null,2),'application/json');}
    if(format==='png'){const blob=cy.png({output:'blob',bg:'#0b111a',scale:3});const a=document.createElement('a');a.href=URL.createObjectURL(blob);a.download=`diagram_${currentDiagramId||'draft'}.png`;a.click();return;}
    const svg=buildArchitectureSVG();
    if(format==='svg') return phase3Download(`diagram_${currentDiagramId||'draft'}.svg`,svg,'image/svg+xml');
    if(format==='pdf'){const win=window.open('','_blank');win.document.write(`<html><head><title>Architecture Diagram</title></head><body style="margin:0">${svg}<script>window.onload=()=>window.print()<\/script></body></html>`);win.document.close();}
}

/* ===== Phase 3 Frontend Integration Upgrade ===== */
(function () {
  function byId(id){ return document.getElementById(id); }
  function setSelect(id, value){ const el=byId(id); if(el) el.value=value ?? 'auto'; }
  function renderQuality(out){
    const l=out?.lint || out; if(!l) return;
    const score=Number(l.score ?? 0), grade=l.grade ?? '--';
    const header=byId('architecture-score'), scoreValue=byId('quality-score-value'), fill=byId('quality-bar-fill'), gradeEl=byId('quality-grade'), findings=byId('quality-findings');
    if(header) header.textContent=`${score}/100`;
    if(scoreValue) scoreValue.textContent=score;
    if(fill) fill.style.width=`${Math.max(0,Math.min(100,score))}%`;
    if(gradeEl) gradeEl.textContent=`Grade ${grade}`;
    if(findings){ findings.innerHTML=''; (l.findings||[]).forEach(f=>{const d=document.createElement('div');d.className=`finding-item ${String(f.severity||'info').toLowerCase()}`;d.textContent=`${String(f.severity||'info').toUpperCase()}: ${f.message}`;findings.appendChild(d);}); if(!(l.findings||[]).length)findings.textContent='No findings. Architecture passed the current checks.'; }
  }
  async function lintAndRender(){ try{ const out=await runArchitectureLint(); if(out) renderQuality(out); }catch(e){ console.error(e); } }
  document.addEventListener('DOMContentLoaded',()=>{
    const qTab=byId('tab-quality'), inspector=byId('panel-inspector'), toolbox=byId('panel-toolbox'), quality=byId('panel-quality');
    if(qTab){ qTab.addEventListener('click',()=>{ [byId('tab-inspector'),byId('tab-toolbox'),qTab].forEach(t=>t?.classList.remove('border-brand-500','text-white')); [byId('tab-inspector'),byId('tab-toolbox'),qTab].forEach(t=>t?.classList.add('border-transparent','text-slate-400')); qTab.classList.add('border-brand-500','text-white'); qTab.classList.remove('border-transparent','text-slate-400'); inspector?.classList.add('hidden'); toolbox?.classList.add('hidden'); quality?.classList.remove('hidden'); }); }
    byId('btn-run-lint')?.addEventListener('click',lintAndRender); byId('btn-run-lint-panel')?.addEventListener('click',lintAndRender);
    byId('architecture-view')?.addEventListener('change',e=>setArchitectureView(e.target.value));
    byId('btn-toggle-left')?.addEventListener('click',()=>document.querySelector('main > section:first-child')?.classList.toggle('sidebar-collapsed'));
    byId('btn-toggle-right')?.addEventListener('click',()=>document.querySelector('main > section:last-child')?.classList.toggle('sidebar-collapsed'));
  });
  window.__phase3RenderQuality=renderQuality; window.__phase3Lint=lintAndRender; window.__phase3SetSelect=setSelect;
})();

function showNodeInspector(node) {
    document.getElementById("no-selection").classList.add("hidden"); document.getElementById("edge-inspector").classList.add("hidden");
    const form=document.getElementById("node-inspector"); form.classList.remove("hidden");
    document.getElementById("inspect-node-label").value=node.data('label')||''; document.getElementById("inspect-node-icon").value=node.data('icon')||'server'; document.getElementById("inspect-node-parent").value=node.data('parent')||''; document.getElementById("inspect-node-desc").value=node.data('description')||'';
    if(document.getElementById('inspect-node-provider')) document.getElementById('inspect-node-provider').value=node.data('provider')||'generic';
    if(document.getElementById('inspect-node-layer')) document.getElementById('inspect-node-layer').value=node.data('layer') ?? '';
}
function showEdgeInspector(edge) {
    document.getElementById("no-selection").classList.add("hidden"); document.getElementById("node-inspector").classList.add("hidden"); document.getElementById("edge-inspector").classList.remove("hidden");
    document.getElementById("inspect-edge-label").value=edge.data('label')||''; document.getElementById("inspect-edge-protocol").value=edge.data('protocol')||''; document.getElementById("inspect-edge-encrypted").checked=!!edge.data('encrypted');
    window.__phase3SetSelect?.('inspect-edge-kind',edge.data('kind')||'sync'); window.__phase3SetSelect?.('inspect-edge-direction',edge.data('direction')||'forward'); window.__phase3SetSelect?.('inspect-edge-source-port',edge.data('sourcePort')||'auto'); window.__phase3SetSelect?.('inspect-edge-target-port',edge.data('targetPort')||'auto');
}
function updateSelectedNode() {
    if(!selectedElement)return; const icon=document.getElementById('inspect-node-icon').value; let iconUrl=getIconUri(icon); if(!iconUrl){const c=customIcons.find(ci=>ci.tag===icon);if(c)iconUrl=c.url;}
    selectedElement.data({label:document.getElementById('inspect-node-label').value.trim(),icon,parent:document.getElementById('inspect-node-parent').value||undefined,icon_url:iconUrl||getIconUri('server'),description:document.getElementById('inspect-node-desc').value.trim(),provider:document.getElementById('inspect-node-provider')?.value||selectedElement.data('provider')||'generic',layer:Number(document.getElementById('inspect-node-layer')?.value||selectedElement.data('layer')||0)}); cy.elements().unselect();
}
function updateSelectedEdge() {
    if(!selectedElement)return; const protocol=document.getElementById('inspect-edge-protocol').value.trim();
    selectedElement.data({label:document.getElementById('inspect-edge-label').value.trim()||protocol,protocol,encrypted:document.getElementById('inspect-edge-encrypted').checked,kind:document.getElementById('inspect-edge-kind')?.value||'sync',direction:document.getElementById('inspect-edge-direction')?.value||'forward',sourcePort:document.getElementById('inspect-edge-source-port')?.value||'auto',targetPort:document.getElementById('inspect-edge-target-port')?.value||'auto'}); canvasAutoLayout(); cy.elements().unselect();
}

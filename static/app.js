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

    // ── Generic / Infrastructure ───────────────────────────────────────

    'database': `<svg viewBox="0 0 40 40" xmlns="http://www.w3.org/2000/svg"><rect width="40" height="40" rx="8" fill="#6d28d9"/><ellipse cx="20" cy="12" rx="10" ry="4" fill="#A78BFA"/><path d="M10 12 v16 c0 2.2 4.5 4 10 4 s10-1.8 10-4 V12" fill="#6d28d9"/><ellipse cx="20" cy="12" rx="10" ry="4" fill="#A78BFA"/><path d="M10 20 c0 2.2 4.5 4 10 4 s10-1.8 10-4" stroke="#A78BFA" stroke-width="1.2" fill="none"/><text x="20" y="37" text-anchor="middle" font-size="6" font-family="Arial" font-weight="bold" fill="white">Database</text></svg>`,

    'server': `<svg viewBox="0 0 40 40" xmlns="http://www.w3.org/2000/svg"><rect width="40" height="40" rx="8" fill="#475569"/><rect x="8" y="10" width="24" height="8" rx="2" stroke="white" stroke-width="1.2" fill="white" opacity="0.1"/><rect x="8" y="21" width="24" height="8" rx="2" stroke="white" stroke-width="1.2" fill="white" opacity="0.1"/><circle cx="12" cy="14" r="1.5" fill="#22c55e"/><circle cx="12" cy="25" r="1.5" fill="#22c55e"/><text x="20" y="38" text-anchor="middle" font-size="7" font-family="Arial" font-weight="bold" fill="white">Server</text></svg>`,

    'client': `<svg viewBox="0 0 40 40" xmlns="http://www.w3.org/2000/svg"><rect width="40" height="40" rx="8" fill="#0ea5e9"/><rect x="8" y="9" width="24" height="16" rx="2" stroke="white" stroke-width="1.5" fill="white" opacity="0.1"/><rect x="11" y="12" width="18" height="10" rx="1" fill="white" opacity="0.15"/><line x1="14" y1="28" x2="26" y2="28" stroke="white" stroke-width="2"/><line x1="20" y1="25" x2="20" y2="28" stroke="white" stroke-width="2"/><text x="20" y="38" text-anchor="middle" font-size="7" font-family="Arial" font-weight="bold" fill="white">Client</text></svg>`,

    'user': `<svg viewBox="0 0 40 40" xmlns="http://www.w3.org/2000/svg"><rect width="40" height="40" rx="8" fill="#64748b"/><circle cx="20" cy="13" r="6" fill="white" opacity="0.9"/><path d="M8 31 Q20 24 32 31" stroke="white" stroke-width="2" fill="none"/></svg>`,

    'dns': `<svg viewBox="0 0 40 40" xmlns="http://www.w3.org/2000/svg"><rect width="40" height="40" rx="8" fill="#059669"/><circle cx="20" cy="17" r="9" stroke="white" stroke-width="1.5" fill="none"/><line x1="11" y1="17" x2="29" y2="17" stroke="white" stroke-width="1.2"/><path d="M20 8 Q24 12 24 17 Q24 22 20 26 Q16 22 16 17 Q16 12 20 8" stroke="white" stroke-width="1.2" fill="none"/><text x="20" y="37" text-anchor="middle" font-size="8" font-family="Arial" font-weight="bold" fill="white">DNS</text></svg>`,

    'router': `<svg viewBox="0 0 40 40" xmlns="http://www.w3.org/2000/svg"><rect width="40" height="40" rx="8" fill="#d97706"/><path d="M10 18 H30 M14 14 L10 18 L14 22 M26 14 L30 18 L26 22" stroke="white" stroke-width="2" fill="none" stroke-linecap="round" stroke-linejoin="round"/><text x="20" y="37" text-anchor="middle" font-size="7" font-family="Arial" font-weight="bold" fill="white">Router</text></svg>`,

    'firewall': `<svg viewBox="0 0 40 40" xmlns="http://www.w3.org/2000/svg"><rect width="40" height="40" rx="8" fill="#dc2626"/><path d="M10 13 H30 V28 H10 Z" fill="white" opacity="0.12" stroke="white" stroke-width="1.5"/><path d="M10 18 H30 M16 13 V18 M24 18 V23 M16 23 V28" stroke="white" stroke-width="1.5"/><text x="20" y="37" text-anchor="middle" font-size="6" font-family="Arial" font-weight="bold" fill="white">Firewall</text></svg>`,

    'cog': `<svg viewBox="0 0 40 40" xmlns="http://www.w3.org/2000/svg"><rect width="40" height="40" rx="8" fill="#64748b"/><circle cx="20" cy="20" r="8" stroke="white" stroke-width="3" fill="none"/><circle cx="20" cy="20" r="3" fill="white"/><path d="M20 8 V12 M20 28 V32 M8 20 H12 M28 20 H32 M11.5 11.5 L14.5 14.5 M25.5 25.5 L28.5 28.5 M28.5 11.5 L25.5 14.5 M14.5 25.5 L11.5 28.5" stroke="white" stroke-width="2"/></svg>`
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
let selectedElement = null;


// Initialize Page
document.addEventListener("DOMContentLoaded", () => {
    try { lucide.createIcons(); } catch (e) { console.warn("Lucide init failed", e); }

    try { initTabs(); } catch (e) { console.error("Tabs initialization failed", e); }
    try { initAuthStatus(); } catch (e) { console.error("Auth status initialization failed", e); }
    try { installExportOverlayFix(); } catch (e) { console.error("Export overlay initialization failed", e); }
    try { initCanvas(); } catch (e) { console.error("Canvas initialization failed", e); }
    try { loadProjects(); } catch (e) { console.error("Projects initialization failed", e); }
    try { loadCustomIcons(); } catch (e) { console.error("Custom icons initialization failed", e); }
    try { populateToolbox(); } catch (e) { console.error("Toolbox initialization failed", e); }
    try { setupFormListeners(); } catch (e) { console.error("Form listeners initialization failed", e); }
    try { setupSelectionListeners(); } catch (e) { console.error("Selection listeners initialization failed", e); }
});


// Defensive tab navigation logic
function initTabs() {

    const wireTabs = (items) => {
        items.forEach(({ tab, panel }) => {
            if (!tab || !panel) return;

            tab.addEventListener("click", (event) => {
                event.preventDefault();
                event.stopPropagation();

                items.forEach(({ tab: otherTab, panel: otherPanel }) => {
                    if (!otherTab || !otherPanel) return;

                    const active = otherTab === tab;

                    otherTab.classList.toggle("border-brand-500", active);
                    otherTab.classList.toggle("text-white", active);
                    otherTab.classList.toggle("border-transparent", !active);
                    otherTab.classList.toggle("text-slate-400", !active);

                    otherPanel.classList.toggle("hidden", !active);
                });
            });
        });
    };

    wireTabs([
        {
            tab: document.getElementById("tab-chat"),
            panel: document.getElementById("panel-chat")
        },
        {
            tab: document.getElementById("tab-icons"),
            panel: document.getElementById("panel-icons")
        }
    ]);

    wireTabs([
        {
            tab: document.getElementById("tab-inspector"),
            panel: document.getElementById("panel-inspector")
        },
        {
            tab: document.getElementById("tab-toolbox"),
            panel: document.getElementById("panel-toolbox")
        }
    ]);
}


// Authentication & ADC status management
async function initAuthStatus() {

    const dot = document.getElementById("auth-status-dot");
    const text = document.getElementById("auth-status-text");

    if (!dot || !text) return;

    try {

        const res = await fetch("/api/auth/status", {
            cache: "no-store"
        });

        if (!res.ok) {
            throw new Error(`HTTP ${res.status}`);
        }

        const data = await res.json();

        if (data.authenticated) {

            dot.className =
                "w-2 h-2 rounded-full bg-emerald-400";

            const model =
                data.active_model ||
                data.configured_model ||
                data.model ||
                "Model pending";

            text.innerText =
                `Vertex AI · ${model}`;

            text.title = [
                `Project: ${data.project}`,
                `Location: ${data.location}`,
                `Authentication: ${data.auth_mode}`,
                `Active Model: ${data.active_model || "Not used yet"}`,
                `Configured Model: ${data.configured_model || data.model || "Unknown"}`
            ].join("\n");

        } else {

            dot.className =
                "w-2 h-2 rounded-full bg-amber-400";

            text.innerText = "ADC Pending";
            text.title =
                data.message || "ADC unavailable";
        }

    } catch (e) {

        dot.className =
            "w-2 h-2 rounded-full bg-rose-400";

        text.innerText = "Auth Error";
        text.title = e.message;
    }
}


// Makes any export dropdown render above sidebars even when its parent creates a stacking context.
function installExportOverlayFix() {

    const style = document.createElement('style');

    style.textContent =
        '.export-overlay-fixed{' +
        'position:fixed!important;' +
        'z-index:2147483000!important;' +
        'pointer-events:auto!important' +
        '}';

    document.head.appendChild(style);

    document.addEventListener(
        'click',
        (event) => {

            const trigger =
                event.target.closest(
                    '[data-export-toggle],' +
                    '#btn-export,' +
                    '#export-button,' +
                    'button[onclick*="toggleExport"]'
                );

            if (!trigger) return;

            const menu =
                document.getElementById('export-menu') ||
                document.querySelector('[data-export-menu]');

            if (!menu) return;

            event.preventDefault();
            event.stopPropagation();

            const hidden =
                menu.classList.contains('hidden');

            if (!hidden) {

                menu.classList.add('hidden');
                menu.classList.remove('export-overlay-fixed');

                return;
            }

            const r =
                trigger.getBoundingClientRect();

            menu.classList.remove('hidden');
            menu.classList.add('export-overlay-fixed');

            menu.style.top =
                `${Math.min(
                    window.innerHeight - 20,
                    r.bottom + 8
                )}px`;

            menu.style.right = 'auto';

            menu.style.left =
                `${Math.max(
                    8,
                    Math.min(
                        window.innerWidth -
                        menu.offsetWidth -
                        8,
                        r.right -
                        menu.offsetWidth
                    )
                )}px`;
        },
        true
    );


    document.addEventListener(
        'click',
        (e) => {

            const m =
                document.getElementById('export-menu') ||
                document.querySelector('[data-export-menu]');

            if (
                m &&
                !m.contains(e.target) &&
                !e.target.closest(
                    '[data-export-toggle],' +
                    '#btn-export,' +
                    '#export-button'
                )
            ) {

                m.classList.add('hidden');
                m.classList.remove(
                    'export-overlay-fixed'
                );
            }
        }
    );
}


// Initialize Cytoscape canvas
function initCanvas() {

    const container =
        document.getElementById('cy');

    if (!container) {
        throw new Error(
            "Cytoscape container #cy not found"
        );
    }

    cy = cytoscape({

        container,

        style: [

            {
                selector: 'node',

                style: {

                    'label': 'data(label)',

                    'color': '#cbd5e1',

                    'font-size': '10px',

                    'font-family':
                        'Inter, sans-serif',

                    'text-valign': 'bottom',

                    'text-margin-y': '6px',

                    'background-color':
                        '#1c1c1e',

                    'border-width': '2px',

                    'border-color':
                        '#3a3a3c',

                    'width': '45px',

                    'height': '45px',

                    'shape':
                        'roundrectangle',

                    'background-image':
                        'data(icon_url)',

                    'background-fit':
                        'contain',

                    'background-width':
                        '65%',

                    'background-height':
                        '65%',

                    'text-wrap': 'wrap',

                    'text-max-width':
                        '100px',

                    'transition-property':
                        'background-color, border-color',

                    'transition-duration':
                        '0.2s'
                }
            },

            {
                selector: 'node:selected',

                style: {

                    'border-color':
                        '#0070f3',

                    'border-width': '3px',

                    'background-color':
                        '#252529'
                }
            },

            {
                selector: 'node[type = "group"]',

                style: {

                    'shape':
                        'roundrectangle',

                    'background-color':
                        '#1a1a1e',

                    'background-opacity':
                        '0.28',

                    'border-color':
                        '#475569',

                    'border-width': '1px',

                    'border-style':
                        'dashed',

                    'padding': '35px',

                    'label':
                        'data(label)',

                    'text-valign':
                        'top',

                    'text-halign':
                        'center',

                    'text-margin-y':
                        '-18px',

                    'font-size':
                        '11px',

                    'font-weight':
                        '600',

                    'color':
                        '#94a3b8',

                    'text-background-opacity':
                        '0',

                    'z-compound-depth':
                        'bottom'
                }
            },

            {
                selector: 'edge',

                style: {

                    'width': '2px',

                    'line-color':
                        '#64748b',

                    'target-arrow-color':
                        '#64748b',

                    'target-arrow-shape':
                        'triangle',

                    'curve-style':
                        'taxi',

                    'taxi-direction':
                        'horizontal',

                    'taxi-turn':
                        '50%',

                    'arrow-scale':
                        0.9,

                    'label':
                        'data(label)',

                    'font-size':
                        '8px',

                    'color':
                        '#94a3b8',

                    'text-background-color':
                        '#111827',

                    'text-background-opacity':
                        0.9,

                    'text-background-padding':
                        '3px',

                    'text-rotation':
                        'autorotate'
                }
            },

            {
                selector:
                    'edge[direction = "bidirectional"]',

                style: {

                    'source-arrow-shape':
                        'triangle'
                }
            },

            {
                selector:
                    'edge[kind = "async"]',

                style: {

                    'line-style':
                        'dashed'
                }
            },

            {
                selector:
                    'edge[kind = "data"]',

                style: {

                    'line-style':
                        'dotted'
                }
            },

            {
                selector:
                    'edge:selected',

                style: {

                    'line-color':
                        '#0070f3',

                    'target-arrow-color':
                        '#0070f3',

                    'width':
                        '3px'
                }
            }
        ],

        layout: {
            name: 'preset'
        },

        wheelSensitivity: 0.2,

        minZoom: 0.15,

        maxZoom: 3
    });

    setupCanvasInteractions();
}
// Hide/show empty state based on elements
cy.on('add remove', () => {
    const emptyState = document.getElementById("empty-state");

    if (cy.elements().length > 0) {
        emptyState?.classList.add("hidden");
    } else {
        emptyState?.classList.remove("hidden");
    }

    updateParentSelectOptions();
});


// Canvas Helpers
function canvasZoomIn() {
    if (!cy) return;
    cy.zoom(cy.zoom() * 1.2);
}

function canvasZoomOut() {
    if (!cy) return;
    cy.zoom(cy.zoom() * 0.8);
}

function canvasFit() {
    if (!cy) return;
    cy.fit(cy.elements(), 50);
}


// ============================================================
// FINAL ARCHITECTURE LAYOUT ENGINE
//
// Design principle:
//
// Semantic Graph
//        ↓
// Pattern Detection
//        ↓
// Semantic Roles
//        ↓
// Architecture Layers
//        ↓
// Peer Ordering
//        ↓
// Boundary / Zone Layout
//        ↓
// Orthogonal Connector Routing
//
// No hard-coded coordinates for individual vendors or prompts.
// ============================================================


function inferPatternFromCanvas() {

    if (!cy) return "generic";

    const explicit =
        String(cy.data("pattern") || "")
            .toLowerCase();

    if (
        explicit &&
        !["generic", "unknown"].includes(explicit)
    ) {
        return explicit;
    }

    const text =
        cy.nodes()
            .filter(
                n =>
                    n.data("type") !== "group" &&
                    n.data("type") !== "layout_zone"
            )
            .map(n =>
                [
                    n.data("label"),
                    n.data("category"),
                    n.data("role"),
                    n.data("icon")
                ]
                    .filter(Boolean)
                    .join(" ")
            )
            .join(" ")
            .toLowerCase();


    // Identity / IAM Architecture
    if (
        /saviynt|identity governance|\biga\b|\biam\b|active directory|entra|okta|scim|ldap/
            .test(text)
    ) {
        return "iam";
    }


    // Event Driven Architecture
    if (
        /kafka|rabbitmq|pubsub|service bus|event bus|event-driven/
            .test(text)
    ) {
        return "event_driven";
    }


    // Data Pipeline
    if (
        /ingest|etl|pipeline|warehouse|lakehouse|transform|bigquery/
            .test(text)
    ) {
        return "data_pipeline";
    }


    // Microservices
    if (
        /kubernetes|microservice|api gateway|service mesh/
            .test(text)
    ) {
        return "microservices";
    }


    // Hybrid Cloud
    if (
        /direct connect|expressroute|on-prem|hybrid cloud|vpn/
            .test(text)
    ) {
        return "hybrid_cloud";
    }


    // Three Tier
    if (
        /(load balancer|alb|application gateway|web tier)/
            .test(text) &&
        /(rds|database|sql|data tier)/
            .test(text)
    ) {
        return "three_tier";
    }


    return "generic";
}


// Normalize node information for semantic analysis
function nodeText(node) {

    return [
        node.data("label"),
        node.data("category"),
        node.data("role"),
        node.data("provider"),
        node.data("icon")
    ]
        .filter(Boolean)
        .join(" ")
        .toLowerCase();
}


// ============================================================
// SEMANTIC ROLE ENGINE
//
// AI provides role where possible.
//
// Renderer also infers roles as a safety net.
//
// This allows arbitrary prompts instead of brittle templates.
// ============================================================

function semanticRole(node, pattern = "generic") {

    const explicit =
        String(
            node.data("role") || ""
        ).toLowerCase();

    const text = nodeText(node);


    // Preserve explicit architecture role
    if (
        explicit &&
        explicit !== "peer_service"
    ) {
        return explicit;
    }


    // Primary IAM / Architecture Platform
    if (/saviynt/.test(text)) {
        return "primary_component";
    }


    // Identity Source
    if (
        /active directory|\bldap\b/
            .test(text)
    ) {
        return "identity_source";
    }


    // Identity Provider
    if (
        /entra|okta|identity provider|azure active directory/
            .test(text)
    ) {
        return "identity_provider";
    }


    // Event Backbone
    if (
        /kafka|rabbitmq|pubsub|service bus|event bus/
            .test(text)
    ) {
        return "event_backbone";
    }


    // External Actor
    if (
        /user|employee|customer|admin|browser|mobile app|client/
            .test(text)
    ) {
        return "external_actor";
    }


    // IAM Target Systems
    if (
        pattern === "iam" &&
        /servicenow|salesforce|workday|aws iam|application/
            .test(text)
    ) {
        return "target_application";
    }


    // Architecture Entry Point
    if (
        /api gateway|load balancer|cloudfront|ingress/
            .test(text)
    ) {
        return "entry_point";
    }


    // Data Store
    if (
        /database|rds|sql|warehouse|storage|s3|gcs/
            .test(text)
    ) {
        return "data_store";
    }


    return explicit || "peer_service";
}


// Remove synthetic layout-only nodes
function clearLayoutArtifacts() {

    if (!cy) return;

    cy.nodes()
        .filter(
            node =>
                node.data("type") === "layout_zone" ||
                node.data("synthetic") === true
        )
        .remove();
}


// ============================================================
// VISUAL HIERARCHY
//
// Enterprise architecture diagrams should visually distinguish:
//
// Primary Component
// Event Backbone
// Identity Provider
// Standard Services
// ============================================================

function setVisualHierarchy(nodes, pattern) {

    nodes.forEach(node => {

        const role =
            semanticRole(node, pattern);

        const primary =
            role === "primary_component" ||
            String(
                node.data("importance") || ""
            ).toLowerCase() === "primary";


        node.data("role", role);

        node.data(
            "importance",
            primary
                ? "primary"
                : "normal"
        );


        // Primary Architecture Component
        if (primary) {

            node.style({

                width: 132,

                height: 92,

                "border-width": 3,

                "font-size": 12,

                "font-weight": 700,

                "background-width": "50%",

                "background-height": "50%",

                "text-max-width": 155
            });

            return;
        }


        // Event Backbone
        if (
            role === "event_backbone"
        ) {

            node.style({

                width: 90,

                height: 72,

                "border-width": 3,

                "font-size": 11,

                "font-weight": 700
            });

            return;
        }


        // Identity Provider
        if (
            role === "identity_provider"
        ) {

            node.style({

                width: 72,

                height: 72,

                "border-width": 3,

                "font-size": 10
            });

            return;
        }


        // Standard Enterprise Component
        node.style({

            width: 60,

            height: 60,

            "border-width": 2,

            "font-size": 10,

            "font-weight": 500
        });

    });
}


// ============================================================
// ROLE → LAYER RANK
//
// The architecture pattern determines the default visual flow.
//
// This is intentionally semantic rather than vendor-specific.
// ============================================================

function roleRank(role, pattern) {

    const iam = {

        external_actor: 0,

        identity_source: 1,

        identity_provider: 2,

        primary_component: 3,

        target_application: 4
    };


    const event = {

        external_actor: 0,

        entry_point: 0,

        event_producer: 1,

        event_backbone: 2,

        event_consumer: 3,

        data_store: 4
    };


    const pipeline = {

        external_actor: 0,

        source: 0,

        entry_point: 1,

        ingestion: 1,

        processing: 2,

        transformation: 2,

        data_store: 3,

        analytics: 4
    };


    const micro = {

        external_actor: 0,

        entry_point: 1,

        primary_component: 2,

        peer_service: 2,

        data_store: 3
    };


    let map = {};


    switch (pattern) {

        case "iam":
            map = iam;
            break;

        case "event_driven":
            map = event;
            break;

        case "data_pipeline":
            map = pipeline;
            break;

        case "microservices":
            map = micro;
            break;

        default:
            map = {};
    }


    if (
        Object.prototype.hasOwnProperty.call(
            map,
            role
        )
    ) {
        return map[role];
    }


    return null;
}


// ============================================================
// GENERIC LAYER INFERENCE
//
// Used when AI did not provide a reliable layer.
//
// Architecture flows:
//
// Users
//   ↓
// Edge
//   ↓
// Application
//   ↓
// Integration
//   ↓
// Data
// ============================================================

function inferGenericLayer(node, pattern) {

    const role =
        semanticRole(node, pattern);

    const text =
        nodeText(node);


    const patternRank =
        roleRank(role, pattern);

    if (
        patternRank !== null
    ) {
        return patternRank;
    }


    // External Actors
    if (
        role === "external_actor" ||
        /user|client|browser|mobile/
            .test(text)
    ) {
        return 0;
    }


    // Edge / Network
    if (
        role === "entry_point" ||
        /gateway|load balancer|alb|dns|cloudfront|firewall/
            .test(text)
    ) {
        return 1;
    }


    // Identity
    if (
        role === "identity_source" ||
        role === "identity_provider"
    ) {
        return 1;
    }


    // Primary / Application
    if (
        role === "primary_component"
    ) {
        return 2;
    }


    // Integration
    if (
        role === "integration" ||
        role === "event_backbone" ||
        /kafka|queue|topic|bus|pubsub|rabbitmq/
            .test(text)
    ) {
        return 3;
    }


    // Data
    if (
        role === "data_store" ||
        /database|storage|warehouse|sql|rds|s3|gcs/
            .test(text)
    ) {
        return 4;
    }


    // Target Applications
    if (
        role === "target_application"
    ) {
        return 4;
    }


    return 2;
}


// ============================================================
// GRAPH DEPTH ANALYSIS
//
// Used to preserve actual connectivity.
//
// This prevents a disconnected semantic layer from
// destroying a meaningful dependency flow.
// ============================================================

function graphDepthMap(nodes, edges) {

    const nodeIds =
        new Set(
            nodes.map(
                n => n.id()
            )
        );


    const incoming = new Map();

    const outgoing = new Map();


    nodes.forEach(node => {

        incoming.set(
            node.id(),
            []
        );

        outgoing.set(
            node.id(),
            []
        );
    });


    edges.forEach(edge => {

        const source =
            edge.source().id();

        const target =
            edge.target().id();


        if (
            !nodeIds.has(source) ||
            !nodeIds.has(target)
        ) {
            return;
        }


        outgoing
            .get(source)
            .push(target);

        incoming
            .get(target)
            .push(source);
    });


    const roots =
        nodes
            .filter(
                node =>
                    incoming
                        .get(node.id())
                        .length === 0
            )
            .map(
                node => node.id()
            );


    const depth = new Map();


    roots.forEach(
        id => depth.set(id, 0)
    );


    const queue =
        [...roots];


    while (
        queue.length
    ) {

        const current =
            queue.shift();

        const currentDepth =
            depth.get(current) || 0;


        const children =
            outgoing.get(current) || [];


        children.forEach(child => {

            const nextDepth =
                currentDepth + 1;

            const previous =
                depth.get(child);


            if (
                previous === undefined ||
                nextDepth > previous
            ) {

                depth.set(
                    child,
                    nextDepth
                );

                queue.push(child);
            }

        });
    }


    // Handle cycles / disconnected graphs
    nodes.forEach(node => {

        if (
            !depth.has(node.id())
        ) {

            depth.set(
                node.id(),
                0
            );
        }

    });


    return depth;
}
// ============================================================
// ENTERPRISE ROLE ORDER
//
// Defines the natural left → right reading order.
//
// The actual AI-generated layer takes precedence.
// This is the fallback semantic ordering.
// ============================================================

function roleOrder(pattern) {

    const common = [

        "external_actor",

        "entry_point",

        "security_control",

        "identity_source",

        "identity_provider",

        "primary_component",

        "peer_service",

        "integration",

        "event_backbone",

        "data_store",

        "target_application",

        "observability"
    ];


    const patterns = {

        iam: [

            "external_actor",

            "identity_source",

            "identity_provider",

            "primary_component",

            "integration",

            "target_application",

            "observability"
        ],


        event_driven: [

            "external_actor",

            "entry_point",

            "event_producer",

            "event_backbone",

            "event_consumer",

            "data_store"
        ],


        data_pipeline: [

            "source",

            "ingestion",

            "processing",

            "transformation",

            "data_store",

            "analytics"
        ],


        microservices: [

            "external_actor",

            "entry_point",

            "primary_component",

            "peer_service",

            "integration",

            "data_store"
        ],


        hybrid_cloud: [

            "external_actor",

            "entry_point",

            "identity_provider",

            "primary_component",

            "integration",

            "data_store",

            "target_application"
        ]
    };


    return patterns[pattern] || common;
}


// ============================================================
// SEMANTIC EDGE STYLING
//
// Connector appearance communicates architecture meaning.
//
// Sync        → Solid
// Async       → Dashed
// Auth        → Blue
// Data        → Green
// Monitoring  → Subtle
// ============================================================

function edgeSemanticStyle() {

    if (!cy) return;


    cy.edges().forEach(edge => {

        const kind =
            String(
                edge.data("kind") || "sync"
            ).toLowerCase();


        const direction =
            String(
                edge.data("direction") || "forward"
            ).toLowerCase();


        const importance =
            String(
                edge.data("importance") || "normal"
            ).toLowerCase();


        const style = {

            "line-style":
                kind === "async"
                    ? "dashed"
                    : "solid",

            "target-arrow-shape":
                "triangle",

            "source-arrow-shape":
                direction === "bidirectional"
                    ? "triangle"
                    : "none",

            "width":

                importance === "primary"
                    ? 3

                    : importance === "supporting"
                        ? 1

                        : 2,

            "curve-style":
                "taxi",

            "taxi-direction":
                "rightward",

            "taxi-turn":
                "45%",

            "taxi-turn-min-distance":
                30
        };


        if (kind === "auth") {

            Object.assign(style, {

                "line-color":
                    "#4a78ff",

                "target-arrow-color":
                    "#4a78ff",

                "source-arrow-color":
                    "#4a78ff"
            });
        }


        if (kind === "async") {

            Object.assign(style, {

                "line-color":
                    "#a56eff",

                "target-arrow-color":
                    "#a56eff",

                "source-arrow-color":
                    "#a56eff"
            });
        }


        if (kind === "data") {

            Object.assign(style, {

                "line-color":
                    "#36b37e",

                "target-arrow-color":
                    "#36b37e",

                "source-arrow-color":
                    "#36b37e"
            });
        }


        edge.style(style);
    });
}


// ============================================================
// PEER ORDERING
//
// Components inside the same layer should not be randomly
// ordered between diagram generations.
//
// Priority:
//
// 1. Primary component
// 2. Explicit peerGroup
// 3. Connectivity
// 4. Alphabetical label
// ============================================================

function sortLayerNodes(
    nodes,
    depthMap
) {

    return [...nodes].sort(
        (a, b) => {

            const aPrimary =
                a.data("importance") === "primary"
                    ? 0
                    : 1;

            const bPrimary =
                b.data("importance") === "primary"
                    ? 0
                    : 1;


            if (aPrimary !== bPrimary) {

                return (
                    aPrimary -
                    bPrimary
                );
            }


            const aGroup =
                String(
                    a.data("peerGroup") || ""
                );

            const bGroup =
                String(
                    b.data("peerGroup") || ""
                );


            if (
                aGroup !== bGroup
            ) {

                return aGroup.localeCompare(
                    bGroup
                );
            }


            const aDepth =
                depthMap.get(
                    a.id()
                ) || 0;

            const bDepth =
                depthMap.get(
                    b.id()
                ) || 0;


            if (
                aDepth !== bDepth
            ) {

                return (
                    aDepth -
                    bDepth
                );
            }


            return String(
                a.data("label") || a.id()
            ).localeCompare(
                String(
                    b.data("label") || b.id()
                )
            );
        }
    );
}


// ============================================================
// MAIN ENTERPRISE AUTO LAYOUT
//
// This intentionally does NOT use:
//
// dagre
// breadthfirst
// cose
// random
//
// Generic graph algorithms are useful for graphs,
// but enterprise architecture diagrams require:
//
// semantic layers
// peer alignment
// visual hierarchy
// readable architecture flow
// ============================================================

function canvasAutoLayout() {

    if (
        !cy ||
        cy.nodes().length === 0
    ) {
        return;
    }


    // Remove artifacts from any previous layout
    clearLayoutArtifacts();


    const pattern =
        cy.data("pattern") ||
        inferPatternFromCanvas();


    const nodes =
        cy.nodes()
            .filter(
                node =>
                    node.data("type") !== "group" &&
                    node.data("type") !== "layout_zone"
            );


    const edges =
        cy.edges();


    // Apply role normalization first
    nodes.forEach(node => {

        const role =
            semanticRole(
                node,
                pattern
            );

        node.data(
            "role",
            role
        );
    });


    // Apply visual hierarchy
    setVisualHierarchy(
        nodes,
        pattern
    );


    // Build graph depth information
    const depthMap =
        graphDepthMap(
            [...nodes],
            [...edges]
        );


    // ========================================================
    // CREATE SEMANTIC LAYERS
    // ========================================================

    const columns =
        new Map();


    nodes.forEach(node => {

        const explicitLayer =
            Number(
                node.data("layer")
            );


        let layer;


        // AI-provided layer
        if (
            Number.isFinite(
                explicitLayer
            )
        ) {

            layer =
                explicitLayer;

        } else {

            layer =
                inferGenericLayer(
                    node,
                    pattern
                );
        }


        if (
            !columns.has(layer)
        ) {

            columns.set(
                layer,
                []
            );
        }


        columns
            .get(layer)
            .push(node);
    });


    // ========================================================
    // SORT LAYERS
    // ========================================================

    const layerKeys =
        [...columns.keys()]
            .sort(
                (a, b) => a - b
            );


    // ========================================================
    // ENTERPRISE SPACING
    // ========================================================

    const baseX =
        160;


    const layerGap =
        230;


    const peerGap =
        125;


    const centerY =
        360;


    // ========================================================
    // PLACE LAYERS
    // ========================================================

    layerKeys.forEach(
        (
            layer,
            columnIndex
        ) => {

            const column =
                sortLayerNodes(
                    columns.get(layer),
                    depthMap
                );


            const x =
                baseX +
                (
                    columnIndex *
                    layerGap
                );


            // Keep peer components
            // centered around the main flow
            const totalHeight =
                (
                    column.length - 1
                ) *
                peerGap;


            const startY =
                centerY -
                (
                    totalHeight / 2
                );


            column.forEach(
                (
                    node,
                    index
                ) => {

                    const y =
                        startY +
                        (
                            index *
                            peerGap
                        );


                    node.position({

                        x,

                        y
                    });
                }
            );
        }
    );


    // ========================================================
    // IAM COMPOSITION
    //
    // Identity diagrams are frequently generated by this app,
    // so we apply architecture constraints rather than a fixed
    // template.
    // ========================================================

    if (
        pattern === "iam"
    ) {

        const byRole =
            role =>
                nodes.filter(
                    node =>
                        node.data("role") === role
                );


        const actors =
            byRole(
                "external_actor"
            );


        const sources =
            byRole(
                "identity_source"
            );


        const providers =
            byRole(
                "identity_provider"
            );


        const primary =
            byRole(
                "primary_component"
            );


        const targets =
            byRole(
                "target_application"
            );


        const placeColumn =
            (
                list,
                x
            ) => {

                const total =
                    (
                        list.length - 1
                    ) *
                    peerGap;


                const start =
                    centerY -
                    (
                        total / 2
                    );


                list.forEach(
                    (
                        node,
                        index
                    ) => {

                        node.position({

                            x,

                            y:
                                start +
                                (
                                    index *
                                    peerGap
                                )
                        });
                    }
                );
            };


        let x =
            130;


        placeColumn(
            actors,
            x
        );


        x += 200;


        placeColumn(
            sources,
            x
        );


        x += 220;


        placeColumn(
            providers,
            x
        );


        x += 240;


        placeColumn(
            primary,
            x
        );


        x += 270;


        placeColumn(
            targets,
            x
        );
    }


    // ========================================================
    // EVENT DRIVEN COMPOSITION
    //
    // The event backbone becomes the visual center.
    // ========================================================

    if (
        pattern ===
        "event_driven"
    ) {

        const backbone =
            nodes.filter(
                node =>
                    node.data("role") ===
                    "event_backbone"
            );


        backbone.forEach(
            (
                node,
                index
            ) => {

                node.position({

                    x: 560,

                    y:
                        centerY +
                        (
                            index *
                            110
                        )
                });
            }
        );
    }


    // ========================================================
    // DATA PIPELINE COMPOSITION
    // ========================================================

    if (
        pattern ===
        "data_pipeline"
    ) {

        const sourceNodes =
            nodes.filter(
                node =>
                    node.data("role") ===
                    "source"
            );


        const ingestionNodes =
            nodes.filter(
                node =>
                    node.data("role") ===
                    "ingestion"
            );


        const processingNodes =
            nodes.filter(
                node =>
                    node.data("role") ===
                    "processing"
            );


        const storageNodes =
            nodes.filter(
                node =>
                    node.data("role") ===
                    "data_store"
            );


        const place =
            (
                list,
                x
            ) => {

                const height =
                    (
                        list.length - 1
                    ) *
                    peerGap;


                list.forEach(
                    (
                        node,
                        index
                    ) => {

                        node.position({

                            x,

                            y:
                                centerY -
                                (
                                    height / 2
                                ) +
                                (
                                    index *
                                    peerGap
                                )
                        });
                    }
                );
            };


        place(
            sourceNodes,
            130
        );

        place(
            ingestionNodes,
            360
        );

        place(
            processingNodes,
            600
        );

        place(
            storageNodes,
            850
        );
    }


    // ========================================================
    // COMPOUND BOUNDARIES
    //
    // Preserve groups generated by the AI.
    //
    // Important:
    // Groups must be positioned AFTER child nodes.
    // ========================================================

    const groups =
        cy.nodes(
            '[type = "group"]'
        );


    const originalParents =
        new Map();


    groups.forEach(group => {

        originalParents.set(
            group.id(),
            group.data("parent") ||
            null
        );
    });


    // Temporarily detach groups
    // so child positions remain absolute.
    groups.forEach(group => {

        group.move({
            parent: null
        });
    });


    nodes.forEach(node => {

        node.move({
            parent: null
        });
    });


    // Group nesting depth
    const groupDepth =
        group => {

            let depth =
                0;


            let parent =
                originalParents.get(
                    group.id()
                );


            while (parent) {

                depth++;

                parent =
                    originalParents.get(
                        parent
                    );
            }


            return depth;
        };


    // Process inner groups first
    const orderedGroups =
        [...groups]
            .sort(
                (a, b) =>
                    groupDepth(b) -
                    groupDepth(a)
            );


    orderedGroups.forEach(group => {

        const members =
            nodes.filter(
                node =>
                    node.data("parent") ===
                    group.id()
            );


        if (
            members.length === 0
        ) {
            return;
        }


        const bb =
            members.boundingBox({

                includeLabels: true,

                includeOverlays: false
            });


        const padding =
            45;


        group.position({

            x:
                bb.x1 +
                (
                    bb.w / 2
                ),

            y:
                bb.y1 +
                (
                    bb.h / 2
                )
        });


        group.style({

            width:
                Math.max(
                    180,
                    bb.w +
                    (
                        padding * 2
                    )
                ),

            height:
                Math.max(
                    140,
                    bb.h +
                    (
                        padding * 2
                    )
                )
        });
    });


    // Restore node parents
    nodes.forEach(node => {

        const parent =
            node.data("parent");

        if (parent) {

            node.move({

                parent
            });
        }
    });


    // Restore nested group parents
    orderedGroups
        .reverse()
        .forEach(group => {

            const parent =
                originalParents.get(
                    group.id()
                );

            if (parent) {

                group.move({

                    parent
                });
            }
        });


    // ========================================================
    // SEMANTIC EDGE STYLING
    // ========================================================

    edgeSemanticStyle();


    // ========================================================
    // FINAL ORTHOGONAL CONNECTOR ROUTING
    //
    // IMPORTANT:
    //
    // Do NOT use:
    //
    // cy.edges().style(...).update()
    //
    // That API caused the original browser error.
    //
    // Use edge.style() directly instead.
    // ========================================================

    cy.edges().forEach(edge => {

        edge.style({

            "curve-style":
                "taxi",

            "taxi-direction":
                "rightward",

            "taxi-turn":
                "50%",

            "taxi-turn-min-distance":
                30
        });
    });


    // ========================================================
    // FIT ENTERPRISE DIAGRAM
    // ========================================================

    cy.fit(
        cy.elements(),
        80
    );
}
// ============================================================
// PROJECT MANAGEMENT
// ============================================================

async function loadProjects() {

    const selector =
        document.getElementById(
            "project-selector"
        );

    if (!selector) return;

    try {

        const res =
            await fetch(
                "/api/projects",
                {
                    cache: "no-store"
                }
            );

        if (!res.ok) {
            throw new Error(
                `Failed to load projects: ${res.status}`
            );
        }

        const projects =
            await res.json();


        selector.innerHTML = "";


        if (
            !Array.isArray(projects) ||
            projects.length === 0
        ) {

            currentProjectId = "";

            const option =
                document.createElement(
                    "option"
                );

            option.value = "";
            option.textContent =
                "No projects";

            selector.appendChild(
                option
            );

            return;
        }


        projects.forEach(project => {

            if (
                !project ||
                !project.id
            ) {
                return;
            }


            const option =
                document.createElement(
                    "option"
                );

            option.value =
                project.id;

            option.textContent =
                project.name ||
                project.id;

            selector.appendChild(
                option
            );
        });


        currentProjectId =
            projects[0].id;


        selector.value =
            currentProjectId;


        selector.addEventListener(
            "change",
            event => {

                currentProjectId =
                    event.target.value;

                currentDiagramId = "";
                currentVersion = 1;

                loadProjectDiagrams();
            }
        );


        loadProjectDiagrams();

    } catch (e) {

        console.error(
            "Error loading projects",
            e
        );
    }
}


// ============================================================
// NEW PROJECT
// ============================================================

const btnNewProj =
    document.getElementById(
        "btn-new-project"
    );


if (btnNewProj) {

    btnNewProj.addEventListener(
        "click",
        () => {

            const modal =
                document.getElementById(
                    "new-project-modal"
                );

            modal?.classList.remove(
                "hidden"
            );
        }
    );
}


function closeNewProjectModal() {

    const modal =
        document.getElementById(
            "new-project-modal"
        );

    modal?.classList.add(
        "hidden"
    );
}


async function createNewProject() {

    const input =
        document.getElementById(
            "new-project-name"
        );

    if (!input) return;


    const name =
        input.value.trim();


    if (!name) {

        alert(
            "Please enter a project name."
        );

        return;
    }


    try {

        const res =
            await fetch(
                "/api/projects",
                {

                    method: "POST",

                    headers: {
                        "Content-Type":
                            "application/json"
                    },

                    body:
                        JSON.stringify({
                            name
                        })
                }
            );


        if (!res.ok) {

            throw new Error(
                `Project creation failed: ${res.status}`
            );
        }


        const project =
            await res.json();


        if (
            !project ||
            !project.id
        ) {

            throw new Error(
                "Invalid project response"
            );
        }


        const selector =
            document.getElementById(
                "project-selector"
            );


        if (selector) {

            const option =
                document.createElement(
                    "option"
                );

            option.value =
                project.id;

            option.textContent =
                project.name ||
                name;

            selector.appendChild(
                option
            );

            selector.value =
                project.id;
        }


        currentProjectId =
            project.id;


        currentDiagramId = "";

        currentVersion = 1;


        closeNewProjectModal();


        input.value = "";


        if (cy) {

            cy.elements().remove();

            cy.data(
                "pattern",
                "generic"
            );

            cy.data(
                "explicitGroups",
                []
            );
        }

    } catch (e) {

        console.error(
            "Error creating project",
            e
        );

        alert(
            "Failed to create project."
        );
    }
}


// ============================================================
// LOAD PROJECT DIAGRAMS
// ============================================================

async function loadProjectDiagrams() {

    if (!currentProjectId) return;

    try {

        const res =
            await fetch(
                `/api/projects/${encodeURIComponent(
                    currentProjectId
                )}/diagrams`,
                {
                    cache: "no-store"
                }
            );


        if (!res.ok) {

            throw new Error(
                `Failed to load diagrams: ${res.status}`
            );
        }


        const diagrams =
            await res.json();


        if (
            Array.isArray(diagrams) &&
            diagrams.length > 0
        ) {

            await loadDiagram(
                diagrams[0].id
            );

        } else {

            if (cy) {

                cy.elements().remove();

                cy.data(
                    "pattern",
                    "generic"
                );

                cy.data(
                    "explicitGroups",
                    []
                );
            }


            currentDiagramId = "";

            currentVersion = 1;
        }

    } catch (e) {

        console.error(
            "Error loading diagrams",
            e
        );
    }
}


// ============================================================
// LOAD SAVED DIAGRAM
// ============================================================

async function loadDiagram(diagramId) {

    if (!diagramId) return;

    try {

        const res =
            await fetch(
                `/api/diagrams/${encodeURIComponent(
                    diagramId
                )}`,
                {
                    cache: "no-store"
                }
            );


        if (!res.ok) {

            throw new Error(
                `Failed to load diagram: ${res.status}`
            );
        }


        const diagram =
            await res.json();


        if (!diagram) {

            throw new Error(
                "Invalid diagram response"
            );
        }


        currentDiagramId =
            diagram.id ||
            diagramId;


        currentVersion =
            Number(
                diagram.version
            ) || 1;


        renderTopology(
            diagram.topology_json
        );

    } catch (e) {

        console.error(
            "Error loading diagram",
            e
        );
    }
}


// ============================================================
// ICON URL RESOLUTION
//
// Resolution order:
//
// 1. Registered static icon
// 2. Built-in SVG icon
// 3. Custom uploaded icon
// 4. Generic server fallback
// ============================================================

function resolveIconUrl(icon) {

    if (!icon) {
        return getIconUri(
            "server"
        );
    }


    // Built-in SVG registry
    const builtIn =
        getIconUri(icon);

    if (builtIn) {
        return builtIn;
    }


    // Registered static icons
    const normalized =
        String(icon)
            .trim()
            .toLowerCase();


    const registry =
        window.ICON_REGISTRY ||
        {};


    if (
        registry[normalized]
    ) {

        return registry[
            normalized
        ];
    }


    // Conventional static path fallback
    const staticCandidates = [

        `/static/icons/${normalized}.svg`,

        `/static/icons/${normalized}.png`
    ];


    if (
        staticCandidates.length
    ) {

        return staticCandidates[0];
    }


    return getIconUri(
        "server"
    );
}


// ============================================================
// TOPOLOGY NORMALIZATION
//
// Gemini may occasionally produce:
//
// - duplicate IDs
// - invalid parent IDs
// - duplicate edges
// - self edges
// - incomplete data objects
//
// This renderer must never crash because of AI output.
// ============================================================

function normalizeTopology(dsl) {

    const source =
        dsl &&
        typeof dsl === "object"
            ? dsl
            : {};


    const rawNodes =
        Array.isArray(
            source.nodes
        )
            ? source.nodes
            : [];


    const rawGroups =
        Array.isArray(
            source.groups
        )
            ? source.groups
            : [];


    const rawEdges =
        Array.isArray(
            source.edges
        )
            ? source.edges
            : [];


    const usedIds =
        new Set();


    const groups = [];


    rawGroups.forEach(
        (
            group,
            index
        ) => {

            if (
                !group ||
                !group.id
            ) {
                return;
            }


            const id =
                String(
                    group.id
                )
                    .trim();


            if (
                !id ||
                usedIds.has(id)
            ) {
                return;
            }


            usedIds.add(id);


            groups.push({

                id,

                label:
                    group.label ||
                    id,

                type:
                    group.type ||
                    "generic",

                parentId:
                    group.parentId ||
                    null,

                role:
                    group.role ||
                    "boundary"
            });
        }
    );


    const groupIds =
        new Set(
            groups.map(
                group =>
                    group.id
            )
        );


    const nodes = [];


    rawNodes.forEach(
        (
            node,
            index
        ) => {

            if (
                !node ||
                !node.id
            ) {
                return;
            }


            let id =
                String(
                    node.id
                )
                    .trim();


            if (!id) {

                id =
                    `node_${index + 1}`;
            }


            // Ensure node IDs never conflict
            // with group IDs or other nodes.
            if (
                usedIds.has(id)
            ) {

                let counter = 1;

                const base = id;

                while (
                    usedIds.has(
                        `${base}_${counter}`
                    )
                ) {
                    counter++;
                }

                id =
                    `${base}_${counter}`;
            }


            usedIds.add(id);


            const data =
                node.data &&
                typeof node.data ===
                "object"
                    ? node.data
                    : {};


            const parentId =
                node.parentId &&
                groupIds.has(
                    String(
                        node.parentId
                    )
                )
                    ? String(
                        node.parentId
                    )
                    : null;


            nodes.push({

                id,

                type:
                    node.type ||
                    "cloudIcon",

                parentId,

                data: {

                    label:
                        data.label ||
                        id,

                    icon:
                        data.icon ||
                        "server",

                    category:
                        data.category ||
                        "general",

                    layer:
                        Number.isFinite(
                            Number(
                                data.layer
                            )
                        )
                            ? Number(
                                data.layer
                            )
                            : null,

                    provider:
                        data.provider ||
                        "generic",

                    role:
                        data.role ||
                        "peer_service",

                    peerGroup:
                        data.peerGroup ||
                        "",

                    importance:
                        data.importance ||
                        "normal",

                    description:
                        data.description ||
                        "",

                    properties:
                        data.properties ||
                        {}
                }
            });
        }
    );


    const validNodeIds =
        new Set(
            nodes.map(
                node =>
                    node.id
            )
        );


    const seenEdges =
        new Set();


    const edges = [];


    rawEdges.forEach(
        (
            edge,
            index
        ) => {

            if (!edge) return;


            const sourceId =
                String(
                    edge.source || ""
                );


            const targetId =
                String(
                    edge.target || ""
                );


            if (
                !validNodeIds.has(
                    sourceId
                ) ||
                !validNodeIds.has(
                    targetId
                ) ||
                sourceId === targetId
            ) {
                return;
            }


            const data =
                edge.data &&
                typeof edge.data ===
                "object"
                    ? edge.data
                    : {};


            const label =
                edge.label ||
                data.protocol ||
                "";


            const kind =
                data.kind ||
                "sync";


            const duplicateKey =
                [
                    sourceId,

                    targetId,

                    label,

                    kind
                ].join("|");


            if (
                seenEdges.has(
                    duplicateKey
                )
            ) {
                return;
            }


            seenEdges.add(
                duplicateKey
            );


            edges.push({

                id:
                    edge.id
                        ? String(edge.id)
                        : `edge_${index + 1}_${sourceId}_${targetId}`,

                source:
                    sourceId,

                target:
                    targetId,

                label,

                data: {

                    protocol:
                        data.protocol ||
                        "",

                    encrypted:
                        Boolean(
                            data.encrypted
                        ),

                    direction:
                        data.direction ||
                        "forward",

                    kind,

                    importance:
                        data.importance ||
                        "normal"
                }
            });
        }
    );


    return {

        diagramType:
            source.diagramType ||
            "architecture",

        pattern:
            source.pattern ||
            "generic",

        groups,

        nodes,

        edges
    };
}


// ============================================================
// RENDER TOPOLOGY
//
// This is intentionally defensive.
//
// AI output should NEVER be able to break
// the browser UI.
// ============================================================

function renderTopology(dsl) {

    if (!cy) return;


    const topology =
        normalizeTopology(
            dsl
        );


    try {

        cy.elements().remove();


        cy.data(
            "pattern",
            topology.pattern ||
            "generic"
        );


        cy.data(
            "explicitGroups",
            topology.groups
        );


        const elements = [];


        // ----------------------------------------------------
        // Groups
        //
        // Groups are stored as metadata first.
        //
        // Nodes are rendered independently so the
        // auto-layout engine controls their positions.
        // ----------------------------------------------------

        topology.groups.forEach(
            group => {

                elements.push({

                    data: {

                        id:
                            group.id,

                        label:
                            group.label,

                        type:
                            "group",

                        group_type:
                            group.type,

                        role:
                            group.role ||
                            "boundary"
                    }
                });
            }
        );


        // ----------------------------------------------------
        // Architecture Nodes
        // ----------------------------------------------------

        topology.nodes.forEach(
            node => {

                const data =
                    node.data ||
                    {};


                const icon =
                    data.icon ||
                    "server";


                const custom =
                    (
                        customIcons ||
                        []
                    ).find(
                        customIcon =>
                            customIcon &&
                            customIcon.tag ===
                            icon
                    );


                const iconUrl =
                    custom?.url ||
                    resolveIconUrl(icon) ||
                    getIconUri("server");


                elements.push({

                    data: {

                        id:
                            node.id,

                        label:
                            data.label ||
                            node.id,

                        type:
                            node.type ||
                            "cloudIcon",

                        // Keep boundary information separate
                        // from Cytoscape compound parenting.
                        boundaryParent:
                            node.parentId ||
                            null,

                        icon,

                        icon_url:
                            iconUrl,

                        category:
                            data.category ||
                            "general",

                        layer:
                            Number.isFinite(
                                Number(
                                    data.layer
                                )
                            )
                                ? Number(
                                    data.layer
                                )
                                : null,

                        provider:
                            data.provider ||
                            "generic",

                        role:
                            data.role ||
                            "peer_service",

                        peerGroup:
                            data.peerGroup ||
                            "",

                        importance:
                            data.importance ||
                            "normal",

                        description:
                            data.description ||
                            "",

                        properties:
                            data.properties ||
                            {}
                    }
                });
            }
        );


        // ----------------------------------------------------
        // Architecture Edges
        // ----------------------------------------------------

        topology.edges.forEach(
            edge => {

                const data =
                    edge.data ||
                    {};


                elements.push({

                    data: {

                        id:
                            edge.id,

                        source:
                            edge.source,

                        target:
                            edge.target,

                        label:
                            edge.label ||
                            data.protocol ||
                            "",

                        protocol:
                            data.protocol ||
                            "",

                        encrypted:
                            Boolean(
                                data.encrypted
                            ),

                        direction:
                            data.direction ||
                            "forward",

                        kind:
                            data.kind ||
                            "sync",

                        importance:
                            data.importance ||
                            "normal"
                    }
                });
            }
        );


        // ----------------------------------------------------
        // Add everything in one transaction.
        // ----------------------------------------------------

        cy.batch(() => {

            cy.add(elements);

        });


        // ----------------------------------------------------
        // Layout after DOM / Cytoscape settle.
        // ----------------------------------------------------

        requestAnimationFrame(
            () => {

                try {

                    canvasAutoLayout();

                } catch (layoutError) {

                    console.error(
                        "Enterprise auto-layout failed",
                        layoutError
                    );

                    // Last-resort safe fallback
                    cy.layout({
                        name: "grid",
                        fit: true,
                        padding: 80
                    }).run();
                }

            }
        );

    } catch (error) {

        console.error(
            "Topology render failed",
            error
        );

        alert(
            "Unable to render this architecture topology. " +
            "Check browser console for details."
        );
    }
}


// ============================================================
// EXPORT TOPOLOGY DSL
//
// Export only meaningful architecture data.
//
// Synthetic layout elements must never be saved.
// ============================================================

function exportTopologyJSON() {

    if (!cy) {

        return {

            diagramType:
                "architecture",

            pattern:
                "generic",

            groups: [],

            nodes: [],

            edges: []
        };
    }


    const nodes = [];


    const groups =
        (
            cy.data(
                "explicitGroups"
            ) ||
            []
        )
            .map(
                group => ({

                    id:
                        group.id,

                    label:
                        group.label,

                    type:
                        group.type ||
                        "generic",

                    parentId:
                        group.parentId ||
                        null,

                    role:
                        group.role ||
                        "boundary"
                })
            );


    const edges = [];


    cy.nodes().forEach(node => {

        const type =
            node.data("type");


        // Never persist temporary layout artifacts
        if (
            type === "layout_zone" ||
            node.data("synthetic") === true
        ) {
            return;
        }


        // Groups are already stored in explicitGroups.
        if (
            type === "group"
        ) {
            return;
        }


        nodes.push({

            id:
                node.id(),

            type:
                type ||
                "cloudIcon",

            parentId:
                node.data(
                    "boundaryParent"
                ) ||
                null,

            data: {

                label:
                    node.data(
                        "label"
                    ),

                icon:
                    node.data(
                        "icon"
                    ) ||
                    "server",

                category:
                    node.data(
                        "category"
                    ) ||
                    "general",

                description:
                    node.data(
                        "description"
                    ) ||
                    "",

                layer:
                    node.data(
                        "layer"
                    ),

                provider:
                    node.data(
                        "provider"
                    ) ||
                    "generic",

                role:
                    node.data(
                        "role"
                    ) ||
                    "peer_service",

                peerGroup:
                    node.data(
                        "peerGroup"
                    ) ||
                    "",

                importance:
                    node.data(
                        "importance"
                    ) ||
                    "normal",

                properties:
                    node.data(
                        "properties"
                    ) ||
                    {}
            }
        });
    });


    cy.edges().forEach(edge => {

        edges.push({

            id:
                edge.id(),

            source:
                edge.source().id(),

            target:
                edge.target().id(),

            label:
                edge.data(
                    "label"
                ) ||
                "",

            data: {

                protocol:
                    edge.data(
                        "protocol"
                    ) ||
                    "",

                encrypted:
                    Boolean(
                        edge.data(
                            "encrypted"
                        )
                    ),

                direction:
                    edge.data(
                        "direction"
                    ) ||
                    "forward",

                kind:
                    edge.data(
                        "kind"
                    ) ||
                    "sync",

                importance:
                    edge.data(
                        "importance"
                    ) ||
                    "normal"
            }
        });
    });


    return {

        diagramType:
            "architecture",

        pattern:
            cy.data(
                "pattern"
            ) ||
            "generic",

        groups,

        nodes,

        edges
    };
}


// ============================================================
// EXPORT DIAGRAM
// ============================================================

function exportDiagram(format) {

    if (
        !cy ||
        cy.elements().length === 0
    ) {

        alert(
            "Nothing to export."
        );

        return;
    }


    const safeId =
        currentDiagramId ||
        "draft";


    if (
        format === "json"
    ) {

        const topology =
            exportTopologyJSON();


        const dataStr =
            "data:text/json;charset=utf-8," +
            encodeURIComponent(
                JSON.stringify(
                    topology,
                    null,
                    2
                )
            );


        const anchor =
            document.createElement(
                "a"
            );


        anchor.href =
            dataStr;

        anchor.download =
            `diagram_${safeId}.json`;


        document.body.appendChild(
            anchor
        );


        anchor.click();

        anchor.remove();

        return;
    }


    if (
        format === "png"
    ) {

        const pngContent =
            cy.png({

                output:
                    "blob",

                bg:
                    "#0c0c0e",

                scale:
                    2,

                full:
                    true
            });


        const anchor =
            document.createElement(
                "a"
            );


        const objectUrl =
            URL.createObjectURL(
                pngContent
            );


        anchor.href =
            objectUrl;


        anchor.download =
            `diagram_${safeId}.png`;


        document.body.appendChild(
            anchor
        );


        anchor.click();


        anchor.remove();


        setTimeout(
            () =>
                URL.revokeObjectURL(
                    objectUrl
                ),
            1000
        );

        return;
    }


    if (
        format === "svg"
    ) {

        alert(
            "SVG export requires the Cytoscape SVG extension. " +
            "PNG and JSON exports are fully supported."
        );

        return;
    }


    alert(
        `Unsupported export format: ${format}`
    );
}
// ============================================================
// SAVE DIAGRAM
// ============================================================

async function saveCurrentDiagram() {

    if (!currentProjectId) {

        alert(
            "Please create or select a project first."
        );

        return;
    }


    const topology =
        exportTopologyJSON();


    if (
        topology.nodes.length === 0 &&
        topology.groups.length === 0
    ) {

        alert(
            "Cannot save an empty diagram."
        );

        return;
    }


    const diagramId =
        currentDiagramId ||
        crypto.randomUUID();


    const payload = {

        id:
            diagramId,

        project_id:
            currentProjectId,

        topology_json:
            topology,

        version:
            currentVersion
    };


    try {

        const res =
            await fetch(
                "/api/diagrams",
                {

                    method:
                        "POST",

                    headers: {

                        "Content-Type":
                            "application/json"
                    },

                    body:
                        JSON.stringify(
                            payload
                        )
                }
            );


        if (!res.ok) {

            let detail =
                "Failed to save diagram.";

            try {

                const error =
                    await res.json();

                detail =
                    error.detail ||
                    detail;

            } catch (_) {}


            throw new Error(
                detail
            );
        }


        const saved =
            await res.json()
                .catch(
                    () => ({})
                );


        currentDiagramId =
            saved.id ||
            diagramId;


        if (
            saved.version
        ) {

            currentVersion =
                Number(
                    saved.version
                );

        }


        alert(
            "Diagram saved successfully!"
        );

    } catch (e) {

        console.error(
            "Save diagram failed",
            e
        );

        alert(
            e.message ||
            "Failed to save diagram."
        );
    }
}


// Save button
document.addEventListener(
    "DOMContentLoaded",
    () => {

        const btnSave =
            document.getElementById(
                "btn-save"
            );

        if (!btnSave) return;


        btnSave.addEventListener(
            "click",
            saveCurrentDiagram
        );
    }
);


// ============================================================
// CUSTOM ICONS
// ============================================================

async function loadCustomIcons() {

    try {

        const res =
            await fetch(
                "/api/icons",
                {
                    cache:
                        "no-store"
                }
            );


        if (!res.ok) {

            throw new Error(
                `Failed to load icons: ${res.status}`
            );
        }


        const data =
            await res.json();


        customIcons =
            Array.isArray(data)
                ? data
                : [];


        renderCustomIconList();

        populateInspectorIconSelect();

        populateToolbox();

    } catch (e) {

        console.error(
            "Custom icon loading failed",
            e
        );

        customIcons = [];
    }
}


function renderCustomIconList() {

    const list =
        document.getElementById(
            "icon-list"
        );


    if (!list) return;


    list.innerHTML = "";


    if (
        !Array.isArray(customIcons) ||
        customIcons.length === 0
    ) {

        list.innerHTML =
            `<p class="text-xs text-slate-500 text-center py-4">
                No custom icons uploaded yet.
            </p>`;

        return;
    }


    customIcons.forEach(icon => {

        if (!icon) return;


        const item =
            document.createElement(
                "div"
            );


        item.className =
            "flex items-center justify-between " +
            "bg-dark-900 border border-dark-50 " +
            "p-2.5 rounded-lg";


        const left =
            document.createElement(
                "div"
            );


        left.className =
            "flex items-center gap-2";


        const image =
            document.createElement(
                "img"
            );


        image.src =
            icon.url;

        image.alt =
            icon.tag ||
            "Custom icon";


        image.className =
            "w-8 h-8 object-contain " +
            "bg-dark-100 p-1.5 rounded";


        const text =
            document.createElement(
                "div"
            );


        const title =
            document.createElement(
                "div"
            );


        title.className =
            "text-xs font-bold text-white";


        title.textContent =
            icon.tag ||
            "Custom Icon";


        const description =
            document.createElement(
                "div"
            );


        description.className =
            "text-[9px] text-slate-400";


        description.textContent =
            icon.description ||
            "";


        text.appendChild(title);

        text.appendChild(description);


        left.appendChild(image);

        left.appendChild(text);


        const removeButton =
            document.createElement(
                "button"
            );


        removeButton.className =
            "p-1 hover:bg-red-500/10 " +
            "rounded text-red-500 " +
            "hover:text-red-400 transition-colors";


        removeButton.type =
            "button";


        removeButton.title =
            "Delete icon";


        removeButton.innerHTML =
            `<i data-lucide="trash-2"
                class="w-4 h-4"></i>`;


        removeButton.addEventListener(
            "click",
            () =>
                deleteCustomIcon(
                    icon.id
                )
        );


        item.appendChild(left);

        item.appendChild(
            removeButton
        );


        list.appendChild(
            item
        );
    });


    try {

        lucide.createIcons();

    } catch (_) {}
}


async function deleteCustomIcon(iconId) {

    if (!iconId) return;


    const confirmed =
        confirm(
            "Are you sure you want to delete this custom icon?"
        );


    if (!confirmed) return;


    try {

        const res =
            await fetch(
                `/api/icons/${encodeURIComponent(
                    iconId
                )}`,
                {

                    method:
                        "DELETE"
                }
            );


        if (!res.ok) {

            throw new Error(
                "Failed to delete icon"
            );
        }


        await loadCustomIcons();

    } catch (e) {

        console.error(
            "Icon deletion failed",
            e
        );

        alert(
            "Unable to delete icon."
        );
    }
}


// ============================================================
// GENERATE / REFINE ARCHITECTURE
// ============================================================

async function generateArchitecture() {

    const promptInput =
        document.getElementById(
            "prompt-input"
        );


    const loader =
        document.getElementById(
            "loader"
        );


    if (!promptInput) return;


    const prompt =
        promptInput.value.trim();


    if (!prompt) {

        promptInput.focus();

        return;
    }


    if (loader) {

        loader.classList.remove(
            "hidden"
        );
    }


    const hasDiagram =
        cy &&
        cy.nodes()
            .filter(
                n =>
                    n.data("type") !==
                    "group"
            )
            .length > 0;


    const endpoint =
        hasDiagram
            ? "/api/refine"
            : "/api/generate";


    const payload =
        hasDiagram
            ? {

                prompt,

                current_diagram:
                    exportTopologyJSON()
            }

            : {

                prompt
            };


    appendChatMessage(
        prompt,
        "user"
    );


    promptInput.value = "";


    try {

        const res =
            await fetch(
                endpoint,
                {

                    method:
                        "POST",

                    headers: {

                        "Content-Type":
                            "application/json"
                    },

                    body:
                        JSON.stringify(
                            payload
                        )
                }
            );


        const responseText =
            await res.text();


        let data;


        try {

            data =
                responseText
                    ? JSON.parse(
                        responseText
                    )
                    : {};

        } catch (_) {

            throw new Error(
                responseText ||
                "Invalid response from architecture agent."
            );
        }


        if (!res.ok) {

            throw new Error(
                data.detail ||
                data.message ||
                "Failed to generate architecture."
            );
        }


        // ----------------------------------------------------
        // Agent may return:
        //
        // topology directly
        //
        // OR
        //
        // {
        //   topology: {...},
        //   model: "...",
        //   ...
        // }
        // ----------------------------------------------------

        const topology =
            data.topology ||
            data.diagram ||
            data;


        if (
            !topology ||
            !Array.isArray(
                topology.nodes
            )
        ) {

            throw new Error(
                "Architecture agent returned an invalid topology."
            );
        }


        renderTopology(
            topology
        );


        // Refresh active model display.
        // This now reflects the backend's actual
        // successful model instead of a hard-coded
        // gemini-1.5-flash label.
        await initAuthStatus();


        if (hasDiagram) {

            currentVersion += 1;
        }


        appendChatMessage(

            hasDiagram
                ? "Architecture refined successfully. The layout has been regenerated using the updated architecture semantics."
                : "Architecture generated successfully. You can now refine it using natural language or edit components manually.",

            "bot"
        );

    } catch (e) {

        console.error(
            "Architecture generation failed",
            e
        );


        appendChatMessage(

            `Error: ${
                e.message ||
                "Failed to generate architecture."
            }`,

            "bot"
        );

    } finally {

        if (loader) {

            loader.classList.add(
                "hidden"
            );
        }
    }
}


// Generate button
document.addEventListener(
    "DOMContentLoaded",
    () => {

        const btn =
            document.getElementById(
                "btn-generate"
            );


        if (!btn) return;


        btn.addEventListener(
            "click",
            generateArchitecture
        );


        const prompt =
            document.getElementById(
                "prompt-input"
            );


        // Ctrl+Enter / Cmd+Enter
        prompt?.addEventListener(
            "keydown",
            event => {

                if (
                    event.key === "Enter" &&
                    (
                        event.ctrlKey ||
                        event.metaKey
                    )
                ) {

                    event.preventDefault();

                    generateArchitecture();
                }
            }
        );
    }
);


// ============================================================
// CHAT MESSAGE
//
// Uses textContent for user content instead of innerHTML
// to prevent prompt content from injecting HTML.
// ============================================================

function appendChatMessage(
    message,
    sender = "bot"
) {

    const list =
        document.getElementById(
            "chat-messages"
        );


    if (!list) return;


    const item =
        document.createElement(
            "div"
        );


    if (
        sender === "user"
    ) {

        item.className =
            "bg-brand-500/10 " +
            "border border-brand-500/20 " +
            "rounded-xl p-3.5 text-xs " +
            "text-slate-300 ml-8";


        const heading =
            document.createElement(
                "div"
            );


        heading.className =
            "font-semibold text-white mb-1";


        heading.textContent =
            "You";


        const body =
            document.createElement(
                "p"
            );


        body.className =
            "leading-relaxed whitespace-pre-wrap";


        body.textContent =
            message;


        item.appendChild(
            heading
        );

        item.appendChild(
            body
        );

    } else {

        item.className =
            "bg-dark-100/50 " +
            "border border-dark-50 " +
            "rounded-xl p-3.5 text-xs " +
            "text-slate-300 mr-8";


        const heading =
            document.createElement(
                "div"
            );


        heading.className =
            "flex items-center gap-2 mb-1.5";


        const icon =
            document.createElement(
                "span"
            );


        icon.className =
            "bg-brand-500/20 " +
            "text-brand-500 p-1 rounded-md";


        icon.innerHTML =
            `<i data-lucide="bot"
                class="w-3.5 h-3.5"></i>`;


        const title =
            document.createElement(
                "span"
            );


        title.className =
            "font-semibold text-white";


        title.textContent =
            "Architecture Agent";


        heading.appendChild(icon);

        heading.appendChild(title);


        const body =
            document.createElement(
                "p"
            );


        body.className =
            "leading-relaxed whitespace-pre-wrap";


        body.textContent =
            message;


        item.appendChild(
            heading
        );

        item.appendChild(
            body
        );
    }


    list.appendChild(
        item
    );


    list.scrollTop =
        list.scrollHeight;


    try {

        lucide.createIcons();

    } catch (_) {}
}


// ============================================================
// CUSTOM ICON UPLOAD
// ============================================================

function setupFormListeners() {

    const form =
        document.getElementById(
            "icon-upload-form"
        );


    if (!form) return;


    form.addEventListener(
        "submit",
        async event => {

            event.preventDefault();


            const tag =
                document
                    .getElementById(
                        "icon-tag"
                    )
                    ?.value
                    ?.trim() ||
                "";


            const description =
                document
                    .getElementById(
                        "icon-desc"
                    )
                    ?.value
                    ?.trim() ||
                "";


            const fileInput =
                document.getElementById(
                    "icon-file"
                );


            const file =
                fileInput?.files?.[0];


            if (!file) {

                alert(
                    "Please select an icon file."
                );

                return;
            }


            const formData =
                new FormData();


            formData.append(
                "tag",
                tag ||
                file.name
                    .replace(
                        /\.[^/.]+$/,
                        ""
                    )
            );


            formData.append(
                "description",
                description
            );


            formData.append(
                "file",
                file
            );


            try {

                const res =
                    await fetch(
                        "/api/icons/upload",
                        {

                            method:
                                "POST",

                            body:
                                formData
                        }
                    );


                const text =
                    await res.text();


                let data = {};

                try {

                    data =
                        text
                            ? JSON.parse(text)
                            : {};

                } catch (_) {}


                if (!res.ok) {

                    throw new Error(
                        data.detail ||
                        text ||
                        "Icon upload failed."
                    );
                }


                form.reset();


                await loadCustomIcons();


                alert(
                    "Icon uploaded successfully!"
                );

            } catch (e) {

                console.error(
                    "Icon upload failed",
                    e
                );


                alert(
                    e.message ||
                    "Error uploading icon."
                );
            }
        }
    );
}


// ============================================================
// TOOLBOX
//
// Standard icons + uploaded icons.
// ============================================================

function populateToolbox() {

    const list =
        document.getElementById(
            "toolbox-node-list"
        );


    if (!list) return;


    list.innerHTML = "";


    const addToolboxItem =
        (
            iconKey,
            label,
            iconUrl
        ) => {

            const button =
                document.createElement(
                    "button"
                );


            button.type =
                "button";


            button.className =
                "flex items-center gap-2 " +
                "w-full px-3 py-2 rounded-lg " +
                "text-left text-xs " +
                "text-slate-300 " +
                "hover:bg-dark-100 " +
                "border border-transparent " +
                "hover:border-dark-50 " +
                "transition-colors";


            const image =
                document.createElement(
                    "img"
                );


            image.src =
                iconUrl ||
                resolveIconUrl(
                    iconKey
                );


            image.alt =
                label;


            image.className =
                "w-7 h-7 object-contain";


            const text =
                document.createElement(
                    "span"
                );


            text.textContent =
                label;


            button.appendChild(
                image
            );

            button.appendChild(
                text
            );


            button.addEventListener(
                "click",
                () => {

                    addCanvasNode(
                        iconKey,
                        {

                            label,

                            icon_url:
                                iconUrl
                        }
                    );
                }
            );


            list.appendChild(
                button
            );
        };


    // Built-in icons
    Object.keys(
        SVG_ICONS
    ).forEach(key => {

        addToolboxItem(

            key,

            key
                .replace(
                    /-/g,
                    " "
                )
                .replace(
                    /\b\w/g,
                    char =>
                        char.toUpperCase()
                ),

            getIconUri(key)
        );
    });


    // Uploaded icons
    (
        customIcons ||
        []
    ).forEach(icon => {

        if (
            !icon ||
            !icon.tag
        ) {
            return;
        }


        addToolboxItem(

            icon.tag,

            icon.tag,

            icon.url
        );
    });
}


// ============================================================
// ADD MANUAL COMPONENT
// ============================================================

function addCanvasNode(
    icon = "server",
    options = {}
) {

    if (!cy) return;


    const id =
        `node_${
            Date.now()
        }_${
            Math.random()
                .toString(36)
                .slice(2, 7)
        }`;


    const existingNodes =
        cy.nodes()
            .filter(
                node =>
                    node.data("type") !==
                    "group"
            );


    const center =
        cy.extent();


    const x =
        (
            center.x1 +
            center.x2
        ) / 2;


    const y =
        (
            center.y1 +
            center.y2
        ) / 2;


    const iconUrl =
        options.icon_url ||
        resolveIconUrl(icon);


    const label =
        options.label ||
        icon
            .replace(
                /-/g,
                " "
            )
            .replace(
                /\b\w/g,
                char =>
                    char.toUpperCase()
            );


    cy.add({

        group:
            "nodes",

        data: {

            id,

            label,

            type:
                "cloudIcon",

            icon,

            icon_url:
                iconUrl,

            category:
                options.category ||
                "general",

            layer:
                options.layer ??
                2,

            provider:
                options.provider ||
                "generic",

            role:
                options.role ||
                "peer_service",

            peerGroup:
                options.peerGroup ||
                "",

            importance:
                options.importance ||
                "normal",

            description:
                options.description ||
                "",

            properties:
                options.properties ||
                {}
        },

        position: {

            x:
                Number.isFinite(x)
                    ? x
                    : 400,

            y:
                Number.isFinite(y)
                    ? y
                    : 300
        }
    });


    const node =
        cy.getElementById(id);


    node.select();


    selectedElement =
        node;


    populateInspectorFromElement(
        node
    );


    updateParentSelectOptions();
}
// ============================================================
// INSPECTOR HELPERS
// ============================================================

function hideInspectors() {

    document
        .getElementById("node-inspector")
        ?.classList.add("hidden");


    document
        .getElementById("edge-inspector")
        ?.classList.add("hidden");


    document
        .getElementById("connection-inspector")
        ?.classList.add("hidden");
}


function populateInspectorIconSelect() {

    const select =
        document.getElementById(
            "inspect-node-icon"
        );


    if (!select) return;


    const currentValue =
        select.value;


    select.innerHTML = "";


    const standardGroup =
        document.createElement(
            "optgroup"
        );


    standardGroup.label =
        "Standard Icons";


    Object.keys(
        SVG_ICONS || {}
    )
        .sort()
        .forEach(key => {

            const option =
                document.createElement(
                    "option"
                );


            option.value =
                key;


            option.textContent =
                key
                    .replace(
                        /[-_]/g,
                        " "
                    )
                    .replace(
                        /\b\w/g,
                        char =>
                            char.toUpperCase()
                    );


            standardGroup.appendChild(
                option
            );
        });


    select.appendChild(
        standardGroup
    );


    if (
        Array.isArray(customIcons) &&
        customIcons.length > 0
    ) {

        const customGroup =
            document.createElement(
                "optgroup"
            );


        customGroup.label =
            "Custom Icons";


        customIcons
            .filter(
                icon =>
                    icon &&
                    icon.tag
            )
            .forEach(icon => {

                const option =
                    document.createElement(
                        "option"
                    );


                option.value =
                    icon.tag;


                option.textContent =
                    icon.tag;


                customGroup.appendChild(
                    option
                );
            });


        select.appendChild(
            customGroup
        );
    }


    if (currentValue) {

        select.value =
            currentValue;
    }
}


// ============================================================
// GROUP / PARENT SELECT
// ============================================================

function updateParentSelectOptions() {

    const select =
        document.getElementById(
            "inspect-node-parent"
        );


    if (!select || !cy) return;


    const currentValue =
        select.value;


    select.innerHTML = "";


    const rootOption =
        document.createElement(
            "option"
        );


    rootOption.value = "";


    rootOption.textContent =
        "None (Root Level)";


    select.appendChild(
        rootOption
    );


    cy.nodes()
        .filter(
            node =>
                node.data("type") ===
                "group"
        )
        .forEach(group => {

            const option =
                document.createElement(
                    "option"
                );


            option.value =
                group.id();


            option.textContent =
                group.data("label") ||
                group.id();


            select.appendChild(
                option
            );
        });


    if (
        currentValue &&
        select.querySelector(
            `option[value="${CSS.escape(
                currentValue
            )}"]`
        )
    ) {

        select.value =
            currentValue;
    }
}


// ============================================================
// NODE INSPECTOR
// ============================================================

function showNodeInspector(node) {

    if (!node || node.empty()) return;


    const inspector =
        document.getElementById(
            "node-inspector"
        );


    if (!inspector) return;


    hideInspectors();


    populateInspectorIconSelect();

    updateParentSelectOptions();


    const label =
        document.getElementById(
            "inspect-node-label"
        );


    const icon =
        document.getElementById(
            "inspect-node-icon"
        );


    const parent =
        document.getElementById(
            "inspect-node-parent"
        );


    const description =
        document.getElementById(
            "inspect-node-desc"
        );


    const layer =
        document.getElementById(
            "inspect-node-layer"
        );


    const role =
        document.getElementById(
            "inspect-node-role"
        );


    const importance =
        document.getElementById(
            "inspect-node-importance"
        );


    if (label) {

        label.value =
            node.data("label") ||
            "";
    }


    if (icon) {

        icon.value =
            node.data("icon") ||
            "server";
    }


    if (parent) {

        parent.value =
            node.data(
                "boundaryParent"
            ) ||
            "";
    }


    if (description) {

        description.value =
            node.data(
                "description"
            ) ||
            "";
    }


    if (layer) {

        layer.value =
            Number.isFinite(
                Number(
                    node.data("layer")
                )
            )
                ? node.data("layer")
                : "";
    }


    if (role) {

        role.value =
            node.data("role") ||
            "peer_service";
    }


    if (importance) {

        importance.value =
            node.data("importance") ||
            "normal";
    }


    inspector.classList.remove(
        "hidden"
    );
}


// ============================================================
// EDGE INSPECTOR
// ============================================================

function showEdgeInspector(edge) {

    if (!edge || edge.empty()) return;


    const inspector =
        document.getElementById(
            "edge-inspector"
        );


    if (!inspector) return;


    hideInspectors();


    const label =
        document.getElementById(
            "inspect-edge-label"
        );


    const protocol =
        document.getElementById(
            "inspect-edge-protocol"
        );


    const encrypted =
        document.getElementById(
            "inspect-edge-encrypted"
        );


    const kind =
        document.getElementById(
            "inspect-edge-kind"
        );


    const direction =
        document.getElementById(
            "inspect-edge-direction"
        );


    if (label) {

        label.value =
            edge.data("label") ||
            "";
    }


    if (protocol) {

        protocol.value =
            edge.data("protocol") ||
            "";
    }


    if (encrypted) {

        encrypted.checked =
            Boolean(
                edge.data("encrypted")
            );
    }


    if (kind) {

        kind.value =
            edge.data("kind") ||
            "sync";
    }


    if (direction) {

        direction.value =
            edge.data("direction") ||
            "forward";
    }


    inspector.classList.remove(
        "hidden"
    );
}


// ============================================================
// CONNECTION INSPECTOR
//
// This appears when exactly two architecture nodes
// are selected.
// ============================================================

function showConnectionInspector(
    nodeA,
    nodeB
) {

    const inspector =
        document.getElementById(
            "connection-inspector"
        );


    if (!inspector) {

        // Fall back to edge inspector
        // if HTML does not contain
        // a separate connection panel.

        prepareConnectionUsingEdgeInspector(
            nodeA,
            nodeB
        );

        return;
    }


    const source =
        document.getElementById(
            "connection-source"
        );


    const target =
        document.getElementById(
            "connection-target"
        );


    const label =
        document.getElementById(
            "connection-label"
        );


    const protocol =
        document.getElementById(
            "connection-protocol"
        );


    const kind =
        document.getElementById(
            "connection-kind"
        );


    if (source) {

        source.textContent =
            nodeA.data("label") ||
            nodeA.id();
    }


    if (target) {

        target.textContent =
            nodeB.data("label") ||
            nodeB.id();
    }


    if (label) {

        label.value =
            "";
    }


    if (protocol) {

        protocol.value =
            "HTTPS";
    }


    if (kind) {

        kind.value =
            "sync";
    }


    inspector.dataset.sourceId =
        nodeA.id();


    inspector.dataset.targetId =
        nodeB.id();


    inspector.classList.remove(
        "hidden"
    );
}


// ============================================================
// FALLBACK CONNECTION USING EDGE INSPECTOR
// ============================================================

function prepareConnectionUsingEdgeInspector(
    nodeA,
    nodeB
) {

    const inspector =
        document.getElementById(
            "edge-inspector"
        );


    if (!inspector) return;


    hideInspectors();


    const label =
        document.getElementById(
            "inspect-edge-label"
        );


    const protocol =
        document.getElementById(
            "inspect-edge-protocol"
        );


    const encrypted =
        document.getElementById(
            "inspect-edge-encrypted"
        );


    if (label) {

        label.value =
            `Connection: ${
                nodeA.data("label") ||
                nodeA.id()
            } → ${
                nodeB.data("label") ||
                nodeB.id()
            }`;
    }


    if (protocol) {

        protocol.value =
            "HTTPS";
    }


    if (encrypted) {

        encrypted.checked =
            true;
    }


    inspector.dataset.connectionMode =
        "true";


    inspector.dataset.sourceId =
        nodeA.id();


    inspector.dataset.targetId =
        nodeB.id();


    inspector.classList.remove(
        "hidden"
    );
}


// ============================================================
// CREATE CONNECTION
// ============================================================

function createConnectionBetween(
    sourceId,
    targetId,
    options = {}
) {

    if (
        !cy ||
        !sourceId ||
        !targetId ||
        sourceId === targetId
    ) {
        return;
    }


    const source =
        cy.getElementById(
            sourceId
        );


    const target =
        cy.getElementById(
            targetId
        );


    if (
        source.empty() ||
        target.empty()
    ) {
        return;
    }


    const existing =
        cy.edges().filter(
            edge =>
                edge.source().id() ===
                    sourceId &&
                edge.target().id() ===
                    targetId
        );


    if (
        existing.length > 0 &&
        !options.allowDuplicate
    ) {

        existing.select();

        selectedElement =
            existing[0];

        showEdgeInspector(
            existing[0]
        );

        return;
    }


    const id =
        `edge_${
            Date.now()
        }_${
            Math.random()
                .toString(36)
                .slice(2, 8)
        }`;


    const edge =
        cy.add({

            group:
                "edges",

            data: {

                id,

                source:
                    sourceId,

                target:
                    targetId,

                label:
                    options.label ||
                    options.protocol ||
                    "",

                protocol:
                    options.protocol ||
                    "HTTPS",

                encrypted:
                    options.encrypted ??
                    true,

                kind:
                    options.kind ||
                    "sync",

                direction:
                    options.direction ||
                    "forward",

                importance:
                    options.importance ||
                    "normal"
            }
        });


    edgeSemanticStyle();


    cy.elements().unselect();


    edge.select();


    selectedElement =
        edge;


    showEdgeInspector(
        edge
    );
}


// ============================================================
// CREATE CONNECTION FROM CONNECTION PANEL
// ============================================================

function createConnectionFromInspector() {

    const inspector =
        document.getElementById(
            "connection-inspector"
        );


    if (!inspector) return;


    const sourceId =
        inspector.dataset.sourceId;


    const targetId =
        inspector.dataset.targetId;


    const label =
        document
            .getElementById(
                "connection-label"
            )
            ?.value
            ?.trim() ||
        "";


    const protocol =
        document
            .getElementById(
                "connection-protocol"
            )
            ?.value
            ?.trim() ||
        "";


    const kind =
        document
            .getElementById(
                "connection-kind"
            )
            ?.value ||
        "sync";


    createConnectionBetween(
        sourceId,
        targetId,
        {

            label,

            protocol,

            kind,

            encrypted:
                true
        }
    );


    inspector.classList.add(
        "hidden"
    );
}


// ============================================================
// UPDATE SELECTED NODE
// ============================================================

function updateSelectedNode() {

    if (
        !selectedElement ||
        selectedElement.empty() ||
        !selectedElement.isNode()
    ) {
        return;
    }


    const node =
        selectedElement;


    if (
        node.data("type") ===
        "group"
    ) {

        updateSelectedGroup();

        return;
    }


    const label =
        document
            .getElementById(
                "inspect-node-label"
            )
            ?.value
            ?.trim();


    const icon =
        document
            .getElementById(
                "inspect-node-icon"
            )
            ?.value ||
        "server";


    const parentId =
        document
            .getElementById(
                "inspect-node-parent"
            )
            ?.value ||
        null;


    const description =
        document
            .getElementById(
                "inspect-node-desc"
            )
            ?.value
            ?.trim() ||
        "";


    const layerInput =
        document.getElementById(
            "inspect-node-layer"
        );


    const role =
        document
            .getElementById(
                "inspect-node-role"
            )
            ?.value ||
        "peer_service";


    const importance =
        document
            .getElementById(
                "inspect-node-importance"
            )
            ?.value ||
        "normal";


    let layer = null;


    if (
        layerInput &&
        layerInput.value !== ""
    ) {

        const numeric =
            Number(
                layerInput.value
            );


        if (
            Number.isFinite(
                numeric
            )
        ) {

            layer =
                numeric;
        }
    }


    const custom =
        (
            customIcons ||
            []
        ).find(
            customIcon =>
                customIcon &&
                customIcon.tag ===
                icon
        );


    const iconUrl =
        custom?.url ||
        resolveIconUrl(
            icon
        ) ||
        getIconUri(
            "server"
        );


    node.data({

        label:
            label ||
            node.id(),

        icon,

        icon_url:
            iconUrl,

        boundaryParent:
            parentId,

        description,

        layer,

        role,

        importance
    });


    // Do NOT use Cytoscape compound parenting
    // for architecture groups here.
    //
    // boundaryParent is semantic metadata.
    //
    // The enterprise layout engine calculates
    // group boundaries independently.

    cy.elements().unselect();


    selectedElement =
        null;


    hideInspectors();


    canvasAutoLayout();
}


// ============================================================
// UPDATE SELECTED GROUP
// ============================================================

function updateSelectedGroup() {

    if (
        !selectedElement ||
        selectedElement.empty()
    ) {
        return;
    }


    const label =
        document
            .getElementById(
                "inspect-node-label"
            )
            ?.value
            ?.trim();


    if (label) {

        selectedElement.data(
            "label",
            label
        );
    }


    cy.elements().unselect();

    selectedElement =
        null;

    hideInspectors();

    canvasAutoLayout();
}


// ============================================================
// UPDATE SELECTED EDGE
// ============================================================

function updateSelectedEdge() {

    const inspector =
        document.getElementById(
            "edge-inspector"
        );


    // --------------------------------------------------------
    // Connection creation fallback mode
    // --------------------------------------------------------

    if (
        inspector?.dataset.connectionMode ===
        "true"
    ) {

        const sourceId =
            inspector.dataset.sourceId;


        const targetId =
            inspector.dataset.targetId;


        const label =
            document
                .getElementById(
                    "inspect-edge-label"
                )
                ?.value
                ?.trim() ||
            "";


        const protocol =
            document
                .getElementById(
                    "inspect-edge-protocol"
                )
                ?.value
                ?.trim() ||
            "";


        const encrypted =
            Boolean(
                document
                    .getElementById(
                        "inspect-edge-encrypted"
                    )
                    ?.checked
            );


        createConnectionBetween(
            sourceId,
            targetId,
            {

                label,

                protocol,

                encrypted
            }
        );


        delete inspector.dataset.connectionMode;
        delete inspector.dataset.sourceId;
        delete inspector.dataset.targetId;


        return;
    }


    if (
        !selectedElement ||
        selectedElement.empty() ||
        !selectedElement.isEdge()
    ) {
        return;
    }


    const edge =
        selectedElement;


    const label =
        document
            .getElementById(
                "inspect-edge-label"
            )
            ?.value
            ?.trim() ||
        "";


    const protocol =
        document
            .getElementById(
                "inspect-edge-protocol"
            )
            ?.value
            ?.trim() ||
        "";


    const encrypted =
        Boolean(
            document
                .getElementById(
                    "inspect-edge-encrypted"
                )
                ?.checked
        );


    const kind =
        document
            .getElementById(
                "inspect-edge-kind"
            )
            ?.value ||
        "sync";


    const direction =
        document
            .getElementById(
                "inspect-edge-direction"
            )
            ?.value ||
        "forward";


    edge.data({

        label:
            label ||
            protocol,

        protocol,

        encrypted,

        kind,

        direction
    });


    edgeSemanticStyle();


    cy.elements().unselect();


    selectedElement =
        null;


    hideInspectors();
}


// ============================================================
// DELETE SELECTED ELEMENT
// ============================================================

function deleteSelectedElement() {

    if (
        !selectedElement ||
        selectedElement.empty()
    ) {
        return;
    }


    const element =
        selectedElement;


    const isGroup =
        element.isNode() &&
        element.data("type") ===
        "group";


    if (
        !confirm(
            isGroup
                ? "Delete this boundary group? Components will remain in the diagram."
                : "Are you sure you want to delete this element?"
        )
    ) {
        return;
    }


    if (isGroup) {

        // Remove semantic parent references
        // from architecture nodes.

        cy.nodes().forEach(node => {

            if (
                node.data(
                    "boundaryParent"
                ) === element.id()
            ) {

                node.data(
                    "boundaryParent",
                    null
                );
            }
        });


        const explicitGroups =
            cy.data(
                "explicitGroups"
            ) ||
            [];


        cy.data(
            "explicitGroups",

            explicitGroups.filter(
                group =>
                    group.id !==
                    element.id()
            )
        );
    }


    cy.remove(
        element
    );


    selectedElement =
        null;


    hideInspectors();


    updateParentSelectOptions();


    requestAnimationFrame(
        () => {

            if (
                cy.nodes()
                    .filter(
                        node =>
                            node.data("type") !==
                            "group"
                    )
                    .length > 0
            ) {

                canvasAutoLayout();
            }
        }
    );
}


// ============================================================
// ADD BOUNDARY GROUP
// ============================================================

function addCanvasGroup(
    groupType = "boundary",
    label = "New Boundary"
) {

    if (!cy) return;


    const id =
        `group_${
            Date.now()
        }_${
            Math.random()
                .toString(36)
                .slice(2, 7)
        }`;


    cy.add({

        group:
            "nodes",

        data: {

            id,

            label,

            type:
                "group",

            group_type:
                groupType,

            role:
                "boundary"
        }
    });


    const explicitGroups =
        cy.data(
            "explicitGroups"
        ) ||
        [];


    explicitGroups.push({

        id,

        label,

        type:
            groupType,

        parentId:
            null,

        role:
            "boundary"
    });


    cy.data(
        "explicitGroups",
        explicitGroups
    );


    updateParentSelectOptions();


    return id;
}


// ============================================================
// SELECTION LISTENERS
//
// Important:
//
// Use one selection event pipeline.
//
// Do NOT independently hide inspectors on every
// unselect event because Cytoscape fires unselect
// while switching selections.
// ============================================================

function setupSelectionListeners() {

    if (!cy) return;


    let selectionTimer =
        null;


    const processSelection =
        () => {

            clearTimeout(
                selectionTimer
            );


            selectionTimer =
                setTimeout(
                    () => {

                        const selectedNodes =
                            cy.nodes(
                                ":selected"
                            )
                                .filter(
                                    node =>
                                        node.data("type") !==
                                        "group"
                                );


                        const selectedEdges =
                            cy.edges(
                                ":selected"
                            );


                        // ------------------------------------------------
                        // Two nodes selected → connection mode
                        // ------------------------------------------------

                        if (
                            selectedNodes.length === 2
                        ) {

                            selectedElement =
                                null;


                            showConnectionInspector(
                                selectedNodes[0],
                                selectedNodes[1]
                            );

                            return;
                        }


                        // ------------------------------------------------
                        // One edge selected
                        // ------------------------------------------------

                        if (
                            selectedEdges.length === 1
                        ) {

                            selectedElement =
                                selectedEdges[0];


                            showEdgeInspector(
                                selectedEdges[0]
                            );

                            return;
                        }


                        // ------------------------------------------------
                        // One node selected
                        // ------------------------------------------------

                        if (
                            cy.nodes(":selected")
                                .length === 1
                        ) {

                            const node =
                                cy.nodes(
                                    ":selected"
                                )[0];


                            selectedElement =
                                node;


                            showNodeInspector(
                                node
                            );

                            return;
                        }


                        // ------------------------------------------------
                        // Nothing selected
                        // ------------------------------------------------

                        selectedElement =
                            null;


                        hideInspectors();

                    },

                    25
                );
        };


    cy.on(
        "select unselect",
        "node, edge",
        processSelection
    );


    // Clicking empty canvas
    cy.on(
        "tap",
        event => {

            if (
                event.target === cy
            ) {

                cy.elements().unselect();


                selectedElement =
                    null;


                hideInspectors();
            }
        }
    );
}


// ============================================================
// MANUAL CONNECTION MODE
//
// Allows the user to:
//
// 1. Click Connect
// 2. Select source
// 3. Select target
//
// without accidentally creating a link.
// ============================================================

let manualConnectionMode =
    false;


let connectionSourceNode =
    null;


function enableConnectionMode() {

    if (!cy) return;


    manualConnectionMode =
        true;


    connectionSourceNode =
        null;


    cy.container()?.classList.add(
        "connection-mode"
    );


    appendChatMessage(
        "Connection mode enabled. Select the source component, then select the target component.",
        "bot"
    );
}


function disableConnectionMode() {

    manualConnectionMode =
        false;


    connectionSourceNode =
        null;


    cy.container()?.classList.remove(
        "connection-mode"
    );
}


function setupManualConnectionMode() {

    if (!cy) return;


    cy.on(
        "tap",
        "node",
        event => {

            if (
                !manualConnectionMode
            ) {
                return;
            }


            const node =
                event.target;


            if (
                node.data("type") ===
                "group"
            ) {
                return;
            }


            if (
                !connectionSourceNode
            ) {

                connectionSourceNode =
                    node;


                node.select();


                return;
            }


            if (
                connectionSourceNode.id() ===
                node.id()
            ) {

                return;
            }


            const source =
                connectionSourceNode;

            const target =
                node;


            disableConnectionMode();


            cy.elements().unselect();


            source.select();

            target.select();


            showConnectionInspector(
                source,
                target
            );
        }
    );
}


// ============================================================
// KEYBOARD SHORTCUTS
//
// Delete / Backspace
// Ctrl+S / Cmd+S
// Escape
// ============================================================

function setupKeyboardShortcuts() {

    document.addEventListener(
        "keydown",
        event => {

            const target =
                event.target;


            const editingInput =
                target instanceof
                    HTMLInputElement ||
                target instanceof
                    HTMLTextAreaElement ||
                target instanceof
                    HTMLSelectElement;


            // Save
            if (
                (
                    event.ctrlKey ||
                    event.metaKey
                ) &&
                event.key.toLowerCase() ===
                "s"
            ) {

                event.preventDefault();

                saveCurrentDiagram();

                return;
            }


            if (editingInput) {
                return;
            }


            // Delete selected
            if (
                event.key === "Delete" ||
                event.key === "Backspace"
            ) {

                if (
                    selectedElement
                ) {

                    event.preventDefault();

                    deleteSelectedElement();
                }

                return;
            }


            // Escape
            if (
                event.key === "Escape"
            ) {

                disableConnectionMode();

                cy?.elements()
                    .unselect();

                selectedElement =
                    null;

                hideInspectors();
            }
        }
    );
}


// ============================================================
// TOOLBOX BUTTON HELPERS
// ============================================================

function setupToolboxActions() {

    const connectButton =
        document.getElementById(
            "btn-connect"
        );


    connectButton?.addEventListener(
        "click",
        () => {

            if (
                manualConnectionMode
            ) {

                disableConnectionMode();

            } else {

                enableConnectionMode();
            }
        }
    );


    const addBoundaryButton =
        document.getElementById(
            "btn-add-boundary"
        );


    addBoundaryButton?.addEventListener(
        "click",
        () => {

            const label =
                prompt(
                    "Boundary name:",
                    "Application Boundary"
                );


            if (
                label === null
            ) {
                return;
            }


            addCanvasGroup(
                "boundary",
                label ||
                "Application Boundary"
            );


            canvasAutoLayout();
        }
    );
}


// ============================================================
// EXPORT MENU
//
// Ensures menu always appears above:
//
// Inspector
// Toolbox
// Canvas
//
// Earlier issue:
// export menu appeared behind side panels.
// ============================================================

function setupExportMenu() {

    const menu =
        document.getElementById(
            "export-menu"
        );


    const button =
        document.getElementById(
            "btn-export"
        );


    if (
        !menu ||
        !button
    ) {
        return;
    }


    menu.style.zIndex =
        "99999";


    button.addEventListener(
        "click",
        event => {

            event.stopPropagation();


            menu.classList.toggle(
                "hidden"
            );


            menu.style.zIndex =
                "99999";
        }
    );


    document.addEventListener(
        "click",
        event => {

            if (
                !menu.contains(
                    event.target
                ) &&
                !button.contains(
                    event.target
                )
            ) {

                menu.classList.add(
                    "hidden"
                );
            }
        }
    );


    menu.querySelectorAll(
        "[data-export]"
    )
        .forEach(item => {

            item.addEventListener(
                "click",
                event => {

                    const format =
                        event.currentTarget.dataset.export;


                    if (format) {

                        exportDiagram(
                            format
                        );
                    }


                    menu.classList.add(
                        "hidden"
                    );
                }
            );
        });
}


// ============================================================
// TAB SYSTEM
//
// Fixes the earlier issue where:
//
// 1. Tabs were visible
// 2. Tabs could not be clicked
//
// This implementation does not depend on
// CSS pointer-events inheritance.
// ============================================================

function setupTabs() {

    const tabButtons =
        document.querySelectorAll(
            "[data-tab]"
        );


    tabButtons.forEach(button => {

        button.style.pointerEvents =
            "auto";


        button.addEventListener(
            "click",
            event => {

                event.preventDefault();

                event.stopPropagation();


                const targetId =
                    button.dataset.tab;


                if (!targetId) {
                    return;
                }


                // Update buttons
                tabButtons.forEach(tab => {

                    const active =
                        tab === button;


                    tab.classList.toggle(
                        "active",
                        active
                    );


                    tab.setAttribute(
                        "aria-selected",
                        active
                            ? "true"
                            : "false"
                    );
                });


                // Update panels
                document
                    .querySelectorAll(
                        "[data-tab-panel]"
                    )
                    .forEach(panel => {

                        const active =
                            panel.dataset.tabPanel ===
                            targetId;


                        panel.classList.toggle(
                            "hidden",
                            !active
                        );


                        panel.style.pointerEvents =
                            active
                                ? "auto"
                                : "none";
                    });
            }
        );
    });


    // Activate first visible tab
    const activeTab =
        document.querySelector(
            "[data-tab].active"
        ) ||
        tabButtons[0];


    activeTab?.click();
}


// ============================================================
// EMPTY STATE
// ============================================================

function setupCanvasEmptyState() {

    if (!cy) return;


    const update =
        () => {

            const emptyState =
                document.getElementById(
                    "empty-state"
                );


            if (!emptyState) {
                return;
            }


            const realNodes =
                cy.nodes()
                    .filter(
                        node =>
                            node.data("type") !==
                            "group"
                    );


            emptyState.classList.toggle(
                "hidden",
                realNodes.length > 0
            );
        };


    cy.on(
        "add remove",
        update
    );


    update();
}


// ============================================================
// SAFE AUTH / MODEL DISPLAY
//
// Frontend never hard-codes:
//
// gemini-1.5-flash
//
// The backend is the source of truth.
// ============================================================

async function initAuthStatus() {

    const statusElement =
        document.getElementById(
            "model-status"
        ) ||
        document.getElementById(
            "auth-status"
        );


    try {

        const response =
            await fetch(
                "/api/auth/status",
                {
                    cache:
                        "no-store"
                }
            );


        if (!response.ok) {

            throw new Error(
                "Unable to retrieve model status"
            );
        }


        const status =
            await response.json();


        if (!statusElement) {
            return;
        }


        const model =
            status.model ||
            status.active_model ||
            status.model_name ||
            "Vertex AI ADC";


        const authenticated =
            status.authenticated ??
            status.ok ??
            true;


        statusElement.textContent =
            authenticated
                ? model
                : "Authentication Required";


        statusElement.dataset.status =
            authenticated
                ? "connected"
                : "error";

    } catch (error) {

        console.warn(
            "Auth status unavailable",
            error
        );


        if (statusElement) {

            statusElement.textContent =
                "Vertex AI ADC";

            statusElement.dataset.status =
                "unknown";
        }
    }
}


// ============================================================
// FINAL APPLICATION INITIALIZATION
//
// All initialization happens once.
//
// This avoids:
//
// duplicate listeners
// duplicate tab handlers
// multiple selection handlers
// multiple project loads
// ============================================================

let applicationInitialized =
    false;


async function initializeApplication() {

    if (
        applicationInitialized
    ) {
        return;
    }


    applicationInitialized =
        true;


    try {

        // ----------------------------------------------------
        // Canvas
        // ----------------------------------------------------

        if (
            typeof initializeCanvas ===
            "function"
        ) {

            initializeCanvas();
        }


        if (!cy) {

            console.error(
                "Cytoscape canvas was not initialized."
            );

            return;
        }


        // ----------------------------------------------------
        // UI
        // ----------------------------------------------------

        setupTabs();

        setupExportMenu();

        setupSelectionListeners();

        setupManualConnectionMode();

        setupKeyboardShortcuts();

        setupToolboxActions();

        setupCanvasEmptyState();

        setupFormListeners();


        // ----------------------------------------------------
        // Data
        // ----------------------------------------------------

        await loadCustomIcons();

        await initAuthStatus();

        await loadProjects();


        // ----------------------------------------------------
        // Parent / Inspector state
        // ----------------------------------------------------

        populateInspectorIconSelect();

        updateParentSelectOptions();


        // ----------------------------------------------------
        // Lucide
        // ----------------------------------------------------

        try {

            lucide.createIcons();

        } catch (error) {

            console.warn(
                "Lucide initialization failed",
                error
            );
        }


        console.log(
            "Enterprise Architecture Diagram Generator initialized successfully."
        );

    } catch (error) {

        console.error(
            "Application initialization failed",
            error
        );

        applicationInitialized =
            false;
    }
}


// ============================================================
// DOM READY
// ============================================================

if (
    document.readyState ===
    "loading"
) {

    document.addEventListener(
        "DOMContentLoaded",
        initializeApplication,
        {
            once: true
        }
    );

} else {

    initializeApplication();
}


// ============================================================
// GLOBAL UI FUNCTIONS
//
// HTML may call these using onclick="...".
//
// Explicitly exposing them prevents failures when
// app.js is loaded as a module or bundled.
// ============================================================

window.generateArchitecture =
    generateArchitecture;


window.saveCurrentDiagram =
    saveCurrentDiagram;


window.exportDiagram =
    exportDiagram;


window.updateSelectedNode =
    updateSelectedNode;


window.updateSelectedEdge =
    updateSelectedEdge;


window.deleteSelectedElement =
    deleteSelectedElement;


window.createNewProject =
    createNewProject;


window.closeNewProjectModal =
    closeNewProjectModal;


window.createConnectionFromInspector =
    createConnectionFromInspector;


window.enableConnectionMode =
    enableConnectionMode;


window.disableConnectionMode =
    disableConnectionMode;


window.addCanvasNode =
    addCanvasNode;


window.addCanvasGroup =
    addCanvasGroup;


window.canvasZoomIn =
    canvasZoomIn;


window.canvasZoomOut =
    canvasZoomOut;


window.canvasFit =
    canvasFit;


window.canvasAutoLayout =
    canvasAutoLayout;
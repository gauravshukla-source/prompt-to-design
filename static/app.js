// Standard SVGs for the cloud and system architecture nodes
const STROKE_WIDTH = 1.8;
const SVG_ICONS = {
    // AWS Icons
    'aws-api-gateway': `<svg viewBox="0 0 24 24" fill="none" stroke="#FF9900" stroke-width="${STROKE_WIDTH}" stroke-linecap="round" stroke-linejoin="round"><path d="M22 13V6a2 2 0 0 0-2-2H4a2 2 0 0 0-2 2v7"></path><path d="M12 22V13"></path><path d="M17 18h5"></path><path d="M2 18h5"></path><circle cx="12" cy="13" r="3"></circle></svg>`,
    'aws-rds': `<svg viewBox="0 0 24 24" fill="none" stroke="#3b82f6" stroke-width="${STROKE_WIDTH}" stroke-linecap="round" stroke-linejoin="round"><ellipse cx="12" cy="5" rx="9" ry="3"></ellipse><path d="M3 5v14c0 1.66 4 3 9 3s9-1.34 9-3V5"></path><path d="M3 12c0 1.66 4 3 9 3s9-1.34 9-3"></path></svg>`,
    'aws-ecs': `<svg viewBox="0 0 24 24" fill="none" stroke="#FF9900" stroke-width="${STROKE_WIDTH}" stroke-linecap="round" stroke-linejoin="round"><rect x="2" y="2" width="20" height="8" rx="2"></rect><rect x="2" y="14" width="20" height="8" rx="2"></rect><line x1="6" y1="6" x2="6.01" y2="6"></line><line x1="6" y1="18" x2="6.01" y2="18"></line></svg>`,
    'aws-s3': `<svg viewBox="0 0 24 24" fill="none" stroke="#FF9900" stroke-width="${STROKE_WIDTH}" stroke-linecap="round" stroke-linejoin="round"><path d="M21 8a2 2 0 0 0-1-1.73l-7-4a2 2 0 0 0-2 0l-7 4A2 2 0 0 0 3 8v8a2 2 0 0 0 1 1.73l7 4a2 2 0 0 0 2 0l7-4A2 2 0 0 0 21 16Z"></path><path d="m3.3 7 8.7 5 8.7-5"></path><path d="M12 22V12"></path></svg>`,
    'aws-lambda': `<svg viewBox="0 0 24 24" fill="none" stroke="#FF9900" stroke-width="${STROKE_WIDTH}" stroke-linecap="round" stroke-linejoin="round"><path d="M5 3h14"></path><path d="M12 3v18"></path><path d="M10 18l2 3 2-3"></path><path d="M19 21H5"></path><path d="M8 8l4-4 4 4"></path></svg>`,
    
    // Azure Icons
    'azure-sql': `<svg viewBox="0 0 24 24" fill="none" stroke="#0072C6" stroke-width="${STROKE_WIDTH}" stroke-linecap="round" stroke-linejoin="round"><ellipse cx="12" cy="5" rx="9" ry="3"></ellipse><path d="M3 5v14c0 1.66 4 3 9 3s9-1.34 9-3V5"></path><path d="M3 12c0 1.66 4 3 9 3s9-1.34 9-3"></path><path d="M12 5v10"></path></svg>`,
    'azure-app-service': `<svg viewBox="0 0 24 24" fill="none" stroke="#0072C6" stroke-width="${STROKE_WIDTH}" stroke-linecap="round" stroke-linejoin="round"><rect x="2" y="3" width="20" height="14" rx="2" ry="2"></rect><line x1="8" y1="21" x2="16" y2="21"></line><line x1="12" y1="17" x2="12" y2="21"></line></svg>`,
    'azure-vm': `<svg viewBox="0 0 24 24" fill="none" stroke="#0072C6" stroke-width="${STROKE_WIDTH}" stroke-linecap="round" stroke-linejoin="round"><rect x="3" y="3" width="18" height="18" rx="2" ry="2"></rect><line x1="9" y1="3" x2="9" y2="21"></line><line x1="15" y1="3" x2="15" y2="21"></line><line x1="3" y1="9" x2="21" y2="9"></line><line x1="3" y1="15" x2="21" y2="15"></line></svg>`,
    
    // GCP Icons
    'gcp-cloud-run': `<svg viewBox="0 0 24 24" fill="none" stroke="#4285F4" stroke-width="${STROKE_WIDTH}" stroke-linecap="round" stroke-linejoin="round"><polygon points="12 2 22 8.5 22 15.5 12 22 2 15.5 2 8.5"></polygon><line x1="12" y1="22" x2="12" y2="12"></line><line x1="12" y1="12" x2="22" y2="8.5"></line><line x1="12" y1="12" x2="2" y2="8.5"></line></svg>`,
    'gcp-gcs': `<svg viewBox="0 0 24 24" fill="none" stroke="#EA4335" stroke-width="${STROKE_WIDTH}" stroke-linecap="round" stroke-linejoin="round"><path d="M12 2L2 7l10 5 10-5-10-5zM2 17l10 5 10-5M2 12l10 5 10-5"></path></svg>`,
    
    // Identity & Integration
    'active-directory': `<svg viewBox="0 0 24 24" fill="none" stroke="#10b981" stroke-width="${STROKE_WIDTH}" stroke-linecap="round" stroke-linejoin="round"><path d="M12 22s8-4 8-10V5l-8-3-8 3v7c0 6 8 10 8 10z"></path><circle cx="12" cy="11" r="3"></circle><path d="M12 14c-2.5 0-4 1.5-4 2.5v.5h8v-.5c0-1-1.5-2.5-4-2.5z"></path></svg>`,
    'kubernetes': `<svg viewBox="0 0 24 24" fill="none" stroke="#326CE5" stroke-width="${STROKE_WIDTH}" stroke-linecap="round" stroke-linejoin="round"><polygon points="12 2 23 8 23 16 12 22 1 16 1 8"></polygon><circle cx="12" cy="12" r="4"></circle><line x1="12" y1="2" x2="12" y2="8"></line><line x1="12" y1="16" x2="12" y2="22"></line><line x1="1" y1="8" x2="8" y2="12"></line><line x1="16" y1="12" x2="23" y2="16"></line></svg>`,
    'kafka': `<svg viewBox="0 0 24 24" fill="none" stroke="#EC4899" stroke-width="${STROKE_WIDTH}" stroke-linecap="round" stroke-linejoin="round"><path d="M4 12v8a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2v-8M4 12V4a2 2 0 0 1 2-2h12a2 2 0 0 1 2 2v8M4 12h16"></path><circle cx="12" cy="12" r="3"></circle></svg>`,
    'rabbitmq': `<svg viewBox="0 0 24 24" fill="none" stroke="#FF6600" stroke-width="${STROKE_WIDTH}" stroke-linecap="round" stroke-linejoin="round"><path d="M10 10s.5-3 2.5-3 2.5 3 2.5 3v4s-.5 3-2.5 3-2.5-3-2.5-3v-4z"></path><path d="M6 14h8"></path><path d="M18 14h-2"></path><circle cx="4" cy="14" r="1"></circle></svg>`,
    
    // Generic
    'database': `<svg viewBox="0 0 24 24" fill="none" stroke="#a855f7" stroke-width="${STROKE_WIDTH}" stroke-linecap="round" stroke-linejoin="round"><ellipse cx="12" cy="5" rx="9" ry="3"></ellipse><path d="M3 5v14c0 1.66 4 3 9 3s9-1.34 9-3V5"></path><path d="M3 12c0 1.66 4 3 9 3s9-1.34 9-3"></path></svg>`,
    'server': `<svg viewBox="0 0 24 24" fill="none" stroke="#94a3b8" stroke-width="${STROKE_WIDTH}" stroke-linecap="round" stroke-linejoin="round"><rect x="2" y="2" width="20" height="8" rx="2" ry="2"></rect><rect x="2" y="14" width="20" height="8" rx="2" ry="2"></rect><line x1="6" y1="6" x2="6.01" y2="6"></line><line x1="6" y1="18" x2="6.01" y2="18"></line></svg>`,
    'client': `<svg viewBox="0 0 24 24" fill="none" stroke="#0ea5e9" stroke-width="${STROKE_WIDTH}" stroke-linecap="round" stroke-linejoin="round"><rect x="2" y="3" width="20" height="14" rx="2" ry="2"></rect><line x1="8" y1="21" x2="16" y2="21"></line><line x1="12" y1="17" x2="12" y2="21"></line></svg>`,
    'user': `<svg viewBox="0 0 24 24" fill="none" stroke="#cbd5e1" stroke-width="${STROKE_WIDTH}" stroke-linecap="round" stroke-linejoin="round"><path d="M20 21v-2a4 4 0 0 0-4-4H8a4 4 0 0 0-4 4v2"></path><circle cx="12" cy="7" r="4"></circle></svg>`,
    'dns': `<svg viewBox="0 0 24 24" fill="none" stroke="#22c55e" stroke-width="${STROKE_WIDTH}" stroke-linecap="round" stroke-linejoin="round"><circle cx="12" cy="12" r="10"></circle><line x1="2" y1="12" x2="22" y2="12"></line><path d="M12 2a15.3 15.3 0 0 1 4 10 15.3 15.3 0 0 1-4 10 15.3 15.3 0 0 1-4-10 15.3 15.3 0 0 1 4-10z"></path></svg>`,
    'router': `<svg viewBox="0 0 24 24" fill="none" stroke="#eab308" stroke-width="${STROKE_WIDTH}" stroke-linecap="round" stroke-linejoin="round"><rect x="2" y="10" width="20" height="8" rx="2"></rect><line x1="6" y1="14" x2="6.01" y2="14"></line><line x1="10" y1="14" x2="14" y2="14"></line><path d="M18 14h.01"></path><path d="M17 10l-5-5-5 5"></path><line x1="12" y1="5" x2="12" y2="10"></line></svg>`,
    'firewall': `<svg viewBox="0 0 24 24" fill="none" stroke="#f43f5e" stroke-width="${STROKE_WIDTH}" stroke-linecap="round" stroke-linejoin="round"><rect x="3" y="3" width="18" height="18" rx="2"></rect><path d="M12 3v18"></path><path d="M3 12h18"></path><path d="M3 8h9"></path><path d="M12 16h9"></path></svg>`,
    'cog': `<svg viewBox="0 0 24 24" fill="none" stroke="#cbd5e1" stroke-width="${STROKE_WIDTH}" stroke-linecap="round" stroke-linejoin="round"><circle cx="12" cy="12" r="3"></circle><path d="M19.4 15a1.65 1.65 0 0 0 .33 1.82l.06.06a2 2 0 1 1-2.83 2.83l-.06-.06a1.65 1.65 0 0 0-1.82-.33 1.65 1.65 0 0 0-1 1.51V21a2 2 0 0 1-4 0v-.09A1.65 1.65 0 0 0 9 19.4a1.65 1.65 0 0 0-1.82.33l-.06.06a2 2 0 1 1-2.83-2.83l.06-.06a1.65 1.65 0 0 0 .33-1.82 1.65 1.65 0 0 0-1.51-1H3a2 2 0 0 1 0-4h.09A1.65 1.65 0 0 0 4.6 9a1.65 1.65 0 0 0-.33-1.82l-.06-.06a2 2 0 1 1 2.83-2.83l.06.06a1.65 1.65 0 0 0 1.82.33H9a1.65 1.65 0 0 0 1-1.51V3a2 2 0 0 1 4 0v.09a1.65 1.65 0 0 0 1 1.51 1.65 1.65 0 0 0 1.82-.33l.06-.06a2 2 0 1 1 2.83 2.83l-.06.06a1.65 1.65 0 0 0-.33 1.82V9a1.65 1.65 0 0 0 1.51 1H21a2 2 0 0 1 0 4h-.09a1.65 1.65 0 0 0-1.51 1z"></path></svg>`
};

// Convert SVG strings to Data URIs for Cytoscape
function getIconUri(iconName) {
    if (SVG_ICONS[iconName]) {
        return 'data:image/svg+xml;utf8,' + encodeURIComponent(SVG_ICONS[iconName]);
    }
    // Fallback if custom icon URL is stored differently
    return null;
}

// State management
let cy = null;
let currentProjectId = "";
let currentDiagramId = "";
let currentVersion = 1;
let customIcons = [];

// Initialize Page
document.addEventListener("DOMContentLoaded", () => {
    lucide.createIcons();
    initTabs();
    initAPIKey();
    initCanvas();
    loadProjects();
    loadCustomIcons();
    populateToolbox();
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

// API Key management
function initAPIKey() {
    const keyInput = document.getElementById("gemini-key");
    const savedKey = localStorage.getItem("gemini_api_key");
    if (savedKey) {
        keyInput.value = savedKey;
    }
    keyInput.addEventListener("input", (e) => {
        localStorage.setItem("gemini_api_key", e.target.value.trim());
    });
}

function getAPIKey() {
    return localStorage.getItem("gemini_api_key") || "";
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
                    'width': '45px',
                    'height': '45px',
                    'shape': 'roundrectangle',
                    'background-image': 'data(icon_url)',
                    'background-fit': 'contain',
                    'background-width': '65%',
                    'background-height': '65%',
                    'text-wrap': 'wrap',
                    'text-max-width': '80px',
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
                    'curve-style': 'bezier',
                    'text-background-opacity': 0.85,
                    'text-background-color': '#0c0c0e',
                    'text-background-padding': '3px',
                    'text-background-shape': 'roundrectangle'
                }
            },
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
function canvasAutoLayout() {
    cy.layout({
        name: 'dagre',
        rankDir: 'LR',
        nodeSep: 50,
        edgeSep: 30,
        rankSep: 80,
        animate: true,
        animationDuration: 400
    }).run();
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
                    group_type: g.type
                }
            });
        });
    }
    
    // Add nodes
    if (dsl.nodes) {
        dsl.nodes.forEach(n => {
            let iconUrl = getIconUri(n.data.icon);
            if (!iconUrl) {
                // Check if it's a custom icon
                const customIcon = customIcons.find(ci => ci.tag === n.data.icon);
                if (customIcon) iconUrl = customIcon.url;
            }
            
            elements.push({
                data: {
                    id: n.id,
                    label: n.data.label,
                    parent: n.parentId || undefined,
                    type: n.type,
                    icon: n.data.icon,
                    icon_url: iconUrl || getIconUri('server'),
                    category: n.data.category,
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
                    encrypted: e.data?.encrypted || false
                }
            });
        });
    }
    
    cy.add(elements);
    canvasAutoLayout();
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
                type: ele.data('group_type') || 'generic'
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
                encrypted: ele.data('encrypted') || false
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
    
    const key = getAPIKey(); // optional: passed if user set one manually
    
    loader.classList.remove("hidden");
    
    const isNew = cy.elements().length === 0;
    const url = isNew ? "/api/generate" : "/api/refine";
    const payload = isNew ? { prompt } : { prompt, current_diagram: exportTopologyJSON() };
    
    // Add user message to log
    appendChatMessage(prompt, "user");
    promptInput.value = "";
    
    try {
        const headers = { "Content-Type": "application/json" };
        if (key) headers["X-Gemini-Key"] = key; // only send if user has set one
        const res = await fetch(url, {
            method: "POST",
            headers,
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
    
    // Add standard icons
    const optGroupStd = document.createElement("optgroup");
    optGroupStd.label = "Standard Icons";
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
    
    let iconUrl = getIconUri(iconName);
    if (!iconUrl) {
        const custom = customIcons.find(ci => ci.tag === iconName);
        if (custom) iconUrl = custom.url;
    }
    
    cy.add({
        data: {
            id,
            label: iconName.replace("aws-", "").replace("azure-", "").replace("gcp-", "").toUpperCase(),
            parent,
            type: 'cloudIcon',
            icon: iconName,
            icon_url: iconUrl || getIconUri('server'),
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
    
    let iconUrl = getIconUri(icon);
    if (!iconUrl) {
        const custom = customIcons.find(ci => ci.tag === icon);
        if (custom) iconUrl = custom.url;
    }
    
    selectedElement.data({
        label,
        icon,
        parent,
        icon_url: iconUrl || getIconUri('server'),
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

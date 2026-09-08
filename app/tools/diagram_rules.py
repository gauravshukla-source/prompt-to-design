from app.models.enums import Viewpoint

VIEW_LAYOUTS = {
    Viewpoint.EXECUTIVE: "layered_horizontal",
    Viewpoint.CONCEPTUAL: "layered",
    Viewpoint.DEPLOYMENT: "domain_horizontal",
    Viewpoint.IAM: "layered_vertical",
    Viewpoint.SECURITY: "security_layers",
    Viewpoint.DATA_FLOW: "flow",
    Viewpoint.INTEGRATION: "layered_horizontal",
}

def get_layout_strategy(viewpoint: Viewpoint) -> str:
    return VIEW_LAYOUTS.get(viewpoint, "layered")

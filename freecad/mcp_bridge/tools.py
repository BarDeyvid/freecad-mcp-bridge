"""MCP tool definitions exposed by the bridge.

Schemas only. `tools/list` returns these; the HTTP layer dispatches
`tools/call` by name.
"""

EXECUTE_PYTHON = {
    "name": "execute_python",
    "description": (
        "Execute Python code inside the running FreeCAD GUI process. "
        "'App'/'FreeCAD' and 'Gui'/'FreeCADGui' are pre-bound — do not import "
        "them. Captured stdout/stderr is returned."
    ),
    "inputSchema": {
        "type": "object",
        "properties": {
            "code": {
                "type": "string",
                "description": "Python source to execute in the FreeCAD session.",
            }
        },
        "required": ["code"],
    },
}

EXECUTE_PYTHON_FILE = {
    "name": "execute_python_file",
    "description": (
        "Read a local Python file and execute it inside the running FreeCAD "
        "GUI process. Same execution context as execute_python."
    ),
    "inputSchema": {
        "type": "object",
        "properties": {
            "filepath": {
                "type": "string",
                "description": "Absolute path to a .py file.",
            }
        },
        "required": ["filepath"],
    },
}

GET_OUTPUT_PAGE = {
    "name": "get_output_page",
    "description": (
        "Retrieve a page of output for a prior execute call that returned "
        "has_more=true. To read forward, pass page_no one higher than the "
        "last page_no you received (0 if you received none yet); repeat until "
        "has_more=false. Requesting a page_no already received replays it."
    ),
    "inputSchema": {
        "type": "object",
        "properties": {
            "job_token": {
                "type": "string",
                "description": (
                    "Token from a previous execute or get_output_page response."
                ),
            },
            "page_no": {
                "type": "integer",
                "minimum": 0,
                "description": "0-based index of the page to retrieve.",
            },
        },
        "required": ["job_token", "page_no"],
    },
}

INSPECT_ACTIVE_DOCUMENT = {
    "name": "inspect_active_document",
    "description": (
        "Read a compact summary of the active FreeCAD document and its shape "
        "objects. This is read-only and does not change the viewport."
    ),
    "inputSchema": {"type": "object", "properties": {}},
}

HIGHLIGHT_OBJECTS = {
    "name": "highlight_objects",
    "description": (
        "Visibly select named objects in the active FreeCAD document and fit "
        "the 3D view around them. This changes selection/view only, not geometry."
    ),
    "inputSchema": {
        "type": "object",
        "properties": {
            "object_names": {
                "type": "array",
                "minItems": 1,
                "maxItems": 100,
                "items": {"type": "string"},
                "description": "Exact internal object names shown in the document tree.",
            }
        },
        "required": ["object_names"],
    },
}

TOOL_DEFINITIONS = [
    EXECUTE_PYTHON,
    EXECUTE_PYTHON_FILE,
    GET_OUTPUT_PAGE,
    INSPECT_ACTIVE_DOCUMENT,
    HIGHLIGHT_OBJECTS,
]

"""
Path: src/interface_adapters/presenters/dashboard_presenter.py
"""

from fastapi.responses import JSONResponse

def present_dashboard(data):
    "Adapta la respuesta del dashboard a un JSONResponse de FastAPI"
    return JSONResponse(content=data)

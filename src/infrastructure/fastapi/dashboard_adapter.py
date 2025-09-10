"""
Path: infrastructure/fastapi/dashboard_adapter.py
"""

from fastapi import APIRouter
from src.interface_adapters.controllers.dashboard_controller import get_dashboard_v1

router = APIRouter(tags=["dashboard"])

@router.get("/v1/dashboard.php")
def dashboard_endpoint_v1():
    """Adaptador HTTP para get_dashboard (v1 estandarizado)"""
    return get_dashboard_v1()

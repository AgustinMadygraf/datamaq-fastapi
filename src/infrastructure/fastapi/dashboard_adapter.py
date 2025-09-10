"""
Path: infrastructure/fastapi/dashboard_adapter.py
"""

from fastapi import APIRouter, Query

from src.interface_adapters.controllers.dashboard_controller import get_dashboard_v1
from src.interface_adapters.presenters.dashboard_presenter import present_dashboard

router = APIRouter(tags=["dashboard"])

@router.get("/v1/dashboard.php")
def dashboard_endpoint_v1(
    periodo: str = Query("dia"),
    fecha: str = Query(...),
    turno: str = Query(None)
):
    """Adaptador HTTP para get_dashboard (v1 estandarizado)"""
    data = get_dashboard_v1(periodo, fecha, turno)
    return present_dashboard(data)

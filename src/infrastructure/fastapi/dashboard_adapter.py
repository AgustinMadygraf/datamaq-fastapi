"""
Path: infrastructure/fastapi/dashboard_adapter.py
"""

from fastapi import APIRouter, Query

from src.infrastructure.sql_alchemy.interval_production_repository import IntervalProductionRepository
from src.infrastructure.sql_alchemy.session_factory import get_session
from src.interface_adapters.controllers.dashboard_controller import get_dashboard_v1
from src.interface_adapters.presenters.dashboard_presenter import present_dashboard
from src.interface_adapters.gateways.dashboard_gateway_impl import DashboardGatewayImpl

router = APIRouter(tags=["dashboard"])

@router.get("/v1/dashboard.php")
def dashboard_endpoint_v1(
    fecha: str = Query(...),
    turno: str = Query(None)
):
    """Adaptador HTTP para get_dashboard (v1 estandarizado)"""
    session = get_session()
    interval_repo = IntervalProductionRepository(session)
    gateway = DashboardGatewayImpl(interval_repo)
    data = get_dashboard_v1(fecha, turno, gateway)
    session.close()
    return present_dashboard(data)

"""
Dashboard controller for Clean Architecture
Path: interface_adapters/controllers/dashboard_controller.py
"""


from src.use_cases.get_dashboard import dashboard_case_use
from src.infrastructure.gateways.dashboard_gateway_impl import DashboardGatewayImpl

def get_dashboard_v1(periodo, fecha, turno):
    "Llama al caso de uso principal para obtener los datos del dashboard"
    gateway = DashboardGatewayImpl()
    dashboard = dashboard_case_use(periodo, fecha, turno, gateway)
    return dashboard.to_dict()

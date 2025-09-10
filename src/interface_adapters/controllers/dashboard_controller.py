"""
Path: interface_adapters/controllers/dashboard_controller.py
"""

from src.use_cases.get_dashboard import dashboard_case_use

def get_dashboard_v1(fecha, turno, gateway):
    "Llama al caso de uso principal para obtener los datos del dashboard"
    dashboard = dashboard_case_use(fecha, turno, gateway)
    return dashboard.to_dict()

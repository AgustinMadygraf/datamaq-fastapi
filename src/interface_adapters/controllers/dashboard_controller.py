"""
Dashboard controller for Clean Architecture
Path: interface_adapters/controllers/dashboard_controller.py
"""

from src.use_cases.get_dashboard import get_dashboard

def get_dashboard_v1():
    """Llama al caso de uso principal para obtener los datos del dashboard"""
    dashboard = get_dashboard()
    return dashboard.to_dict()

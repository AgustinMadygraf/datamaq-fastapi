"""
Caso de uso para obtener dashboard
Path: src/use_cases/get_dashboard.py
"""

from datetime import datetime
from babel.dates import format_datetime
from src.entities.dashboard import Dashboard
from src.interface_adapters.gateways.dashboard_gateway import DashboardGateway

def dashboard_case_use(periodo, fecha, turno, gateway: DashboardGateway):
    "Lógica de negocio principal para obtener los datos del dashboard"
    dt = datetime.strptime(fecha, "%Y-%m-%d")
    title = format_datetime(dt, "EEEE d 'de' MMMM 'del' yyyy", locale='es').capitalize()

    data = gateway.get_series(periodo, fecha, turno)

    return Dashboard(
        meta={
            "title": title,
            "date": fecha,
            "turno": turno,
            "periodo": periodo
        },
        series={
            "hoy": {"data": data["hoy"]},
            "ayer": {"data": data["ayer"]},
            "semana_anterior": {"data": data["semana_anterior"]}
        },
        velocidad=data["velocidad"],
        formato=data["formato"],
        ancho_bobina=data["ancho_bobina"]
    )

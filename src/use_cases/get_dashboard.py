"""
Caso de uso para obtener dashboard
Path: src/use_cases/get_dashboard.py
"""

from datetime import datetime
from babel.dates import format_datetime
from src.entities.dashboard import Dashboard

def dashboard_case_use(periodo, fecha, turno, hoy, ayer, semana_anterior, velocidad, formato, ancho_bobina):
    "Lógica de negocio principal para obtener los datos del dashboard"
    # Convierte la fecha a objeto datetime (asumiendo formato 'YYYY-MM-DD')
    dt = datetime.strptime(fecha, "%Y-%m-%d")
    # Formatea la fecha como 'miércoles 10 de septiembre del 2025'
    title = format_datetime(dt, "EEEE d 'de' MMMM 'del' yyyy", locale='es').capitalize()

    return Dashboard(
        meta={
            "title": title,
            "date": fecha,
            "turno": turno,
            "periodo": periodo
        },
        series={
            "hoy": {
                "data": hoy
            },
            "ayer": {
                "data": ayer
            },
            "semana_anterior": {
                "data": semana_anterior
            }
        },
        velocidad=velocidad,
        formato=formato,
        ancho_bobina=ancho_bobina
    )

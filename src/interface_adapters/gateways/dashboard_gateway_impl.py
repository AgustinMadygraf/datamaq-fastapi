"""
Path: src/interface_adapters/gateways/dashboard_gateway_impl.py
REVISAR ACÁ, PORQUE NO ESTÁ FUNCIOANDO, ES SÓLO A MODO DE EJEMPLO
MODIFICAR EL CÓDIGO EN FUNCIÓN DE LA TABLA REAL
UBICADO EN interval_production_repository.py
"""


from datetime import timedelta
from src.interface_adapters.gateways.dashboard_gateway import DashboardGateway
from src.interface_adapters.gateways.interval_production_repository import IntervalProductionRepositoryInterface

class DashboardGatewayImpl(DashboardGateway):
    "Implementación del DashboardGateway usando repository (por interfaz)"
    def __init__(self, interval_repo: IntervalProductionRepositoryInterface):
        self.interval_repo = interval_repo

    def get_series(self, fecha: str, turno: str) -> dict:
        _interval_data = self.interval_repo.get_by_date_and_turno(fecha, turno)
        _hoy = [row.HR_COUNTER1 for row in _interval_data]
        _ayer = [row.HR_COUNTER1 for row in _interval_data if row.fecha == fecha - timedelta(days=1)]
        _semana_anterior = [row.HR_COUNTER1 for row in _interval_data if row.fecha == fecha - timedelta(weeks=1)]
        hoy = [0] * 288
        ayer = [1] * 288
        semana_anterior = [2] * 288


        return {
            "hoy": hoy,
            "ayer": ayer,
            "semana_anterior": semana_anterior,
            "velocidad": None,
            "formato": None,
            "ancho_bobina": None
        }

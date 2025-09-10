"""
Path: src/interface_adapters/gateways/dashboard_gateway_impl.py
REVISAR ACÁ, PORQUE NO ESTÁ FUNCIOANDO, ES SÓLO A MODO DE EJEMPLO
MODIFICAR EL CÓDIGO EN FUNCIÓN DE LA TABLA REAL
UBICADO EN interval_production_repository.py
"""


from datetime import datetime
from src.interface_adapters.gateways.dashboard_gateway import DashboardGateway
from src.interface_adapters.gateways.interval_production_repository import IntervalProductionRepositoryInterface

class DashboardGatewayImpl(DashboardGateway):
    "Implementación del DashboardGateway usando repository (por interfaz)"
    def __init__(self, interval_repo: IntervalProductionRepositoryInterface):
        self.interval_repo = interval_repo

    def get_series(self, fecha: str, turno: str) -> dict:
        """
        Implementación de get_series. El filtrado de los datos por turno se realiza sobre la fecha recibida por GET (parámetro 'fecha').
        """
        _interval_data = self.interval_repo.get_by_date_and_turno(fecha, turno)
        hoy = [0] * 288
        # Definir los rangos de turnos (ejemplo, ajustar según tu lógica real)
        turnos = {
            'mañana': (0, 8*60*60),           # 00:00 a 08:00
            'tarde': (8*60*60, 16*60*60),     # 08:00 a 16:00
            'noche': (16*60*60, 24*60*60),    # 16:00 a 24:00
            'central': (0, 24*60*60)          # 00:00 a 24:00 (todo el día)
        }
        start_dt = datetime.strptime(fecha, "%Y-%m-%d")
        start_ts = int(start_dt.timestamp())
        # Determinar el rango de segundos del turno
        if turno in turnos:
            turno_ini, turno_fin = turnos[turno]
        else:
            turno_ini, turno_fin = 0, 24*60*60
        # Filtrar los datos por el rango de turno sobre la fecha recibida
        for row in _interval_data:
            offset = row.unixtime - start_ts
            if 0 <= offset < 24*60*60 and turno_ini <= offset < turno_fin:
                idx = offset // 300
                if 0 <= idx < 288:
                    hoy[idx] = row.HR_COUNTER1

        ayer = [0] * 288
        semana_anterior = [0] * 288

        return {
            "hoy": hoy,
            "ayer": ayer,
            "semana_anterior": semana_anterior,
            "velocidad": None,
            "formato": None,
            "ancho_bobina": None
        }

"""
Gateway interface para Dashboard
"""

from typing import List, Optional, Dict

class DashboardGateway:
    """
    Interfaz para obtener datos del dashboard.
    """
    def get_series(
        self, periodo: str, fecha: str, turno: str
    ) -> Dict[str, List[Optional[int]]]:
        """
        Debe devolver un diccionario con las series: hoy, ayer, semana_anterior.
        """
        raise NotImplementedError

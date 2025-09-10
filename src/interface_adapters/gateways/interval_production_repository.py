"""
Interfaz para el repository de IntervalProduction
Path: src/interface_adapters/gateways/interval_production_repository.py
"""
from typing import List

class IntervalProductionRepositoryInterface:
    " Interfaz para el repository de IntervalProduction "
    def get_by_date_and_turno(self, fecha: str, turno: str) -> List:
        """Obtiene registros filtrados por fecha y turno"""
        raise NotImplementedError

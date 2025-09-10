"""
Repository para IntervalProduction
Path: src/infrastructure/sql_alchemy/interval_production_repository.py
"""


from typing import List
from sqlalchemy.orm import Session
from src.infrastructure.sql_alchemy.models import IntervalProduction
from src.interface_adapters.gateways.interval_production_repository import IntervalProductionRepositoryInterface


class IntervalProductionRepository(IntervalProductionRepositoryInterface):
    "Repositorio para la entidad IntervalProduction que implementa la interfaz."
    def __init__(self, session: Session):
        self.session = session

    def get_by_date_and_turno(self, fecha: str, turno: str) -> List[IntervalProduction]:
        # Ejemplo básico: filtrar por fecha (asumiendo que unixtime representa la fecha)
        # Debes adaptar esto a tu modelo real
        return self.session.query(IntervalProduction).filter(
            # IntervalProduction.unixtime.between(...)
        ).all()

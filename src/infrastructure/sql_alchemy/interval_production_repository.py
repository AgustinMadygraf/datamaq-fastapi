"""
Path: src/infrastructure/sql_alchemy/interval_production_repository.py
REVISAR ACÁ, PORQUE NO ESTÁ FUNCIOANDO, ES SÓLO A MODO DE EJEMPLO
MODIFICAR EL CÓDIGO EN FUNCIÓN DE LA TABLA REAL
"""

from typing import List
from sqlalchemy.orm import Session
from datetime import datetime, timedelta

from src.infrastructure.sql_alchemy.models import IntervalProduction
from src.interface_adapters.gateways.interval_production_repository import IntervalProductionRepositoryInterface


class IntervalProductionRepository(IntervalProductionRepositoryInterface):
    "Repositorio para la entidad IntervalProduction que implementa la interfaz."
    def __init__(self, session: Session):
        self.session = session

    def get_by_date_and_turno(self, fecha: str, turno: str) -> List[IntervalProduction]:
        start_dt = datetime.strptime(fecha, "%Y-%m-%d")
        end_dt = start_dt + timedelta(days=1)
        start_ts = int(start_dt.timestamp())
        end_ts = int(end_dt.timestamp())
        query = self.session.query(IntervalProduction).filter(
            IntervalProduction.unixtime >= start_ts,
            IntervalProduction.unixtime < end_ts
        )
        return query.all()

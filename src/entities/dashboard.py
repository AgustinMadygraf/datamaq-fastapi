"""
Entidad Dashboard
Path: src/entities/dashboard.py
"""
from typing import Optional, List, Dict, Any

class Dashboard:
    " Entidad Dashboard "
    def __init__(
        self,
        meta: Dict[str, Any],
        series: Dict[str, Dict[str, List[Optional[int]]]],
        velocidad: int,
        formato: str,
        ancho_bobina: int
    ):
        self.meta = meta
        self.series = series
        self.velocidad = velocidad
        self.formato = formato
        self.ancho_bobina = ancho_bobina

    def to_dict(self):
        " Convierte la instancia a un diccionario "
        return {
            "meta": self.meta,
            "series": self.series,
            "velocidad": self.velocidad,
            "formato": self.formato,
            "ancho_bobina": self.ancho_bobina
        }

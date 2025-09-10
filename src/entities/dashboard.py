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
        features: List[Any],
        producto: str,
        velocidad: int,
        formato: str,
        ancho_bobina: int,
        debug_params: List[Any]
    ):
        self.meta = meta
        self.series = series
        self.features = features
        self.producto = producto
        self.velocidad = velocidad
        self.formato = formato
        self.ancho_bobina = ancho_bobina
        self.debug_params = debug_params

    def to_dict(self):
        " Convierte la instancia a un diccionario "
        return {
            "meta": self.meta,
            "series": self.series,
            "features": self.features,
            "producto": self.producto,
            "velocidad": self.velocidad,
            "formato": self.formato,
            "ancho_bobina": self.ancho_bobina,
            "debug_params": self.debug_params
        }

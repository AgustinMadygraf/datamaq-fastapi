"""
Path: src/infrastructure/sql_alchemy/models.py
"""

from sqlalchemy import Column, Integer, String, Date, DECIMAL, Float, ForeignKey, DateTime, Boolean
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class ListadoPrecios(Base):
    " Modelo para la tabla listado_precios "
    __tablename__ = "listado_precios"
    ID_listado = Column(Integer, primary_key=True)
    ID_formato = Column(Integer)
    cantidad = Column(Integer)
    precio_u_sIVA = Column(DECIMAL(8,2))
    fecha_listado = Column(Date)

class Tabla1(Base):
    " Modelo para la tabla tabla_1 "
    __tablename__ = "tabla_1"
    ID_formato = Column(Integer, primary_key=True)
    formato = Column(String(14))
    ancho = Column(Integer)
    fuelle = Column(Integer)
    alto = Column(Integer)
    color = Column(String(11))
    gramaje = Column(Integer)
    cantidades = Column(Integer)
    manijas = Column(Boolean)

class ProduccionBolsasAux(Base):
    " Modelo para la tabla produccion_bolsas_aux "
    __tablename__ = "produccion_bolsas_aux"
    ID = Column(Integer, primary_key=True)
    ancho_bobina = Column(DECIMAL(5,2))
    ID_formato = Column(Integer, ForeignKey("tabla_1.ID_formato"))
    Fecha = Column(DateTime)

class Tabla2(Base):
    " Modelo para la tabla tabla_2 "
    __tablename__ = "tabla_2"
    ID_registro = Column(Integer, primary_key=True)
    ID_formato = Column(Integer)
    papel = Column(String(11))
    fecha = Column(Date)
    pedido = Column(Integer)
    detalle = Column(String(50))
    origen = Column(Integer)
    ingreso = Column(Integer)
    egreso = Column(Integer)
    saldo = Column(Integer)
    destino_sobrante = Column(Integer)
    sobrante = Column(Integer)
    facturado = Column(Integer)
    entregado = Column(Integer)
    remito = Column(Integer)
    sobreconsumo = Column(Integer)
    lote = Column(Integer)

class IntervalProduction(Base):
    " Modelo para la tabla intervalproduction "
    __tablename__ = "intervalproduction"
    ID = Column(Integer, primary_key=True)
    unixtime = Column(Integer)
    HR_COUNTER1 = Column(Integer)
    HR_COUNTER2 = Column(Integer)
    production_rate = Column(Float)

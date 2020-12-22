from pydantic import BaseModel
#from datetime import datetime

class Registro(BaseModel):
    id: int
    id_usuario: int
    tipo: str
    valor: int
    fecha: str 
    etiqueta: str
    nota: str
class Presupuesto(BaseModel):
    id: int
    id_usuario: int
    etiqueta: str
    valor: int
    mes: int 

registros = {
  1: Registro(id=1, id_usuario=1, tipo="egreso", valor=2600, fecha="10-12-2020", etiqueta="comida", nota="pina"),
  2: Registro(id=2, id_usuario=1, tipo="egreso", valor=28000, fecha="10-12-2020", etiqueta="casa", nota="Recibo de Luz"),
  3: Registro(id=3, id_usuario=1, tipo="egreso", valor=4000, fecha="10-12-2020", etiqueta="comida", nota="pina"),
  4: Registro(id=4, id_usuario=1, tipo="egreso", valor=28000, fecha="11-12-2020", etiqueta="transporte", nota="trayecto al trabajo"),
  5: Registro(id=5, id_usuario=1, tipo="egreso", valor=2600, fecha="12-12-2020", etiqueta="comida", nota="pina"),
  6: Registro(id=6, id_usuario=1, tipo="egreso", valor=28000, fecha="13-12-2020", etiqueta="casa", nota="Recibo Telefono"),
  7: Registro(id=7, id_usuario=1, tipo="egreso", valor=4000, fecha="14-12-2020", etiqueta="casa", nota="Recibo Gas"),
  8: Registro(id=8, id_usuario=1, tipo="egreso", valor=28000, fecha="15-12-2020", etiqueta="transporte", nota="Trayecto al trabajo")
}

presupuesto = {
  1: Presupuesto(id=1, id_usuario=1, etiqueta="casa", valor= 500000, mes= 12),
  2: Presupuesto(id=2, id_usuario=1, etiqueta="transporte", valor= 200000, mes= 12),
  3: Presupuesto(id=3, id_usuario=1, etiqueta="comida", valor= 300000, mes= 12),
  4: Presupuesto(id=4, id_usuario=1, etiqueta="entretenimiento", valor= 100000, mes= 12)
}


def obtener_registros():
    lista_datos = []
    for e in registros:
      lista_datos.append(registros[e])
        #for i in range lista_datos.len():
    return lista_datos

def crear_registro(registro: Registro):
      if registro.id in registros:
            return False
      else:
            registros[registro.id] = registro
            return True 

def obtener_presupuesto():
    lista_presupuesto = []
    for e in presupuesto:
      lista_presupuesto.append(presupuesto[e])
    return lista_presupuesto

def crear_presupuesto(presupuesto: Presupuesto):
      if presupuesto.id in presupuesto:
            return False
      else:
            presupuesto[presupuesto.id] = presupuesto
            return True 
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

registros = {
  1: Registro(id=1, id_usuario=1, tipo="egreso", valor= 2600, fecha="10-12-2020", etiqueta="comida", nota="pina"),
  2: Registro(id=2, id_usuario=1, tipo="ingreso", valor=28000, fecha="10-12-2020", etiqueta="venta", nota="galletas y torta"),
  3: Registro(id=3, id_usuario=2, tipo="egreso", valor=2600, fecha="10-12-2020", etiqueta="comida", nota="pina"),
  4: Registro(id=4, id_usuario=2, tipo="ingreso", valor=28000, fecha="10-12-2020", etiqueta="venta", nota="galletas y torta")
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
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
import datetime
import db
    
app = FastAPI()

origins = [
    "http://localhost",
    "http://localhost:8081",
    "http://localhost:8080",
    "https://contador-ala-mano-app.herokuapp.com",
    "https://contador-ala-mano-front.herokuapp.com",
    "https://contador-a-la-mano-app.herokuapp.com"
]


app.add_middleware(
    CORSMiddleware,
    allow_origins = origins,
    allow_credentials = True,
    allow_methods = ["*"],
    allow_headers = ["*"],
)

@app.get("/registro/balance/{id_usuario}")
async def obtener_balance(id_usuario : int):
    registros = db.obtener_registros()
    lista_final = []
    ingresos = []
    egresos = []
    for i in range(len(registros)):
        if registros[i].id_usuario == id_usuario:
           lista_final.append(registros[i])       
    for i in range(len(lista_final)):
        if lista_final[i].tipo == "ingreso":
            ingresos.append(lista_final[i].valor)
        else:
            egresos.append(lista_final[i].valor)

    return {"data":lista_final, "balance":sum(ingresos)-sum(egresos)}

@app.get("/presupuesto/balance/{id_usuario}")
async def obtener_presupuesto(id_usuario : int, etiqueta : str, mes : int):
    registros = db.obtener_registros()
    presupuesto = db.obtener_presupuesto()
    lista_registros = []
    lista_presupuesto = []
    gasto_total = 0
    for i in range(len(registros)):
        if registros[i].id_usuario == id_usuario and registros[i].etiqueta == etiqueta:
           lista_registros.append(registros[i])
    for i in range(len(presupuesto)):
        if presupuesto[i].etiqueta == etiqueta and presupuesto[i].mes == mes:
            lista_presupuesto.append(presupuesto[i])
    estado = lista_presupuesto[0].valor
    for i in range(len(lista_registros)):
        if lista_registros[i].tipo == "egreso" and lista_registros[i].etiqueta == etiqueta:
            gasto_total += lista_registros[i].valor
            estado-= lista_registros[i].valor
     
    return {"registros":lista_registros, "presupuesto": lista_presupuesto ,"estado": estado, "gastos_totales": gasto_total}


@app.post("/registro/")
async def crear_registro(registro: db.Registro):
    creado_exitosamente = db.crear_registro(registro)
    if creado_exitosamente:
        return {"mensaje": "Registro creado exitosamente"}
    else:
        raise HTTPException(status_code=400, detail="Error, la ID ya se encuentra registrada")


@app.get("/registro/tipo/{id_usuario}")
async def obtener_balance(id_usuario : int,Tipo : str):
    registros = db.obtener_registros()
    lista_usuario = []
    tipo_registro = []
    
    for i in range(len(registros)):
        if registros[i].id_usuario == id_usuario:
           lista_usuario.append(registros[i])
    
    for i in range(len(lista_usuario)):
        if lista_usuario[i].tipo == Tipo:
            tipo_registro.append(lista_usuario[i])

    return {Tipo:tipo_registro}

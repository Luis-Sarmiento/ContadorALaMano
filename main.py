from fastapi import FastAPI, HTTPException
import db
    
app = FastAPI()

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


@app.post("/registro/")
async def crear_registro(registro: db.Registro):
    creado_exitosamente = db.crear_registro(registro)
    if creado_exitosamente:
        return {"mensaje: Registro creado exitosamente"}
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
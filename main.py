from fastapi import FastAPI, HTTPException
import db
    
app = FastAPI()

@app.get("/registro/balance/")
async def obtener_balance():
    registros = db.obtener_registros()
    lista_final = []
    for i in range(len(registros)):
        if registros[i].id_usuario == 1:
           lista_final.append(registros[i])
    return lista_final

@app.post("/registro/")
async def crear_registro(registro: db.Registro):
    creado_exitosamente = db.crear_registro(registro)
    if creado_exitosamente:
        return {"mensaje: Registro creado exitosamente"}
    else:
        raise HTTPException(status_code=400, detail="Error, la ID ya se encuentra registrada")

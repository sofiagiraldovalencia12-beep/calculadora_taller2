"""
API REST de la calculadora (Paso 3 del taller).
Expone cada operación como un endpoint que recibe dos números
y devuelve el resultado en formato JSON.

Para ejecutar localmente:
    uvicorn app.main:app --reload

Documentación interactiva (Swagger):
    http://127.0.0.1:8000/docs
"""

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

from app.calculator import sumar, restar, multiplicar, dividir

app = FastAPI(title="Calculadora API", version="1.0.0")


class OperacionRequest(BaseModel):
    a: float
    b: float


class OperacionResponse(BaseModel):
    resultado: float


@app.get("/")
def root():
    return {"mensaje": "Calculadora API. Ve a /docs para probar los endpoints."}


@app.post("/sumar", response_model=OperacionResponse)
def endpoint_sumar(datos: OperacionRequest):
    return {"resultado": sumar(datos.a, datos.b)}


@app.post("/restar", response_model=OperacionResponse)
def endpoint_restar(datos: OperacionRequest):
    return {"resultado": restar(datos.a, datos.b)}


@app.post("/multiplicar", response_model=OperacionResponse)
def endpoint_multiplicar(datos: OperacionRequest):
    return {"resultado": multiplicar(datos.a, datos.b)}


@app.post("/dividir", response_model=OperacionResponse)
def endpoint_dividir(datos: OperacionRequest):
    try:
        resultado = dividir(datos.a, datos.b)
    except ValueError as error:
        # Se traduce el error de negocio a un error HTTP 400 (Bad Request)
        raise HTTPException(status_code=400, detail=str(error))
    return {"resultado": resultado}

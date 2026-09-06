# Pruebas de integración con SoapUI (Paso 5 del taller)

SoapUI no se puede automatizar desde aquí, así que sigue estos pasos en tu computador.

## 1. Requisitos previos
1. Instala **SoapUI Open Source**: https://www.soapui.org/downloads/soapui/
2. Ten la API corriendo localmente:
   ```
   cd calculadora_taller2
   pip install -r requirements.txt
   uvicorn app.main:app --reload
   ```
   La API quedará disponible en `http://127.0.0.1:8000`.

## 2. Crear el proyecto en SoapUI
1. Abre SoapUI → `File > New REST Project`.
2. En "URI" pega: `http://127.0.0.1:8000/sumar`
3. Repite `File > New REST Project` (o agrega un nuevo recurso al mismo proyecto) para `/restar`, `/multiplicar` y `/dividir`.

## 3. Configurar cada request
Para cada endpoint (sumar, restar, multiplicar, dividir):
1. Método: `POST`
2. Header: `Content-Type: application/json`
3. Body (ejemplo para sumar con positivos):
   ```json
   { "a": 5, "b": 3 }
   ```
4. Ejecuta el request (botón ▶) y revisa la respuesta:
   ```json
   { "resultado": 8 }
   ```

## 4. Casos de prueba a crear (uno por operación, positivos y negativos)

| Endpoint      | Body                        | Resultado esperado |
|---------------|------------------------------|---------------------|
| /sumar        | {"a": 5, "b": 3}             | 8                    |
| /sumar        | {"a": -5, "b": -3}           | -8                   |
| /restar       | {"a": 10, "b": 4}            | 6                    |
| /restar       | {"a": -10, "b": -4}          | -6                   |
| /multiplicar  | {"a": 6, "b": 7}             | 42                   |
| /multiplicar  | {"a": -6, "b": -7}           | 42                   |
| /dividir      | {"a": 20, "b": 5}             | 4                    |
| /dividir      | {"a": -20, "b": -5}          | 4                    |
| /dividir      | {"a": 10, "b": 0}             | Error 400 (entrada inválida) |

## 5. Agregar aserciones (Assertions)
Por cada request, en la pestaña "Assertions":
1. Click en `+` → `Property Content` → `Contains` o `JsonPath Match`.
2. Para validar el JSON de respuesta, usa un **JsonPath Match**:
   - Expresión: `$.resultado`
   - Valor esperado: el número esperado (ej. `8`)
3. Para el caso de división entre cero, agrega una aserción de **Valid HTTP Status Codes** = `400`.

## 6. Agrupar todo en un Test Suite
1. Click derecho sobre el proyecto → `New TestSuite` → nómbralo "Calculadora - Pruebas de Integración".
2. Dentro, crea un `New TestCase` por operación (SumaTestCase, RestaTestCase, etc.).
3. Arrastra los requests con sus aserciones dentro de cada TestCase.
4. Ejecuta el TestSuite completo con el botón ▶ verde y revisa que todos los casos queden en verde (PASS).

## 7. Evidencia a guardar
- Captura de pantalla del TestSuite ejecutado con todos los casos en verde.
- Exporta el reporte: click derecho sobre el TestSuite → `Generate TestSuite Summary Report`.

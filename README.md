# Taller 2 — Calculadora en Python con pruebas unitarias, de integración y E2E

Este proyecto resuelve el Taller 2 de Diseño de Sistemas de Información: una
calculadora expuesta como API REST, validada en tres niveles: **pytest**
(unitarias), **SoapUI** (integración) y **Serenity BDD** (E2E).

## Estructura del proyecto

```
calculadora_taller2/
├── app/
│   ├── __init__.py
│   ├── calculator.py      # Lógica de negocio (suma, resta, multiplicación, división)
│   └── main.py             # API REST con FastAPI (endpoints)
├── tests/
│   ├── __init__.py
│   └── test_calculator.py  # Pruebas unitarias con pytest
├── soapui/
│   └── GUIA_SOAPUI.md      # Guía paso a paso para las pruebas de integración
├── serenity/
│   ├── pom.xml
│   └── src/test/
│       ├── resources/features/calculadora.feature
│       └── java/
│           ├── steps/CalculadoraStepDefinitions.java
│           └── runners/CalculadoraTestSuite.java
├── requirements.txt
└── README.md
```

Esto cumple el **Paso 1** del taller: la lógica de negocio (`calculator.py`)
está separada de la API (`main.py`), y las pruebas están en su propia carpeta.

## Paso a paso para ejecutar TODO el taller

### 1. Instalar dependencias de Python
```bash
cd calculadora_taller2
python -m venv venv
source venv/bin/activate      # En Windows: venv\Scripts\activate
pip install -r requirements.txt
```

### 2. Levantar la API (Paso 3)
```bash
uvicorn app.main:app --reload
```
Abre `http://127.0.0.1:8000/docs` para ver y probar los endpoints en Swagger:
- `POST /sumar`
- `POST /restar`
- `POST /multiplicar`
- `POST /dividir`

Cada uno recibe `{"a": <número>, "b": <número>}` y devuelve `{"resultado": <número>}`.
La división entre cero devuelve un error HTTP 400 con un mensaje claro — así se
maneja la validación de división entre cero pedida en el taller.

### 3. Ejecutar las pruebas unitarias con pytest (Paso 4)
En otra terminal (con el entorno virtual activado):
```bash
pytest -v
```
Ya validé manualmente la lógica de `calculator.py` y todos los casos pasan
(sumas, restas, multiplicaciones y divisiones con positivos y negativos, más
el caso de división entre cero). Cuando ejecutes `pytest -v` en tu máquina
deberías ver 9 pruebas en verde — esa salida (captura de pantalla o log) es
la evidencia que pide el Paso 7.

### 4. Pruebas de integración con SoapUI (Paso 5)
Sigue la guía detallada en `soapui/GUIA_SOAPUI.md`. Resumen:
1. Con la API corriendo (`uvicorn app.main:app --reload`), crea un proyecto REST en SoapUI apuntando a `http://127.0.0.1:8000`.
2. Crea un TestCase por operación, con casos de números positivos, negativos y el caso de división entre cero.
3. Agrega aserciones JsonPath sobre el campo `resultado` y valida el código de estado HTTP.
4. Exporta el reporte del TestSuite como evidencia.

### 5. Pruebas E2E con Serenity BDD (Paso 6)
La carpeta `serenity/` contiene un proyecto Maven listo para usar (requiere Java 11+ y Maven):
1. Con la API corriendo, entra a la carpeta `serenity/`.
2. Ejecuta:
   ```bash
   mvn clean verify
   ```
3. Esto corre el archivo `calculadora.feature` (escrito en Gherkin, lenguaje
   de negocio) contra la API real, y genera un reporte HTML en
   `serenity/target/site/serenity/index.html`.
4. El feature cubre las 4 operaciones con positivos, negativos y el caso de
   división entre cero — igual que el taller pide.

### 6. Documentar y comparar resultados (Paso 7)
Para la entrega final, te recomiendo una tabla como esta:

| Tipo de prueba | Herramienta | Qué valida | Nivel |
|---|---|---|---|
| Unitaria | pytest | La lógica matemática pura, aislada de la API | Función individual |
| Integración | SoapUI | Que la API REST responde bien a peticiones HTTP reales | Comunicación API-cliente |
| E2E | Serenity BDD | El flujo completo desde la perspectiva del usuario de negocio | Sistema completo |

## Notas importantes
- El manejo de división entre cero se hace en la capa de lógica
  (`calculator.py` lanza `ValueError`) y se traduce a un error HTTP 400 en la
  API — así cada capa (unitaria e integración) puede probarlo de forma
  independiente.
- Los nombres de las pruebas en `test_calculator.py` siguen exactamente el
  patrón sugerido en el enunciado del taller (`test_sum_positive_numbers`, etc.).

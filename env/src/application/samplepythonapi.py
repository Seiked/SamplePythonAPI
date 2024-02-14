
# samplepythonapi:

from fastapi import FastApi

app: FastApi = FastApi(
    title = "SamplePythonApi",
    description = "USBCS202401"
)

####################################################

@app.get(
    "/operacionGet",
    summary = "Operacion Get",
    tags=["Get"])
async def operacion_get(dato_entrada: str):
    return dato_entrada

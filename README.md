# Proyecto nombre_pro_clientes

# Datos personales
Nombre: Anamaria Forigua Murcia
Ficha:3407180
# Descripción
Proyecto realizado con FastAPI para mostrar un mensaje principal y una lista de clientes.


# Proceso realizado realizado

# 1. Crear carpeta del proyecto llamada:
nombre_pro_clientes

# 2. Crear archivo principal:

main.py

# 3.Escribir en el archivo principal:
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def inicio():
    return {"mensaje": "Este es el proyecto de clientes a desarrollar"}

@app.get("/clientes")
def  clientes():
    clientes= ["Ana", "Edward", "Johanna", "Shakira","Maluma"]
    return {"mensaje":clientes }

Ir al terminal de visual (powershell) y digitar lo siguiente

# 4. Crear entorno virtual (recomendado):
python -m venv venv


# 5. Activar entorno virtual:
* Windows:
venv\Scripts\activate

# 6. Instalar dependencias:

pip install fastapi uvicorn

# 7. Ejecutar el proyecto
En la terminal de Visual Studio Code (PowerShell), escribe el siguiente comando:
fastapi dev main.py

# 8. Esperar la carga del servidor
Espera a que el servidor termine de iniciar. Una vez completado el proceso, aparecerá en la terminal el siguiente enlace:
*server   Documentation at http://127.0.0.1:8000/docs*

# 9 Abrir el enlace en el navegador
Ubica el cursor sobre el enlace que apareció en la terminal. Luego, mantén presionada la tecla *Ctrl* y haz clic izquierdo con el mouse para abrirlo en el navegador.

# 10 Explorar la documentación de FastAPI
Se cargará la interfaz interactiva de FastAPI (Swagger UI), donde podrás visualizar, probar, modificar o eliminar los endpoints de tu proyecto.

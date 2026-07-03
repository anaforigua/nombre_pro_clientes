# Proyecto nombre_pro_clientes

# Datos personales

**Nombre:** Anamaria Forigua Murcia  
**Ficha:** 3407180

---

# Descripción

Proyecto desarrollado con **FastAPI** y **SQLModel** para la gestión de clientes, facturas y transacciones utilizando una base de datos SQLite.

---

# Tecnologías utilizadas

- Python
- FastAPI
- SQLModel
- SQLite
- Uvicorn
- Git
- GitHub
- Visual Studio Code

---

# Proceso realizado

## 1. Crear la carpeta del proyecto

```bash
mkdir nombre_pro_clientes
cd nombre_pro_clientes
```

---

## 2. Crear el entorno virtual

```bash
python -m venv .mi_env
```

---

## 3. Activar el entorno virtual

### Windows

```bash
.mi_env\Scripts\activate
```

---

## 4. Instalar FastAPI

```bash
pip install fastapi
```

---

## 5. Instalar Uvicorn

```bash
pip install "uvicorn[standard]"
```

---

## 6. Instalar SQLModel

```bash
pip install sqlmodel
```

---

## 7. Verificar las dependencias instaladas

```bash
pip list
```

---

## 8. Generar el archivo requirements.txt

```bash
pip freeze > requirements.txt
```

---

## 9. Crear la estructura del proyecto

```
nombre_pro_clientes/
│
├── app/
│   ├── modelos/
│   ├── enrutadores/
│   ├── conexionbd.py
│   ├── main.py
│   └── __init__.py
│
├── .mi_env/
├── requirements.txt
├── .gitignore
└── bd_clientes.sqlte3
```

---

## 10. Ejecutar el proyecto

Desde la terminal:

```bash
fastapi dev app/main.py
```

o

```bash
python -m uvicorn app.main:app --reload
```

---

## 11. Abrir Swagger

Abrir en el navegador:

```
http://127.0.0.1:8000/docs
```

---

# Base de datos SQLite

La base de datos utilizada es:

```
bd_clientes.sqlte3
```

Crear las tablas automáticamente con SQLModel:

```python
SQLModel.metadata.create_all(motor_bd)
```

---

# Comandos Git utilizados

## Inicializar repositorio

```bash
git init
```

## Configurar usuario

```bash
git config --global user.name "Anamaria Forigua Murcia"
```

```bash
git config --global user.email "correo@ejemplo.com"
```

Verificar configuración

```bash
git config --global --list
```

---

## Agregar archivos

```bash
git add .
```

---

## Crear el primer commit

```bash
git commit -m "Primer commit"
```

---

## Agregar el repositorio remoto

```bash
git remote add origin https://github.com/anaforigua/nombre_pro_clientes.git
```

Si el remoto ya existía:

```bash
git remote set-url origin https://github.com/anaforigua/nombre_pro_clientes.git
```

---

## Descargar los cambios del repositorio remoto

```bash
git pull origin main --allow-unrelated-histories
```

---

## Resolver conflictos

Después de editar los archivos con conflicto:

```bash
git add .
```

```bash
git commit -m "Resolver conflictos"
```

---

## Cambiar el nombre de la rama principal

```bash
git branch -M main
```

---

## Subir el proyecto a GitHub

```bash
git push -u origin main
```

---

## Verificar el estado del repositorio

```bash
git status
```

---

## Ver historial de commits

```bash
git log --oneline
```

---

# Comandos útiles de SQLModel y FastAPI

## Instalar FastAPI

```bash
pip install fastapi
```

## Instalar SQLModel

```bash
pip install sqlmodel
```

## Instalar Uvicorn

```bash
pip install "uvicorn[standard]"
```

## Ejecutar el servidor

```bash
fastapi dev app/main.py
```

o

```bash
python -m uvicorn app.main:app --reload
```

## Instalar todas las dependencias del proyecto

```bash
pip install -r requirements.txt
```

## Actualizar requirements.txt

```bash
pip freeze > requirements.txt
```

---

# Funcionalidades desarrolladas

- Gestión de clientes.
- Gestión de facturas.
- Gestión de transacciones.
- Relaciones entre tablas mediante SQLModel.
- Base de datos SQLite.
- Documentación automática mediante Swagger.
- API REST desarrollada con FastAPI.
- Control de versiones utilizando Git y GitHub.

---
## Archivo principal (main.py)

El archivo `main.py` es el punto de entrada de la aplicación. En él se crea la aplicación de FastAPI, se configura la creación automática de las tablas de la base de datos al iniciar el servidor y se registran las rutas correspondientes a clientes, facturas y transacciones.

```python
from fastapi import FastAPI, HTTPException, status
from .enrutadores.clientes import rutas_clientes
from .enrutadores.facturas import rutas_facturas
from .enrutadores.transacciones import rutas_transacciones
from .conexionbd import crear_tablas

app = FastAPI(lifespan=crear_tablas)

# Incluir rutas
app.include_router(rutas_clientes, tags=["Clientes"])
app.include_router(rutas_facturas, tags=["Facturas"])
app.include_router(rutas_transacciones, tags=["Transacciones"])
```

### Explicación del código

- **FastAPI:** Crea la aplicación principal.
- **crear_tablas:** Ejecuta automáticamente la creación de las tablas de la base de datos al iniciar el proyecto.
- **rutas_clientes:** Registra todos los endpoints relacionados con los clientes.
- **rutas_facturas:** Registra todos los endpoints relacionados con las facturas.
- **rutas_transacciones:** Registra todos los endpoints relacionados con las transacciones.
- **tags:** Organiza los endpoints por categorías dentro de la documentación de Swagger (`/docs`), facilitando su navegación.


# Autor

**Anamaria Forigua Murcia**  
**Ficha:** 3407180

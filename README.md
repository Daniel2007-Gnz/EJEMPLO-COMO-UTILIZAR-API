# EjemploQuiz - API de Productos con Flask

API REST desarrollada en **Flask** que permite gestionar un catálogo de productos mediante los métodos **GET, POST, PUT y DELETE**.

## Requisitos previos

- [Python](https://www.python.org/downloads/) instalado (versión 3.9 o superior)
- [Git](https://git-scm.com/) instalado
- [Visual Studio Code](https://code.visualstudio.com/) instalado
- [Postman](https://www.postman.com/downloads/) instalado, para probar la API

## Instalación y ejecución paso a paso

### 1. Clonar el repositorio

Abre una terminal en la carpeta donde quieras guardar el proyecto y ejecuta:

```bash
git clone https://github.com/Daniel2007-Gnz/EJEMPLO-COMO-UTILIZAR-API.git
```

### 2. Entrar a la carpeta del proyecto

```bash
cd EJEMPLO-COMO-UTILIZAR-API
```

### 3. Abrir el proyecto en VS Code

```bash
code .
```

### 4. Crear el entorno virtual

Dentro de la carpeta del proyecto, ejecuta:

```bash
python -m venv .env
```

### 5. Activar el entorno virtual

**En Windows (PowerShell):**
```bash
.\.env\Scripts\Activate.ps1
```

**En Mac/Linux:**
```bash
source .env/bin/activate
```

Sabrás que el entorno está activo porque la terminal mostrará `(.env)` al inicio de la línea.

> ⚠️ Si PowerShell muestra un error de permisos, ejecuta primero:
> `Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass`

### 6. Instalar las dependencias

Con el entorno virtual activado:

```bash
pip install -r requirements.txt
```

### 7. Ejecutar el proyecto

```bash
python app.py
```

Si todo salió bien, verás un mensaje similar a este en la terminal:

```
* Running on http://127.0.0.1:5000
* Debugger is active!
```

La API ya está corriendo y lista para recibir peticiones en `http://127.0.0.1:5000`.

> 💡 Ejecuta siempre `python app.py` desde la terminal integrada de VS Code (con el entorno `.env` activado), no con el botón ▶️ "Run" de extensiones como Code Runner, ya que este puede usar un intérprete de Python distinto al del entorno virtual y arrojar el error `ModuleNotFoundError: No module named 'flask'`.

## Endpoints disponibles

| Método | Endpoint | Descripción |
|--------|----------|-------------|
| GET | `/api/productos` | Obtiene la lista completa de productos |
| GET | `/api/productos/<id>` | Obtiene un producto específico por su id |
| POST | `/api/productos` | Crea un nuevo producto |
| PUT | `/api/productos/<id>` | Modifica un producto existente |
| DELETE | `/api/productos/<id>` | Elimina un producto por su id |

## Pruebas con Postman

Con el servidor Flask corriendo, abre Postman y prueba cada endpoint:

### 1. GET - Obtener todos los productos

Método `GET` a `http://127.0.0.1:5000/api/productos`. Devuelve el listado completo en formato JSON.

![GET todos los productos](01-get-productos.png)

### 2. GET - Obtener un producto por id

Método `GET` a `http://127.0.0.1:5000/api/productos/1`. Devuelve únicamente el producto solicitado.

![GET un producto](02-get-producto-id.png)

### 3. PUT - Modificar un producto

Método `PUT` a `http://127.0.0.1:5000/api/productos/1`, enviando en el **Body** (raw JSON) los campos a actualizar, por ejemplo:

![PUT modificar producto](03-put-modificar.png)

### 4. POST - Crear un producto

Método `POST` a `http://127.0.0.1:5000/api/productos`, enviando en el **Body** (raw JSON) el nuevo producto:

![POST crear producto](04-post-crear.png)
La API responde con código `201 CREATED` y el producto creado, incluyendo su nuevo `id`.

### 5. DELETE - Eliminar un producto

Método `DELETE` a `http://127.0.0.1:5000/api/productos/3`. La API responde confirmando la eliminación:


![DELETE eliminar producto](05-delete-borrar.png)

## Notas

- El servidor levanta por defecto en `http://127.0.0.1:5000`.

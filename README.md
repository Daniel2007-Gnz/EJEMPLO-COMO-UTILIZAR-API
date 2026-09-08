# EjemploQuiz - API de Productos con Flask

API REST desarrollada en **Flask** que permite gestionar un catálogo de productos mediante los métodos **GET, POST, PUT y DELETE**.

## Requisitos previos

- [Python](https://www.python.org/downloads/) instalado (versión 3.9 o superior)
- [Git](https://git-scm.com/) instalado
- [Visual Studio Code](https://code.visualstudio.com/) instalado
- [Postman](https://www.postman.com/downloads/) instalado, para probar la API

## Instalación y ejecución paso a paso

### 1. Abrir Visual Studio Code

Abre Visual Studio Code. Puede estar en una carpeta vacía o en cualquier carpeta donde quieras guardar el proyecto; en el siguiente paso clonaremos el repositorio ahí dentro.

### 2. Abrir la terminal integrada de VS Code

Con VS Code abierto, abre la terminal integrada usando el atajo de teclado:

```
Ctrl + Ñ
```

> En teclados en español, este es el atajo por defecto de VS Code para mostrar/ocultar la terminal. Si no te funciona, ve al menú **Terminal → Nueva terminal**.

Verás un panel en la parte inferior de VS Code donde puedes escribir comandos. A partir de aquí, todos los comandos siguientes se ejecutan dentro de esa terminal.

### 3. Clonar el repositorio

Desde la terminal que acabas de abrir, ubícate (si quieres) en la carpeta donde quieras guardar el proyecto y ejecuta:

```
git clone https://github.com/Daniel2007-Gnz/EJEMPLO-COMO-UTILIZAR-API.git
```

### 4. Entrar a la carpeta del proyecto

```
cd EJEMPLO-COMO-UTILIZAR-API
```

Si VS Code no abrió automáticamente la carpeta del proyecto, puedes abrirla con:

```
code .
```

> Ten en cuenta que `code .` abre la carpeta del proyecto en VS Code, pero **no abre la terminal automáticamente**. Sigue con el siguiente paso para volver a abrirla.

### 5. Volver a abrir la terminal en el proyecto

Como `code .` no abre la terminal por sí solo, ábrela de nuevo con el mismo atajo que en el paso 2:

```
Ctrl + Ñ
```

Ahora la terminal ya está ubicada dentro de la carpeta del proyecto (`EJEMPLO-COMO-UTILIZAR-API`), lista para los siguientes comandos.

### 6. Crear el entorno virtual

Dentro de la carpeta del proyecto, ejecuta:

```
python -m venv .env
```

Esto creará una carpeta `.env` con un entorno de Python aislado para el proyecto.

### 7. Activar el entorno virtual

Si cerraste la terminal después de crear el entorno virtual, vuelve a abrirla con `Ctrl + Ñ` (como en el paso 2) antes de continuar.

**En Windows (PowerShell):**

```
.env\Scripts\activate
```

Si la activación fue correcta, verás `(.env)` al inicio de la línea de la terminal.

> Si PowerShell muestra un error de permisos al activar el entorno, ejecuta primero:
> ```
> Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
> ```
> y vuelve a intentarlo.

### 8. Instalar las dependencias

Con el entorno virtual activado:

```
pip install -r requirements.txt
```

### 9. Ejecutar el proyecto

```
python app.py
```

Si todo salió bien, verás un mensaje similar a este en la terminal:

```
* Running on http://127.0.0.1:5000
* Debugger is active!
```

Copia esa URL (`http://127.0.0.1:5000`); la vas a usar en Postman en el siguiente paso. Deja esta terminal abierta y corriendo mientras pruebas la API; es el servidor Flask.

## Endpoints disponibles

| Método | Endpoint              | Descripción                              |
| ------ | --------------------- | ----------------------------------------- |
| GET    | `/api/productos`      | Obtiene la lista completa de productos    |
| GET    | `/api/productos/<id>` | Obtiene un producto específico por su id  |
| POST   | `/api/productos`      | Crea un nuevo producto                    |
| PUT    | `/api/productos/<id>` | Modifica un producto existente            |
| DELETE | `/api/productos/<id>` | Elimina un producto por su id             |

## 10. Probar la API con Postman

Con el servidor Flask corriendo y la URL copiada, abre Postman y crea una petición para cada endpoint:

1. Abre Postman y crea una nueva pestaña de petición con el botón **+**.
2. En el menú desplegable de la izquierda de la barra de dirección, selecciona el **método HTTP** (GET, POST, PUT o DELETE).
3. En el campo de la URL, pega la dirección copiada y agrega la ruta del endpoint, por ejemplo `http://127.0.0.1:5000/api/productos`.
4. Si el endpoint necesita datos (POST o PUT), ve a la pestaña **Body**, selecciona **raw** y elige el formato **JSON** en el menú desplegable de la derecha, y escribe el JSON con los datos a enviar.
5. Haz clic en el botón azul **Send**.
6. Revisa la respuesta en la parte inferior: el código de estado (200, 201, 404, etc.) y el cuerpo de la respuesta en formato JSON.

Puedes ir creando una pestaña nueva en Postman para cada uno de los siguientes casos:

### 10.1. GET - Obtener todos los productos

- Método: `GET`
- URL: `http://127.0.0.1:5000/api/productos`
- Body: no necesita body.

![GET todos los productos](https://github.com/Daniel2007-Gnz/EJEMPLO-COMO-UTILIZAR-API/raw/main/01-get-productos.png)

### 10.2. GET - Obtener un producto por id

- Método: `GET`
- URL: `http://127.0.0.1:5000/api/productos/1`
- Body: no necesita body.

![GET un producto](https://github.com/Daniel2007-Gnz/EJEMPLO-COMO-UTILIZAR-API/raw/main/02-get-producto-id.png)

### 10.3. PUT - Modificar un producto

- Método: `PUT`
- URL: `http://127.0.0.1:5000/api/productos/1`
- Body (raw JSON), con los campos a actualizar, por ejemplo:

```
{
  "nombre": "Asus",
  "precio": 1200
}
```

![PUT modificar producto](https://github.com/Daniel2007-Gnz/EJEMPLO-COMO-UTILIZAR-API/raw/main/03-put-modificar.png)

### 10.4. POST - Crear un producto

- Método: `POST`
- URL: `http://127.0.0.1:5000/api/productos`
- Body (raw JSON), con el nuevo producto:

```
{
  "nombre": "mustang",
  "precio": 1234
}
```

La API responde con código `201 CREATED` y el producto creado, incluyendo su nuevo `id`.

![POST crear producto](https://github.com/Daniel2007-Gnz/EJEMPLO-COMO-UTILIZAR-API/raw/main/04-post-crear.png)

### 10.5. DELETE - Eliminar un producto

- Método: `DELETE`
- URL: `http://127.0.0.1:5000/api/productos/3`
- Body: no necesita body.

La API responde confirmando la eliminación:

```
{
  "mensaje": "Producto eliminado"
}
```

![DELETE eliminar producto](https://github.com/Daniel2007-Gnz/EJEMPLO-COMO-UTILIZAR-API/raw/main/05-delete-borrar.png)

## Notas

- El servidor levanta por defecto en `http://127.0.0.1:5000`.
- Para detener el servidor, en la terminal donde está corriendo presiona `Ctrl + C`.
- Para volver a activar el entorno virtual en una nueva sesión (por ejemplo, si cerraste VS Code y lo vuelves a abrir), abre la terminal con `Ctrl + Ñ` y repite el paso 7 antes de ejecutar `python app.py`.

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

Con el servidor Flask corriendo y la URL `http://127.0.0.1:5000` copiada, abre Postman.

### ¿Qué es el `id` y por qué a veces se usa `1`, a veces `3`, etc.?

Cada producto que existe en la API tiene un número identificador único llamado `id` (por ejemplo, el producto 1, el producto 2, el producto 3...). Ese número es el que se usa en la URL cuando quieres trabajar con **un producto en particular** (para consultarlo, modificarlo o borrarlo).

- En el endpoint `GET /api/productos` (sin id) pides **todos** los productos, así que no hace falta poner ningún número.
- En los endpoints que sí llevan `<id>` en la URL (`GET /api/productos/<id>`, `PUT /api/productos/<id>`, `DELETE /api/productos/<id>`), `<id>` se reemplaza por el número del producto exacto que quieres consultar, modificar o eliminar.

Por eso en los ejemplos de abajo se usa `1` para consultar y modificar (porque el producto con id `1` ya existe en los datos de ejemplo del proyecto) y `3` para eliminar (porque también existe un producto con id `3`). Si quieres trabajar con otro producto, cambia ese número por el `id` real que quieras usar. Para saber qué ids existen, primero puedes hacer la petición **GET - Obtener todos los productos** (punto 10.1) y revisar la lista.

### Cómo crear cada petición en Postman, paso a paso

Para **cada uno** de los 5 casos de abajo (10.1 a 10.5), repite exactamente estos pasos:

1. En Postman, haz clic en el botón **+** para abrir una pestaña de petición nueva.
2. Haz clic en el menú desplegable que dice `GET` (está a la izquierda de la barra de dirección) y selecciona el método indicado en el caso que estés siguiendo (`GET`, `POST`, `PUT` o `DELETE`).
3. Haz clic en el campo de la barra de dirección (donde dice "Enter URL or paste text").
4. **Copia y pega exactamente la URL** que se indica en ese caso, sin escribirla a mano y sin cambiar nada, salvo que se indique lo contrario.
5. Si el caso indica un **Body**, haz clic en la pestaña **Body** (debajo de la barra de dirección), selecciona la opción **raw**, y en el menú desplegable que aparece a la derecha (por defecto dice "Text") selecciona **JSON**.
6. **Copia y pega exactamente el JSON** que se muestra en ese caso dentro del cuadro de texto grande que aparece.
7. Haz clic en el botón azul **Send**, a la derecha de la barra de dirección.
8. Revisa la respuesta que aparece abajo: el código de estado (por ejemplo `200`, `201`, `404`) y el contenido en formato JSON.

Puedes crear una pestaña nueva en Postman para cada uno de los siguientes 5 casos, siguiendo siempre los pasos de arriba.

### 10.1. GET - Obtener todos los productos

Este endpoint no necesita ningún `id` porque devuelve **todos** los productos de una vez.

- Método a seleccionar en Postman: `GET`
- URL a copiar y pegar: `http://127.0.0.1:5000/api/productos`
- Body: no se necesita body, así que no hagas los pasos 5 y 6 de arriba.

![GET todos los productos](https://github.com/Daniel2007-Gnz/EJEMPLO-COMO-UTILIZAR-API/raw/main/01-get-productos.png)

### 10.2. GET - Obtener un producto por id

Este endpoint sí necesita un `id` en la URL, porque le estás pidiendo un producto específico y no toda la lista. En el ejemplo se usa `1` porque ese producto ya existe en los datos de prueba.

- Método a seleccionar en Postman: `GET`
- URL a copiar y pegar: `http://127.0.0.1:5000/api/productos/1`
- Body: no se necesita body.

![GET un producto](https://github.com/Daniel2007-Gnz/EJEMPLO-COMO-UTILIZAR-API/raw/main/02-get-producto-id.png)

### 10.3. PUT - Modificar un producto

Este endpoint también necesita un `id` en la URL, porque le estás diciendo a la API **cuál** producto quieres cambiar. Se usa `1` porque es el mismo producto que consultaste en el paso anterior. El Body indica los datos nuevos que reemplazarán a los datos actuales de ese producto.

- Método a seleccionar en Postman: `PUT`
- URL a copiar y pegar: `http://127.0.0.1:5000/api/productos/1`
- Body a copiar y pegar (raw JSON):

```
{
  "nombre": "Asus",
  "precio": 1200
}
```

![PUT modificar producto](https://github.com/Daniel2007-Gnz/EJEMPLO-COMO-UTILIZAR-API/raw/main/03-put-modificar.png)

### 10.4. POST - Crear un producto

Este endpoint **no** lleva `id` en la URL, porque todavía no existe el producto: es la API la que le asigna un `id` nuevo automáticamente cuando lo creas. El Body indica los datos del producto nuevo que quieres agregar.

- Método a seleccionar en Postman: `POST`
- URL a copiar y pegar: `http://127.0.0.1:5000/api/productos`
- Body a copiar y pegar (raw JSON):

```
{
  "nombre": "mustang",
  "precio": 1234
}
```

La API responde con código `201 CREATED` y el producto creado, incluyendo su nuevo `id` (ese `id` es el que se generó automáticamente y podrías usar luego en un GET, PUT o DELETE).

![POST crear producto](https://github.com/Daniel2007-Gnz/EJEMPLO-COMO-UTILIZAR-API/raw/main/04-post-crear.png)

### 10.5. DELETE - Eliminar un producto

Este endpoint necesita un `id` en la URL, porque le estás diciendo a la API **cuál** producto eliminar de la lista. En el ejemplo se usa `3` porque ese producto ya existe en los datos de prueba (distinto al `1` de los casos anteriores, solo para mostrar que puede ser cualquier id existente).

- Método a seleccionar en Postman: `DELETE`
- URL a copiar y pegar: `http://127.0.0.1:5000/api/productos/3`
- Body: no se necesita body.

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

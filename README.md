# EjemploQuiz - Guía de instalación y uso

Guía paso a paso para configurar, ejecutar y sincronizar este proyecto Flask con Git, además de cómo probar la API con Postman.

## Requisitos previos

- [Python](https://www.python.org/downloads/) instalado
- [Visual Studio Code](https://code.visualstudio.com/) instalado
- [Git](https://git-scm.com/downloads) instalado
- [Postman](https://www.postman.com/downloads/) instalado (para probar la API)

## 1. Crear la carpeta del proyecto

Crea una carpeta vacía con cualquier nombre. En este ejemplo se usó `EjemploQuiz2`.

## 2. Abrir Visual Studio Code

Abre Visual Studio Code (VS Code).

## 3. Importar la carpeta al proyecto

En VS Code, ve a `Archivo > Abrir carpeta...` y selecciona la carpeta creada en el paso 1.

## 4. Abrir la terminal

Abre la terminal integrada de VS Code con el atajo `Ctrl + Ñ` (o desde el menú `Terminal > Nueva terminal`).

## 5. Crear el entorno virtual

```bash
python -m venv .env
```

Esto crea una carpeta `.env` que contendrá el entorno virtual de Python, aislado del resto del sistema.

## 6. Activar el entorno virtual

```bash
.env\Scripts\activate
```

> **Nota:** Si PowerShell no permite activar el entorno virtual (error de permisos/políticas de ejecución), ejecuta el siguiente comando y luego repite el paso 6:
>
> ```powershell
> Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
> ```
>
> Este comando permite ejecutar scripts locales firmados (como el de activación del entorno virtual) sin comprometer la seguridad del sistema.

Cuando el entorno esté activo, verás `(.env)` al inicio de la línea de la terminal.

## 7. Instalar Flask

```bash
python -m pip install flask
```

## 8. Generar e instalar las dependencias del proyecto

Primero, generar el archivo con las librerías instaladas en el entorno:

```bash
pip freeze > requirements.txt
```

Luego, para instalar las librerías listadas en ese archivo (por ejemplo, en otra máquina o al clonar el repo):

```bash
pip install -r requirements.txt
```

## 9. Ejecutar el proyecto

```bash
python app.py
```

Por defecto, Flask levanta el servidor en `http://127.0.0.1:5000/`.

## 10. Sincronización con Git

Inicializar el repositorio y subir los archivos:

```bash
git init
git add .
git commit -m "mensaje del commit"
git branch -M main
git remote add origin <URL-del-repositorio>
git push -u origin main
```

> **Nota:** Si el repositorio remoto ya tiene contenido (por ejemplo, un README creado desde GitHub), antes de hacer push es necesario traer esos cambios:
>
> ```bash
> git pull origin main --allow-unrelated-histories
> ```
>
> Esto puede abrir un editor de texto (Vim) para confirmar el mensaje del merge. Para guardar y salir: presiona `Esc`, escribe `:wq` y presiona `Enter`.

## 11. Probar la API con Postman

Postman es una herramienta para enviar peticiones HTTP a tu API y ver la respuesta, sin necesidad de usar un navegador o escribir código de prueba.

Pasos básicos:

1. Abre Postman y crea una nueva petición (`+`).
2. Selecciona el método HTTP, por ejemplo `GET`.
3. En el campo de la URL, escribe la dirección de tu servidor local, por ejemplo:
   ```
   http://127.0.0.1:5000/
   ```
4. En la pestaña **Params** puedes agregar parámetros de consulta (query params) si tu endpoint los necesita, escribiendo el `Key` y el `Value` correspondiente.
5. Haz clic en **Send** para enviar la petición.
6. La respuesta del servidor (JSON, HTML, código de estado, etc.) aparecerá en la parte inferior de la ventana.

> Asegúrate de que el servidor Flask esté corriendo (`python app.py`) antes de enviar la petición desde Postman.

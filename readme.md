
# DataMaq FastAPI

DataMaq FastAPI es un backend moderno para monitoreo y gestión de producción industrial, desarrollado en Python utilizando FastAPI y SQLAlchemy. Implementa Clean Architecture para garantizar escalabilidad, mantenibilidad y separación de responsabilidades. Expone una API RESTful y sirve archivos estáticos para una SPA frontend.

![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)
![FastAPI](https://img.shields.io/badge/FastAPI-0.100+-brightgreen.svg)

## 📋 Requisitos

- Python 3.8+
- FastAPI 0.100+
- Uvicorn

## 🚀 Instalación

1. Clonar el repositorio:
   ```bash
   git clone https://github.com/agustinmadygraf/datamaq-fastapi.git
   cd datamaq-fastapi
   ```

2. Crear un entorno virtual e instalar dependencias:
   ```bash
   python -m venv venv
   Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope Process
   venv\Scripts\activate
   pip install -r requirements.txt
   ```


## ⚙️ Configuración

1. Crear un archivo .env en la raíz del proyecto:
   ```
    # --- MySQL ---
    MYSQL_HOST=localhost
    MYSQL_PORT=3306
    MYSQL_DB=tu_base_de_datos
    MYSQL_USER=tu_usuario
    MYSQL_PASSWORD=tu_contraseña
    STATIC_PATH="C:\AppServ\www\datamaq_vue\dist"
   ```

### Inicialización de la base de datos

Para crear la base de datos, las tablas y cargar los datos iniciales, ejecuta el siguiente comando:

```bash
python init_database.py
```

Este script utiliza los scripts SQL ubicados en la carpeta `database/` y las variables de entorno definidas en tu archivo `.env`.

## 🏃‍♂️ Ejecución


Para iniciar el servidor con la configuración por defecto (según tu archivo `.env`):
```bash
python run.py
```


El servicio estará disponible en `http://localhost:5000`.


## 🏗️ Estructura del proyecto

```
datamaq-fastapi/
│
├── run.py                  # Script principal para iniciar el servidor FastAPI
├── db_inicializer.py       # Inicialización y carga de la base de datos
├── requirements.txt        # Dependencias del proyecto
├── database/               # Scripts SQL para inicialización y carga
├── src/
│   ├── entities/           # Entidades del dominio
│   ├── use_cases/          # Casos de uso (Application)
│   ├── interface_adapters/ # Controladores, gateways, presenters
│   ├── infrastructure/     # Implementaciones concretas (FastAPI, SQLAlchemy)
│   └── shared/             # Configuración y utilidades
├── tools/                  # Utilidades y scripts auxiliares
└── readme.md
```


## 🧩 Arquitectura

Este proyecto implementa Clean Architecture tanto en backend (Python) como en frontend (JavaScript):

### Backend (Python)
1. **Domain**: Interfaces y reglas de negocio.
2. **Application**: Casos de uso.
3. **Infrastructure**: Implementaciones concretas.
4. **Adapters**: Conectores entre capas.
5. **Presentation**: Controladores HTTP.

### Frontend (JavaScript)
1. **Entities**: Modelos y entidades del dominio.
2. **Use Cases**: Casos de uso y lógica de aplicación.
3. **Interface Adapters**: Presenters, gateways y controladores.
4. **Infrastructure**: Adaptadores concretos (DOM, HTTP, WebSocket).
5. **Adapters**: Utilidades y adaptadores secundarios.

## ⚙️ Configuración (Frontend)

La configuración de IP, puerto y rutas del servidor de streaming está centralizada en `static/src/infrastructure/config.js`.  
Asegúrate de que los valores coincidan con los definidos en tu archivo `.env` del backend.

## 🚀 Endpoints y UI

La interfaz web se encuentra en `dist/index.html` y consume los endpoints definidos en el backend.  
La comunicación con el backend se realiza mediante WebSocket y MJPEG stream, configurados en el frontend.

## 📚 Documentación adicional

Consulta la carpeta `docs/` para documentación técnica y de API.
```

## 🧩 Arquitectura

Este proyecto implementa una arquitectura limpia (Clean Architecture) con las siguientes capas:

1. **Domain**: Define las interfaces y reglas de negocio.
2. **Application**: Implementa los casos de uso que orquestan el flujo de la aplicación.
3. **Infrastructure**: Contiene implementaciones concretas de las interfaces del dominio.
4. **Adapters**: Conecta la lógica de negocio con las interfaces externas.
5. **Presentation**: Maneja la forma en que se exponen las funcionalidades.


## 🌐 API

El servicio expone los siguientes endpoints principales:

- `GET /api/v1/dashboard` — Obtiene datos agregados para el dashboard de producción.
- `GET /static/{path}` — Sirve archivos estáticos del frontend (SPA).
- `GET /` — Sirve la SPA principal (`index.html`).

> **Nota:** La lista completa de endpoints y sus parámetros está documentada en la API interactiva generada automáticamente por FastAPI en `/docs` y `/redoc`.


## 🔧 Tecnologías utilizadas

- **Python 3.8+**
- **FastAPI** — Framework web moderno y asíncrono
- **Uvicorn** — Servidor ASGI para producción
- **SQLAlchemy** — ORM para acceso a base de datos
- **MySQL** — Motor de base de datos relacional
- **dotenv** — Manejo de variables de entorno


## 📝 Licencia

Este proyecto está bajo la Licencia MIT. Consulta el archivo LICENSE para más detalles.


## 🤝 Contribución

Las contribuciones son bienvenidas. Por favor, abre un issue o pull request con tus sugerencias o mejoras.
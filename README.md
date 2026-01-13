# 🌸 Iris Prediction App

Una aplicación full-stack para predecir especies de flores Iris usando Machine Learning, construida con FastAPI, Streamlit y SQLite.

## 📋 Tabla de Contenidos

- [Características](#características)
- [Arquitectura](#arquitectura)
- [Requisitos Previos](#requisitos-previos)
- [Instalación](#instalación)
- [Uso](#uso)
- [Estructura del Proyecto](#estructura-del-proyecto)
- [API Endpoints](#api-endpoints)
- [Base de Datos](#base-de-datos)
- [Desarrollo](#desarrollo)
- [Despliegue con Docker](#despliegue-con-docker)

## ✨ Características

- 🤖 **Predicción ML**: Modelo entrenado con el dataset Iris clásico
- 💾 **Persistencia**: Almacenamiento automático de predicciones en SQLite
- 🎨 **Interfaz Intuitiva**: Frontend interactivo con Streamlit
- 🚀 **API RESTful**: Backend robusto con FastAPI
- 🐳 **Dockerizado**: Fácil despliegue con Docker Compose
- 📊 **Historial**: Registro de todas las predicciones con timestamp

## 🏗️ Arquitectura

```
┌─────────────┐      HTTP      ┌─────────────┐      SQL      ┌──────────┐
│  Streamlit  │ ────────────> │   FastAPI   │ ───────────> │  SQLite  │
│  Frontend   │    requests    │   Backend   │   queries    │ database │
└─────────────┘                └─────────────┘               └──────────┘
  Port: 8501                     Port: 8000                   database.db
```

## 📦 Requisitos Previos

- Python 3.13+
- pip o uv
- Docker y Docker Compose (opcional, para despliegue containerizado)

## 🚀 Instalación

### 1. Clonar el repositorio

```bash
git clone <repository-url>
cd <project-folder>
```

### 2. Instalar dependencias

#### Backend
```bash
cd backend
pip install -r requirements.txt
```

#### Frontend
```bash
cd frontend
pip install -r requirements.txt
```

## 💻 Uso

### Opción 1: Ejecución Local (Desarrollo Rápido)

#### Terminal 1 - Iniciar Backend
```bash
cd backend/app
fastapi dev main.py
```

El backend estará disponible en: `http://localhost:8000`

#### Terminal 2 - Iniciar Frontend
```bash
cd frontend
streamlit run app.py
```

El frontend estará disponible en: `http://localhost:8501`

### Opción 2: Usar Docker Compose (Recomendado)

```bash
# Construir y ejecutar
docker-compose up --build

# Ejecutar en segundo plano
docker-compose up -d

# Detener
docker-compose down
```

## 📁 Estructura del Proyecto

```
.
├── backend/
│   ├── app/
│   │   ├── api/
│   │   │   └── predict.py          # Endpoints de predicción
│   │   ├── database/
│   │   │   └── database.py         # Configuración de BD
│   │   ├── models/
│   │   │   ├── iris_model.joblib   # Modelo ML entrenado
│   │   │   └── train_model.py      # Script de entrenamiento
│   │   ├── schemas/
│   │   │   └── input_output.py     # Modelos Pydantic/SQLModel
│   │   ├── utils/
│   │   │   └── loader.py           # Utilidades
│   │   └── main.py                 # Aplicación FastAPI
│   ├── Dockerfile
│   └── requirements.txt
├── frontend/
│   ├── app.py                      # Aplicación Streamlit
│   ├── Dockerfile
│   └── requirements.txt
├── docker-compose.yml
├── database.db                     # Base de datos SQLite
└── README.md
```

## 🔌 API Endpoints

### `POST /predict/`

Realiza una predicción y guarda el resultado en la base de datos.

**Request Body:**
```json
{
  "feature1": 5.1,
  "feature2": 3.5,
  "feature3": 1.4,
  "feature4": 0.2
}
```

**Response:**
```json
{
  "id": 1,
  "feature1": 5.1,
  "feature2": 3.5,
  "feature3": 1.4,
  "feature4": 0.2,
  "predicted_class": 0,
  "timestamp": "2026-01-13T20:53:41.213950"
}
```

**Clases de Predicción:**
- `0`: Iris Setosa
- `1`: Iris Versicolor
- `2`: Iris Virginica

### Documentación Interactiva

Una vez que el backend esté corriendo, accede a:
- Swagger UI: `http://localhost:8000/docs`
- ReDoc: `http://localhost:8000/redoc`

## 🗄️ Base de Datos

### Esquema de la Tabla `prediction`

| Campo | Tipo | Descripción |
|-------|------|-------------|
| `id` | INTEGER | Primary key (auto-incremental) |
| `feature1` | FLOAT | Longitud del sépalo |
| `feature2` | FLOAT | Ancho del sépalo |
| `feature3` | FLOAT | Longitud del pétalo |
| `feature4` | FLOAT | Ancho del pétalo |
| `predicted_class` | INTEGER | Clase predicha (0, 1, 2) |
| `timestamp` | DATETIME | Fecha y hora de la predicción |

### Consultar la Base de Datos

```python
import sqlite3

conn = sqlite3.connect('database.db')
cursor = conn.cursor()
cursor.execute("SELECT * FROM prediction")
print(cursor.fetchall())
conn.close()
```

## 🛠️ Desarrollo

### Entrenar el Modelo

```bash
cd backend/app/models
python train_model.py
```

Esto generará un nuevo archivo `iris_model.joblib`.

### Ejecutar Tests

```bash
cd backend/app/models
python test_prediction.py
```

### Variables de Entorno

Para desarrollo local, el frontend usa `http://localhost:8000`.

Para Docker, usa `http://backend:8000` (se configura automáticamente).

### Hot Reload

El backend con `fastapi dev` y el frontend con `streamlit run` tienen hot-reload automático al detectar cambios en el código.

## 🐳 Despliegue con Docker

### Configuración de Producción

Modifica `docker-compose.yml` para producción:

```yaml
version: "3.11"
services:
  backend:
    build: ./backend
    ports:
      - "8000:8000"
    volumes:
      - ./database.db:/home/proyect/database.db
    restart: always
    
  frontend:
    build: ./frontend
    ports:
      - "8501:8501"
    environment:
      - DOCKER_ENV=true
    depends_on:
      - backend
    restart: always
```

### Comandos Útiles

```bash
# Ver logs
docker-compose logs -f

# Ver logs de un servicio específico
docker-compose logs -f backend

# Reconstruir solo un servicio
docker-compose up -d --build backend

# Limpiar contenedores y volúmenes
docker-compose down -v
```

## 📊 Características del Modelo

El modelo utiliza las siguientes características de las flores Iris:

1. **Feature 1**: Longitud del sépalo (cm)
2. **Feature 2**: Ancho del sépalo (cm)
3. **Feature 3**: Longitud del pétalo (cm)
4. **Feature 4**: Ancho del pétalo (cm)

## 🤝 Contribuir

1. Fork el proyecto
2. Crea una rama para tu feature (`git checkout -b feature/AmazingFeature`)
3. Commit tus cambios (`git commit -m 'Add some AmazingFeature'`)
4. Push a la rama (`git push origin feature/AmazingFeature`)
5. Abre un Pull Request

## 📝 Licencia

Este proyecto está bajo la Licencia MIT.

## 👨‍💻 Autor

Desarrollado como proyecto de aprendizaje de FastAPI, Streamlit y Docker.

## 🙏 Agradecimientos

- Dataset Iris: Ronald Fisher (1936)
- FastAPI: Sebastián Ramírez
- Streamlit: Streamlit Inc.
- SQLModel: Sebastián Ramírez

---

**¿Problemas?** Abre un issue en el repositorio.

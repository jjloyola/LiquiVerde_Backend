# 🛒 Desafío LiquiVerde de Grupo Lagos - Backend

Backend de **LiquiVerde**, una API REST desarrollada con FastAPI que proporciona servicios para asistencia inteligente de compras, permitiendo a los usuarios buscar productos, gestionar listas de compras y optimizar sus compras considerando precio y sostenibilidad.

## 📋 Tabla de Contenidos

- [Descripción](#-descripción)
- [Arquitectura y Estructura](#-arquitectura-y-estructura)
- [Funcionalidades Implementadas](#-funcionalidades-implementadas)
- [Instalación](#-instalación)
- [Configuración](#-configuración)
- [Algoritmos Implementados](#-algoritmos-implementados)
- [Uso de IA](#-uso-de-ia)

## 🎯 Descripción

LiquiVerde Backend es una API REST desarrollada con **FastAPI** y **Python** que proporciona los siguientes servicios:

- Búsqueda de productos por nombre o código de barras
- Gestión de listas de compras (crear, consultar, añadir/eliminar items)
- Optimización de listas de compras considerando precio y sostenibilidad
- Consulta de información de productos con precios en diferentes tiendas
- Información de sostenibilidad (EcoScore) de productos

## 🏗️ Arquitectura y Estructura

### Arquitectura Limpia (Clean Architecture)

El proyecto sigue una **arquitectura limpia en capas** que separa las responsabilidades en diferentes niveles.

### Distribución de Carpetas

```
LiquiVerde_Backend/
├── apps/                          # Capa de Aplicación
│   ├── product/                   # Servicios de productos
│   │   └── product_service.py
│   └── shopping_list/             # Servicios de listas de compras
│       └── shopping_list_service.py
│
├── domains/                       # Capa de Dominio
│   ├── product.py                 # Entidad Product
│   ├── shopping_list.py           # Entidad ShoppingList
│   ├── list_item.py               # Entidad ListItem
│   ├── product_repository_interface.py    # Contrato de repositorio
│   ├── shopping_list_repository_interface.py
│   ├── list_item_repository_interface.py
│   ├── product_service_interface.py       # Contrato de servicio
│   ├── shopping_list_service_interface.py
│   └── optimization/              # Lógica de optimización
│       ├── optimizatin_product_with_store.py
│       ├── optimization_product_list_with_store.py
│       └── shopping_list_optimization_data.py
│
├── infrastructures/               # Capa de Infraestructura
│   ├── database/
│   │   ├── connection.py          # Configuración de BD
│   │   └── models.py              # Modelos SQLModel
│   └── repositories/              # Implementaciones de repositorios
│       ├── product_repository.py
│       ├── shopping_list_repository.py
│       └── list_item_repository.py
│
├── resources/                      # Capa de Presentación
│   ├── product_resource.py        # Endpoints de productos
│   ├── shopping_list_resource.py  # Endpoints de listas
│   └── dtos/                      # Data Transfer Objects
│       ├── input/                 # DTOs de entrada
│       └── output/                 # DTOs de salida
│
├── dependencies/                   # Inyección de dependencias
│   ├── product_dependencies.py
│   └── shopping_list_dependencies.py
│
├── main.py                         # Punto de entrada de FastAPI
└── requirements.txt                # Dependencias del proyecto
```

### Flujo de Datos

1. **Request HTTP** → `resources/*_resource.py` (Endpoints)
2. **Validación y Transformación** → DTOs (Input/Output)
3. **Lógica de Negocio** → `apps/*/service.py` (Servicios)
4. **Acceso a Datos** → `infrastructures/repositories/*.py` (Repositorios)
5. **Base de Datos** → PostgreSQL mediante SQLModel

## ✨ Funcionalidades Implementadas

### 1. Gestión de Productos

#### Endpoints Disponibles:

La información de productos siempre se retorna con información sobre tiendas asociadas, stock y precios

- **`GET /products/get_all_products`**: Obtiene todos los productos (con límite)

  - Parámetros: `limit` (default: 100)

- **`GET /products/{product_id}`**: Obtiene un producto por ID

  - Retorna información completa del

- **`GET /products/get_by_barcode/{barcode}`**: Busca producto por código de barras

  - Retorna el producto si existe

- **`GET /products/get_by_name_like/{text}`**: Búsqueda de productos por nombre
  - Utiliza búsqueda con trigramas para encontrar similitudes
  - Retorna lista de productos con información resumida (menos campos de detalle en el objeto Producto)

### 2. Gestión de Listas de Compras

#### Endpoints Disponibles:

- **`POST /api/lists/{list_id}/items`**: Añade un item a una lista

  - Si `list_id` es `None`, crea una nueva lista automáticamente
  - Parámetros: `product_id`, `quantity`, `priority`, `notes`

- **`GET /api/lists/{list_id}`**: Obtiene una lista de compras por ID

  - Retorna la lista con todos sus items

- **`DELETE /api/lists/{list_id}/items/{item_id}`**: Elimina un item de una lista

  - Valida que el item pertenezca a la lista

- **`POST /api/lists/optimize`**: Optimiza una lista de compras
  - **Nota**: Endpoint parcialmente implementado (retorna datos dummy)
  - Parámetros: lista de productos, porcentajes de importancia (precio/sostenibilidad), presupuesto máximo

### 3. Características Técnicas

- **Búsqueda Inteligente**: Búsqueda por nombre usando trigramas de PostgreSQL
- **Validación de Datos**: Pydantic para validación de DTOs
- **Manejo de Errores**: HTTPExceptions con códigos de estado apropiados
- **CORS Configurado**: Permite requests desde frontend (localhost:5173)
- **Documentación Automática**: Swagger UI disponible en `/` y ReDoc en `/redoc`

## 🚀 Instalación

### Prerrequisitos

- Python 3.10 o superior
- PostgreSQL (base de datos accesible y configurada)
- pip (gestor de paquetes de Python)

### Pasos de Instalación

1. **Clonar el repositorio** (si aplica):

```bash
git clone <url-del-repositorio>
cd LiquiVerde_Backend
```

2. **Crear entorno virtual** (recomendado):

```bash
python -m venv venv
source venv/bin/activate  # En Windows: venv\Scripts\activate
```

3. **Instalar dependencias**:

```bash
pip install -r requirements.txt
```

4. **Configurar variables de entorno**:

Crear un archivo `.env` en la raíz del proyecto con la siguiente configuración:

```env
DATABASE_URL=postgresql://usuario:contraseña@localhost:5432/nombre_bd
```

**Nota**: Asegurar que la base de datos ya esté creada y accesible.

4.5. **Habilitar extensión pg_trgm en PostgreSQL**:

La búsqueda de productos por nombre requiere la extensión `pg_trgm` de PostgreSQL. Para habilitarla, ejecuta el siguiente comando SQL en tu base de datos:

```sql
-- Conectarse a la base de datos
psql -U usuario -d nombre_bd

-- Habilitar la extensión
CREATE EXTENSION IF NOT EXISTS pg_trgm;
```

**Alternativa usando psql directamente**:

```bash
psql -U usuario -d nombre_bd -c "CREATE EXTENSION IF NOT EXISTS pg_trgm;"
```

**Nota**: Asegúrate de tener permisos de superusuario o permisos para crear extensiones en la base de datos.

5. **Iniciar el servidor**:

```bash
uvicorn main:app --reload
```

6. **Verificar la instalación**:

- La API estará disponible en `http://localhost:8000`
- La documentación Swagger UI estará en `http://localhost:8000/`
- ReDoc estará disponible en `http://localhost:8000/redoc`

## ⚙️ Configuración

### Variables de Entorno

El proyecto utiliza las siguientes variables de entorno:

| Variable       | Descripción                  | Ejemplo                                    |
| -------------- | ---------------------------- | ------------------------------------------ |
| `DATABASE_URL` | URL de conexión a PostgreSQL | `postgresql://user:pass@localhost:5432/db` |

### Configuración de Base de Datos

- **ORM**: SQLModel (combinación de SQLAlchemy y Pydantic)
- **Motor**: PostgreSQL con psycopg2-binary
- **Creación de Tablas**: Automática al iniciar la aplicación (mediante `create_db_and_tables()`)

### Configuración de CORS

El middleware CORS está configurado para permitir requests desde:

- `http://localhost:5173` (frontend en desarrollo)

Para producción, modificar en `main.py`:

```python
allow_origins=["http://localhost:5173", "https://tu-dominio.com"]
```

### Endpoints Principales

#### Productos

- `GET /products/get_all_products?limit=100`
- `GET /products/{product_id}`
- `GET /products/get_by_barcode/{barcode}`
- `GET /products/get_by_name_like/{keyword}`

#### Listas de Compras

- `POST /api/lists/{list_id}/items`
- `GET /api/lists/{list_id}`
- `DELETE /api/lists/{list_id}/items/{item_id}`
- `POST /api/lists/optimize`

## 🔬 Algoritmos Implementados

### 1. Búsqueda de Productos por Nombre (Trigramas)

**Ubicación**: `infrastructures/repositories/product_repository.py`

El algoritmo utiliza la extensión `pg_trgm` de PostgreSQL para realizar búsquedas de similitud:

```python
# Pseudocódigo del algoritmo
1. Activar extensión pg_trgm en PostgreSQL
2. Crear índice GIN en nombre del producto usando trigramas
3. Realizar búsqueda con operador de similitud (similarity)
4. Ordenar resultados por similitud descendente
5. Retornar productos con mayor similitud
```

**Ventajas**:

- Encuentra productos con nombres similares aunque tengan errores tipográficos
- Más flexible que búsqueda exacta o LIKE
- Mejor rendimiento con índices GIN

**Complejidad**: O(n log n) donde n es el número de productos (con índice)

### 2. Cálculo de Puntuación de Optimización

**Ubicación**: `domains/optimization/optimization_product_list_with_store.py`

El algoritmo calcula puntuaciones para optimización de listas de compras:

```python
# Propiedades calculadas:
1. total_price: Suma de (precio × cantidad) para todos los productos
2. total_sustainability_score: Suma de (sustainability_score × sustainability_importance_percentage)
3. total_price_score: Suma de (precio × cantidad × price_importance_percentage)
4. total_objective_score: total_price_score + total_sustainability_score
5. is_within_budget: Verifica si total_price <= max_budget
```

**Lógica**:

- Combina precio y sostenibilidad según porcentajes de importancia
- Permite balancear entre ahorro económico y sostenibilidad ambiental
- Valida restricción de presupuesto máximo

**Complejidad**: O(n) donde n es el número de productos en la lista

### 3. Gestión de Listas de Compras

**Ubicación**: `apps/shopping_list/shopping_list_service.py`

Algoritmo para añadir items a listas:

```python
# Pseudocódigo
1. Si list_id es None:
   a. Crear nueva lista con nombre "New List"
   b. Usar el ID de la nueva lista
2. Verificar que la lista existe
3. Crear ListItem con:
   - list_id, product_id, quantity, priority, notes
   - timestamp automático (added_at)
4. Guardar en base de datos
```

**Características**:

- Creación automática de lista si no existe
- Validación de existencia de lista antes de añadir items
- Timestamps automáticos para auditoría

### 4. Optimización de Lista de Compras (Parcial)

**Ubicación**: `apps/shopping_list/shopping_list_service.py`

**Estado Actual**: Parcialmente implementado (retorna datos dummy)

**Algoritmo Esperado**:

```python
# Pseudocódigo del algoritmo esperado
1. Recibir lista original con productos y tiendas
2. Para cada producto:
   a. Buscar alternativas (mismo producto en otras tiendas)
   b. Buscar sustitutos (productos similares)
3. Calcular todas las combinaciones posibles
4. Evaluar cada combinación según:
   - Precio total
   - Puntuación de sostenibilidad
   - Restricción de presupuesto
5. Seleccionar mejor solución según objective_score
6. Retornar lista optimizada con diferencias calculadas
```

**Nota**: La implementación completa está pendiente. Actualmente retorna la lista original sin optimización.

## 🤖 Uso de IA

Este proyecto ha recibido asistencia de IA para su desarrollo. A continuación se detalla el uso de herramientas de IA:

### Asistencia Recibida

Durante el desarrollo de este proyecto se utilizó asistencia de IA principalmente para:

- Consultas sobre arquitectura limpia y mejores prácticas de diseño
- Sugerencias sobre estructura y organización de código en capas
- Revisión y optimización de implementaciones
- Generación de documentación y comentarios en código
- Resolución de problemas técnicos y debugging

### Herramientas Utilizadas

- **Cursor AI**: Editor con asistencia de IA para desarrollo. Se utilizó para consultas sobre arquitectura, patrones de diseño y mejores prácticas en Python y FastAPI.

---

## 📝 Notas Adicionales

- El proyecto asume que PostgreSQL está instalado y la base de datos está creada y accesible
- La extensión `pg_trgm` debe estar habilitada en PostgreSQL para la búsqueda por nombre (ver instrucciones en sección [Instalación](#-instalación))
- El endpoint de optimización está parcialmente implementado y requiere desarrollo adicional
- La documentación interactiva (Swagger/ReDoc) está disponible en la raíz de la API

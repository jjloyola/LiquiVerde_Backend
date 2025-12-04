# LiquiVerde – Planificación de Implementación

Este documento detalla el plan de desarrollo paso a paso para el proyecto LiquiVerde, priorizando la funcionalidad core antes de las mejoras opcionales.

> **Nota:** Para ver los requerimientos completos del proyecto, consulta [README_LiquiVerde.md](./README_LiquiVerde.md)

## Estructura del Proyecto

Este proyecto está organizado en múltiples repositorios:

- **Repositorio actual (Preparacion):** Contiene la Fase 1 (Modelo de Datos y Dataset)
- **Repositorio Backend:** Contendrá las Fases 0, 2, 3 y 6 (Backend)
- **Repositorio Frontend:** Contendrá las Fases 0, 4, 5 y 6 (Frontend)

La Fase 0 (Configuración) se realizará en los repositorios de backend y frontend por separado, después de completar la Fase 1.

---

## Fase 1: Modelo de Datos y Dataset de Ejemplo (2-3 horas)

**Objetivo:** Diseñar y poblar la base de datos con datos realistas para desarrollo y pruebas.

- [x] **1.** Definir esquema de base de datos:
  - Tabla `products` (id, nombre, barcode, categoría, precio, unidad, etc.)
  - Tabla `stores` (id, nombre, dirección, coordenadas, etc.)
  - Tabla `product_stores` (relación muchos-a-muchos: producto, tienda, precio, disponibilidad)
  - Tabla `sustainability_scores` (producto, score_economico, score_ambiental, score_social, huella_carbono)
  - Tabla `shopping_lists` (id, nombre, fecha_creacion, presupuesto_max)
  - Tabla `list_items` (lista_id, producto_id, cantidad, prioridad)
- [x] **2.** Crear scripts de migración o esquema SQL inicial
- [x] **3.** Documentar relaciones y campos clave

### 1.2 Evaluación de APIs Públicas

- [x] **4.** Por cada API pública mencionada, descargar una muestra de datos:
  - Open Food Facts: 20-30 productos de ejemplo (guardar JSON/CSV)
  - USDA FoodData: 10-15 productos (si requiere API key, evaluar alternativa)
  - Tesco API: evaluar disponibilidad y formato de respuesta
  - Carbon Interface: probar con algunos productos de ejemplo
  - OpenStreetMap: probar búsqueda de direcciones
- [x] **5.** Evaluar cada fuente según:
  - **Legibilidad:** ¿Los datos son claros y completos?
  - **Facilidad de uso:** ¿La API es fácil de integrar?
  - **Cumplimiento:** ¿Proporciona datos necesarios para el proyecto?
- [x] **6.** Seleccionar 1-2 APIs principales para datos de productos
- [x] **7.** Decidir si usar APIs en tiempo real o datos pre-cargados

### 1.3 Creación de Tablas e Inserción de Datos

- [x] **8.** Crear script SQL o migración para todas las tablas
- [x] **9.** Ejecutar creación de tablas en PostgreSQL
- [x] **10.** Crear script Python (`scripts/load_sample_data.py`) que:
  - Obtenga datos de las APIs seleccionadas
  - Transforme y normalice los datos
  - Inserte productos en la base de datos
  - Genere datos sintéticos realistas para precios, tiendas y disponibilidad
- [x] **11.** Poblar base de datos con al menos 50-100 productos de ejemplo
- [x] **12.** Crear datos de ejemplo para 3-5 tiendas
- [x] **13.** Validar integridad de datos insertados

**Entregables:** TODO

- Esquema de base de datos documentado
- Base de datos poblada con datos de ejemplo
- Scripts de carga de datos funcionales
- Archivos CSV/JSON de muestra de APIs (para referencia)

---

## Fase 0: Configuración Inicial del Proyecto (1-2 horas)

**Objetivo:** Establecer la estructura base del proyecto y entorno de desarrollo.

> **Nota:** Esta fase se realizará en los repositorios separados de backend y frontend.

### Tareas Backend:

- [ ] **14.** Crear estructura de carpetas del proyecto backend
- [ ] **15.** Configurar repositorio Git con `.gitignore` apropiado
- [ ] **16.** Configurar entorno virtual de Python
- [ ] **17.** Instalar dependencias base: FastAPI/Flask, psycopg2
- [ ] **18.** Configurar conexión a PostgreSQL (usar base de datos de Fase 1)
- [ ] **19.** Crear archivo `.env.example` con variables de entorno necesarias
- [ ] **20.** Configurar scripts básicos de inicialización

### Tareas Frontend:

- [ ] **21.** Crear estructura de carpetas del proyecto frontend
- [ ] **22.** Configurar repositorio Git con `.gitignore` apropiado
- [ ] **23.** Inicializar proyecto React + Vite
- [ ] **24.** Configurar routing (React Router)
- [ ] **25.** Configurar cliente HTTP (axios/fetch) para conectar con backend
- [ ] **26.** Crear estructura de componentes base
- [ ] **27.** Configurar variables de entorno para URL del backend

**Entregables:**

- Proyectos backend y frontend con estructura organizada
- Conexión a base de datos PostgreSQL establecida
- Entornos de desarrollo funcionando en ambos repositorios

---

## Fase 2: Backend Core - Productos y Scoring (2-3 horas)

**Objetivo:** Implementar endpoints básicos y sistema de scoring de sostenibilidad.

> **Nota:** Esta fase corresponde al repositorio Backend.

### 2.1 Endpoints de Productos

- [ ] **28.** `GET /api/products` - Listar productos (con paginación y filtros)
- [ ] **29.** `GET /api/products/{id}` - Obtener detalle de producto
- [ ] **30.** `GET /api/products/search?q={query}` - Búsqueda de productos
- [ ] **31.** `GET /api/products/{id}/barcode` - Buscar por código de barras
- [ ] **32.** Implementar manejo de errores y validaciones
- [ ] **33.** Documentar endpoints (Swagger/OpenAPI si usas FastAPI)

### 2.2 Sistema de Scoring de Sostenibilidad

- [ ] **34.** Implementar algoritmo de scoring que calcule:
  - **Score Económico:** Basado en precio y relación precio/calidad
  - **Score Ambiental:** Basado en huella de carbono, packaging, origen
  - **Score Social:** Basado en comercio justo, producción local, etc.
- [ ] **35.** `POST /api/products/{id}/score` - Calcular score de un producto
- [ ] **36.** `GET /api/products/{id}/sustainability` - Obtener métricas de sostenibilidad
- [ ] **37.** Crear función que combine los 3 scores en un score total
- [ ] **38.** Documentar fórmulas y criterios de scoring

**Entregables:**

- API REST funcional para consulta de productos
- Sistema de scoring implementado y documentado
- Endpoints probados con datos de ejemplo

---

## Fase 3: Backend Core - Listas y Optimización (3-4 horas)

**Objetivo:** Implementar gestión de listas de compras y algoritmo de optimización multiobjetivo.

> **Nota:** Esta fase corresponde al repositorio Backend.

### 3.1 Endpoints de Listas de Compras

- [ ] **39.** `POST /api/lists` - Crear nueva lista de compras
- [ ] **40.** `GET /api/lists` - Listar todas las listas
- [ ] **41.** `GET /api/lists/{id}` - Obtener lista específica
- [ ] **42.** `POST /api/lists/{id}/items` - Agregar producto a lista
- [ ] **43.** `PUT /api/lists/{id}/items/{item_id}` - Actualizar cantidad/prioridad
- [ ] **44.** `DELETE /api/lists/{id}/items/{item_id}` - Eliminar producto de lista
- [ ] **45.** `DELETE /api/lists/{id}` - Eliminar lista

### 3.2 Algoritmo de Mochila Multiobjetivo

- [ ] **46.** Implementar algoritmo de optimización que considere:
  - **Presupuesto máximo** (restricción)
  - **Maximizar score de sostenibilidad** (objetivo 1)
  - **Minimizar costo total** (objetivo 2)
  - **Maximizar disponibilidad** (objetivo 3)
- [ ] **47.** `POST /api/lists/{id}/optimize` - Optimizar lista de compras
- [ ] **48.** Retornar lista optimizada con:
  - Productos seleccionados
  - Costo total
  - Score de sostenibilidad total
  - Ahorro estimado (si aplica)
- [ ] **49.** Documentar algoritmo y parámetros

### 3.3 Algoritmo de Sustitución Inteligente (Opcional - si se implementa como 2º algoritmo)

- [ ] **50.** `POST /api/products/{id}/alternatives` - Buscar productos alternativos
- [ ] **51.** Implementar lógica de sustitución basada en:
  - Categoría similar
  - Precio comparable
  - Mejor score de sostenibilidad
- [ ] **52.** `POST /api/lists/{id}/suggest-substitutions` - Sugerir sustituciones para lista

**Entregables:**

- API completa de gestión de listas
- Algoritmo de optimización multiobjetivo funcionando
- Al menos 2 de los 3 algoritmos obligatorios implementados
- Endpoints de optimización probados

---

## Fase 4: Frontend - Búsqueda y Detalle (2-3 horas)

**Objetivo:** Implementar interfaz básica para buscar y visualizar productos.

> **Nota:** Esta fase corresponde al repositorio Frontend. La configuración básica ya se hizo en la Fase 0.

### 4.2 Página de Búsqueda

- [ ] **53.** Componente de búsqueda de productos
- [ ] **54.** Input de búsqueda por texto
- [ ] **55.** Input de búsqueda por código de barras (escáner simulado)
- [ ] **56.** Lista de resultados con cards de productos
- [ ] **57.** Paginación de resultados
- [ ] **58.** Manejo de estados de carga y error

### 4.3 Página de Detalle de Producto

- [ ] **59.** Vista de detalle con información completa
- [ ] **60.** Mostrar precio, categoría, disponibilidad
- [ ] **61.** Mostrar scores de sostenibilidad (económico, ambiental, social)
- [ ] **62.** Botón para agregar a lista
- [ ] **63.** Mostrar productos alternativos (si está implementado)

**Entregables:**

- Frontend básico funcionando
- Búsqueda y visualización de productos operativa
- Conexión frontend-backend establecida

---

## Fase 5: Frontend - Listas y Optimización (2-3 horas)

**Objetivo:** Implementar gestión de listas y visualización de optimización.

> **Nota:** Esta fase corresponde al repositorio Frontend.

### 5.1 Gestión de Listas

- [ ] **64.** Página de listas de compras
- [ ] **65.** Crear nueva lista
- [ ] **66.** Ver lista existente con productos agregados
- [ ] **67.** Agregar/eliminar productos de lista
- [ ] **68.** Editar cantidades y prioridades

### 5.2 Optimización de Listas

- [ ] **69.** Botón "Optimizar Lista" en vista de lista
- [ ] **70.** Página de resultados de optimización que muestre:
  - Lista original vs lista optimizada
  - Comparación de costos
  - Comparación de scores de sostenibilidad
  - Ahorro estimado
  - Impacto ambiental mejorado
- [ ] **71.** Opción de aplicar optimización o mantener original
- [ ] **72.** Visualización clara de diferencias

**Entregables:**

- Flujo completo: buscar → agregar → optimizar
- Interfaz funcional y clara
- Aplicación mínima viable completa

---

## Fase 6: Mejoras y Bonus (2-4 horas)

**Objetivo:** Implementar funcionalidades bonus y mejoras de calidad.

> **Nota:** Esta fase se distribuye entre los repositorios Backend y Frontend según corresponda.

### 6.1 Mejoras de Algoritmos (Backend)

- [ ] **73.** Refinar fórmulas de scoring
- [ ] **74.** Mejorar algoritmo de optimización (considerar más factores)
- [ ] **75.** Añadir cálculo de ahorros detallado
- [ ] **76.** Añadir cálculo de impacto ambiental total

### 6.2 Funcionalidades Bonus Backend

- [ ] **77.** `GET /api/lists/{id}/savings` - Calcular ahorros detallados
- [ ] **78.** `GET /api/lists/{id}/environmental-impact` - Calcular impacto ambiental
- [ ] **79.** Endpoints de tiendas y geolocalización (si aplica)

### 6.3 Funcionalidades Bonus Frontend

- [ ] **80.** Dashboard de ahorro e impacto
- [ ] **81.** Comparador de productos lado a lado
- [ ] **82.** Gráficos de sostenibilidad
- [ ] **83.** Mejoras de UI/UX

### 6.4 Calidad y Documentación (Backend y Frontend)

- [ ] **84.** Tests unitarios básicos (al menos para algoritmos críticos)
- [ ] **85.** Mejorar manejo de errores
- [ ] **86.** Documentar código complejo
- [ ] **87.** Actualizar README con instrucciones completas

### 6.5 Dockerización (Bonus)

- [ ] **88.** Crear `Dockerfile` para backend
- [ ] **89.** Crear `Dockerfile` para frontend
- [ ] **90.** Crear `docker-compose.yml` con backend, frontend y PostgreSQL
- [ ] **91.** Documentar despliegue con Docker

**Entregables:**

- Funcionalidades bonus implementadas
- Código con mejor calidad y tests
- Proyecto dockerizado (opcional)
- Documentación completa

---

## Resumen de Prioridades

### Crítico (MVP - Mínimo Viable):

1. ✅ Fase 1: Modelo de datos (Repositorio Preparacion)
2. ✅ Fase 0: Configuración (Repositorios Backend y Frontend)
3. ✅ Fase 2: Backend productos y scoring
4. ✅ Fase 3: Backend listas y optimización (al menos 2 algoritmos)
5. ✅ Fase 4: Frontend búsqueda
6. ✅ Fase 5: Frontend listas y optimización

### Importante (Mejora calidad):

- Refinamiento de algoritmos
- Mejoras de UI/UX
- Manejo robusto de errores

### Bonus (Puntos extra):

- Dockerización
- Tests unitarios
- Dashboard y visualizaciones
- Despliegue en cloud
- PWA

---

## Estimación de Tiempo por Fase

| Fase                                | Tiempo Estimado | Prioridad | Repositorio        |
| ----------------------------------- | --------------- | --------- | ------------------ |
| Fase 1: Modelo de Datos             | 2-3 horas       | Crítica   | Preparacion        |
| Fase 0: Configuración               | 1-2 horas       | Crítica   | Backend + Frontend |
| Fase 2: Backend Core - Productos    | 2-3 horas       | Crítica   | Backend            |
| Fase 3: Backend Core - Optimización | 3-4 horas       | Crítica   | Backend            |
| Fase 4: Frontend - Búsqueda         | 2-3 horas       | Crítica   | Frontend           |
| Fase 5: Frontend - Listas           | 2-3 horas       | Crítica   | Frontend           |
| Fase 6: Mejoras y Bonus             | 2-4 horas       | Opcional  | Backend + Frontend |
| **Total MVP**                       | **12-18 horas** |           |                    |
| **Total con Bonus**                 | **14-22 horas** |           |                    |

---

# Fin del Documento

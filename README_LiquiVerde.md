# LiquiVerde – Resumen Técnico del Desafío (Input para IA)

Este documento consolida **todos los requerimientos obligatorios, opcionales, objetivos del sistema y criterios de evaluación** del desafío técnico de Grupo Lagos. Está diseñado como **input inicial para que una IA pueda planificar, diseñar o desarrollar el proyecto**.

---

# 1. Objetivo General

Construir una **plataforma de retail inteligente** que permita a los consumidores:

- **Ahorrar dinero** al optimizar sus decisiones de compra.
- **Reducir su impacto ambiental y social** mediante análisis de sostenibilidad.
- **Tomar mejores decisiones de compra** considerando precio, impacto y disponibilidad.

La aplicación debe funcionar como un **asistente de compras inteligente**, combinando datos de productos, precios y sostenibilidad.

---

# 2. Arquitectura Requerida (Full Stack)

La solución debe incluir:

## 2.1 Backend API (Obligatorio)

- Sistema de análisis de productos y sostenibilidad.
- Optimización de listas de compras multiobjetivo.
- Endpoints para consulta, análisis y optimización.
- Persistencia de datos.

### Bonus Backend:

- Cálculo de ahorros.
- Cálculo de impacto ambiental.
- Sistema inteligente de sustitución de productos.
- Planificación temporal de compras.
- Optimización de rutas de tiendas.
- Sistema de recompensas por sostenibilidad.

---

## 2.2 Frontend Web/Móvil (Obligatorio)

- Escáner o búsqueda de productos.
- Pantalla de generación de listas optimizadas.
- UI funcional y clara.

### Bonus Frontend:

- Dashboard de ahorro e impacto.
- Comparador de productos y alternativas.
- Mapa de tiendas y rutas eficientes.
- Versión PWA.

---

# 3. Stack Tecnológico Permitido

## Frontend

- React + Vite

## Backend

- Python (FastAPI, Flask o Django)

## Bases de datos

- PostgreSQL

## Opcionales (bonus)

- Docker / Docker Compose
- Despliegue en servicios gratuitos
- PWA (Progressive Web App)

---

# 4. APIs Públicas Permitidas (cualquiera pública además de estas)

### Datos de productos:

- Open Food Facts API  
  https://world.openfoodfacts.org/api/v0/product/{barcode}.json  
  https://world.openfoodfacts.org/api/v2/search?countries=chile&categories=food
- USDA FoodData Central  
  https://api.nal.usda.gov/fdc/v1/foods/search?api_key=YOUR_API_KEY

### Precios y comercio:

- Tesco API (o alternativa)  
  https://dev.tescolabs.com/grocery/products/?query={product}

### Huella de carbono:

- Carbon Interface API  
  https://www.carboninterface.com/api/v1/estimates

### Geolocalización:

- OpenStreetMap Nominatim  
  https://nominatim.openstreetmap.org/search?format=json&q={address}

---

# 5. Algoritmos Requeridos

## Obligatorios (mínimo 2 de los 3 siguientes)

Debes implementar **al menos 2** de estos 3 algoritmos:

1. **Algoritmo de Mochila Multiobjetivo** para optimización de lista de compras.
2. **Sistema de Scoring de Sostenibilidad** (económico, ambiental, social).
3. **Algoritmo de Sustitución Inteligente** de productos.

## Opcionales

- Planificación temporal de compras.
- Optimización de rutas de tiendas.
- Sistema de recompensas por sostenibilidad.

---

# 6. Entregables Obligatorios

1. **Repositorio Git** con:

   - Código fuente completo.
   - Archivo `README.md` con:
     - Instrucciones de despliegue.
     - Configuración de APIs públicas.
     - Variables de entorno.
     - Explicación de algoritmos implementados.
     - Sección “Uso de IA”.
   - Dataset de ejemplo.

2. Aplicación funcional que cumpla con:
   - Análisis de productos escaneados/buscados.
   - Generación de listas optimizadas.
   - Cálculo de ahorros e impacto (nota: según requerimientos originales aparece como obligatorio en entregables, pero funcionalmente es bonus).

---

# 7. Criterios de Evaluación

## 7.1 Funcionalidad (50%)

- API funcional.
- Análisis de productos.
- Listas optimizadas con criterios multiobjetivo.
- Interfaz clara.
- Ahorro/impacto ambiental (bonus).

## 7.2 Algoritmos (30%)

- Correcta implementación del algoritmo de optimización.
- Cálculos de sostenibilidad.
- Calidad del código algorítmico.

## 7.3 Calidad del Código (20%)

- Arquitectura limpia.
- Buen manejo de errores.
- Documentación adecuada.

## 7.4 Bonus (+10%)

- Dockerización.
- Despliegue en cloud.
- Tests unitarios.
- Funcionalidades extra.

---

# 8. Requisitos Mínimos y Deseables

## Mínimos:

- Backend con APIs completas.
- Frontend capaz de buscar productos y optimizar listas.
- Implementación de 2 algoritmos obligatorios.
- Dataset inicial.
- README bien documentado.

## Deseables:

- Scoring sostenible más sofisticado.
- Mapa/tiendas.
- Sustitución inteligente.
- Dashboard.
- Despliegue online.
- Docker Compose.
- Tests unitarios o e2e.

---

# 9. Recomendaciones Clave para el Desarrollo

- Enfocarse primero en **backend + datos** antes del frontend.
- Priorizar la optimización de lista (core del desafío).
- Usa datos realistas: Crea un dataset de ejemplo convincente.
- Explica tus fórmulas: Documenta cómo calculas sostenibilidad y ahorro.
- Piensa en el usuario: La interfaz debe hacer complejidad simple.
- Diseñar un flujo de usuario sencillo (buscar → agregar → optimizar).
- **La innovación en sostenibilidad y ahorro será altamente valorada.**

---

# 10. Planificación de Implementación

> 📋 **Nota:** La planificación detallada con todas las fases, tareas numeradas y estimaciones de tiempo se encuentra en el archivo **[README_PLANIFICACION.md](./README_PLANIFICACION.md)**

La planificación incluye 6 fases principales:

1. **Fase 0:** Configuración Inicial (1-2 horas)
2. **Fase 1:** Modelo de Datos y Dataset (2-3 horas)
3. **Fase 2:** Backend Core - Productos y Scoring (2-3 horas)
4. **Fase 3:** Backend Core - Listas y Optimización (3-4 horas)
5. **Fase 4:** Frontend - Búsqueda y Detalle (2-3 horas)
6. **Fase 5:** Frontend - Listas y Optimización (2-3 horas)
7. **Fase 6:** Mejoras y Bonus (2-4 horas)

**Total MVP:** 12-18 horas | **Total con Bonus:** 14-22 horas

---

# 11. Uso de IA (para completar más adelante)

Debe incluir:

- Qué partes fueron generadas, corregidas o planificadas con IA.
- Cómo se mantuvo revisión humana.
- Limitaciones del uso de IA.

---

# 12. Tiempo Estimado

- **Tiempo total:** 24 horas
- **Trabajo efectivo:** 8-12 horas
- **Ver planificación detallada en [README_PLANIFICACION.md](./README_PLANIFICACION.md)**

---

# 13. Notas Adicionales

- Los requisitos marcados como bonus no son obligatorios, pero otorgan mayor puntaje en la evaluación.
- Puedes crear libremente features adicionales que consideres necesarias, así como APIs backend.
- Puedes utilizar cualquier API pública además de las mencionadas, siempre y cuando sean públicas.

---

# Fin del Documento

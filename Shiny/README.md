# README.md

# LaLiga 23/24 – Scout Dashboard

## 1. Descripción general del proyecto

Este proyecto consiste en el desarrollo de una aplicación interactiva de análisis deportivo utilizando **Shiny en R** para estudiar el rendimiento de jugadores de LaLiga durante la temporada 2023/2024.

La aplicación integra datos estadísticos, eventos de juego, historial de lesiones y métricas avanzadas en un dashboard dinámico y visualmente interactivo orientado al análisis de scouting y rendimiento individual.

El sistema permite explorar perfiles completos de futbolistas mediante visualizaciones avanzadas, filtros dinámicos y comparaciones estadísticas.

---

# 2. Objetivos del proyecto

Los principales objetivos del proyecto son:

- Analizar el perfil estadístico de jugadores de LaLiga.
- Visualizar acciones y eventos sobre el terreno de juego.
- Representar mapas de calor y zonas de influencia.
- Explorar historiales de lesiones y disponibilidad física.
- Comparar jugadores entre sí mediante percentiles.
- Facilitar procesos de scouting y análisis deportivo.
- Integrar múltiples fuentes de datos en una única plataforma interactiva.

---

# 3. Tecnologías utilizadas

## Lenguaje principal

- R 4.5.x

## Framework principal

- Shiny

## Librerías utilizadas

```r
library(shiny)
library(bslib)
library(reactable)
library(dplyr)
library(ggiraph)
library(ggplot2)
library(readxl)
library(jsonlite)
library(png)
library(tidyr)
library(stringr)
library(purrr)
library(lubridate)
library(scales)
library(patchwork)
library(htmltools)
```

---

# 4. Archivos utilizados

La aplicación utiliza múltiples archivos de datos y recursos visuales.

## Archivos principales

| Archivo | Descripción |
|---|---|
| `app.R` | Archivo principal de la aplicación Shiny |
| `estadisticas2.xlsx` | Métricas y estadísticas avanzadas |
| `lesiones.json` | Historial de lesiones |
| `Transfermarkt_2324.json` | Información general de jugadores |
| `bodymap2.png` | Imagen anatómica para lesiones |
| `README.md` | Documentación del proyecto |

---

# 5. Estructura general de la aplicación

La aplicación se organiza en 6 pestañas principales:

1. Resumen
2. Perfil estadístico
3. Eventos
4. Lesiones
5. Comparador
6. Explorador

Cada módulo contiene herramientas específicas de análisis y visualización.

---

# 6. Página “Resumen”

La pestaña **Resumen** funciona como una vista general rápida del jugador seleccionado.

## Funcionalidades principales

- Información general del jugador.
- Equipo actual.
- Posiciones principales.
- Edad.
- ID del jugador.
- Enlace a Transfermarkt.
- Resumen estadístico global.

## Indicadores principales

La parte superior muestra tarjetas resumen con:

- Equipo.
- Percentil medio.
- Número total de eventos.
- Número de lesiones.
- Días acumulados de baja.

## Apartados internos

### Perfil y eventos

Incluye:

- Radar charts de percentiles.
- Eventos más frecuentes.
- Métricas agrupadas.

### Percentiles y lesiones

Permite relacionar:

- rendimiento estadístico,
- disponibilidad física,
- historial médico.

### Lectura rápida

Resumen automático del perfil del jugador.

---

# 7. Página “Perfil estadístico”

La pestaña **Perfil estadístico** permite analizar profundamente el rendimiento del jugador mediante percentiles y métricas avanzadas.

---

## 7.1 Opciones de filtrado

El panel lateral incluye:

- Posición de referencia.
- Grupo de métricas.
- Métrica principal para ranking.

---

## 7.2 Apartados principales

### Radar

Visualización principal del perfil del jugador mediante radar charts.

#### Métricas agrupadas

- Ataque
- Creación
- Defensa
- Progresión

#### Variables representadas

- Penetración
- Éxito defensivo
- Actividad defensiva
- Dominio aéreo
- Impacto ofensivo
- Conversión
- Calidad de tiro
- Eficiencia de pase
- Creatividad
- Verticalidad
- Participación
- Progresión

---

### Barras de percentiles

Representación individual de métricas mediante barras comparativas.

---

### Fortalezas

Identifica automáticamente:

- fortalezas,
- debilidades,
- métricas élite,
- métricas por debajo de la media.

---

### Ranking dentro de la posición

Compara al jugador con otros futbolistas de la misma posición.

---

### Tabla estadística

Muestra todas las métricas numéricas en formato tabular interactivo.

---

# 8. Página “Eventos”

La pestaña **Eventos** representa espacialmente las acciones realizadas por el jugador sobre el terreno de juego.

---

## 8.1 Filtros disponibles

### Tipos de evento

La app permite seleccionar:

- Pass
- Cross
- Take On
- Interception
- Ball recovery
- Shot
- Goal
- Assist
- Aerial
- Tackle
- Miss
- Attempt Saved

---

### Sectores del campo

El campo se divide en zonas:

- C1–C20

Esto permite analizar:

- zonas naturales,
- sectores vecinos,
- áreas de influencia.

---

## 8.2 Indicadores superiores

Se muestran tarjetas con:

- Eventos filtrados.
- % zona natural.
- % zona vecina.
- Partidos analizados.

---

## 8.3 Apartados internos

### Mapas

#### Mapa de acciones

Scatter plot espacial sobre el terreno de juego.

#### Mapa de calor

Heatmap de intensidad por sectores.

---

### Tendencia

Visualiza la evolución temporal de eventos.

---

### Tabla de partidos

Muestra estadísticas evento por evento y partido por partido.

---

# 9. Página “Lesiones”

La pestaña **Lesiones** analiza el historial físico y médico del jugador.

---

## 9.1 Indicadores superiores

La aplicación muestra:

- Número de lesiones.
- Días acumulados de baja.
- Partidos perdidos.
- Zona corporal más afectada.

---

## 9.2 Filtros disponibles

### Temporada

Filtrado por campañas deportivas.

### Bodymap por

- Número de lesiones.
- Días de baja.
- Severidad.

---

## 9.3 Apartados internos

### Mapa corporal

Visualización anatómica utilizando:

`bodymap2.png`

Las zonas lesionadas aparecen resaltadas sobre el cuerpo humano.

---

### Evolución y severidad

Representación temporal de lesiones.

---

### Tabla de lesiones

Incluye:

- tipo de lesión,
- fecha inicio,
- fecha fin,
- duración,
- partidos perdidos.

---

## 9.4 Zonas corporales detectadas

La app clasifica automáticamente lesiones en:

- Muslo
- Rodilla
- Tobillo
- Gemelo
- Aductores
- Hombro
- Pie
- Abdomen
- Cabeza
- Enfermedad/estado físico

---

# 10. Página “Comparador”

La pestaña **Comparador** permite enfrentar estadísticamente varios jugadores.

---

## 10.1 Funcionalidades

- Selección múltiple de jugadores.
- Comparación por posición.
- Comparación por grupos de métricas.
- Comparación visual mediante radar charts.

---

## 10.2 Indicadores superiores

- Número de jugadores comparados.
- Posición analizada.
- Grupo de métricas activo.

---

## 10.3 Apartados internos

### Radar comparativo

Compara perfiles estadísticos simultáneamente.

---

### Mapa de calor

Muestra diferencias visuales entre jugadores.

---

### Métrica seleccionada

Comparativa específica de una variable concreta.

---

### Jugadores similares

Identifica futbolistas con perfiles estadísticos parecidos.

---

# 11. Página “Explorador”

La pestaña **Explorador** permite analizar la base de datos completa.

---

## 11.1 Apartados internos

### Equipos

Incluye rankings globales por club.

#### Métricas representadas

- Días de baja acumulados.
- Eventos Opta.
- Producción estadística.

---

### Base de jugadores

Tabla interactiva completa con:

- nombres,
- equipos,
- posiciones,
- edades,
- métricas.

---

### Diccionario de métricas

Explica el significado de todas las variables estadísticas utilizadas.

---

# 12. Datos utilizados y origen

La aplicación integra múltiples fuentes de datos deportivas.

---

## 12.1 Archivo estadístico

### Archivo

`estadisticas2.xlsx`

### Contenido

- estadísticas avanzadas,
- percentiles,
- métricas ofensivas,
- métricas defensivas,
- progresión,
- creación.

---

## 12.2 Archivo de lesiones

### Archivo

`lesiones.json`

### Contenido

- historial médico,
- duración de lesiones,
- partidos perdidos,
- gravedad.

---

## 12.3 Archivo Transfermarkt

### Archivo

`Transfermarkt_2324.json`

### Contenido

- nombre,
- equipo,
- fecha de nacimiento,
- URL Transfermarkt,
- ID del jugador.

---

# 13. Arquitectura técnica

La aplicación se estructura en:

---

## 13.1 Carga de datos

Lectura mediante:

```r
read_excel()
fromJSON()
```

---

## 13.2 Procesamiento y limpieza

Incluye:

- transformación de variables,
- limpieza de datos,
- normalización,
- cálculo de percentiles,
- categorización.

---

## 13.3 Interfaz (UI)

Construida mediante:

```r
fluidPage()
navbarPage()
sidebarLayout()
tabPanel()
```

---

## 13.4 Lógica reactiva (Server)

Uso intensivo de:

```r
reactive()
observe()
renderPlot()
renderUI()
renderReactable()
```

---

# 14. Visualizaciones utilizadas

## Tipos de gráficos

- Radar charts
- Scatter plots
- Heatmaps
- Gráficos de barras
- Donut charts
- Bodymaps anatómicos
- Tablas interactivas

---

# 15. Reactividad de la aplicación

La aplicación actualiza automáticamente:

- gráficos,
- tablas,
- rankings,
- mapas,
- estadísticas,

según:

- jugador seleccionado,
- filtros,
- posición,
- grupo estadístico.

---

# 16. Diseño visual

El dashboard utiliza un diseño moderno basado en:

- colores oscuros,
- tarjetas KPI,
- visualización modular,
- distribución responsive.

---

# 17. Distribución del trabajo

## Limpieza y transformación de datos

Realizado por:

- Dani
- Alejandro

---

## Diseño de interfaz

Realizado por:

- Sara
- Dani

---

## Programación reactiva y servidor

Realizado por:

- Alejandro

---

## README y documentación

Realizado por:

- Sara

---

## GitHub y repositorio

Realizado por:

- Dani

---

# 18. Ejecución de la aplicación

## Instalar librerías

```r
install.packages(c(
  "shiny",
  "bslib",
  "reactable",
  "dplyr",
  "ggplot2",
  "ggiraph",
  "readxl",
  "jsonlite",
  "png",
  "tidyr",
  "stringr",
  "purrr",
  "lubridate",
  "patchwork",
  "scales",
  "htmltools"
))
```

---

## Ejecutar aplicación

```r
shiny::runApp()
```

---

# 19. Estructura del proyecto

```text
Trabajo_Shiny/
│
├── app.R
├── estadisticas2.xlsx
├── lesiones.json
├── Transfermarkt_2324.json
├── bodymap2.png
├── README.md
│
└── www/
```

---

# 20. Posibles mejoras futuras

- Incorporar xG y xA.
- Añadir más ligas.
- Comparador avanzado.
- Integración completa con Opta/Wyscout.
- Machine Learning aplicado a lesiones.
- Exportación PDF.
- Despliegue online.

---

# 21. Conclusiones

La aplicación desarrollada constituye una plataforma completa de scouting y análisis deportivo capaz de integrar:

- estadísticas avanzadas,
- visualización espacial,
- análisis médico,
- comparación de jugadores,
- exploración interactiva.

El proyecto demuestra el potencial de Shiny y R para el desarrollo de dashboards complejos orientados al análisis futbolístico profesional.

---

# 22. Referencias

## Fuentes de datos

- Transfermarkt
- Datos de eventos deportivos
- Datos estadísticos de LaLiga

## Herramientas utilizadas

- R
- Shiny
- ggplot2
- Reactable
- JSON
- Excel

---

# 23. Archivos incluidos

- `app.R`
- `estadisticas2.xlsx`
- `lesiones.json`
- `Transfermarkt_2324.json`
- `bodymap2.png`
- `README.md`


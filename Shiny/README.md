# LaLiga 23/24 – Scout Dashboard

# 1. Descripción del proyecto y objetivos

## Descripción del proyecto

Este proyecto consiste en el desarrollo de una aplicación interactiva de análisis deportivo utilizando **Shiny en R** para estudiar el rendimiento de jugadores de LaLiga durante la temporada 2023/2024.

La aplicación integra estadísticas avanzadas, eventos de juego, mapas de calor, historial de lesiones y métricas de scouting en un dashboard dinámico e interactivo orientado al análisis profesional de futbolistas.

El sistema permite explorar perfiles completos de jugadores mediante visualizaciones avanzadas, filtros dinámicos y comparaciones estadísticas.

## Objetivos principales

- Analizar el perfil estadístico de jugadores de LaLiga.
- Visualizar acciones y eventos sobre el terreno de juego.
- Representar mapas de calor y zonas de influencia.
- Explorar historiales de lesiones y disponibilidad física.
- Comparar jugadores entre sí mediante percentiles.
- Facilitar procesos de scouting y análisis deportivo.
- Integrar múltiples fuentes de datos en una única plataforma interactiva.

---

# 2. Estructura del dashboard y funcionalidades implementadas

La aplicación se organiza en 6 pestañas principales:

1. Resumen
2. Perfil estadístico
3. Eventos
4. Lesiones
5. Comparador
6. Explorador

Cada módulo contiene herramientas específicas de análisis y visualización.

---

## Resumen

La pestaña **Resumen** funciona como una vista general rápida del jugador seleccionado.

### Funcionalidades principales

- Información general del jugador.
- Equipo actual.
- Posiciones principales.
- Edad.
- ID del jugador.
- Enlace a Transfermarkt.
- Resumen estadístico global.

### Indicadores principales

La parte superior muestra tarjetas resumen con:

- Equipo.
- Percentil medio.
- Número total de eventos.
- Número de lesiones.
- Días acumulados de baja.

### Visualizaciones

- Radar charts de percentiles.
- Eventos más frecuentes.
- Métricas agrupadas.
- Relación entre rendimiento y lesiones.
- Lectura rápida automática del perfil del jugador.

---

## Perfil estadístico

La pestaña **Perfil estadístico** permite analizar profundamente el rendimiento del jugador mediante percentiles y métricas avanzadas.

### Funcionalidades

- Filtro por posición.
- Filtro por grupos de métricas.
- Ranking por métrica principal.
- Radar de percentiles.
- Barras de percentiles.
- Tabla estadística interactiva.
- Detección automática de fortalezas y debilidades.

### Métricas agrupadas

- Ataque
- Creación
- Defensa
- Progresión

### Variables representadas

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

## Eventos

La pestaña **Eventos** representa espacialmente las acciones realizadas por el jugador sobre el terreno de juego.

### Funcionalidades

- Filtros por tipo de evento.
- Filtros por sectores del campo.
- KPI dinámicos sobre eventos filtrados.
- Identificación de zonas naturales y zonas vecinas.
- Mapas de acciones.
- Heatmaps.
- Tendencias temporales.
- Tabla de partidos.

### Eventos disponibles

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

### Indicadores principales

- Eventos filtrados.
- % zona natural.
- % zona vecina.
- Partidos analizados.

### Visualizaciones

#### Mapa de acciones

Scatter plot espacial sobre el terreno de juego.

#### Heatmap

Mapa de calor de intensidad por sectores del campo.

#### Tendencia

Visualiza la evolución temporal de eventos.

---

## Lesiones

La pestaña **Lesiones** analiza el historial físico y médico del jugador.

### Incluye

- Número de lesiones.
- Días acumulados de baja.
- Partidos perdidos.
- Zona corporal más afectada.

### Visualizaciones

- Bodymap anatómico.
- Evolución temporal y severidad.
- Tabla de lesiones.
- Distribución por zonas corporales.

### Zonas corporales detectadas

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

## Comparador

La pestaña **Comparador** permite enfrentar estadísticamente varios jugadores.

### Funcionalidades

- Selección múltiple de jugadores.
- Comparación por posición.
- Comparación por grupos de métricas.
- Radar comparativo.
- Heatmap comparativo.
- Comparativa específica por métricas.
- Detección automática de jugadores similares.

### Indicadores superiores

- Número de jugadores comparados.
- Posición analizada.
- Grupo de métricas activo.

---

## Explorador

La pestaña **Explorador** permite analizar la base de datos completa.

### Incluye

- Rankings globales por equipos.
- Base completa de jugadores.
- Diccionario de métricas.
- Estadísticas globales de LaLiga.

### Métricas representadas

- Días de baja acumulados.
- Eventos Opta.
- Producción estadística.

---

# 3. Descripción de los datos utilizados y su origen

La aplicación integra múltiples fuentes de datos deportivas.

## Archivos utilizados

| Archivo | Descripción |
|---|---|
| `app.R` | Archivo principal de la aplicación Shiny |
| `estadisticas2.xlsx` | Estadísticas avanzadas y percentiles |
| `lesiones.json` | Historial médico y lesiones |
| `Transfermarkt_2324.json` | Información general de jugadores |
| `bodymap2.png` | Imagen anatómica utilizada en lesiones |
| `README.md` | Documentación del proyecto |

---

## Origen de los datos

- Transfermarkt
- Datos estadísticos de LaLiga
- Datos de eventos deportivos tipo Opta

---

## Información integrada

### Estadísticas avanzadas

- Métricas ofensivas
- Métricas defensivas
- Progresión
- Creación
- Percentiles

### Eventos espaciales

- Pases
- Recuperaciones
- Intercepciones
- Centros
- Acciones ofensivas

### Lesiones

- Duración
- Gravedad
- Partidos perdidos
- Zona corporal afectada

---

# 4. Distribución del trabajo

## Limpieza y transformación de datos

- Dani
- Alejandro

---

## Diseño de interfaz

- Sara
- Dani

---

## Programación reactiva y servidor

- Alejandro

---

## README y documentación

- Sara

---

## GitHub y despliegue

- Dani

---

# 5. Enlace a versión desplegada del dashboard

La aplicación ha sido desplegada públicamente mediante **ShinyApps.io**, permitiendo acceder al dashboard desde cualquier navegador sin necesidad de instalar R o dependencias adicionales.

## Acceso online

👉 https://alejandropascual.shinyapps.io/Scout-Dashboard-LaLiga-2324/

---

# 6. Explicación de los fundamentos de visualización de datos aplicados en el dashboard

El dashboard aplica múltiples principios de visualización de datos orientados a facilitar la interpretación rápida de información compleja dentro del contexto del análisis deportivo.

## Visualizaciones utilizadas

### Radar charts

Permiten representar perfiles estadísticos multidimensionales y comparar fortalezas y debilidades de los jugadores.

### Heatmaps

Representan la intensidad de acciones por zonas del terreno de juego para identificar áreas de influencia y comportamiento espacial.

### Scatter plots espaciales

Visualizan eventos directamente sobre el campo para analizar patrones tácticos y posicionamiento.

### KPI Cards

Las tarjetas superiores resumen información clave como:

- percentiles,
- eventos,
- lesiones,
- días de baja,
- partidos analizados.

### Donut charts

Utilizados para representar distribuciones de lesiones por zonas corporales.

### Tablas interactivas

Permiten explorar grandes cantidades de datos mediante filtros dinámicos y ordenación interactiva.

---

## Diseño visual aplicado

El dashboard utiliza:

- tema oscuro moderno,
- diseño modular,
- navegación superior,
- estructura responsive,
- jerarquía visual clara,
- colores diferenciados por grupos estadísticos.

Todo ello mejora la legibilidad y experiencia de usuario.

---

## Arquitectura técnica

### Carga de datos

```r
read_excel()
fromJSON()
```

### Procesamiento y limpieza

- transformación de variables,
- limpieza de datos,
- normalización,
- cálculo de percentiles,
- categorización.

### Interfaz (UI)

```r
fluidPage()
navbarPage()
sidebarLayout()
tabPanel()
```

### Lógica reactiva (Server)

```r
reactive()
observe()
renderPlot()
renderUI()
renderReactable()
```

---

## Tecnologías utilizadas

### Lenguaje principal

- R 4.5.x

### Framework principal

- Shiny

### Librerías utilizadas

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

### Ejecución de la aplicación

#### Instalar librerías

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

#### Ejecutar aplicación

```r
shiny::runApp()
```

---

### Estructura del proyecto

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

# 7. Conclusiones y posibles mejoras futuras

## Conclusiones

La aplicación desarrollada constituye una plataforma completa de scouting y análisis deportivo capaz de integrar:

- estadísticas avanzadas,
- visualización espacial,
- análisis médico,
- comparación de jugadores,
- exploración interactiva.

El proyecto demuestra el potencial de **Shiny** y **R** para el desarrollo de dashboards complejos orientados al análisis futbolístico profesional.

Además, el despliegue online mediante ShinyApps.io convierte la aplicación en una herramienta accesible y funcional desde cualquier dispositivo.

---

## Posibles mejoras futuras

- Incorporar métricas xG y xA.
- Añadir nuevas ligas y competiciones.
- Mejorar el comparador avanzado.
- Integración con APIs deportivas profesionales.
- Machine Learning aplicado a lesiones.
- Incorporar análisis táctico colectivo.
- Optimización de rendimiento online.
- Exportación PDF.

---

## Referencias

### Fuentes de datos

- Transfermarkt
- Datos de eventos deportivos
- Datos estadísticos de LaLiga

### Herramientas utilizadas

- R
- Shiny
- ggplot2
- Reactable
- JSON
- Excel

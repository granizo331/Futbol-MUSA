# 📊 Perfil de Jugadores de LaLiga 2023/2024

## 1. Descripción del proyecto y objetivos

Este proyecto consiste en el desarrollo de una aplicación interactiva utilizando **Quarto (.qmd)** y **Shiny en R**, cuyo propósito es analizar el rendimiento de jugadores de LaLiga durante la temporada 2023/2024.

El objetivo principal es construir un **dashboard dinámico e intuitivo** que permita al usuario explorar de forma integral el perfil de un jugador, combinando distintas dimensiones del análisis deportivo.

En concreto, la aplicación permite:

- Analizar el **perfil estadístico detallado** de un jugador.
- Visualizar su **comportamiento en el campo** mediante datos de eventos.
- Explorar su **historial de lesiones** de forma gráfica e informativa.
- Consultar **información general de jugadores** de manera interactiva.

Además, el proyecto busca integrar múltiples fuentes de datos heterogéneas y presentarlas de forma clara, coherente y visualmente accesible.

---

## 2. Estructura del dashboard y funcionalidades implementadas

La aplicación se organiza en **cuatro pestañas principales**, cada una centrada en un aspecto específico del análisis:

### 📈 Estadísticas
- Selección dinámica de jugador mediante `selectInput`.
- Visualización de métricas agregadas en formato tabular.
- Gráficos de percentiles (tipo **radar chart**) para comparar el rendimiento relativo.
- Agrupación de métricas en categorías clave:
  - Defensa
  - Ataque
  - Creación
  - Progresión

### ⚽ Eventos
- Representación visual de acciones del jugador sobre un campo de fútbol.
- Uso de coordenadas espaciales (x, y).
- División del campo en zonas (C1–C18) para facilitar el análisis posicional.
- Visualización mediante **scatter plots**, permitiendo identificar patrones de juego.

### 🏥 Lesiones
- Tabla con el historial completo de lesiones del jugador.
- Gráfico de distribución de lesiones según la zona corporal afectada.
- Representación visual sobre un **mapa corporal**, facilitando la interpretación.

### 📋 Data
- Tabla interactiva con información general de jugadores.
- Funcionalidades de búsqueda, filtrado y paginación.
- Exploración libre de la base de datos.

---

## 3. Descripción de los datos utilizados y su origen

El proyecto integra diversas fuentes de datos, combinando formatos estructurados y semiestructurados:

- **`estadisticas2.xlsx`**  
  Contiene métricas deportivas agregadas por jugador (rendimiento ofensivo, defensivo, etc.).

- **`lesiones.json`**  
  Incluye el historial de lesiones: tipo de lesión, fechas, duración y partidos perdidos.

- **`Transfermarkt_2324.json`**  
  Información general de jugadores (nombre, equipo, identificador), basada en datos de Transfermarkt.

- **Datos de eventos**  
  Coordenadas espaciales (x, y) que representan acciones realizadas en el campo.

- **`bodymap2.png`**  
  Imagen utilizada para la representación visual de las zonas corporales afectadas por lesiones.

Todos estos datos se integran y procesan dentro del archivo principal **`Trabajo_Shiny.qmd`**, donde se realiza su limpieza, transformación y unificación.

---

## 4. Distribución del trabajo

El desarrollo del proyecto se ha organizado de manera colaborativa, dividiendo responsabilidades por áreas:

### 🔧 Desarrollo técnico

**1. Depuración y preparación de datos**
- Limpieza, transformación e integración de datos provenientes de Excel y JSON.
- Estandarización de formatos y cálculo de métricas.
- **Responsables:** Dani y Alejandro

**2. Interfaz de usuario (UI)**
- Diseño del dashboard.
- Estructuración de pestañas y componentes interactivos.
- Definición de inputs y organización visual.
- **Responsables:** Sara y Dani

**3. Lógica del servidor**
- Implementación de la reactividad.
- Filtrado dinámico de datos según el jugador seleccionado.
- Generación de gráficos y tablas.
- **Responsable:** Alejandro

### 📝 Otras tareas

**4. Documentación (README)**
- Redacción y estructuración del documento.
- **Responsable:** Sara

**5. Gestión del repositorio**
- Creación y organización del repositorio en GitHub.
- Control de versiones y subida de archivos.
- **Responsable:** Dani

---

## 5. Enlace a la versión desplegada

Actualmente, la aplicación se ejecuta en entorno local:

http://127.0.0.1:6735

 *Nota:* Como mejora futura, se plantea su despliegue en plataformas como **ShinyApps.io** para facilitar el acceso público.

---

## 6. Fundamentos de visualización de datos aplicados

El diseño del dashboard se basa en varios principios clave de visualización de datos:

- **Organización por categorías**  
  Las métricas se agrupan (defensa, ataque, creación, progresión) para mejorar la comprensión.

- **Uso de percentiles**  
  Permiten comparar el rendimiento de un jugador respecto al resto de la liga.

- **Representación espacial**  
  Los eventos se visualizan sobre el campo, aportando contexto táctico.

- **Interactividad**  
  El usuario puede explorar dinámicamente los datos mediante selección de jugador.

- **Integración de múltiples fuentes**  
  Se combinan estadísticas, eventos y lesiones en un único entorno.

- **Claridad visual**  
  Se prioriza un diseño limpio, legible y centrado en la experiencia del usuario.

---

## 7. Conclusiones y posibles mejoras futuras

### ✅ Conclusiones

- El dashboard permite realizar un **análisis completo del perfil de un jugador**.
- Integra de forma efectiva **estadísticas, eventos y lesiones**.
- Facilita la interpretación de datos complejos mediante visualizaciones interactivas.
- Demuestra el potencial de **Shiny y Quarto** para el desarrollo de aplicaciones analíticas.

### 🚀 Mejoras futuras

- Implementar un **comparador avanzado entre jugadores**.
- Incorporar métricas avanzadas como **xG (expected goals)** y **xA (expected assists)**.
- Ampliar el alcance a **más ligas y temporadas**.
- Mejorar el **diseño visual y experiencia de usuario (UX/UI)**.
- Desplegar la aplicación en un entorno online accesible públicamente.

---

## 🧩 Estructura del archivo `Trabajo_Shiny.qmd`

El archivo principal sigue una estructura clara y modular:

1. **Configuración inicial**  
   Carga de librerías (`shiny`, `tidyverse`, `plotly`, `readxl`, `jsonlite`).

2. **Carga de datos**  
   Lectura de archivos Excel y JSON.

3. **Limpieza y transformación**  
   Procesamiento de datos y cálculo de métricas.

4. **Interfaz de usuario (UI)**  
   Definición de inputs y estructura del dashboard.

5. **Lógica del servidor (Server)**  
   Implementación de la reactividad.

6. **Visualizaciones**
   - Radar charts (estadísticas)
   - Scatter plots (eventos)
   - Gráficos de lesiones
   - Tablas interactivas

7. **Reactividad**  
   Actualización automática de todos los elementos según la interacción del usuario.

---

## 🧾 Conclusión técnica

El archivo `.qmd` integra en un único documento reproducible:

- Procesamiento de datos  
- Visualización avanzada  
- Interactividad en tiempo real  

Esto permite desarrollar una aplicación completa, flexible y fácilmente mantenible, alineada con buenas prácticas en análisis de datos.

# SmartTalent Strategies 
# Optimización de talento para ABC Corporation

### Equipo de desarrollo
[Raquel Pedraza](https://github.com/RaquelPedraza), [Sandra Moreno](https://github.com/sandranomore), [Elena Águila](https://github.com/eaguilag) y [Luana Magnabosco](https://github.com/LuanaMagnabosco)
## Descripción del Proyecto

Este repositorio contiene el código y la documentación del proyecto realizado por el equipo de SmartTalent Strategies para ABC Corporation. El objetivo del proyecto es llevar a cabo un análisis y transformación de datos, diseñar y poblar una base de datos, realizar un experimento A/B para analizar la rotación de empleados y crear un proceso ETL automatizado.

## Objetivos del Proyecto

1. **Reducir la Rotación de Empleados**: Identificar las causas de la rotación de empleados y proponer estrategias basadas en datos para reducirla.
2. **Mejorar la Satisfacción en el Trabajo**: Analizar los factores que afectan la satisfacción en el trabajo y sugerir medidas para mejorarla.

## Fases del Proyecto

### Fase 1: Análisis Exploratorio de Datos (EDA)
**Objetivo**: Comprender las características del conjunto de datos y familiarizarse con la información disponible.

**Desarrollo**:
- Se realizó un análisis descriptivo de todas las columnas del dataset.
- Se identificaron patrones, tendencias y posibles inconsistencias en los datos.
- Se generaron visualizaciones iniciales para entender la distribución y relación entre las variables.

**Conclusiones**:
- Se identificaron algunas inconsistencias en los datos, como valores negativos y errores tipográficos.
- Se observó una distribución desigual de ciertos datos categóricos que necesitarán transformación.

### Fase 2: Transformación de los Datos
**Objetivo**: Limpiar y preparar los datos para análisis más profundos.

**Desarrollo**:
- Se reemplazaron los valores de la columna `Gender` por "Male" y "Female".
- Se convirtió la columna `DailyRate` de tipo string a tipo numérico.
- Se evaluaron y eliminaron valores duplicados donde fue necesario.
- Se corrigieron valores inconsistentes y errores tipográficos en las columnas.
- Se eliminaron columnas redundantes que no aportaban valor adicional.

**Conclusiones**:
- Los datos quedaron limpios y listos para análisis posteriores.
- Se mejoró la calidad y consistencia de los datos, lo que facilitará su uso en el diseño de la base de datos y el análisis estadístico.

### Fase 3: Diseño de Base de Datos e Inserción de Datos
**Objetivo**: Crear una base de datos estructurada y almacenar los datos transformados.

**Desarrollo**:
- Se diseñó la estructura de la base de datos, definiendo las tablas necesarias y sus relaciones.
- Se creó la base de datos utilizando MySQL Workbench.
- Se insertaron los datos transformados en las tablas correspondientes.

**Conclusiones**:
- La base de datos quedó estructurada y poblada correctamente.
- La organización de los datos en una base de datos relacional permite consultas eficientes y análisis más detallados.

### Fase 4: Problema de A/B Testing
**Objetivo**: Determinar la relación entre el nivel de satisfacción en el trabajo y la rotación de empleados.

**Desarrollo**:
- Se creó una nueva columna para dividir a los empleados en dos grupos basados en su nivel de satisfacción (Grupo A y Grupo B).
- Se calculó la tasa de rotación en cada grupo.
- Se realizó un análisis estadístico para determinar la significancia de la diferencia en las tasas de rotación entre los grupos.
- Se calculó la magnitud de la relación utilizando la diferencia de medias.

**Conclusiones**:
- Se encontró una relación significativa entre el nivel de satisfacción en el trabajo y la rotación de empleados.
- Los empleados con niveles de satisfacción más bajos (Grupo B) tenían una mayor probabilidad de dejar la empresa.

### Fase 5: Creación de una ETL
**Objetivo**: Automatizar el proceso de extracción, transformación y carga (ETL) de datos.

**Desarrollo**:
- Se desarrollaron funciones en Python para la extracción de datos desde diversas fuentes.
- Se implementaron las transformaciones necesarias para garantizar la integridad y calidad de los datos.
- Se creó una función para la creación de la base de datos.
- Se desarrollaron funciones para la carga de datos transformados en la base de datos.

**Conclusiones**:
- Se automatizó el proceso ETL, asegurando que los datos estén siempre actualizados y listos para análisis.
- La implementación de ETL permite la integración continua de nuevos datos con mínima intervención manual.

### Fase 6: Reporte de los Resultados
**Objetivo**: Proporcionar un informe detallado a ABC Corporation con visualizaciones y análisis descriptivos.

**Desarrollo**:
- Se generaron visualizaciones en Python utilizando matplotlib y seaborn.
- Se creó un informe completo que incluye análisis descriptivos y visualizaciones de las tendencias, áreas de mejora y fortalezas de la empresa.
- El informe fue diseñado para ser presentado durante la demo del proyecto.

**Conclusiones**:
- El informe proporcionó a ABC Corporation una comprensión profunda de la situación actual.
- Las visualizaciones ayudaron a resaltar las áreas críticas y las posibles estrategias para mejorar la satisfacción y reducir la rotación.

## Herramientas Utilizadas

### Lenguajes y Librerías
- **Python**: Lenguaje principal utilizado para el análisis de datos y las transformaciones.
  - **pandas**: Para la manipulación y análisis de datos.
  - **numpy**: Para operaciones matemáticas y manejo de matrices.
  - **scipy**: Para análisis estadísticos.
  - **matplotlib** y **seaborn**: Para visualizaciones de datos.
  - **sqlalchemy**: Para la creación y gestión de bases de datos.

### Bases de Datos
- **MySQL Workbench**: Base de datos relacional utilizada para almacenar los datos transformados.

### Entornos y Herramientas de Desarrollo
- **Jupyter Notebook**: Para el análisis exploratorio de datos y A/B testing.
- **Visual Studio Code**: Editor de código utilizado para el desarrollo de scripts en Python.
- **Git**: Para el control de versiones del proyecto.
- **GitHub**: Para la gestión del repositorio del proyecto.

## Contacto
Para cualquier consulta o sugerencia, por favor contactar a SmartTalent Strategies en [contact@smarttalent.com]


# Reporte de Transacciones Bancarias - Aplicación de Línea de Comandos

## Introducción

Este proyecto consiste en una aplicación de línea de comandos (CLI) desarrollada en Python para procesar un archivo CSV que contiene transacciones bancarias. El objetivo de esta aplicación es analizar los datos de las transacciones y generar un reporte con información como el balance final, transacción de mayor monto y conteo de transacciones por tipo.

## Instrucciones de Ejecución

1.  **Prerrequisitos:**
   * Asegúrate de tener Python instalado en tu sistema. Puedes verificar la instalación abriendo la terminal o el símbolo del sistema y ejecutando el comando:
       ```bash
       python --version
       ```
     o
       ```bash
       python3 --version
       ```

2. **Preparar el archivo CSV:**
   * Crea un archivo CSV (por ejemplo, `data.csv`) con los datos de las transacciones bancarias. El archivo debe tener una estructura con las siguientes columnas y encabezados en la primera fila:
      * `id`: Identificador único de la transacción.
      * `tipo`: Tipo de transacción, debe ser "Crédito" o "Débito".
      * `monto`: Valor numérico de la transacción.
   * Asegúrate de que el archivo CSV esté ubicado en una ruta accesible por la aplicación.

3. **Ejecutar la aplicación:**
   * Abre la terminal o el símbolo del sistema.
   * Navega hasta el directorio donde guardaste el archivo `procesar_transacciones.py`.
   * Ejecuta el script de Python pasando la ruta del archivo CSV como argumento:
       ```bash
       python procesar_transacciones.py ruta_del_archivo.csv
       ```
     Reemplaza `ruta_del_archivo.csv` con la ruta real a tu archivo CSV (por ejemplo, `data.csv` si está en el mismo directorio, o `C:\ruta\al\archivo\data.csv` si está en otra ubicación).

## Enfoque y Solución

La lógica implementada en la aplicación se centra en los siguientes pasos:

1.  **Lectura del archivo CSV:** Se utiliza la librería `csv` de Python para leer el contenido del archivo CSV, interpretando la primera fila como los encabezados de las columnas. Se asume que el archivo contiene las columnas "id", "tipo" y "monto".

2.  **Procesamiento de transacciones:** Se itera a través de cada fila del archivo CSV. Para cada transacción, se realiza lo siguiente:
   * Se verifica el tipo de transacción ("Crédito" o "Débito").
   * Se convierte el monto a un valor numérico para realizar cálculos.
   * Se actualizan las variables para calcular el balance de créditos y débitos, identificar la transacción de mayor monto y contar el número de transacciones por tipo.

3.  **Cálculo del balance final:** El balance final se calcula restando la suma total de los montos de débito a la suma total de los montos de crédito.

4.  **Identificación de la transacción de mayor monto:** Durante la iteración, se compara el monto de cada transacción con el monto de la transacción más alta encontrada hasta el momento. Se almacena el id y el monto de la transacción con el valor más alto.

5.  **Conteo de transacciones por tipo:** Se utilizan contadores separados para llevar el registro del número de transacciones de tipo "Crédito" y "Débito".

6.  **Generación del reporte:** La aplicación imprime en la consola un reporte con el balance final, información de la transacción de mayor monto y el conteo de transacciones por cada tipo.

**Decisiones de Diseño:**

* Se optó por una aplicación CLI para facilitar la ejecución.
* Se utilizó la librería `csv` de Python, que es la forma más eficiente de trabajar con archivos CSV en Python.
* Se incluyó manejo básico de errores para casos como la no existencia del archivo CSV o problemas con el formato de los datos (columnas faltantes o valores no numéricos en el monto).
* Se utilizaron nombres de variables descriptivos para mejorar la legibilidad del código.

## Estructura del Proyecto

El proyecto consiste en los siguientes archivos principales:

* `procesar_transacciones.py`: Este archivo contiene el código fuente de la aplicación.
* `README.md`: Este archivo proporciona información general sobre el proyecto, instrucciones de ejecución, enfoque de la solución y estructura del proyecto.
* `datacsv` Es el archivo CSV que contiene los datos de las transacciones bancarias. Este es el archivo que la aplicación procesa.

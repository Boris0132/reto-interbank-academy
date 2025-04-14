import csv  # Importa la librería para trabajar con archivos CSV
import sys  # Importa la librería para acceder a los argumentos de la línea de comandos

def procesar_transacciones(ruta_archivo):

    # Inicialización de variables para almacenar los resultados
    balance_credito = 0.0  # Suma de todos los montos de crédito
    balance_debito = 0.0   # Suma de todos los montos de débito
    transaccion_mayor_monto = {"id": None, "monto": 0.0}  # Diccionario para almacenar la transacción de mayor monto
    conteo_credito = 0     # Contador de transacciones de tipo Crédito
    conteo_debito = 0      # Contador de transacciones de tipo Débito

    try:
        # Abre el archivo CSV en modo lectura r con manejo de codificación y saltos de línea
        with open(ruta_archivo, 'r', newline='', encoding='utf-8') as archivo_csv:
            # Crea un objeto DictReader para leer el CSV como un diccionarion usando la primera fila como encabezados
            lector_csv = csv.DictReader(archivo_csv)

            # Itera a través de cada fila en el archivo CSV
            for fila in lector_csv:
                try:
                    # Obtiene el tipo de transacción, elimina espacios en blanco y lo convierte a minúsculas para comparar
                    tipo = fila['tipo'].strip().lower()
                    # Obtiene el monto de la transacción y lo convierte a un número de punto flotante
                    monto = float(fila['monto'])
                    # Obtiene el ID de la transacción
                    id_transaccion = fila['id']

                    # Procesa las transacciones de tipo crédito
                    if tipo == 'crédito':
                        balance_credito += monto  # Suma el monto al balance de crédito
                        conteo_credito += 1      # Incrementa el contador de créditos
                        # Verifica si la transacción actual tiene un monto mayor que la transacción de mayor monto encontrada hasta ahora
                        if monto > transaccion_mayor_monto['monto']:
                            transaccion_mayor_monto['monto'] = monto  # Actualiza el monto mayor
                            transaccion_mayor_monto['id'] = id_transaccion  # Actualiza el ID de la transacción de mayor monto
                    # Procesa las transacciones de tipo débito
                    elif tipo == 'débito':
                        balance_debito += monto   # Suma el monto al balance de débito
                        conteo_debito += 1       # Incrementa el contador de débitos
                        # Verifica si la transacción actual tiene un monto mayor que la transacción de mayor monto encontrada hasta ahora
                        if monto > transaccion_mayor_monto['monto']:
                            transaccion_mayor_monto['monto'] = monto  # Actualiza el monto mayor
                            transaccion_mayor_monto['id'] = id_transaccion  # Actualiza el ID de la transacción de mayor monto
                except KeyError as e:
                    # Captura el error si una columna esperada Tipo, Monto o ID no se encuentra en el CSV
                    print(f"Error: La columna '{e}' no se encontró en el archivo CSV.")
                    return
                except ValueError:
                    # Captura el error si el valor de Monto no puede ser convertido a un número
                    print(f"Error: El valor de 'Monto' para la transacción con ID '{fila.get('ID', 'Desconocido')}' no es un número válido.")
                    return

        # Calcula el balance final restando el total de débitos al total de créditos
        balance_final = balance_credito - balance_debito

        # Imprime el reporte de transacciones bancarias
        print("\nReporte de Transacciones Bancarias")
        print("---------------------------------------------")
        print(f"Balance Final: ${balance_final:.2f}")  # Muestra el balance final con dos decimales
        print(f"Transacción de Mayor Monto: ID: {transaccion_mayor_monto['id']} - {transaccion_mayor_monto['monto']:.2f}") # Muestra la transacción de mayor monto
        print(f"Conteo de Transacciones: Crédito: {conteo_credito} Débito: {conteo_debito}") # Muestra el número total de transacciones de crédito y débito

    except FileNotFoundError:
        # Captura el error si el archivo especificado no se encuentra
        print(f"Error: No se pudo encontrar el archivo en la ruta: {ruta_archivo}")
    except Exception as e:
        # Captura cualquier otro error inesperado durante el procesamiento del archivo
        print(f"Ocurrió un error inesperado: {e}")

# Este bloque de código se ejecuta cuando el script se llama directamente
if __name__ == "__main__":
    # Verifica si el número de argumentos de la línea de comandos es el correcto (el nombre del script y la ruta del archivo)
    if len(sys.argv) != 2:
        print("Uso: python nombre_del_script.py ruta_del_archivo.csv")
    else:
        # Obtiene la ruta del archivo CSV del segundo argumento de la línea de comandos
        ruta_archivo_csv = sys.argv[1]
        # Llama a la función para procesar el archivo CSV
        procesar_transacciones(ruta_archivo_csv)
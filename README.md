# Resumen del Proyecto

Este proyecto procesa un archivo CSV con transacciones financieras y genera un resumen con información clave como el balance final, la transacción de mayor monto y el conteo de transacciones por tipo (Crédito/Débito).

## Instrucciones de Ejecución

### Requisitos

Este proyecto utiliza Python y la biblioteca pandas. Para instalar las dependencias necesarias, ejecuta:

```sh
pip install pandas
```

### Ejecución

Para ejecutar el script, usa el siguiente comando en la terminal:

```sh
python app.py [ruta_del_archivo] [separador]
```

- `ruta_del_archivo` (opcional): Ruta del archivo CSV con los datos de las transacciones (por defecto `data.csv`).
- `separador` (opcional): Separador de columnas en el archivo CSV (por defecto `,`).

Ejemplo de ejecución:

```sh
python app.py transacciones.csv ;
```

## Enfoque y Solución

El código implementa las siguientes funciones:

- `get_balance(data)`: Calcula el balance total de las transacciones.
- `get_max_transaction(data)`: Encuentra la transacción con el mayor monto.
- `get_count_transaction(data)`: Cuenta la cantidad de transacciones por tipo.
- `show_summary(balance, transaction, counts_transactions)`: Muestra el resumen de los datos.
- `create_summary(path_file, sep)`: Carga los datos, los procesa y genera el informe.

### Decisiones de Diseño

- Se utilizó pandas para manejar los datos de manera eficiente.
- Se agruparon las transacciones por tipo para calcular rápidamente el balance y conteo.
- Se implementó `if __name__ == "__main__"` para permitir la ejecución del script desde la terminal con argumentos personalizados.

## Estructura del Proyecto

```
/
│── app.py  # Script principal con la lógica del procesamiento de transacciones
│── data.csv   # Archivo de ejemplo con transacciones
│── README.md  # Documentación del proyecto
```

## Notas Adicionales

- Asegúrate de que el archivo CSV contenga las columnas `id`, `tipo` y `monto`.
- Puedes modificar la función `create_summary` para agregar más análisis si es necesario.


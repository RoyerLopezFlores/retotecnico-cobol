import pandas as pd
import sys

def show_summary(balance, transation, counts_transactions):
    """
    Muestra un resumen de las transacciones.
    
    Parámetros:
        balance (float): Balance final calculado.
        transaction (pd.Series): Transacción con el monto más alto.
        counts_transactions (dict): Conteo de transacciones por tipo (Crédito/Débito).
    """
    print("Reporte de Transacciones")
    print("---------------------------------------------")
    print(f"Balance Final: {balance}")
    print(f"Transacción de Mayor Monto: ID {transation['id']} - {transation['monto']}")
    print(f"Conteo de Transacciones: Crédito: {counts_transactions.get('Crédito', 0)} Débito: {counts_transactions.get('Débito', 0)}")

def get_balance(data:pd.DataFrame)->float:
    """
    Calcula el balance total basado en los montos de las transacciones.
    
    Parámetros:
        data (pd.DataFrame): DataFrame que contiene las transacciones con columnas 'tipo' y 'monto'.
    
    Retorna:
        float: Balance final calculado como la diferencia entre créditos y débitos.
    """
    totales_transactions = data.groupby('tipo')['monto'].sum()
    total_credito = totales_transactions.get('Crédito',0)
    total_debito = totales_transactions.get('Débito',0)
    balance = total_credito - total_debito
    return balance
def get_max_transsaction(data:pd.DataFrame)-> pd.Series:
    """
    Obtiene la transacción con el mayor monto.
    
    Parámetros:
        data (pd.DataFrame): DataFrame de transacciones con la columna 'monto'.
    
    Retorna:
        pd.Series: Fila del DataFrame correspondiente a la transacción con el monto más alto.
    """
    index_max = data["monto"].idxmax()
    transac_max = data.loc[index_max]
    return transac_max
def get_count_transaction(data:pd.DataFrame)-> dict:
    """
    Cuenta la cantidad de transacciones por tipo (Crédito/Débito).
    
    Parámetros:
        data (pd.DataFrame): DataFrame de transacciones con la columna 'tipo'.
    
    Retorna:
        dict: Diccionario con la cantidad de transacciones por tipo.
    """
    count_transactions = data.groupby('tipo')['monto'].count()
    return count_transactions
def create_sumary(path_file = "data.csv",sep=","):
    """
    Carga los datos desde un archivo CSV y genera un resumen de las transacciones.
    
    Parámetros:
        path_file (str): Ruta del archivo CSV que contiene las transacciones.
        sep (str): Separador de los valores en el archivo CSV.
    """
    data = pd.read_csv(path_file,sep=sep)
    balance = get_balance(data)
    transac_max = get_max_transsaction(data)
    count_transactions = get_count_transaction(data)
    

    show_summary(balance,transac_max,count_transactions)

if __name__ == "__main__":
    argv = sys.argv
    path_file = "data.csv"
    sep=","
    print(argv)
    if len(argv)>=2:
        path_file = argv[1]
    if len(argv)>=3:
        sep = argv[2]
    create_sumary(path_file,sep)


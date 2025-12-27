import pandas as pd
import numpy as np
from word2number import w2n

def read_file(path, index_col=0):
    df = pd.read_csv(path, index_col=index_col)
    return df

def explore_dataframe(df):
    print("*" * 50)
    print(f"--- DATAFRAME EXPLORATION: ---")
    print("*" * 50)
    
    # Estructura del dataframe y tipos de datos
    print(f"\nEl DataFrame tiene {df.shape[0]} filas y {df.shape[1]} columnas.\n")
    print("_" * 50)
    
    print("\nMuestra de filas aleatorias:\n")
    print(df.sample(5))
    print("_" * 50)
    
    print(f"\nTipos de datos por columna:\n")
    print(df.dtypes)
    print("_" * 50)
    
    print(f"\nInformación del DataFrame:\n")
    df.info()
    print("_" * 50)
    
    # Valores duplicados
    duplicated_values = df.duplicated().sum()
    duplicated_percentage = round(duplicated_values / df.shape[0] * 100, 2)
    print(f"\nNúmero de duplicados en el conjunto de datos: {duplicated_values}, un {duplicated_percentage}%.\n")
    print("_" * 50)
    
    # Valores nulos
    print("\nValores nulos por columna:\n")
    null_values = df.isnull().sum()
    null_percentage = (null_values / df.shape[0]) * 100
    df_nulos = pd.DataFrame({'nulos': null_values, 'porcentaje_nulos': null_percentage})
    print(df_nulos[df_nulos['porcentaje_nulos'] > 0])
    print("_" * 50)
    
    # Estadísticas básicas para columnas numéricas
    col_num = df.select_dtypes(include=["number"])
    if not col_num.empty:
        print("\nEstadísticas básicas de columnas numéricas:\n")
        print(col_num.describe().T)
        print("_" * 50)
    else:
        print("\nNo hay columnas numéricas en el DataFrame.\n")
        print("_" * 50)
    
    # Estadísticas básicas para columnas categóricas
    col_cat = df.select_dtypes(include=["object", "category"])
    if not col_cat.empty:
        print("\nEstadísticas básicas de columnas categóricas:\n")
        print(col_cat.describe().T)
    else:
        print("\nNo hay columnas categóricas en el DataFrame.\n")
    
    print("\n\n")

def convert_int64_to_int(df):
    for col in df.columns:
        if df[col].dtype == np.int64:
            df[col] = df[col].astype(int)
    return df

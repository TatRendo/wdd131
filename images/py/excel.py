import os
import pandas as pd

carpeta = 'C:\\Users\\A.Ramirez\\OneDrive - LABORATORIOS REMO S.A.S\\Documentos\\Alejandro\\Rotación\\Agosto 2024\\LISTOS\\csv_output'
carpeta2 = 'C:\\Users\\A.Ramirez\\OneDrive - LABORATORIOS REMO S.A.S\\Documentos\\Alejandro\\Rotación\\Agosto 2024\\LISTOS\\'
carpeta3 = 'C:\\Users\\A.Ramirez\\OneDrive - LABORATORIOS REMO S.A.S\\Documentos\\Alejandro\\Rotación\\Agosto 2024\\'
carpeta_salida = 'C:\\Users\\A.Ramirez\\OneDrive - LABORATORIOS REMO S.A.S\\Documentos\\Alejandro\\Rotación\\Agosto 2024\\LISTOS\\csv_output'
datos_consolidados = []

def leer_ultimas_24_filas_csv(ruta_archivo):
    df_prueba = pd.read_csv(ruta_archivo)
    if 'Unnamed:' in df_prueba.columns[0]: 
        df = pd.read_csv(ruta_archivo,header=1)
    else:
        df = pd.read_csv(ruta_archivo)    
    if df.shape[1] < 24:
        return df
    else:
        return df.iloc[:, -24:]

if not os.path.exists(carpeta_salida):
    os.makedirs(carpeta_salida)

def convertir_excel_a_csv(ruta_archivo, hoja, nombre_hoja):
    df = pd.read_excel(ruta_archivo, sheet_name=hoja)
    nombre_archivo = os.path.splitext(os.path.basename(ruta_archivo))[0]
    ruta_salida_csv = os.path.join(carpeta_salida, f'{nombre_archivo}_{nombre_hoja}.csv')
    df.to_csv(ruta_salida_csv, index=False)
    print(f'Archivo CSV generado: {ruta_salida_csv}')

print('Conversión Archivos de XLSX a CSV')
for archivo in os.listdir(carpeta2):
    if archivo.endswith('.xlsx'):
        ruta_archivo = os.path.join(carpeta2, archivo)        
        xls = pd.ExcelFile(ruta_archivo)
        for hoja in xls.sheet_names:            
            convertir_excel_a_csv(ruta_archivo, hoja, hoja)

print('Lectura Archivos CSV')
for archivo in os.listdir(carpeta):
    if archivo.endswith('.csv'):
        ruta_archivo = os.path.join(carpeta, archivo)        
        df = leer_ultimas_24_filas_csv(ruta_archivo)
        datos_consolidados.append(df)
        print(archivo)

datos_consolidados2 = []
columnas = ["Cliente","PDV o Codigo","Nombre PDV","Ciudad","Departamento",
"Cedi o Bodega","Regional","Tipo","PLU","Lab","Producto","Clave","Precio Lab",
"Cant Venta"," Vr, total precio Cliente ","Cant Inv","Vr,Total Inv Cliente",
"Vr. Total Venta precio lab"," Vr,Total Inv Lab ","Mes","Año","Mes2","FUENTE","CANAL"]

for d in datos_consolidados:
    d.columns = columnas
    datos_consolidados2.append(d)

print('Consolidación de Información de Archivos')

df_consolidado = pd.concat(datos_consolidados2, ignore_index=True)

df_consolidado.to_excel(carpeta3+'salida_consolidada.xlsx', index=False)
df_consolidado.to_csv(carpeta3+'salida_consolidada.csv', index=False)

print(f"Consolidación completa. Archivo guardado en {carpeta3}")
print('HE TERMINADO')

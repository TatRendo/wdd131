# CÓDIGO CON VALIDACIÓN Y LOG DE ERRORES

import os
import pandas as pd

# === RUTAS (MODIFICABLES SEGÚN EL EQUIPO) ===
carpeta = 'C:\\Users\\A.Ramirez\\OneDrive - LABORATORIOS REMO S.A.S\\Documentos\\Alejandro\\Rotación\\Agosto 2024\\LISTOS\\csv_output'
carpeta2 = 'C:\\Users\\A.Ramirez\\OneDrive - LABORATORIOS REMO S.A.S\\Documentos\\Alejandro\\Rotación\\Agosto 2024\\LISTOS\\'
carpeta3 = 'C:\\Users\\A.Ramirez\\OneDrive - LABORATORIOS REMO S.A.S\\Documentos\\Alejandro\\Rotación\\Agosto 2024\\'
carpeta_salida = carpeta  # misma carpeta para salida

# === ARCHIVO DE LOG DE ERRORES ===
log_errores_path = os.path.join(carpeta3, 'log_errores.txt')
with open(log_errores_path, 'w') as log_file:
    log_file.write("ARCHIVOS OMITIDOS POR ERRORES:\n\n")

# === LISTA PARA DATOS CORRECTOS ===
datos_consolidados = []

# === FUNCIÓN PARA LEER CSV (ULTIMAS 24 COLUMNAS) ===
def leer_ultimas_24_filas_csv(ruta_archivo):
    df_prueba = pd.read_csv(ruta_archivo)
    if 'Unnamed:' in df_prueba.columns[0]: 
        df = pd.read_csv(ruta_archivo, header=1)
    else:
        df = pd.read_csv(ruta_archivo)    
    if df.shape[1] < 24:
        return df
    else:
        return df.iloc[:, -24:]

# === CREA CARPETA DE SALIDA SI NO EXISTE ===
if not os.path.exists(carpeta_salida):
    os.makedirs(carpeta_salida)

# === FUNCIÓN CONVERSIÓN DE EXCEL A CSV ===
def convertir_excel_a_csv(ruta_archivo, hoja, nombre_hoja):
    df = pd.read_excel(ruta_archivo, sheet_name=hoja)
    nombre_archivo = os.path.splitext(os.path.basename(ruta_archivo))[0]
    ruta_salida_csv = os.path.join(carpeta_salida, f'{nombre_archivo}_{nombre_hoja}.csv')
    df.to_csv(ruta_salida_csv, index=False)
    print(f'Archivo CSV generado: {ruta_salida_csv}')

# === PASO 1: CONVERTIR ARCHIVOS .XLSX A .CSV ===
print('🔄 Conversión de archivos XLSX a CSV...')
for archivo in os.listdir(carpeta2):
    if archivo.endswith('.xlsx'):
        ruta_archivo = os.path.join(carpeta2, archivo)
        xls = pd.ExcelFile(ruta_archivo)
        for hoja in xls.sheet_names:
            convertir_excel_a_csv(ruta_archivo, hoja, hoja)

# === PASO 2: LECTURA Y CONSOLIDACIÓN DE CSV ===
print('📄 Lectura de archivos CSV...')
for archivo in os.listdir(carpeta):
    if archivo.endswith('.csv'):
        ruta_archivo = os.path.join(carpeta, archivo)
        try:
            df = leer_ultimas_24_filas_csv(ruta_archivo)
            datos_consolidados.append((archivo, df))
            print(f'Leído: {archivo}')
        except Exception as e:
            with open(log_errores_path, 'a') as log_file:
                log_file.write(f"{archivo} - ERROR AL LEER: {str(e)}\n")
            print(f"⚠️  Error al leer {archivo}: {e}")

# === PASO 3: VALIDACIÓN DE COLUMNAS Y NOMBRADO ===
print('🧪 Validación de columnas...')
datos_consolidados2 = []
columnas = [
    "Cliente","PDV o Codigo","Nombre PDV","Ciudad","Departamento","Cedi o Bodega",
    "Regional","Tipo","PLU","Lab","Producto","Clave","Precio Lab","Cant Venta",
    " Vr, total precio Cliente ","Cant Inv","Vr,Total Inv Cliente",
    "Vr. Total Venta precio lab"," Vr,Total Inv Lab ","Mes","Año",
    "Mes2","FUENTE","CANAL"
]

for nombre_archivo, d in datos_consolidados:
    if d.shape[1] != 24:
        with open(log_errores_path, 'a') as log_file:
            log_file.write(f"{nombre_archivo} - COLUMNAS INVALIDAS: tiene {d.shape[1]} columnas\n")
        print(f"⚠️  {nombre_archivo} tiene {d.shape[1]} columnas. Omitido.")
        continue
    d.columns = columnas
    datos_consolidados2.append(d)

# === PASO 4: CONSOLIDACIÓN FINAL ===
print('📊 Consolidando información...')
if datos_consolidados2:
    df_consolidado = pd.concat(datos_consolidados2, ignore_index=True)
    df_consolidado.to_excel(os.path.join(carpeta3, 'salida_consolidada.xlsx'), index=False)
    df_consolidado.to_csv(os.path.join(carpeta3, 'salida_consolidada.csv'), index=False)
    print(f"✅ Consolidación completada. Archivos guardados en {carpeta3}")
else:
    print("⚠️ No hay archivos válidos para consolidar.")

print(f"📋 Revisa los errores en el archivo de log: {log_errores_path}")
print("🏁 HE TERMINADO")

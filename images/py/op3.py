# CÓDIGO COMPLETO MEJORADO

import os
import pandas as pd
from datetime import datetime

# ========================
# 1. RUTAS DE TRABAJO (EDITABLE SEGÚN EL PC)
# ========================
# Estas rutas pueden cambiar en otro PC. Modifica esto según tu ubicación de archivos:
carpeta = r'C:\Users\A.Ramirez\...\LISTOS\csv_output'     # Donde están los CSV generados
carpeta2 = r'C:\Users\A.Ramirez\...\LISTOS'                # Donde están los archivos .xlsx
carpeta3 = r'C:\Users\A.Ramirez\...\Rotación\Agosto 2024'  # Carpeta raíz para guardar el archivo final
carpeta_salida = carpeta  # Igual que carpeta de CSV

# ========================
# 2. LISTA PARA DATOS
# ========================
datos_consolidados = []

# ========================
# 3. FUNCIONES
# ========================

# Lee las últimas 24 columnas del CSV si existen
def leer_ultimas_24_filas_csv(ruta_archivo):
    try:
        df_prueba = pd.read_csv(ruta_archivo)
        
        # Leer con encabezado correcto si tiene columnas "Unnamed:"
        if 'Unnamed:' in df_prueba.columns[0]: 
            df = pd.read_csv(ruta_archivo, header=1)
        else:
            df = df_prueba

        # Validar si hay al menos 24 columnas
        if df.shape[1] < 24:
            print(f"[ADVERTENCIA] {os.path.basename(ruta_archivo)} tiene menos de 24 columnas ({df.shape[1]})")
            return None
        else:
            return df.iloc[:, -24:]
    
    except Exception as e:
        print(f"[ERROR] al leer CSV: {ruta_archivo} - {e}")
        return None

# Convierte un Excel a CSV por hoja
def convertir_excel_a_csv(ruta_archivo, hoja, nombre_hoja):
    try:
        df = pd.read_excel(ruta_archivo, sheet_name=hoja)
        nombre_archivo = os.path.splitext(os.path.basename(ruta_archivo))[0]
        ruta_salida_csv = os.path.join(carpeta_salida, f'{nombre_archivo}_{nombre_hoja}.csv')
        df.to_csv(ruta_salida_csv, index=False)
        print(f'[✔] CSV generado: {ruta_salida_csv}')
    except Exception as e:
        print(f"[ERROR] al convertir Excel: {ruta_archivo} - Hoja: {hoja} - {e}")

# ========================
# 4. CREAR CARPETA SI NO EXISTE
# ========================
if not os.path.exists(carpeta_salida):
    os.makedirs(carpeta_salida)

# ========================
# 5. CONVERSIÓN DE ARCHIVOS
# ========================
print('⏳ Conversión de XLSX a CSV...')
for archivo in os.listdir(carpeta2):
    if archivo.endswith('.xlsx'):
        ruta_archivo = os.path.join(carpeta2, archivo)        
        try:
            xls = pd.ExcelFile(ruta_archivo)
            for hoja in xls.sheet_names:            
                convertir_excel_a_csv(ruta_archivo, hoja, hoja)
        except Exception as e:
            print(f"[ERROR] al abrir archivo Excel: {archivo} - {e}")

# ========================
# 6. LECTURA DE ARCHIVOS CSV
# ========================
print('\n📥 Lectura de Archivos CSV...')
for archivo in os.listdir(carpeta):
    if archivo.endswith('.csv'):
        ruta_archivo = os.path.join(carpeta, archivo)
        df = leer_ultimas_24_filas_csv(ruta_archivo)
        if df is not None:
            datos_consolidados.append(df)

# ========================
# 7. VALIDACIÓN Y RENOMBRADO DE COLUMNAS
# ========================
columnas = [
    "Cliente", "PDV o Codigo", "Nombre PDV", "Ciudad", "Departamento", 
    "Cedi o Bodega", "Regional", "Tipo", "PLU", "Lab", "Producto", "Clave", 
    "Precio Lab", "Cant Venta", "Vr total precio Cliente", "Cant Inv", 
    "Vr Total Inv Cliente", "Vr Total Venta precio lab", "Vr Total Inv Lab", 
    "Mes", "Año", "Mes2", "FUENTE", "CANAL"
]

datos_consolidados2 = []
for d in datos_consolidados:
    if d.shape[1] == len(columnas):
        d.columns = columnas
        datos_consolidados2.append(d)
    else:
        print(f"[ADVERTENCIA] Archivo con columnas incorrectas: {d.shape[1]} columnas")

# ========================
# 8. CONSOLIDACIÓN Y EXPORTACIÓN
# ========================
if datos_consolidados2:
    print('\n📦 Consolidación de Información...')
    df_consolidado = pd.concat(datos_consolidados2, ignore_index=True)

    # Agregar marca de tiempo
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    excel_out = os.path.join(carpeta3, f'salida_consolidada_{timestamp}.xlsx')
    csv_out = os.path.join(carpeta3, f'salida_consolidada_{timestamp}.csv')

    df_consolidado.to_excel(excel_out, index=False)
    df_consolidado.to_csv(csv_out, index=False)

    print(f"[✔] Consolidación completa. Archivos guardados en:\n- {excel_out}\n- {csv_out}")
else:
    print("[❌] No hay archivos válidos para consolidar.")

print('✅ FINALIZADO')

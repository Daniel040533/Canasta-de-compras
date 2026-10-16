import sys
import pandas as pd
from estructuras import Nodo, ListaEnlazada

def cargar_y_vincular_datos(ruta_archivo, limite_filas=None):
    df = pd.read_excel(ruta_archivo, sheet_name='Online Retail')
    
    # Limpiamos nulos. CustomerID es necesario para los calculos de cliente
    df = df.dropna(subset=['InvoiceNo', 'StockCode', 'CustomerID'])
    
    # Filtramos la base completa excluyendo a Reino Unido
    df = df[df['Country'] != 'United Kingdom']
    
    if limite_filas:
        df = df.head(limite_filas)
        
    facturas_db = {}
    
    for index, fila in df.iterrows():
        invoice_no = fila['InvoiceNo']
        datos_linea = {
            'StockCode': fila['StockCode'],
            'Description': fila['Description'],
            'Quantity': fila['Quantity'],
            'UnitPrice': fila['UnitPrice'],
            'CustomerID': fila['CustomerID']
        }
        
        # Si la factura no existe en el diccionario, creamos una nueva ListaEnlazada
        if invoice_no not in facturas_db:
            facturas_db[invoice_no] = ListaEnlazada()
            
        lista_actual = facturas_db[invoice_no]
        lista_actual.insertar(lista_actual.contar(), datos_linea)
        
    return facturas_db, len(df)

def calcular_total_factura_enlazada(lista_factura):
    total = 0.0
    for linea in lista_factura.recorrer():
        total += linea['Quantity'] * linea['UnitPrice']
    return total

def calcular_acumulado_cliente_enlazada(facturas_db, customer_id):
    total_acumulado = 0.0
    for invoice_no, lista_factura in facturas_db.items():
        # Verificamos que la factura pertenezca al cliente solicitado
        if lista_factura.cabeza and lista_factura.cabeza.datos['CustomerID'] == customer_id:
            total_acumulado += calcular_total_factura_enlazada(lista_factura)
    return total_acumulado

def buscar_producto_en_subconjunto(facturas_db, stock_code):
    lineas_encontradas = []
    sys.setrecursionlimit(2500) # Previene desbordamiento en listas muy largas
    
    for invoice_no, lista_factura in facturas_db.items():
        if lista_factura.cabeza is not None:
            resultados_factura = lista_factura.buscar_producto_recursivo(
                lista_factura.cabeza, 
                stock_code
            )
            lineas_encontradas.extend(resultados_factura)
            
    return lineas_encontradas

if __name__ == "__main__":
    print("Cargando base de datos y limpiando subconjunto (Sin Reino Unido)...")
    
    # Prueba inicial rapida con 5000 filas. Para la entrega final, quitar el limite_filas
    base_de_datos, total_filas = cargar_y_vincular_datos("Online Retail.xlsx", limite_filas=5000)
    
    print("-" * 50)
    print(f"Total de lineas validas en el subconjunto: {total_filas}")
    print("-" * 50)
    
    producto_a_buscar = '85123A'
    resultados = buscar_producto_en_subconjunto(base_de_datos, producto_a_buscar)
    print(f"Se encontraron {len(resultados)} lineas con el producto {producto_a_buscar}.")
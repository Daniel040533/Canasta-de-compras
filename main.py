import sys
import pandas as pd
from estructuras import Nodo, ListaEnlazada

def cargar_y_vincular_datos(ruta_archivo, limite_filas=None):
    df = pd.read_excel(ruta_archivo, sheet_name='Online Retail')
    
    # Limpieza de nulos requerida para agrupar facturas y clientes
    df = df.dropna(subset=['InvoiceNo', 'StockCode', 'CustomerID'])
    df = df[df['Country'] != 'United Kingdom'] # Filtro del subconjunto asignado
    
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
        
        if invoice_no not in facturas_db:
            facturas_db[invoice_no] = ListaEnlazada()
            
        lista_actual = facturas_db[invoice_no]
        # Al insertar en el tamaño actual (contar), se mantiene el orden de registro
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
        if lista_factura.cabeza and lista_factura.cabeza.datos['CustomerID'] == customer_id:
            total_acumulado += calcular_total_factura_enlazada(lista_factura)
    return total_acumulado

def buscar_producto_en_subconjunto(facturas_db, stock_code):
    lineas_encontradas = []
    sys.setrecursionlimit(2500) # Previene desbordamiento de pila en recursión
    
    for invoice_no, lista_factura in facturas_db.items():
        if lista_factura.cabeza is not None:
            resultados_factura = lista_factura.buscar_producto_recursivo(
                lista_factura.cabeza, 
                stock_code
            )
            lineas_encontradas.extend(resultados_factura)
            
    return lineas_encontradas

if __name__ == "__main__":
    print("Cargando base de datos (Sin Reino Unido)...")
    base_de_datos, total_filas = cargar_y_vincular_datos("Online Retail.xlsx", limite_filas=5000)
    print(f"Total de líneas cargadas: {total_filas}\n")
    
    print("--- DEMOSTRACIÓN: PROBLEMA 1 ---")
    
    # Recuperamos la primera factura registrada
    factura_prueba = list(base_de_datos.keys())[0]
    lista_prueba = base_de_datos[factura_prueba]
    print(f"Factura: {factura_prueba} | Líneas originales: {lista_prueba.contar()}")
    
    linea_correccion = {
        'StockCode': 'CORR-01',
        'Description': 'CORRECCIÓN MANUAL',
        'Quantity': 1,
        'UnitPrice': 0.0,
        'CustomerID': lista_prueba.cabeza.datos['CustomerID'] if lista_prueba.cabeza else 0
    }
    
    # Inserción en posición específica (índice 1)
    lista_prueba.insertar(1, linea_correccion)
    print("-> Se insertó línea de corrección en la posición 1.")
    
    # Eliminación en posición específica (la última)
    if lista_prueba.contar() > 0:
        pos_eliminar = lista_prueba.contar() - 1
        borrada = lista_prueba.eliminar(pos_eliminar)
        print(f"-> Se eliminó línea en posición {pos_eliminar} ({borrada['Description']}).")
        
    print(f"Líneas finales en la factura {factura_prueba}: {lista_prueba.contar()}")
    print("-" * 50)
    

    print("--- DEMOSTRACIÓN: PROBLEMA 2 ---")
    
    total_factura = calcular_total_factura_enlazada(lista_prueba)
    print(f"Importe total de la factura {factura_prueba}: £{total_factura:.2f}")
    
    if lista_prueba.cabeza:
        cliente_prueba = lista_prueba.cabeza.datos['CustomerID']
        total_cliente = calcular_acumulado_cliente_enlazada(base_de_datos, cliente_prueba)
        print(f"Gasto total acumulado del cliente {cliente_prueba}: £{total_cliente:.2f}")
    else:
        print("La factura está vacía.")
        
    print("-" * 50)
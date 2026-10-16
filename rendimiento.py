import time 
import numpy as np 
from estructuras import ListaEnlazada

def medir_tiempos(tamanos):
    for n in tamanos:
        print(f"\n --Evaluando tamaños de entrada: {n} elementos--")

        #1. Preparar datos y estructuras
        datos_prueba = [{"Quantity":2, "UnitPrice": 5.0} for _ in range(n)]
        lista_enlazada = ListaEnlazada()
        lista_nativa = []

        for i, dato in enumerate(datos_prueba):
            lista_enlazada.insertar(i, dato)
            lista_nativa.append(dato)

        array_numpy = np.array([5.0 * 2 for _ in range(n)])#Arreglos contiguos de totales
        pos_medio = n // 2
        nuevo_dato = {"Quantity": 1, "UnitPrice":10.0 }

        #Medir insercion en el medio
        inicio = time.perf_counter()
        lista_enlazada.insertar(pos_medio, nuevo_dato)
        t_enlazada_ins = time.perf_counter() - inicio

        inicio = time.perf_counter()
        lista_nativa.insert(pos_medio, nuevo_dato)
        t_nativa_ins = time.perf_counter() - inicio

        #3. Medir eliminacion en el medio
        inicio = time.perf_counter()
        lista_enlazada.eliminar(pos_medio)
        t_enlazada_elim = time.perf_counter() - inicio

        inicio = time.perf_counter()
        lista_nativa.pop(pos_medio)
        t_nativa_elim = time.perf_counter() - inicio

        #4. Medir recorridos(Suma total)
        inicio = time.perf_counter()
        total = 0 
        for linea in lista_enlazada.recorrer():
            total += linea["Quantity"] * linea["UnitPrice"]
        t_enlazada_rec = time.perf_counter() - inicio

        inicio = time.perf_counter()
        total = sum(linea["Quantity"] * linea["UnitPrice"] for linea in lista_nativa)
        t_nativa_rec = time.perf_counter() - inicio

        inicio = time.perf_counter()
        total = np.sum(array_numpy)
        t_numpy_rec = time.perf_counter() - inicio#Aqui termina la comparacion de recorrido

        print("Insercion (medio): Enlazada {:.6f}s | Nativa {:.6f}s".format(t_enlazada_ins, t_nativa_ins))
        print("Eliminacion (medio): Enlazada {:.6f}s | Nativa {:.6f}s".format(t_enlazada_elim, t_nativa_elim))
        print("Recorrido (suma): Enlazada {:.6f}s | Nativa {:.6f}s | Numpy {:.6f}s".format(t_enlazada_rec, t_nativa_rec, t_numpy_rec))

if __name__ == "__main__":
    tamanos_prueba = [1000, 10000, 50000] #Tres tamaños requeridos por la rubrica
    medir_tiempos(tamanos_prueba)
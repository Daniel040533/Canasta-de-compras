<h1>Bitácora de Estructuras</h1>
<hr>
<h3>Se comenzo a trabajar en un repositorio el cual fue nuestro borrador ya que desconociamos como funcionaba git.
En ese repositorio hicimos todos los archivos necesarios para el proyecto a prueba y error para finalmente pasar en limpio todos nuestros archivos para que a la hora de correrlo, este funcionara correctamente</h3>
<hr>
<h3>Para comenzar a trabajar en nuestro proyecto se utilizo la IA con el promp 
<h3 style="color: #FF0000;">Actúa como un tutor de Estructuras de Datos en Python. Voy a construir un "Motor de análisis de canasta de compras" para mi materia. Primero, ayúdame a diseñar la arquitectura del sistema con estos requisitos:

Tarea 1 — Implementar la lista enlazada a mano:

Implementa en Python una lista enlazada simple desde cero, usando clases Nodo y ListaEnlazada. Debe soportar: insertar en cualquier posición, eliminar en cualquier posición, recorrer en orden, y contar elementos. Incluye docstrings y comentarios explicando cada método. No uses listas nativas de Python dentro de la implementación.

Tarea 2 — Cargar datos reales:

Escribe código en Python para cargar un archivo CSV de facturas (con columnas típicas: id_factura, id_cliente, id_producto, cantidad, importe) usando solo csv o pandas para la carga inicial, y luego almacenar cada factura como una lista enlazada de líneas. Muestra cómo recorrer una factura específica en el orden registrado.

Tarea 3 — Problema 1 (orden, inserción, eliminación):

Agrega a mi lista enlazada métodos para: insertar una línea de corrección en una posición dada y eliminar una línea cancelada en cualquier posición, manteniendo el orden original. Explica cómo el orden se preserva y qué pasa con los enlaces al insertar/eliminar.

Tarea 4 — Problema 2 (importes):

Escribe funciones que recorran la lista enlazada de una factura para calcular su importe total, y que recorran todas las facturas de un cliente para calcular su total acumulado. Compara esto con hacerlo con una lista nativa de Python.

Tarea 5 — Problema 3 (buscar producto):

Implementa una función que recorra la lista enlazada y devuelva todas las líneas que contengan un producto dado (por id_producto). Muestra el resultado para el subconjunto de datos asignado.

Tarea 6 — Problema 4 (comparación de costos):

Crea un script que mida el tiempo de recorrer, insertar y eliminar en: (a) mi lista enlazada a mano, (b) una lista nativa de Python, y (c) un array de NumPy, para al menos 3 tamaños de entrada (ej. 100, 1000, 10000 elementos). Genera una tabla con los tiempos y compárala con las cotas teóricas O(n), O(1), etc.</h3>
<hr>
<p><b>¿Qué se aceptó de la IA?</b> Se aceptó la lógica principal de la estructura del Nodo y la Lista Enlazada para la gestión de memoria sin listas nativas, así como el uso de <code>yield</code> para optimizar los recorridos.</p>
<p><b>¿Qué se corrigió de la IA?</b> Se ajustó el motor de carga porque la IA originalmente sugirió usar librerías nativas <code>csv</code>, pero decidimos utilizar Pandas para realizar una limpieza más robusta (<code>dropna</code>) y aplicar el filtro geográfico solicitado (excluyendo a Reino Unido). También adaptamos las impresiones de prueba para que encajaran con nuestra lógica de importes.</p>
<hr>
<h1>Daniel</h1>
<h3>Para empezar programé la clase Nodo, que sirve para guardar los datos de cada línea y usar el atributo "siguiente" para unirse con el nodo que le sigue. Después armé la clase ListaEnlazada, poniendo "cabeza" para identificar el inicio y una variable "tamano" para saber cuántos elementos hay sin tener que contarlos uno por uno. Agregué el método contar para que me devuelva ese tamaño. Luego hice el método insertar, que me deja meter un nuevo nodo en cualquier posición válida ajustando las conexiones de los punteros. También hice eliminar, que saca un nodo saltándolo en las conexiones para que ya no sea parte de la lista y restando el tamaño. Para terminar esta parte, creé el método recorrer con un ciclo while y la instrucción yield; así puedo ir viendo los elementos uno por uno sin necesidad de crear listas nativas de Python que gasten memoria extra.</h3>
<h3>Usé el método insertar para agregar líneas de corrección pasándole la posición exacta, así el nodo nuevo se acomoda moviendo los enlaces sin desordenar el resto. Para quitar las líneas canceladas usé eliminar, dándole la posición para que desconecte ese nodo de la lista. Además, implementé el método buscar_producto_recursivo, que es una función que se llama a sí misma para buscar un producto usando su identificador (StockCode). Le puse un caso base para que se detenga y devuelva los resultados si llega al final de la lista, y un caso recursivo que va checando nodo por nodo y guardando las coincidencias. Al final, usé recorrer para asegurarme de que los datos quedaron bien y contar para verificar que el tamaño final de la lista fuera el correcto.</h3>

<h2>Omar</h2>
<hr>
<h3>Me encargué de programar la función <code>cargar_y_vincular_datos</code> para leer el Excel con Pandas, limpiar los valores nulos con <code>dropna</code> y filtrar los registros excluyendo al Reino Unido. También desarrollé las funciones clave para calcular el total de cada factura (<code>calcular_total_factura_enlazada</code>), obtener el gasto acumulado por cliente (<code>calcular_acumulado_cliente_enlazada</code>) y realizar la búsqueda de productos en el subconjunto. Finalmente, estructuré el bloque de pruebas principal para demostrar el Problema 1, insertando una línea de corrección manual en la posición 1 y eliminando un elemento al final de la lista enlazada.</h3>
<hr>

<h2>Fernanda</h2>
<hr>
<h3>Me tocó resolver el punto 2 del problema 3, que consistió en armar la función para buscar productos en las facturas usando la búsqueda recursiva, recorriendo los nodos uno por uno para encontrar las coincidencias exactas por su código (StockCode).</h3>

<h2>Brandon</h2>
<hr>
<h3>Me encargué de realizar la comparación en los cálculos de importes entre nuestra lista enlazada y una lista nativa de Python. Asimismo, desarrollé el script de pruebas de rendimiento utilizando <code>time.perf_counter()</code> para medir con precisión los tiempos de inserción, eliminación y recorrido. Evalué el comportamiento probando con 1,000, 10,000 y 50,000 elementos, lo que permitió contrastar nuestra estructura frente a listas nativas y arreglos de NumPy para analizar cómo cambia el rendimiento según el volumen de datos.</h3>
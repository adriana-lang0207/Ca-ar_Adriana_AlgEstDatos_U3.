from utilidades import *
while True:
    print("\n===== RED DE CIUDADES =====\n1. Grado de cada ciudad \n2 Recorrido BFS \n3. Ruta mínima con Dijkstra \n4. Salir")
    o = input("Opción: ")
    # R1: Mostrar el grado de todas las ciudades.
    if o == '1':
        print(grados(grafo))
    # R2: Ejecutar el recorrido BFS desde Quito.
    elif o == '2':
        print(bfs(grafo, 'Quito'))
    # R3: Ejecutar el algoritmo de Dijkstra.
    elif o == '3':
        d = dijkstra(grafo, 'Quito') # Calcula las distancias mínimas desde Quito.
        print(d)
        x = {k: v for k, v in d.items() if v > 0}
        print("Ciudad más cercana:", min(x, key=x.get))
        print("Ciudad más lejana:", max(x, key=x.get))
    elif o == '5':
        break

from collections import deque
# heapq utiliza una cola de prioridad en el algoritmo de Dijkstra.
import heapq

# La clave es una ciudad y el valor es una lista de tuplas: (ciudad vecina, distancia en kilómetros) 
grafo = {
    'Quito': [('Latacunga', 90), ('Ibarra', 120), ('Cuenca', 500)],
    'Latacunga': [('Quito', 90), ('Ambato', 50), ('Riobamba', 180)],
    'Ibarra': [('Quito', 120), ('Tulcan', 130)],
    'Ambato': [('Latacunga', 50), ('Riobamba', 60)],
    'Riobamba': [('Ambato', 60), ('Latacunga', 180), ('Cuenca', 250)],
    'Tulcan': [('Ibarra', 130), ('Cuenca', 600)],
    'Cuenca': [('Riobamba', 250), ('Tulcan', 600), ('Quito', 500)]
}

def grados(g):
    # O(V)
    # El grado es el número de ciudades con las que tiene conexión directa.
    return {k: len(v) for k, v in g.items()}

def bfs(g, o):
    # BFS: O(V + E)
    # almacena las ciudades visitadas y el número de escalas desde la ciudad de origen.
    vis={o:0};q=deque([o])
    while q:
        u = q.popleft()
        for v, _ in g[u]:
            if v not in vis: vis[v]=vis[u]+1;q.append(v)
    return vis, len(vis) == len(g)     # devuelve las escalas de cada ciudad y verifica si toda la red está conectada.

def dijkstra(grafo, origen):
    # Dijkstra: O((V + E) log V)
    # Inicializa todas las distancias como infinitas. Almacena (distancia, ciudad)
    dist={c:float('inf') for c in grafo};dist[origen]=0;heap=[(0,origen)]
    while heap:
        d,u=heapq.heappop(heap)
        if d>dist[u]: continue
        for vecino,peso in grafo[u]:
            if dist[u]+peso<dist[vecino]: dist[vecino]=dist[u]+peso;heapq.heappush(heap,(dist[vecino],vecino))

    # Devuelve las distancias mínimas desde la ciudad de origen.
    return dist

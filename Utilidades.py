from collections import deque
import heapq
grafo={'Quito':[('Latacunga',90),('Ibarra',120)],'Latacunga':[('Quito',90),('Ambato',50),('Riobamba',180)],'Ibarra':[('Quito',120),('Tulcan',130)],'Ambato':[('Latacunga',50),('Riobamba',60)],'Riobamba':[('Ambato',60),('Latacunga',180),('Cuenca',250)],'Tulcan':[('Ibarra',130),('Cuenca',600)],'Cuenca':[('Riobamba',250),('Tulcan',600)]}
def grados(g):
 return {k:len(v) for k,v in g.items()}
def bfs(g,o):
 vis={o:0};q=deque([o])
 while q:
  u=q.popleft()
  for v,_ in g[u]:
   if v not in vis: vis[v]=vis[u]+1;q.append(v)
 return vis,len(vis)==len(g)
def dijkstra(grafo,origen):
 dist={c:float('inf') for c in grafo};dist[origen]=0;heap=[(0,origen)]
 while heap:
  d,u=heapq.heappop(heap)
  if d>dist[u]: continue
  for vecino,peso in grafo[u]:
   if dist[u]+peso<dist[vecino]: dist[vecino]=dist[u]+peso;heapq.heappush(heap,(dist[vecino],vecino))
 return dist
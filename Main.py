from utilidades import *
while True:
 print('1 Grados\n2 BFS\n3 Dijkstra\n4 Comparacion\n5 Salir')
 o=input('Opcion:')

 if o=='1': print(grados(grafo))
 elif o=='2': print(bfs(grafo,'Quito'))
 elif o=='3':
  d=dijkstra(grafo,'Quito');print(d)
  x={k:v for k,v in d.items() if v>0};print(min(x,key=x.get),max(x,key=x.get))
 elif o=='4': print('BFS minimiza escalas; Dijkstra minimiza distancia.')
 elif o=='5': break
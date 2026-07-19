# Red de Ciudades

Este programa desarrollado en Python, modela una red de ciudades conectadas por carreteras mediante un grafo ponderado. Además, permite recorrer la red, calcular rutas mínimas y comparar distintos tipos de recorridos.

## Requisitos

* Tener instalado Python 3.

## Cómo ejecutar el programa

1. Descargue o clone el repositorio.
2. Abra una terminal en la carpeta del proyecto.
3. Ejecute el siguiente comando:

```bash
python main.py
```

Si su sistema utiliza Python 3 como comando principal, puede ejecutar:

```bash
python3 main.py
```

## Requerimientos implementados

### R1 – Modelado del grafo

Se representa la red de ciudades mediante una lista de adyacencia utilizando un diccionario. Cada ciudad almacena las ciudades vecinas y la distancia en kilómetros. Además, el programa muestra el grado de cada ciudad, es decir, el número de conexiones directas que posee.

### R2 – Recorrido del grafo (BFS)

Se implementa el algoritmo BFS para recorrer la red desde una ciudad de origen. El programa muestra todas las ciudades alcanzables, el número de escalas necesarias para llegar a cada una y verifica si la red está completamente conectada.

### R3 – Ruta minima con Dijkstra

Se integra el algoritmo de Dijkstra para calcular la distancia mínima desde una ciudad de origen hasta todas las demás. También identifica la ciudad más cercana y la más lejana según la distancia recorrida.

### R4 – Comparación entre BFS y Dijkstra

Se compara la ruta con menor número de escalas obtenida mediante BFS con la ruta de menor distancia calculada por Dijkstra, mostrando que ambas pueden ser diferentes dependiendo de la distribución de las carreteras.

## Estructura del proyecto

```text
red_ciudades/
│
├── main.py
├── utilidades.py
└── README.md
```

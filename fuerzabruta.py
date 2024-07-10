import itertools

# Matriz de distancias proporcionada
distancias = [
    [0, 7, 9, 11, 13],
    [7, 0, 4, 12, 10],
    [9, 4, 0, 5, 8],
    [11, 12, 5, 0, 6],
    [13, 10, 8, 6, 0]
]

# Función para calcular la longitud total de una ruta
def calcular_longitud_ruta(ruta, distancias):
    longitud = 0
    for i in range(len(ruta) - 1):
        longitud += distancias[ruta[i]][ruta[i + 1]]
    longitud += distancias[ruta[-1]][ruta[0]]  # Volver al nodo inicial
    return longitud

# Generar todas las posibles rutas (permutaciones)
nodos = list(range(len(distancias)))
permutaciones = list(itertools.permutations(nodos))

# Inicializar la mejor ruta y la mejor longitud
mejor_ruta = None
mejor_longitud = float('inf')

# Evaluar todas las permutaciones
for ruta in permutaciones:
    longitud = calcular_longitud_ruta(ruta, distancias)
    if longitud < mejor_longitud:
        mejor_ruta = ruta
        mejor_longitud = longitud

# Imprimir la mejor ruta y la mejor longitud
print("Mejor ruta:", mejor_ruta)
print("Mejor longitud:", mejor_longitud)

import random

class ACO:
    def __init__(self, num_hormigas, num_nodos, evaporacion, deposito, distancias):
        self.num_hormigas = num_hormigas
        self.num_nodos = num_nodos
        self.evaporacion = evaporacion
        self.deposito = deposito
        self.feromonas = [[1.0 for _ in range(num_nodos)] for _ in range(num_nodos)]
        self.distancias = distancias
    
    def construir_soluciones(self):
        soluciones = []
        for _ in range(self.num_hormigas):
            solucion = self.construir_solucion()
            soluciones.append(solucion)
        return soluciones
    
    def construir_solucion(self):
        solucion = [0]  # Comenzar en el nodo 0
        nodos_restantes = set(range(1, self.num_nodos))
        while nodos_restantes:
            ultimo_nodo = solucion[-1]
            probabilidades = self.calcular_probabilidades(ultimo_nodo, nodos_restantes)
            siguiente_nodo = self.elegir_siguiente_nodo(probabilidades, nodos_restantes)
            solucion.append(siguiente_nodo)
            nodos_restantes.remove(siguiente_nodo)
        solucion.append(0)  # Volver al nodo inicial
        return solucion
    
    def calcular_probabilidades(self, ultimo_nodo, nodos_restantes):
        # Calcular probabilidades basadas en feromonas y heurística
        probabilidades = []
        for nodo in nodos_restantes:
            feromona = self.feromonas[ultimo_nodo][nodo]
            heuristica = 1.0 / self.distancias[ultimo_nodo][nodo] if self.distancias[ultimo_nodo][nodo] != 0 else 0.1  # Evitar división por cero
            probabilidades.append(feromona * heuristica)
        suma_probabilidades = sum(probabilidades)
        return [p / suma_probabilidades for p in probabilidades]
    
    def elegir_siguiente_nodo(self, probabilidades, nodos_restantes):
        return random.choices(list(nodos_restantes), probabilidades)[0]
    
    def actualizar_feromonas(self, soluciones):
        # Evaporación
        for i in range(self.num_nodos):
            for j in range(self.num_nodos):
                self.feromonas[i][j] *= (1 - self.evaporacion)
        
        # Deposición
        for solucion in soluciones:
            contribucion = self.deposito / self.calcular_longitud_solucion(solucion)
            for k in range(len(solucion) - 1):
                i, j = solucion[k], solucion[k+1]
                self.feromonas[i][j] += contribucion
                self.feromonas[j][i] += contribucion
    
    def calcular_longitud_solucion(self, solucion):
        # Función de longitud de la solución (distancia total)
        longitud = 0
        for i in range(len(solucion) - 1):
            longitud += self.distancias[solucion[i]][solucion[i+1]]
        return longitud
    
    def optimizar(self, num_iteraciones_max, mejora_minima):
        mejor_solucion = None
        mejor_longitud = float('inf')
        for _ in range(num_iteraciones_max):
            soluciones = self.construir_soluciones()
            self.actualizar_feromonas(soluciones)
            for solucion in soluciones:
                longitud = self.calcular_longitud_solucion(solucion)
                if longitud < mejor_longitud:
                    mejor_solucion = solucion
                    mejor_longitud = longitud
            if mejor_longitud <= mejora_minima:
                break
        return mejor_solucion, mejor_longitud

# Matriz de distancias proporcionada
distancias = [
    [0, 7, 9, 11, 13],
    [7, 0, 4, 12, 10],
    [9, 4, 0, 5, 8],
    [11, 12, 5, 0, 6],
    [13, 10, 8, 6, 0]
]

# Ejemplo de uso
aco = ACO(num_hormigas=10, num_nodos=5, evaporacion=0.5, deposito=100, distancias=distancias)
mejor_solucion, mejor_longitud = aco.optimizar(num_iteraciones_max=100, mejora_minima=0.01)
print("Mejor solución:", mejor_solucion)
print("Mejor longitud:", mejor_longitud)


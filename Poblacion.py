from random import randint, random

def generar_tableros_aleatorios(n, num_tableros):
    tableros = []
    for i in range(num_tableros):
        tablero = []
        for j in range(n):
            tablero.append(randint(0, n-1))
        tableros.append(tablero)
    return tableros

def calcular_fitness(tablero):
    ataques = 0
    for i in range(len(tablero)):
        for j in range(i+1, len(tablero)):
            if tablero[i] == tablero[j]:
                ataques += 1
            if abs(tablero[i] - tablero[j]) == j - i:
                ataques += 1
    return 1 / (ataques + 1)

def seleccionar_padres(poblacion, fitness_total):
    padre1 = None
    padre2 = None
    while padre1 is None:
        valor_aleatorio = random() * fitness_total
        acumulado = 0
        for cromosoma in poblacion:
            acumulado += cromosoma['fitness']
            if acumulado >= valor_aleatorio:
                padre1 = cromosoma
                break
    while padre2 is None:
        valor_aleatorio = random() * fitness_total
        acumulado = 0
        for cromosoma in poblacion:
            acumulado += cromosoma['fitness']
            if acumulado >= valor_aleatorio and cromosoma != padre1:
                padre2 = cromosoma
                break
    return padre1, padre2

def reproducir(padre1, padre2):
    punto_cruce = randint(1, len(padre1) - 1)
    hijo1 = {'genes': padre1['genes'][:punto_cruce] + padre2['genes'][punto_cruce:], 'fitness': None}
    hijo2 = {'genes': padre2['genes'][:punto_cruce] + padre1['genes'][punto_cruce:], 'fitness': None}
    return hijo1, hijo2

def mutar(cromosoma, probabilidad_mutacion):
    if random() < probabilidad_mutacion:
        posicion_mutation = randint(0, len(cromosoma['genes']) - 1)
        cromosoma['genes'][posicion_mutation] = randint(0, len(cromosoma['genes']) - 1)
        cromosoma['fitness'] = None

def encontrar_solucion(tableros):
    for tablero in tableros:
        if calcular_fitness(tablero) == 1:
            return {'genes': tablero, 'fitness': 1}
    return None

def generar_poblacion_inicial(tamano_poblacion, n):
    poblacion = []
    for i in range(tamano_poblacion):
        cromosoma = {'genes': [], 'fitness': None}
        for j in range(n):
            cromosoma['genes'].append(randint(0, n-1))
        while len(set(cromosoma['genes'])) < n:
            for j in range(n):
                if cromosoma['genes'].count(j) > 1:
                    indice_repetido = cromosoma['genes'].index(j)
                    cromosoma['genes'][indice_repetido] = randint(0, n-1)
        poblacion.append(cromosoma)
    return poblacion


def resolver_problema(n, num_tableros, num_generaciones, tamano_poblacion, probabilidad_mutacion, num_soluciones_unicas):
    tableros = generar_tableros_aleatorios(n, num_tableros)
    solucion_inicial = encontrar_solucion(tableros)
    poblacion = generar_poblacion_inicial(tamano_poblacion, n)
    poblacion[0] = solucion_inicial
    for cromosoma in poblacion:
        cromosoma['fitness'] = calcular_fitness(cromosoma['genes'])
    soluciones = algoritmo_genetico(poblacion, num_generaciones, probabilidad_mutacion, num_soluciones_unicas)
    return soluciones


n = 6
num_tableros = 100
num_generaciones = 100
tamano_poblacion = 100
probabilidad_mutacion = 0.1
num_soluciones_unicas = 10

soluciones = resolver_problema(n, num_tableros, num_generaciones, tamano_poblacion, probabilidad_mutacion, num_soluciones_unicas)

for solucion in soluciones:
    print(solucion['genes'])

#Algoritmo las 6 Reinas

def verificar_tablero(tablero, fila, columna):
    """
    Esta función verifica si es seguro colocar una reina en la posición (fila, columna)
    en el tablero actual.
    """
    for i in range(fila):
        # Verifica si hay una reina en la misma columna
        if tablero[i] == columna:
            return False
        # Verifica si hay una reina en la misma diagonal
        if abs(tablero[i] - columna) == fila - i:
            return False
    return True

def resolver(tablero, fila):
    """
    Esta función utiliza la técnica de backtracking para resolver el problema de las
    6 reinas. Comienza en la fila 'fila' y trata de colocar una reina en cada columna.
    """
    # Si se han colocado 6 reinas (es decir, si se llegó a la última fila), retorna True
    if fila == 6:
        return True
    
    # Intenta colocar una reina en cada columna de la fila actual
    for columna in range(6):
        if verificar_tablero(tablero, fila, columna):
            # Si es seguro colocar una reina en la posición (fila, columna), colócala
            tablero[fila] = columna
            # Intenta resolver el resto del tablero recursivamente
            if resolver(tablero, fila+1):
                return True
    # Si no se pudo colocar una reina en ninguna columna, retrocede a la fila anterior
    tablero[fila] = None
    return False




from CromosomaSolucion import resolver;

print("------ Ejercicio de las 6 Reinas -------\n");

#Crea un tablero vacío
tablero = [None] * 6

# Llama a la función 'resolver' con el tablero vacío y la primera fila
if resolver(tablero, 0):
    print("Se encontró una solución:")
    print(tablero)
else:
    print("No se encontró ninguna solución.")

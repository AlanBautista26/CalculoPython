def main():
    filas = int(input("Ingrese el numero de filas: "))
    columnas = int(input("Ingrese el numero de columnas: "))
    
    matriz1 = []
    matriz2 = []

    print("Ingrese los elementos de la primera matriz:")
    for i in range(filas):
        fila = []
        for j in range(columnas):
            elemento = float(input(f"Elemento [{i + 1}, {j + 1}]: "))
            fila.append(elemento)
        matriz1.append(fila)

    print("Ingrese los elementos de la segunda matriz:")
    for i in range(filas):
        fila = []
        for j in range(columnas):
            elemento = float(input(f"Elemento [{i + 1}, {j + 1}]: "))
            fila.append(elemento)
        matriz2.append(fila)

    matriz_suma = []
    for i in range(filas):
        fila_suma = []
        for j in range(columnas):
            suma = matriz1[i][j] + matriz2[i][j]
            fila_suma.append(suma)
        matriz_suma.append(fila_suma)

    print("La suma de las matrices es:")
    for fila in matriz_suma:
        print(fila)
main()
from geometria import Circulo, Cuadrado

def main():
    while True:
        print("Escoga la figura a calcular: ")
        print("1. Circulo")
        print("2. Cuadrado")
        print("3. Salir ")
        opcion = input("Ingrese el numero de la opción: ")

        if opcion == "1":
            radio = float(input("Ingrese el radio del círculo: "))
            circulo = Circulo(radio)
            print("area del circulo:", circulo.calcular_area())
            print("perimetro del circulo:", circulo.calcular_perimetro())
        elif opcion == "2":
            lado = float(input("Ingrese el lado del cuadrado: "))
            cuadrado = Cuadrado(lado)
            print("Área del cuadrado:", cuadrado.calcular_area())
            print("Perímetro del cuadrado:", cuadrado.calcular_perimetro())
        elif opcion == "3":
            break
        else:
            print("Opcion no valida.")
main()
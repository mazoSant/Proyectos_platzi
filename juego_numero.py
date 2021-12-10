import random
def run():
    numero_aleatorio=random.randint(1,101)
    numero=int(input("""Este es un juego que se trata de adivinar un numero aleatorio del 1 al 100
    Por favor ingrese el numero que cree que es: """))
    while numero<numero_aleatorio:
        print("Es un numero mayor")
        numero=int(input("Por favor ingrese el numero que cree que es: "))
    while numero>numero_aleatorio:
        print("Es un numero menor")
        numero=int(input("Por favor ingrese el numero que cree que es: "))
    if numero==numero_aleatorio:
        print("Acertaste correctamente")
run()


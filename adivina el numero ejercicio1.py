from random import randint

def adivina_el_numero():
    numero_secreto =randint (0,100)
    intentos = 0

    print("¡Bienvenido al juego de adivina el número!")
    print("Estoy pensando en un número entre 1 y 100. ¿Puedes adivinar cuál es?")

    
    while True:
        intento =int(input("introduce tu número: "))
        intentos = intentos + 1
        distancia=abs(numero_secreto-intento)
        if intento < numero_secreto:
            if distancia<=10:
               print("demasiado bajo y estas cerca, intenta de nuevo")
            else:
                print("demasiado bajo y estas cerca, intenta de nuevo.")
        elif intento > numero_secreto:
            if distancia<=10:
                print("demasiado alto y estas cerca, intenta de nuevo")
            else: 
                print("demasiado alto y estas lejos, intenta de nuevo.")
        else:
            print(f"felicidades! adivinastes el numero en {intentos} intentos")
            break
adivina_el_numero() 
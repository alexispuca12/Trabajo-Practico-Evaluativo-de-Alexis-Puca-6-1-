#Carga el modulo "random" que permite el uso de generadores de aleatoriedad
import random

#Funcion para generar un carton con sus numeros del 1 al 75 separado en limites de 5 por 5 con un espacio en el medio denominado "free"
def generar_carton(): 
    carton = []
    columnas = ['B', 'I', 'N', 'G', 'O']
    limites = [(1, 15), (16, 30), (31, 45), (46, 60), (61, 75)]

    for i in range(5):
        numeros_columna = random.sample(range(limites[i][0], limites[i][1] + 1), 5)
        carton.append(numeros_columna)

    # Espacio libre en el centro
    carton[2][2] = 'FREE'
    return carton

#Funcion para imprimir los cartones con su correspondiente lugar en el carton
def imprimir_carton(carton): 
    columnas = ['B', 'I', 'N', 'G', 'O']
    print(' '.join(columnas))
    for fila in range(5):
        for columna in range(5):
            print(f'{carton[columna][fila]:^5}', end=' ')
        print()

#Funcion para "aleatorizar" los numeros a sortear
def sortear_numero(numeros_sorteados):
    numero = random.randint(1, 75)
    while numero in numeros_sorteados:
        numero = random.randint(1, 75)
    numeros_sorteados.add(numero)
    return numero


inicio = 1

#Repetir si el valor es 1 y abortar al aprecionar 1
while inicio == 1: 
    inicio = int(input("1.Empezar / 2.Abortar: "))
    if inicio == 1:
        numero_de_jugadores = int(input("Ingresar el numero de jugadores"))
        numero_cartones = numero_de_jugadores #Cambiar por persona en bingo
        cartones = [generar_carton() for _ in range(numero_cartones)]
        
        for i, carton in enumerate(cartones, start=1):
            print(f"\nCartón {i}:")
            imprimir_carton(carton)
            
        numeros_sorteados = set()
        print("\nSorteo de números:")
        for _ in range(75):  # Numeros del sorteo
            numero = sortear_numero(numeros_sorteados)
            print(f"Número sorteado: {numero}")
    else:
        break
"""
Imprimea a tabuada do 1 ao 10
"""
__version__ = "0.1.0"
__author__ = "Rodrigo"

#numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
numeros = list(range(1, 11))

for numero in numeros:
    print("Tabuada do:", numero)
    for outro_numero in numeros:
        resultado = numero * outro_numero
        print(str(numero) + " x " + str(outro_numero) + " = " + str(resultado))
    print("-" * 20)
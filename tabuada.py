"""
Imprimea a tabuada do 1 ao 10
"""
__version__ = "0.1.0"
__author__ = "Rodrigo"

# Definicao dos numeros a serem calculados
numeros = list(range(1, 11))

for numero in numeros:
    print("Tabuada do:", numero)
    for outro_numero in numeros:
        resultado = numero * outro_numero
        #print(str(numero) + " x " + str(outro_numero) + " = " + str(resultado))
        print(f"O valor de {numero} x {outro_numero} e {resultado}")
    print("-" * 20)
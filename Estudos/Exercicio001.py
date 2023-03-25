# Desenvolva um método que verifique se um número informado é:
# - Se é par ou ímpar
# - Se é multiplo de 2
# - Se é multiplo de 3
# - Se é multiplo de 5


def calculo():

    numero = int(input("Digite um numero: "))

    if numero % 2 == 0:
        print("Numero e par")

    else:
        print("Numero e impar")

    if numero % 2 == 0:
        print("Numero e multiplo de 2")

    if numero % 3 == 0:
        print("Numero e multiplo de 2")

    if numero % 5 == 0:
        print("Numero e multiplo de 2")


calculo()
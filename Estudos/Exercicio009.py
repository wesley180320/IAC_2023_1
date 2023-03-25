# Desafio 39 - Desenvolva um método que imprime todos os números que são divisíveis por
# 3 ou por 4 entre 0 e 120.


def cal():
    soma = 0

    for i in range(1,120):
        if i % 3 == 0 or i % 4 == 0:
            print(f"{i}")
cal()
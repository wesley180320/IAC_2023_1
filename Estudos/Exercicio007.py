# Desafio 37 - Utilizando uma lista de nomes de funcionários previamente carregada,
# desenvolva um método que solicite o salário de cada um, e armazene em uma lista
# paralela. Em seguida, calcule e exiba o salário reajustado, de acordo com a seguinte
# regra: Salário até R$ 300,00, reajuste de 50%; Salários maiores que R$ 300,00, reajuste de
# 30%.

nomes = ["Wesley","Wesley","Wesley","Wesley","Wesley","Wesley","Wesley"]
lista_salarios = []
def solicitar_salario():
    for i in nomes:
        salario = float(input(f"Digite seu salario {i}"))
        lista_salarios.append(salario)
    for i in range(len(lista_salarios)):
        reajustado = 0
        novo = lista_salarios
        if novo <= 300:
            reajustado = novo + (novo * 0.5)
        elif novo > 300:
            reajustado = novo + (novo * 0.5)

        print(f'O novo salirio do {nomes[i]} será de: {reajustado}')
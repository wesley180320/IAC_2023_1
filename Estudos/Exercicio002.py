# Desafio 32 - Crie uma lista com os nomes de uma turma de 20 alunos. Em seguida, elabore
# um método que solicite a idade de cada um, e armazene em uma lista paralela. Por fim,
# calcule a idade média da turma.


alunos = ["Wesley","Wesley","Wesley","Wesley","Wesley",]



def solicitarIdade():

    idades = []

    contador = 0
    soma = 0

    while contador < len(alunos):
        contador += 1
        idade = int(input("Digite sua idade: "))
        idades.append(idade)

    for i in idades:
        soma += i

    valor = soma / len(alunos)
    print(f'Media {valor}')

solicitarIdade()
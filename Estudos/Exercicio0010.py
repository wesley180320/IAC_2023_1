# Desafio 40 – Crie uma lista com os nomes de uma turma de 10 alunos. Em seguida,
# desenvolva um método que solicite a altura, e o código da matrícula de cada aluno,
# armazenando em listas paralelas. Por fim, mostre a altura e o código da matrícula, do
# aluno mais alto, e do aluno mais baixo.

turma = ["Wesley","Wesley","Wesley","Wesley","Wesley","Wesley","Wesley"]
alturas = []
matriculas = []

def solicitarAltura():

    for i in turma:
        altura = float(input(f"digite a altura do {i}"))
        alturas.append(altura)

        matricula = int(input(f'Digite a matricula do {i}'))
        matriculas.append(matricula)

    if max(alturas):
        inh = max(alturas)
        index = alturas.index(inh)
        print(f"O aluno mais alto tem {max(alturas)} matecula {matriculas[index]}")

    if min(alturas):
        inh = min(alturas)
        index = alturas.index(inh)
        print(f"O aluno mais alto tem {max(alturas)} matecula {matriculas[index]}")


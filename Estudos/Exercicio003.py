# Desafio 33 - Utilizando uma lista com nomes de pessoas, previamente carregada, elabore
# um método solicite a idade de cada um, armazene na mesma ordem em outra lista, e
# exiba quantas pessoas possuem mais de 18 anos. Seu código deverá ler a idade de 10
# pessoas.

nomes = ["Wesley","Wesley","Wesley","Wesley","Wesley",]
idades = []
maiorDe18 = 0

for nome in nomes:
    idade = int(input("Digite sua idade: "))
    idades.append(idade)
    if idade >=18:
        maiorDe18 +=1
print(f'Das{len(nomes)} pessoas, {maiorDe18} são maiores de 18 anos')
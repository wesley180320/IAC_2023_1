# Desafio 36 - Uma pessoa só pode votar em eleições brasileiras se ela for maior que 16 anos
# e for cidadã brasileira. Desenvolva um método que leia uma lista previamente carregada
# com o nome de 10 pessoas. Em seguida, solicite a idade da pessoa, e sua nacionalidade,
# armazenando em listas paralelas. Por fim, verifique quantas pessoas estão aptas a votar
# ou não, de acordo com os dados armazenados.

nomes = ["Wesley","Wesley","Wesley","Wesley","Wesley","Wesley","Wesley"]
idades = []
nacionalidades = []
total = 0

for i in nomes:
    idade = int(input(f'Informe a idade da pessoa: '))
    nacionalidade = input(f'Informe a nacionalidade da pessoa {i}')
    idades.append(idade)
    nacionalidades.append(nacionalidade)
    if nacionalidade == 'br' and idade > 16:
        total += 1

print(f'{nomes}')
print(f'{nacionalidades}')
print(f'{idades}')
print(f'Aptos para votacao: {total} pessoas')
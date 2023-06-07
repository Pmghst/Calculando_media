# Nota e média de um aluno

nota1 = float(input('A primeira nota é: '))
nota2 = float(input('A segunda nota é: '))
nota3 = float(input('A terceira nota é: '))
nota4 = float(input('A quarta nota é: '))

media = (nota1 + nota2 + nota3 + nota4) / 4

print(f' A media do aluno é:{media} ')

# Dicionário de média de um aluno

dados = {}
notas = []

dados['nome'] = input('Nome: ').strip().title()

for _ in range(1, 5):
  nota = float(input(f'Nota: '))
  notas.append(nota)

dados['notas'] = notas
dados['maior_nota'] = max(notas)
dados['menor_nota'] = min(notas)
dados['media'] = sum(notas) / len(notas)
dados['situacao'] = 'Aprovado' if dados['media'] >= 7 else 'Reprovado'

print(f'O aluno {dados["nome"]} foi {dados["situacao"]}')
print(f'Notas obtidas pelo aluno: {dados["notas"]}')

print(f'Média: {round(dados["media"], 2)}')
print(f'Maior nota: {dados["maior_nota"]}')
print(f'Menor nota: {dados["menor_nota"]}')
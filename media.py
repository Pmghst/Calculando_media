# Calculando_media

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

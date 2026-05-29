import random
#   matriz = [[1, 0, 0, 0, 0],
#             [0, 1, 0, 0, 0,],
#             [0, 0, 1, 0, 0,],
#             [0, 0, 0, 1, 0,],
#             [0, 0, 0, 0, 1]]
#   for L in matriz:
#       for C in L:
#           print(C, end=" ")
#       print()

#   linhas, colunas = 4, 4
#   print("A matriz 4x4 abaixo")
#   # Preenche com números inteiros aleatórios entre 1 e 100
#   matriz = [[random.randint(1, 100+1) for C in range(colunas)] for L in range(linhas)]
#   for L in matriz:
#          for C in L:
#              print(C, end=" ")
#          print()
#   print("\nAgora o maior e o menor valor")
#   maior_valor = max(valor for linha in matriz for valor in linha)
#   menor_valor = min(valor for linha in matriz for valor in linha)
#   
#   print(f"O maior valor da matriz é: {maior_valor}\nE o menor valor é: {menor_valor}")

linhas = 5
colunas = 4

matriz = []

for i in range(linhas):

    matricula = random.randint(1000, 10000)

    media_provas = random.randint(0, 10)

    media_trabalhos = random.randint(0, 10)

    nota_final = (media_provas + media_trabalhos) / 2

    matriz.append([
        matricula,
        media_provas,
        media_trabalhos,
        nota_final
    ])

print("MATRÍCULA|PROVAS|TRABALHOS|FINAL")

for linha in matriz:
    for valor in linha:
        print(valor, end="\t")
    print()

maior = matriz[0][3] 

for linha in matriz:
    if linha[3] > maior:
        maior = linha[3] 

print(f"\nA maior nota final é: {maior}")

matricula_aluno = matriz[0][0]
for linha in matriz:
    if linha[3] == maior:
        matricula_aluno = linha[0]
print(f"A matrícula do aluno com a maior nota final é: {matricula_aluno}")
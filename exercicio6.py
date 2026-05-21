import random
#while True:
#    numExercicio = int(input("escolha o numero do exercicio que deseja ver: "))
#    
#    if numExercicio == 1: 
#        A = [1, 0, 5, -2, -5, 7]
#        soma = A[0] + A[1] + A[5] 
#        print(f"o valor da soma das posições 0, 1 e 5 do vetor A: {soma}")
#        A[4] = 100
#        for i in range(len(A)):
#            print(f"Print da posição {i}: {A[i]}")
#
#    elif numExercicio == 2:
#        nums = [random.randint(1, 100) for i in range(6)]
#        print(nums)
#
#    elif numExercicio == 3:
#       primeiroConjunto = [random.randint(1, 20) for i in range(10)]
#       segundoConjunto = [i ** 2 for i in primeiroConjunto]
#       print(f"valores do primeiro array: {primeiroConjunto}")
#       print(f"valores do segundo array: {segundoConjunto}")
#
#    elif numExercicio == 4:
#       primeiroConjunto = [random.randint(1, 20) for i in range(8)]
#       leituraX = random.choice(primeiroConjunto)
#       leituraY = random.choice(primeiroConjunto)
#       soma = leituraX + leituraY
#       print(soma) 
#
#    eliif numExercicio == 5:  
#       array10pos = [random.randint(1, 20) for i in range(10)]        
#       contador = 0 
#       for i in range(len(array10pos)):
#           if array10pos[i] % 2 == 0:
#               print(f"Valor par do array: {array10pos[i]}")
#               contador += 1
#           else:
#               pass
#       print(f"A quantidade de números pares contidos nesse array: {contador}")
#
#     elif numExercicio == 6:
#       vetorValores = []
#       for i in range(10):
#           entradaUsuario = int(input("Insira aqui o valor para adicionar ao vetor: "))
#           vetorValores.append(entradaUsuario)
#       maiorValor = max(vetorValores)
#       menorValor = min(vetorValores)
#
#     elif numExercicio == 7:
#       print(f"O maior valor do vetor é: {maiorValor}\nO menor valor do vetor é: {menorValor}")
#       vetor = [random.randint(1, 100) for i in range(10)]
#       print(f"{vetor}")
#       
#       maior = max(vetor)
#       posicaoMaior = vetor.index(maior)
#       
#       print(f"O maior numero deste vetor é: {maior}")
#       print(f"E sua localização respectiva dentro deste vetor é: {posicaoMaior}")
#
#    elif numExercicio == 8:
#       vetorNota = [random.randint(4, 10) for i in range(15)]
#       coloquei com valor de nota minima de 4 por dó dos alunos que tiram 1 ponto
#       print(f"Todos os valores do vetor: {vetorNota}")
#
#       somaVetor = sum(vetorNota)
#       print(f"O valor da soma de todos estes valores: {somaVetor}")
#
#       mediaVetor = somaVetor / len(vetorNota)
#       print(f"E agora o valor da média do vetor dependendo de seu tamanho: {mediaVetor}")
#
#    elif numExercicio == 9:
#       vetorNumeros = [random.randint(-20, 20) for i in range(10)]
#       vetorPositivo = []
#       contadorNegativo = 0
#       for num in range(len(vetorNumeros)):
#           if vetorNumeros[num] >= 0:
#               vetorPositivo.append(vetorNumeros[num])
#           else:
#               contadorNegativo += 1
#       somaPositivo = sum(vetorPositivo)
#
#       print(f"Vetor de numeros totais: {vetorNumeros}")
#       print(f"Vetor de numeros positivos: {vetorPositivo}")
#       print(f"A soma de todos os numeros positivos do array é: {somaPositivo}")
#       print(f"E o número de números negativos dentro do array é: {contadorNegativo}")

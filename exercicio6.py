import random
#while True:
#    numExercicio = int(input("escolha o numero do exercicio que deseja ver: "))
#    
#    if numExercicio == 1: 
#        A = [1, 0, 5, -2, -5, 7]
#        soma = A[0] + A[1] + A[5] 
#    
#        print(f"o valor da soma das posições 0, 1 e 5 do vetor A: {soma}")
#    
#        A[4] = 100
#        for i in range(len(A)):
#            print(f"Print da posição {i}: {A[i]}")
#    if numExercicio == 2:
#        
#        nums = [random.randint(1, 100) for i in range(6)]
#        print(nums)
#     if numExercicio == 3:
#    
#       primeiroConjunto = [random.randint(1, 20) for i in range(10)]
#       segundoConjunto = [i ** 2 for i in primeiroConjunto]
#       print(f"valores do primeiro array: {primeiroConjunto}")
#       print(f"valores do segundo array: {segundoConjunto}")
#
#     if numExercicio == 4:
#      
#       primeiroConjunto = [random.randint(1, 20) for i in range(8)]
#       leituraX = random.choice(primeiroConjunto)
#       leituraY = random.choice(primeiroConjunto)
#       soma = leituraX + leituraY
#       print(soma) 
#
#     if numExercicio == 5:  
#       array10pos = [random.randint(1, 20) for i in range(10)]        
#       contador = 0 
#       for i in range(len(array10pos)):
#           if array10pos[i] % 2 == 0:
#               print(f"Valor par do array: {array10pos[i]}")
#               contador += 1
#           else:
#               pass
#       print(f"A quantidade de números pares contidos nesse array: {contador}")
#     if numExercicio == 6:
#       vetorValores = []
#       for i in range(10):
#           entradaUsuario = int(input("Insira aqui o valor para adicionar ao vetor: "))
#           vetorValores.append(entradaUsuario)
#       maiorValor = max(vetorValores)
#       menorValor = min(vetorValores)
#       
#       print(f"O maior valor do vetor é: {maiorValor}\nO menor valor do vetor é: {menorValor}")

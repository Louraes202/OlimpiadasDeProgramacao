N = int(input())
A = input().split()
for i in range(len(A)): # conversão de todos os elementos da lista para inteiro
    A[i] = int(A[i])
contador = 0
for i in range(N):
    if i == 0: # o primeiro elemento vê sempre a bilheteira, independentemente da altura
        contador = contador + 1
    else: # verificação das alturas
        k = i + 1
        if max(A[:k]) == A[i] and A[i] not in A[:k-1]:
            contador = contador + 1

print(contador)

# 7 
# 10 120 30 135 11 2 186
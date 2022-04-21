N, Ni, M, Mi = int(input()), list(map(int, input().split())), int(input()), list(map(int, input().split()))
pares = 0
contador_1 = 0 # nº de pares em A
contador_2 = 0 # nº de impares em A
contador_3 = 0 # nº de pares em B
contador_4 = 0 # nº de impares em B

for n in Ni:
    if n % 2 == 0:
        contador_1 += 1
    else:
        contador_2 += 1

for m in Mi:
    if m % 2 == 0:
        contador_3 += 1
    else:
        contador_4 += 1

pares_totais = (contador_1 * contador_3) + (contador_4 * contador_2)
impares_totais = (contador_1 * contador_4) + (contador_2 * contador_3)
      
print(pares_totais, impares_totais)
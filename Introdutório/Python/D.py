N, K = map(int, input().split())
arvores = []

for i in range(N):
    arvores.append([])
    linha = input()
    for k in linha:
        arvores[i].append(k)

contador = 0
possivel = False
for i in range(len(arvores)):
    contador = 0
    for k in arvores[i]:
        if k != "#":
            contador += 1
            if contador >= K:
                possivel = True
        elif k == "#":
            contador = 0


resposta = 1 if possivel == True else 0

print(resposta)
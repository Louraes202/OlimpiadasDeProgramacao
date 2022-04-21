N, M = map(int, input().split())
cromospedro = map(int, input().split())
cromos = []
Ntem = 0
tem = 0
for i in range(1, N+1):
    cromos.append(i)
for cromo in cromospedro:
    if cromo in cromos and cromo not in cromospedro[:cromospedro.index(cromo)]:
        tem += 1

Ntem = N - tem
print(Ntem)

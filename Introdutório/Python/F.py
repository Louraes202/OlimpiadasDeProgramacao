
# N, Ni, M, Mi = int(input()), map(int, input().split()), int(input()), map(int, input().split())
N, Ni, M, Mi = int(input()), list(map(int, input().split())), int(input()), list(map(int, input().split()))

pairsN = [(Ni[i],Ni[j]) for i in range(len(Ni)) for j in range(i+1, len(Ni))]
pairsM = [(Ni[i],Ni[j]) for i in range(len(Ni)) for j in range(i+1, len(Ni))]
pairs = pairsN + pairsM
somapares, somaimpares = 0, 0

print(pairsM)

# for l in pairs:





print(somapares, somaimpares)
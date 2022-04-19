A, L, C = map(int, input().split())
Area = A * L * C 
if Area >= 50 and A >= 3:
    print(1)
else:
    print(0)
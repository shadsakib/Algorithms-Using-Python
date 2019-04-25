n = int(input())

p = 1
for i in range(365, 365 - n, -1):
    print(i)
    p *= i / 365

print(100 - int(p * 100))
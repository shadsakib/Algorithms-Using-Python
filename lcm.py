from math import gcd

n = int(input())
l = []
for i in input().split():
    l.append(int(i))

lcm = l[0]
for i in l[1:]:
    lcm = lcm * i // gcd(lcm, i)

print(lcm)
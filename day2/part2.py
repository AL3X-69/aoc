import math

r = 0

def divisors(n):
    l = []
    for i in range(1, math.ceil(n / 2) + 1):
        if n % i == 0: 
            l.append(i)
    return l

def slices_equals(s, n):
    sub = s[:n]
    for j in range(1, int(len(s) / n)):
        if s[j * n : (j + 1) * n] != sub:
            return False
    return True

with open("input.txt") as f:
   ids = f.read().split(',')
   for id in ids:
       start, end = id.split("-")
       for i in range(int(start), int(end) + 1):
            s = str(i)
            l = len(s)
            if l < 2:
                continue
            for d in divisors(l):
                if slices_equals(s, d):
                    r += i
                    break

print(r)

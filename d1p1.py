pos = 50
r = 0

with open("d1.txt") as f:
    for s in f.read().splitlines():
        left = s[0] == 'L'
        i = (-1 if left else 1) * int(s[1:])
        pos = ((pos + i) % 100 + 100) % 100
        if pos == 0:
            r += 1
        print(s, pos)

print(r)

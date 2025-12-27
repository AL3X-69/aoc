r = 0

with open("input.txt") as f:
    for s in f.read().splitlines():
        a = 0
        b = 0
        _i = 0
        for i in range(len(s) - 1):
            n = int(s[i])
            if n > a:
                a = n
                _i = i
        for i in range(_i + 1, len(s)):
            n = int(s[i])
            if n > b:
                b = n
        print(s, a, b)
        r += int(f"{a}{b}")

print(r)

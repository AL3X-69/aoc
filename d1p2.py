pos = 50
r = 0

with open("d1.txt") as f:
    for s in f.read().splitlines():
        left = s[0] == 'L'
        delta = (-1 if left else 1) * int(s[1:])
        new_pos = ((pos + delta) % 100 + 100) % 100
        r += abs(delta) // 100
        if pos != 0 and ((left and (new_pos > pos or new_pos == 0)) or (not left and new_pos < pos)):
            r += 1
        pos = new_pos
        print(f"command: {s}, delta: {delta}, pos: {pos}, r: {r}")

print(r)

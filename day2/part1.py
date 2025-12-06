r = 0

with open("input.txt") as f:
   ids = f.read().split(',')
   for id in ids:
       start, end = id.split("-")
       for i in range(int(start), int(end) + 1):
            s = str(i)
            l = len(s)
            if l % 2 == 0 and s[int(l / 2):] == s[:int(l / 2)]:
                r += i

print(r)

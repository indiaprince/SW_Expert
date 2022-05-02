s = list(input())
ls = []
for ch in s:
    ls.append(ord(ch)-ord('A')+1)

for num in ls: print(num, end = ' ')
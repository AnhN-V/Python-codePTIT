n = input()
i = len(n)-3
while i > 0:
    n = n[:i] + ',' + n[i:]
    i -= 3
print(n)
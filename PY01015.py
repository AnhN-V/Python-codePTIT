def check(s):
    n = len(s)
    for i in range(1, n):
        if s[i-1] > s[i]:
            return False
    return True
for t in range(int(input())):
    s = input()
    if check(s) == True:
        print("YES")
    else:
        print("NO")
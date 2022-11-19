def gcd(a, b):
    if b == 0:
        return a
    if a % b == 0:
        return b
    return gcd(b, a % b)
for t in range(int(input())):
    n = int(input())
    str1 = str(n)[::-1]
    a = int(str1)
    if gcd(n, a) == 1:
        print("YES")
    else:
        print("NO")

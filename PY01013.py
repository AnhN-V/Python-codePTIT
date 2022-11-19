def GCD(a, b):
    if a == 0:
        return b
    return GCD(b%a, a)
def isPrime(n):
    flag = 1
    if n < 2:
        flag = 0
        return flag
    for p in range(2, n):
        if n % p == 0:
            flag = 0
            break
    return flag
def sumdigit(n):
    sum = 0
    for i in n:
        sum += int(i)
    return sum

for t in range(int(input())):
    a,b = [int (x) for x in input().split()]
    if isPrime(sumdigit(str(GCD(a, b)))) == 1:
        print("YES")
    else:
        print("NO")
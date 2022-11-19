def isPrime(n):
    flag = 1;
    if (n < 2):
        flag = 0
        return flag
    for p in range(2, n):
        if n % p == 0:
            flag = 0
            break  
    return flag

def GCD(a, b):
    if a == 0:
        return b
    return GCD(b%a, a)

for t in range(int(input())):
    n = int(input())
    temp = 0
    for i in range (1, n):
        if GCD(i, n) == 1:
            temp += 1
    if isPrime(temp) == 1:
        print("YES")
    else:
        print("NO")
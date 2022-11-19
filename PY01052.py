def isPrime(n):
    if n < 2:
        return 0
    for p in range(2, n):
        if n % p == 0:
            return 0
    return 1
for test in range(int(input())):
    n = input()
    sum = 0
    for i in range(len(n)):
        sum += int(n[i])
    if isPrime(sum) == 1:
        print("YES")
    else:
        print("NO")

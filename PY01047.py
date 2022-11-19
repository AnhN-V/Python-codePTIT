def isPrime(n):
    if n < 2:
        return 0
    else:
        for i in range(2, n):
            if n % i == 0:
                return 0
    return 1
for test in range(int(input())):
    s = input()
    tach = s[(len(s)-4):len(s)]
    if isPrime(int(tach)) == 1:
        print("YES")
    else:
        print("NO")
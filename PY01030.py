def GCD(a, b):
    if a == 0:
        return b
    return GCD(b%a, a)
n, k = [int(x) for x in input().split()]
count = 0
for i in range(10 ** (k-1), 10 ** k):
    if GCD(i, n) == 1 and len(str(i)) == k:
        if count == 9:
            count = 0;
            print(i,"\n")
        else:
            count += 1
            print(i, end =" ")


def isThuannghich(str):
    str1 = str[::-1]
    if int(str) != int(str1):
        return 0
    return 1

for t in range(int(input())):
    n = input()
    sum = 0
    for i in range(len(n)):
        sum += int(n[i])
    if len(str(sum)) > 1 and isThuannghich(str(sum)) == 1:
        print("YES")
    else:
        print("NO")


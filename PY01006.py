for t in range(int(input())):
    n = input()
    result = "YES"
    for i in n:
        if i != '4' and i != '7':   result = "NO"
    print(result)
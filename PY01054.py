for t in range(int(input())):
    n = input()
    tich = 1
    for i in range(len(n)):
        if int(n[i]) != 0:
            tich *= int(n[i])
    print(tich)
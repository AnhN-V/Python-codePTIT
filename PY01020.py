for t in range(int(input())):
    n = input()
    if n[len(n)-1] == '6' and n[len(n)-2] == '8':
        print("YES")
    else:
        print("NO")

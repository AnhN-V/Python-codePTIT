for t in range(int(input())):
    s = input()
    n = len(s)
    dem = 1
    s += 'a'
    for i in range(0, n):
        if s[i] == s[i+1]:
            dem += 1
        else:
            print(f"{dem}{s[i]}", end ="")
            dem = 1
    print()

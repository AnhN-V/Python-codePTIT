def isperfectnum(n):
    str1 = str(n)
    str2 = str1[::-1]
    if str1.split() == ['0', '2', '4', '6', '8']:
        if str1 == str2:
            return True
        else:
            return False


for t in range(int(input())):
    n = int(input())
    str1 = str(n)
    if len(str1) % 2 == 0:
        isperfectnum(n)
        print(str1)

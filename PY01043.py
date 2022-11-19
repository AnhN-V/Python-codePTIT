def checkTN(n):
    str1 = n
    str2 = str1[::-1];
    if (str1 == str2):
        return True;
    return False
def checksum(n):
    if len(n) % 2 == 0:
        return True
    return False
def checknumber(n):
    for i in n:
        if int(i) % 2 != 0:
            return False
    return True
for i in range (int(input())):
    n = input()
    for j in range(22, int(n)):
        if checkTN(str(j)) == True and  checknumber(str(j)) == True and checksum(str(j)) == True:
            print(j, end=" ")
    print()

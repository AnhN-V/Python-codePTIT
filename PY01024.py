def totalDigitsOfNumber(b):
    total = 0
    while b > 0:
        total = total + b % 10
        b = int(b / 10)
    return total


for t in range(int(input())):
    n = input()
    b = int(n)
    for i in range(len(n)-1):
        if ( int( n[i+1] ) - int( n[i] ) == 2) and totalDigitsOfNumber(b) % 10 == 0:
            print ("YES")
            break
        else:
            print ("NO")
            break

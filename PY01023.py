
import math

for t in range(int(input())):
    n = int(input())
    print(1, end =' ')
    for i in range(2, int(math.sqrt(n))):
        temp = 0
        if n % i == 0:
            while(n % i == 0):
                temp += 1
                n /= i
            print("* " + str(i) + "^" + str(temp), end = " ")
    if n > 1:
        print("* " + str(int(n)) + "^1" , end=" ")
    print()
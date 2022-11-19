import math
for t in range(int(input())):
    n,x,m = [float(i) for i in input().split()]
    year = math.log(m/n, 1+x/100)
    if year == int(year):
        print(year)
    else:
        print(int(year)+1)
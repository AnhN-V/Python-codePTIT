n=input()
count4 = 0
count7 = 0
for i in n:
    if i == '4':
        count4 += 1
    elif i == '7':
        count7 += 1
if count4 + count7 == 4 or count4 + count7 ==7:
    print("YES")
else:
    print("NO")
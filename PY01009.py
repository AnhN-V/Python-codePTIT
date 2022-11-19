s = input()
isUpper = 0;
isLower = 0;
for character in s:
    if character >= 'a' and character <= 'z':
        isLower += 1
    if character >= 'A' and character <= 'Z':
        isUpper += 1
if isLower >= isUpper:
    print(s.lower())
else:
    print(s.upper())

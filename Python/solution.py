
num = 153
string_num = str(num)
digits = []
for i in range(len(string_num)):
    digit = int(string_num[i])
    print(type(digit))
    digits.append(digit)
print(digits)
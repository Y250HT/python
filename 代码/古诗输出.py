n = int(input())
str1 = input()
if len(str1)%n != 0:
    str1 = str1 + (n - (len(str1)%n)) * ' '
for i in range(n):
    print(str1[i::n][::-1])
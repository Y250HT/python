str1=input()
before = '0 1 3 4 5 6 7'
after = 'o i e a s g t'
table = ''.maketrans(before, after)
print(str1.translate(table))
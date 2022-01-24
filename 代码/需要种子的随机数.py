import random
str1 = 'ABCDEFGHIJ0123456789'
for j in range (6):
    random.seed(int(input()))
    for i in range(6):
        print(random.choice(str1),end='')
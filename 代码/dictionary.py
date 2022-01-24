fruits = {"apple":
10
,"mango":
12
,"durian":
20
,"banana":
5
}
for key,value in fruits.items():
    if (value == max(fruits.values())):
        m=key
        print('{}:{}'.format(m,fruits[m]))
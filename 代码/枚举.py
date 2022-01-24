print(list(enumerate('abcd')))
print(list(enumerate(['Python','Greate'])))
print(list(enumerate({'a':97,'b':98,'c':99}.items())))
for index,value in enumerate(range(10,15)):
    print((index,value),end='')
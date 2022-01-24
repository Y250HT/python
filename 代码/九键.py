keyboard=[['0',' '],['1', ',','.','?','!'],['2','A','B','C' ], ['3','D','E','F'],['4','G','H','I'] ,\
['5','J','K','L'], ['6','M','N','O'],['7','P','Q','R','S' ],\
['8','T','U','V'],['9','W','X','Y','Z']]
a=input()
b=[]
for i in a.split( ):
    x = len(i) - 1
    b.append(keyboard[int(i[0])][x])
print(b)
c = ''.join(b)
print(c)
n =int(input())
k= int(input())
ls = list(range(1,n+1))
while len(ls) > k-1:
    ls = ls[k:] + ls[:k-1]
if (k < 2 or n < k):
    print('Data Error!')
else:
    print(ls)

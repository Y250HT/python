list=[]
def defactor(N):
    t=int(N)
    if(t%2==0):
        list.append(2)
        t/=2
        if(t<2):
            return list
        else:
            return defactor(t)
    else:
        for i in range(t+1):
            if(i>2):
                if t % i ==0:
                    list.append(i)
                    t=t/i
                    if(t<3):
                        return list
                    else:
                        return defactor(t)
N = eval(input())
print(defactor(N))
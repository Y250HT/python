for i in input():
    if 65<=ord(i)<=90:
        w = ord(i)+5
        if w>90:
            w=w-25
        print(chr(w),end='')
    elif 97<=ord(i)<=122:
        w = ord(i)+3
        if w > 122:
            w=w-26
        print(chr(w),end='')
    else:
        print(i,end='')

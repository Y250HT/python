def search(search):
    dic = {}
    search=1
    print("请输入题号")
    with open ('data.csv') as f:
        for line in f:
            name = line[:19]
            answer = line[20:21]
            dic[name] = answer
        while(search):
            search = input()
            for keys in dic:
                if(search == keys):
                    print(dic[search])
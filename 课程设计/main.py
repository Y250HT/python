import requests
import re
import csv
import time
import search
import download
import move

#from bs4 import BeautifulSoup
#from lxml import etree

password = eval(input("请输入第一位同学的学号:"))   # 202003010001
all = eval(input("请输入最后一位同学的学号:"))    # 202003010121
zero = password-1   # 202003010000
list = [' ']
coursID = eval(input("请输入coursID:"))    # 59
value = input("请输入历史考试value，如有多次请以空格分割:").split()  #  1272, 1273, 1258, 1257, 1228, 1227, 1201
for i in value:
    list.append(i)
scale = all - password
start=time.perf_counter()
while(password != all):
    k = password - zero
    m = k
    a = '*' * m
    b = '.' * (scale - m)
    c = (m / scale) * 100
    dur = time.perf_counter() - start

    session = requests.session()
    data = {
        "IndexStyle": "1",
        "stid": f"{password}",
        "pwd": f"{password}"
    }
    #print(password)
    for testid in list:
        i = testid
        if(i != ' '):
            url = "http://10.185.255.107/login/loginproc.jsp"
            session.post(url, data=data)
            session.get(f'http://10.185.255.107/courselist.jsp?courseID={coursID}')  #59
            params = {
                "examID": f"{i}"    #f"{b_id}|{cid}"
            }
            resp = session.get(url = 'http://10.185.255.107/exam/index_history.jsp', params=params)
            page_content = resp.text

            obj = re.compile(r'<tr>.*?<td>.*?<p><img src="/userfiles/image/2020/'
                             r'(?P<name>.*?).png.*?<strong>.*?正确答案: (?P<value>.*?)</span>', re.S)

            result = obj.finditer(page_content)
            f = open("data.csv", mode="a", newline='')   # a就是循环写入！！！
            csvwriter = csv.writer(f)
            for it in result:
                dic = it.groupdict()
                csvwriter.writerow(dic.values())
            f.close()
            ob = re.compile(r'<tr>.*?<p>.*?<img src="(?P<page_main>.*?)"', re.S)
            resu = ob.finditer(page_content)
            for i in resu:
                src = 'http://10.185.255.107' + i.group("page_main")
                img_name = src.split("/")[-1]
                download.download(src)
    print("\r{:^3.0f}%[{}->{}]{:.2f}s".format(c, a, b, dur), end='')
    password += 1
move.move()
print("题目下载完成，默认以data.csv命名")
print("是否使用搜题程序,YES/NO")
ans=input()
if(ans=='YES'):
    while(True):
        m=eval(input())
        search.search(m)


#以下为尝试
#main_page = BeautifulSoup(resp.text, "html.parser")
#alist = main_page.find("div", class_="col-9").find_all("img")
#print(alist)
#for a in alist:
    #print(a.get('src'))

#html = etree.HTML(resp.text)
#divs = html.xpath("/html/body/div[1]/div[2]/table/tbody/tr[2]/td/form/div/div[1]/p/text()")
#print(divs)
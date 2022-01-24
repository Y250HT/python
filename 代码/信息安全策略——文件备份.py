import os
def file_backups(file_name, path):
    # 备份的文件名
    file_back = file_name.split('\\')[-1]
    # 判断用户输入的内容是文件还是文件夹
    if os.path.isdir(file_name) is not True:
        with open(file_name, mode='r') as file_data:
            # 创建新文件 , 以只读的方式打开
            new_path = path + '/' + file_back
            with open(new_path, 'w') as file_back:
                # 逐行复制源文件内容到新文件中
                for line_content in file_data.readlines():
                    file_back.write(line_content)

# 判断是目录还是文件
def judge(back_path, file_path):
    if os.path.isdir(file_path) is True:
        # 遍历当前目录下的文件
        file_li = os.listdir(file_path)
        for i in file_li:
            # 拼接文件名称
            new_file = file_path + '\\' + i
            file_backups(new_file, back_path)
    else:
        # 是文件
        if os.path.exists((file_path)):
            file_backups(file_path, back_path)
        else:
            print("备份的文件不存在!")
            exit()

# 备份目录
def backups_catalog():
    # 指定备份的目录
    back_path = input("请输入备份的目录：\n")
    file_path = input("请输入备份的文件:\n")
    # 指定目录不存在
    if os.path.exists(back_path) is False:
        os.mkdir(back_path)
        judge(back_path, file_path)
        print('备份成功!')
    # 指定目录存在
    else:
        judge(back_path, file_path)
        print('备份成功!')

if __name__ == '__main__':
    backups_catalog()

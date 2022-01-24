"""
好友管理程序
增加
删除
备注
展示
分组
数据存储结构：['王五', '张三', '赵柳', {'家人': ['李四','刘备']},{'同事': ['李龙','张飞']}]
"""
"""
好友管理程序
增加
删除
备注
展示
分组
数据存储结构：['王五', '张三', '赵柳', {'家人': ['李四','刘备']},{'同事': ['李龙','张飞']}]
"""


class Friend:
    def __init__(self):
        self.friend_li = []

    def welcome(self):
        print("* * 欢迎使用好友管理系统 * * ")
        print("1：添加好友")
        print("2：删除好友")
        print("3：备注好友")
        print("4：展示好友")
        print("5：好友分组")
        print("6：退出")
        while True:
            option = input("请选择功能\n")
            # 添加好友
            if option == '1':
                self.add_friend()
            # 删除好友
            elif option == '2':
                self.del_friend()
            # 备注好友
            elif option == '3':
                self.modify_friend()
            # 展示好友
            elif option == '4':
                self.show_friend()
            # 分组好友
            elif option == '5':
                self.group_friend()
            elif option == '6':
                break

    #  添加好友
    def add_friend(self):
        add_friend = input("请输入要添加的好友：")
        self.friend_li.append(add_friend)
        print('好友添加成功')

    # 获取所有好友
    def get_all_friends(self):
        new_li = []
        for friend_li_elem in self.friend_li:
            # 判断元素类型
            if type(friend_li_elem) == dict:
                # 遍历字典
                [new_li.append(dict_elem_name) for dict_elem in friend_li_elem.values()
                 for dict_elem_name in dict_elem]
            else:
                new_li.append(friend_li_elem)
        return new_li

    # 获取所有分组及其好友
    def get_all_groups(self):
        groups = []
        for friend_li_elem in self.friend_li:
            if type(friend_li_elem) == dict:
                groups.append(friend_li_elem)
        return groups

    # 获取所有分组名称
    def get_all_groups_name(self):
        groups_name = []
        for dict_elem in self.get_all_groups():
            for j in dict_elem:
                groups_name.append(j)
        return groups_name

    #  删除好友（在分组中，不在分组中）
    def del_friend(self):
        if len(self.friend_li) != 0:
            del_name = input("请输入删除好友姓名：")
            # 删除的好友未分组
            if del_name in self.friend_li:
                self.friend_li.remove(del_name)
                print('删除成功')
            else:
                # 删除的好友在分组内
                if del_name in self.get_all_friends():
                    for group_data in self.get_all_groups():
                        for group_friend_li in group_data.values():
                            if del_name in group_friend_li:
                                group_friend_li.remove(del_name)
                                continue
                            print('删除成功')
        else:
            print('好友列表为空')

    #  备注好友
    def modify_friend(self):
        friends = self.get_all_friends()
        if len(friends) == 0:
            print('好友列表为空')
        else:
            before_name = input("请输入要修改的好友姓名：")
            after_name = input("请输入修改后的好友姓名：")
            if before_name in self.friend_li:
                friend_index = self.friend_li.index(before_name)
                self.friend_li[friend_index] = after_name
                print("备注成功")
            elif before_name not in self.friend_li:
                for friend_li_elem in self.friend_li:
                    if type(friend_li_elem) == dict:
                        for dict_elem in friend_li_elem.values():
                            if before_name in dict_elem:
                                modify_index = dict_elem.index(before_name)
                                dict_elem[modify_index] = after_name
                print('备注成功')
            # print('备注成功')

    #  展示好友 （选择展示所有好友，或分组）
    def show_friend(self):
        print("1.展示所有好友")
        print("2.展示分组名称")
        option_show = input("请输入选项：")
        groups = self.get_all_groups()
        friends = self.get_all_friends()
        if option_show == '1':
            # 展示所有好友
            if len(friends) == 0:
                print("当前没有任何好友")
            else:
                print(friends)
        elif option_show == '2':
            if len(friends) == 0:
                print("当前没有任何好友")
            else:
                if len(groups) == 0:
                    print("当前没有任何分组")
                else:
                    # 展示分组
                    for dict_groups in groups:
                        for group_name in dict_groups:
                            print(group_name)
                    is_show_group = input("是否展示组内好友：y/n\n")
                    if is_show_group == 'y':
                        show_group_name = input("请输入查看的分组名称")
                        for i in groups:
                            if show_group_name in i:
                                show_index = groups.index(i)
                                print(groups[show_index][show_group_name])

    #  分组好友
    def group_friend(self):
        create_group = input("是否创建新的分组y/n\n")
        friends = self.get_all_friends()
        if create_group == 'y':
            if len(friends) == 0:
                print("当前没有任何好友")
            else:
                # 请创建分组
                group_name = input("请输入分组名称：\n")
                group_name_li = list()
                # 展示当前好友
                print(friends)
                # 移动联系人到哪个组
                friend_name = input("请输入好友名称：\n")
                if friend_name in friends:
                    all_friend = []
                    for friend_li_elem in self.friend_li:
                        if type(friend_li_elem) == dict:
                            [all_friend.append(dict_friends) for dict_elem in friend_li_elem.values()
                             for dict_friends in dict_elem]
                        else:
                            all_friend.append(friend_li_elem)
                    if friend_name in all_friend:
                        group_name_li.append(friend_name)
                        self.friend_li.remove(friend_name)
                        # 构建字典： {组名称：分组列表}
                        friend_dict = dict()
                        friend_dict[group_name] = group_name_li
                        self.friend_li.append(friend_dict)
                    else:
                        print("请输入正确的名称")
                else:
                    print('请输入正确好友名称')
        elif create_group == 'n':
            # 显示当前的分组，将用户添加到指定的组
            current_groups = self.get_all_groups()
            print('当前分组:')
            for current_group in current_groups:
                for group_name in current_group:
                    print(group_name)
            add_group = input('请选择添加的组:\n')
            # 判断用户输入的组名是否在当前已存在的分组名中
            if add_group in self.get_all_groups_name():
                # 添加好友到指定的组
                add_name = input('请选择添加的好友名称：\n')
                # 判断用户输入的好友是否存在好友列表中
                if add_name in self.friend_li:
                    # 判断用户是否在其他组中
                    if add_name not in current_groups:
                        # 将好友添加到指定的组内
                        add_group_index = self.get_all_groups_name().index(add_group)
                        current_groups[add_group_index][add_group].append(add_name)
                else:
                    print('该好友已在其他分组中')
            else:
                print('请输入正确的组名')


if __name__ == '__main__':
    friend = Friend()
    friend.welcome()

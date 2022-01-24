# 饮品信息
def all_goods():
    goods = {"可口可乐": 2.5, "百事可乐": 2.5, "冰红茶": 3, "脉动": 3.5, "果缤纷": 3,
             "绿茶": 3, "茉莉花茶": 3, "尖叫": 2.5}
    return goods


# 展示饮品信息
def show_goods():
    for x, y in all_goods().items():
        print(x, ":", str(y) + "元")


# 计算总额
def total(goods_dict):
    count = 0
    for name, num in goods_dict.items():
        total_money = all_goods()[name] * num
        # 总金额
        count += total_money
    print("需要支付金额：", count, "元")


def main():
    goods_dict = {}
    print("饮 品 自 动 售 货 机")
    show_goods()
    # 循环选购的商品
    print("输入q完成购买")
    while True:
        goods_name = input("请输入购物的商品：")
        if goods_name == 'q':
            break
        if goods_name in [g_name for g_name in  all_goods().keys()]:
            goods_num = input("请输入购物数量：")
            if goods_num.isdigit():
                goods_dict[goods_name] = float(goods_num)
            else:
                print('商品数量不合法')
        else:
            print('请输入正确的商品名称')
    total(goods_dict)


if __name__ == '__main__':
    main()

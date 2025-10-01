"""
现有商品字典 prd_info 包含商品名和价格
商品： 屠龙刀 倚天剑 辟邪剑谱 葵花宝典 九阳神功 九阴神功
价格： 100 100 10 10 200 300
编号： 101 102 103 104 105 106
1. 用户按1键进行购买，用户按2键进行结算
2. 如果用户按1键进入购买环节，先列出所有商品
格式： 编号：101，商品：屠龙刀，价格：100
2.1 用户输入商品编号购买商品：
2.1.1 如果商品编号不存在，则让用户重新输入编号
2.1.2 如果商品编号存在，则让用户输入购买数量
2.1.2.1 用户输入购买数量后，添加到购物车中(只能添加商品编号和数量)
3. 如果用户按2键则结算购物车，先列出购物车中的商品
格式： 商品：屠龙刀，价格：100 数量：10
可以显示当前购物车的总价，也可以不显示
输入金额：
总价 ：1000元 请输入交易金额
如果支付金额等于总价，打印：欢迎下次光临
如果支付金额大于总价，打印：找零xxx，欢迎下次光临
如果支付金额小于总价，打印：还差xxx
"""

prd_info = {
    101: {"name": "屠龙到", "price": 100},
    102: {"name": "倚天建", "price": 100},
    103: {"name": "辟邪简朴", "price": 10},
    104: {"name": "葵花宝典", "price":10},
    105: {"name": "九阳神功", "price": 200},
    106: {"name": "飞龙在天", "price": 300}
}

list_cart = []

while True:
    item = input("请输入服务编号： 按1键购买， 按2键结算， 按3键退出系统")
    if item == "1":
                        # 展示商品
        for kye, value in prd_info.items():
            print(f"编号: {kye}, 商品:{value['name']}, 价格: {value['price']}")
        # 输入商品编号
        while True:
            pid = int(input("请输入商品编号"))

            if pid in prd_info:
                break
            else:
                print("商品不存在～")
        count = int(input("请输入购买商品的数量"))

        # 添加到购物车
        list_cart.append({'pid': pid, "count": count})
        print(list_cart)

    elif item == "2":
        total = 0
        for item in list_cart:
            prd_item = prd_info[item["pid"]]
            total += item['count'] * prd_item['price']
            print(total)

        while True:
            # 结算环节
            money = float(input(f"总价:{total}, 请输入支付金额"))
            if money == total:
                print("结算成功， 欢迎下次光临")
                list_cart = []
                break
            elif money > total:
                print(f"结算成功， 找零{money - total}, 欢迎下次光临～")
                list_cart.clear()
                break
            else:
                print( f"还差{total - money}, 请重新支付～")
    elif item == "3":
        break
    else:
            print("没有此服务")



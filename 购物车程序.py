'''
要求：
1.启动程序后，让用户输入工资（工资作为初始值，用其买东西），然后打印商品列表。
2.允许用户根据商品编号购买商品。
3.用户选择商品后，检测工资余额是否够，够就直接扣款，不够就提醒。
4.用户可以一直购买商品，也可以随时退出，退出时，打印已购买商品和余额。
'''


products = [["iPhone 8", 6888], ["Mac Pro", 14800], ["小米6", 2499],\
["Coffee", 31], ["Book", 80], ["Nike Shoes", 899]]
shopping_cart = []
Run_flag = True
while True:
    user_salary = input("请输入您的工资：")
    if user_salary.isdigit():
        user_salary = int(user_salary)
        money = user_salary
        break
    else:
        print("工资输入只能是数字，请您重新输入！\n")  
print("--------商品列表----------")
for index, product in enumerate(products,1):
    print("%s   %s     %s元" %(index, product[0], product[1]))
while Run_flag:
    choice = input("\n请输入要买商品的编号来进行购买（如果想退出，则输入q）：")      
    if choice.isdigit():
        choice = int(choice)
        if choice >= 1 and choice <= len(products):
            if products[int(choice)-1][1] <= money:           
                money = money-products[int(choice)-1][1]                      
                shopping_cart.append(products[choice-1])
                print("已经将 %s 放入购物车中,您的余额为 %s 元\n"%(products[choice-1][0], money))
            else:
                print("您的余额不足，请考虑其他商品！\n")
                continue
        else:
            print("商品不存在，请您重新输入！\n")
            continue
    elif choice == "q":
        print("\n\n您已退出购物，以下是您的购物清单：")
        for index, product in enumerate(shopping_cart,1):
            print("%s   %s       %s元" %(index, product[0], product[1]))
        print("\n这是您的余额：%s 元\n"%(money))
        Run_flag=False
    else: 
        print("商品不存在，请您重新输入！\n")
        continue


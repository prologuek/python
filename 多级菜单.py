'''需求：
1.现在省、市、县3级结构，要求程序启动后，允许用户可依次选择进入各子菜单。
2.可在任意一级菜单返回上一级。
3.可以在任意一级菜单退出程序。
所需新知识点：列表、字典。
'''


menu = {
    "河北省":{
        "保定市":{
            "高阳县":"1", "容城县":"2", "雄县":"3", "唐县":"4"
        },
        "石家庄市":{
            "长安区":"1", "正定县":"2", "灵寿县":"3", "赵县":"4"
        },
        "秦皇岛市":{
            "海港区": "1", "北戴河区": "2", "抚宁区": "3", "卢龙区": "4"
        },
        "承德市":{
            "双桥区": "1", "平泉区": "2", "滦平县": "3", "兴隆县": "4"
        }
    },
    "上海市": {
        "虹口区": {
            "嘉兴路": "1", "曲阳路": "2", "江湾镇": "3", "广中路": "4"
        },
        "徐汇区": {
            "徐家汇": "1", "枫林路": "2", "长桥": "3", "田林": "4"
        },
        "松江区": {
            "佘山": "1", "新桥": "2", "小昆山": "3", "岳阳": "4"
        },
        "浦东新区": {
            "陆家嘴": "1", "周家渡": "2", "高桥": "3", "塘桥": "4"
        }
    },
    "北京市": {
        "东城区": {
            "前门": "1", "东单": "2", "东四": "3", "王府井": "4"
        },
        "西城区": {
            "西单": "1", "金融界": "2", "新街口": "3", "西四": "4"
        },
        "海淀区": {
            "五道口": "1", "学院路": "2", "知春里": "3", "牡丹园": "4"
        },
        "朝阳区": {
            "芍药居": "1", "三里屯": "2", "国贸": "3", "望京": "4"
        }
    }
}
while True: #进入第一层
    for province in menu:
        print(province)
    choice = input("输入地名：").strip()
    if not choice:continue
    if choice  in menu:       
        while True: #进入第二层
            print("你将来到 ",menu[choice].keys())              
            for city in menu[choice]:
                print(city)
            choice2 = input("输入地名（输入b返回上一层）：").strip()
            if not choice2:continue
            if choice2 in menu[choice]:                         
                while True: #进入第三层
                    print("你将来到",menu[choice][choice2].keys())  
                    for v in menu[choice][choice2]:
                        print(v)
                    choice3 = input("输入地名（输入b返回上一层）：").strip()
                    if not choice3:continue
                    if choice3 in menu[choice][choice2]:
                        print("你将来到 ", menu[choice][choice2][choice3])
                        choice4 = input("b返回上一级，q退出程序：")
                        if choice4 == "b":
                            break
                        elif choice4 == "q":
                            exit("bye!")
                        else:
                            print("输入不存在")
                            continue

                    elif choice3 == "b":
                        break
                    elif choice3 == "q":
                        exit("bye!")
                    else:
                        print("输入不存在!")
            elif choice2 == "b":
                break            
            elif choice2 == "q":
                exit("bye!")
            else:
                print("输入不存在!")  
    elif choice == "q":
        exit("bye!") 
    else:
        print("输入不存在!")


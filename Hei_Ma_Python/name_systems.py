#! /usr/bin/env python3 -- linux下命令所在的目录
# chmod +x 文件名
# -*- coding: utf-8 -*-


class Cards_v1_0(object):
    def __init__(self):
        self.cards = []

    def main(self):
        while True:
            print(
                """%s\n欢迎使用 [名片管理系统] v1.0\n1. 新建名片\n2. 显示全部\n3. 查询名片\n0. 退出系统\n%s"""
                % ("*" * 50, "*" * 50)
            )
            num = input("请选择操作的功能：")
            print("您选择的功能是：%s" % num)
            if int(num) == 0:
                print("欢迎再次使用名片管理系统")
                break
            elif int(num) == 1:
                self.cards.append(self.new_people())

            elif int(num) == 2:
                self.show_all_people(self.cards)
            elif int(num) == 3:
                self.find_people(self.cards)
            else:
                print("您输入的不正确，请重新选择")

    # 新建名片
    def new_people(self):
        new_man = {}
        print("""%s\n功能： 新建名片""" % ("-" * 50,))
        new_man["姓名"] = input("请输入姓名：")
        new_man["电话"] = input("请输入电话：")
        new_man["QQ"] = input("请输入 QQ 号码：")
        new_man["邮箱"] = input("请输入邮箱：")

        print("成功添加 %s 的名片" % new_man["姓名"])

        return new_man

    # 显示所有名片
    def show_all_people(self, cards):
        print("""%s\n功能： 显示全部""" % ("-" * 50,))
        if len(cards) == 0:
            print("提示：没有任何名片记录")
        else:
            print("姓名%s电话%sQQ%s邮箱" % (" "*10, " "*10, " "*10))
            for people in cards:
                for info in people:
                    print(people[info], end="%s" % (" "*10,))
                print("")  # 换行显示
            print("%s" % ("-"*50,))

    # 查询名片
    def find_people(self, cards):
        print(
            """%s\n功能： 搜索名片""" % ("-" * 50,))
        name = input("请输入要搜索的姓名：").strip()
        if name == "":
            print("输入出错")
        else:
            count = 0
            for man in cards:
                if name == man["姓名"]:
                    print("姓名%s电话%sQQ%s邮箱" % (" " * 10, " " * 10, " " * 10))
                    print("%s" % ("-" * 80,))
                    for info in man:
                        print(man[info], end="\t")
                    print("\n%s" % ("-" * 80,))
                    change_num = input("请输入对名片的操作：1：修改/ 2：删除/ 0：返回上一级菜单")
                    if int(change_num) == 0:
                        return cards
                    elif int(change_num) == 1:
                        c_name = input("请输入姓名[回车不修改]：").strip()
                        if c_name != "":
                            man["姓名" ] = c_name
                        c_phone = input("请输入电话[回车不修改]：").strip()
                        if c_phone != "":
                            man["电话"] = c_phone
                        c_qq = input("请输入QQ[回车不修改]：").strip()
                        if c_qq != "":
                            man["QQ"] = c_qq
                        c_email = input("请输入邮箱[回车不修改]：").strip()
                        if c_email != "":
                            man["电话"] = c_email
                        print("修改成功")
                        return cards
                    elif int(change_num) == 2:
                        del cards[count]
                        print("删除成功")
                        return cards
                    break
                count += 1
            else:
                print("该名片系统中没有 %s " % name)


class Cards_v1_1(object):
    """
    框架搭建
    """
    def __init__(self):
        # 记录所有的名片列表
        self.cards = []
        # 所有的函数会使用的应该放在模块顶部

    def main(self):
        while True:
            # TODO(man--author) 注释 -- 用于标记需要操作的事情
            # 显示功能菜单
            self.show_menu()
            action_str = input("请选择希望执行的操作：")
            print("您选择的操作是 [%s]" % action_str)

            # 1,2,3 针对名片的操作
            # 不使用int转换，可以避免用户输入的不是数字
            if action_str in ['1', '2', '3']:
                # 新增名片
                if action_str == "1":
                    self.new_card()
                # 显示全部
                if action_str == "2":
                    self.show_all()
                # 查询名片
                if action_str == "3":
                    self.search_card()
            # 0 退出系统
            elif action_str == "0":
                print("欢迎再次使用 [名片管理系统] ")
                break
            # 其他输入错误，需要提示用户
            else:
                print("您输入的不正确，请重新选择")

    def show_menu(self):
        """显示菜单"""
        print("*"*50)
        print("欢迎使用 [名片管理系统] V 1.0")
        print("")
        print("1. 新增名片")
        print("2. 显示全部")
        print("3. 搜索名片")
        print("")
        print("0. 退出系统")
        print("*"*50)

    def new_card(self):
        """新增名片"""
        print("-" * 50)
        print("新增名片")

        # 1. 提示用户输入名片的详细信息
        name_str = input("请输入姓名：")
        phone_str = input("请输入电话：")
        qq_str = input("请输入QQ：")
        email_str = input("请输入邮箱：")

        # 2. 使用用户的信息建立一个名片字典
        card_dict = {"name": name_str,
                     "phone": phone_str,
                     "qq": qq_str,
                     "email": email_str}

        # 3. 将名片字典添加到列表中
        self.cards.append(card_dict)

        # 4. 提示用户添加成功
        print("添加 %s 的名片成功!" % name_str)

    def show_all(self):
        """显示所有名片"""
        print("-" * 50)
        print("显示所有名片")
        # 判断是否存在名片记录
        if len(self.cards) == 0:
            print("当前没有任何名片记录，请使用新增功能添加名片！")
            # return 可以返回一个函数的执行结果
            # 下方的代码不会被执行
            # 如果return后面没有任何内容，表示返回调用函数的位置
            # 并且不返回任何的结果
            return
        # 打印表头
        for name in ["姓名", "电话", "QQ", "邮箱"]:
            print(name,end="\t\t")
        print("")
        # 打印分隔线
        print("="*50)

        # 遍历名片列表，依次输出列表信息
        for card_dict in self.cards:
            print("%s\t\t%s\t\t%s\t\t%s" % (card_dict["name"],
                                            card_dict["phone"],
                                            card_dict["qq"],
                                            card_dict["email"]))

    def search_card(self):
        """搜索名片"""
        print("-" * 50)
        print("搜索名片")

        # 1.提示用户要搜索的姓名
        find_name = input("请输入要搜索的姓名：")

        # 2.遍历查找，没有找到要提示用户
        for card_dict in self.cards:
            if card_dict["name"] == find_name:
                print("姓名\t\t电话\t\tQQ\t\t邮箱")
                print("=" * 50)
                print("%s\t\t%s\t\t%s\t\t%s" % (card_dict["name"],
                                                card_dict["phone"],
                                                card_dict["qq"],
                                                card_dict["email"]))
                # 针对找到的名片记录执行修改和删除的操作
                self.deal_card(card_dict)
                break
        else:
            print("抱歉，没有找到 %s" % find_name)

    def deal_card(self, find_dict):
        """
        处理查找到名片
        :param find_dict: 查找到的名片
        """
        print(find_dict)
        action_str = input("请选择要执行的操作 "
                           "[1] 修改 [2] 删除 [0] 返回上级菜单")

        if action_str == "1":
            find_dict["name"] = self.input_card_info(find_dict["name"], "姓名：")
            find_dict["phone"] = self.input_card_info(find_dict["phone"], "电话：")
            find_dict["qq"] = self.input_card_info(find_dict["qq"], "QQ：")
            find_dict["email"] = self.input_card_info(find_dict["email"], "邮箱：")

            print("修改名片成功！")
        elif action_str == "2":
            self.cards.remove(find_dict)
            print("删除名片成功！")

    def input_card_info(self, dict_value, tip_message):
        """
        输入名片信息
        :param dict_value:
        :param tip_message:
        :return:
        """
        # 1.提示用户输入内容
        result_str = input(tip_message)
        # 2. 针对用户输入进行判断，如果用户输入了内容直接返回结果
        if len(result_str) > 0:
            return result_str
        # 3. 如果用户没有输入内容，返回原有的值
        else:
            return dict_value


if __name__ == "__main__":
    first_test = Cards_v1_1()
    first_test.main()

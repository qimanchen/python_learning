#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
list -- tuple -- string -- dict

list 定义:
name_list = ["zhangsan", "lisi", "wangwu"]
[], 用逗号分隔开
列表索引（下标）值从0开始，超出索引范围会报错
name_list. + tab --> 得到其相应的方法
四种的公共方法
"""


def list_learning():
    name_list = ["zhangsan", "lisi", "wangwu"]
    # 1.取值和取索引
    print(name_list[2])
    # 知道数据内容，想知道数据在列表中的位置 --- index
    # 使用index方法时，若传递的数据不在列表中，则会报错
    print(name_list.index("wangwu"))

    # 2.修改
    # list assignment index out of range
    # 列表指定的索引超出范围会报错
    name_list[1] = "李四"

    # 3.增加
    # append 可以向列表的末尾增加数据
    name_list.append("王小二")
    # insert 在列表的指定索引位置增加数据
    name_list.insert(1, "小妹妹")

    temp_list = ["孙悟空", "猪八戒", "沙师弟"]
    # extend 把其他列表中的完整内容，追加到当前列表的末尾
    name_list.extend(temp_list)

    # 4.删除
    # remove 可以从列表中删除指定的数据
    name_list.remove("wangwu")
    # pop 默认可以把列表中最后的参数删除
    name_list.pop()
    # 3 --> 删除name_list[3]
    name_list.pop(3)
    # clear 清空列表
    name_list.clear()
    print(name_list)
    # del name_list[4] --> 删除指定数值
    # del 本质上是用来将一个变量从内存中删除
    del name_list
    # len -- 统计列表中元素的总数
    # count 方法统计列表中某个元素出现的次数

    # 从列表中删除的方法，remove 方法删除第一个找到的数据-- 从0开始索引

    # 排序
    name_list = ["zhangsan", "lisi", "wangwu", "wangxiaoer"]
    num_list = [6, 8, 4, 1, 10]
    # 列表.sort() 升序排序
    num_list.sort()
    print(num_list)
    # 列表.sort(reverse=True) 降序排序
    num_list.sort(reverse=True)
    print(num_list)
    # 逆序（翻转）
    # reverse()
    num_list.reverse()
    print(num_list)
    """
    关键字后面不需要使用括号
    import keyword 
    print(keyword.kwlist) --> 可以得到所有关键字
    
    函数 封装了独立功能，可以直接调用
    函数需要死记硬背
    
    方法 --> 对象.方法()  
    """

    """
    遍历 ---〉 从头到尾依次遍历 -- 迭代 iteration
    可以实现for进行遍历
    name_list = ["张三", "李四", "wangwu","wangxiaoer"]
    for name_list in 列表变量:
        print("my name is %s" % my_name)
    """
    """
    列表应用的场景：
    列表可以存储不同类型的数据
    1.存储相同类型的数据
    2.迭代遍历
    """


def tuple_learning():
    """
    元组的元素不能改变
    使用(,)使用
    元组 -- 使用存储不同类型中的数据
    """
    info_tuple = ("zhangsan", "18", "1.75")
    # 索引同样使用 info[1] 的样式
    print(type(info_tuple))
    # 创建空元组
    empty_tuple = ()
    print(empty_tuple)
    # 只包含一个元素的元组
    # 注意： 必须加逗号,否则是个变量
    single_tuple = (3,)
    print(single_tuple)

    # tuple 只有两个方法
    # 取值和取索引
    # tuple.count("tuple[1]")-> 出现一次 tuple.index("tuple[1]") -> 1位置为1
    # 同样可以使用len函数获得

    # 遍历循环
    for my_info in info_tuple:
        # 使用格式化字符串来拼接my_info 不方便
        # 元组中存储不同的数据类型
        print(my_info)
    """
    应用场景:
    1.函数参数和返回值
    2.格式字符串
    3.让列表不可被修改
    """
    print("%s 年龄是 %d 身高是 %.2f" % info_tuple)
    # 可以使用元组来拼接字符串
    info_str = "%s 年龄是 %d 身高是 %.2f" % info_tuple
    print(info_str)
    # 格式化字符串后面显示的是元组

    """
    元组和列表之间的转换
    list() # 使得元组可被修改
    tuple() # 保护列表不被改变
    """


def dict_learning():
    """
    字典 -- 无序的集合
    :return:
    """
    xiaoming = {"name": "小明", "age": 18, "gender": True, "height": 1.75}
    # key: value --- key必须是唯一的
    print(xiaoming)
    # 字典 -- 用来描述物体的相关信息
    # 1.取值 dict[key] -> value
    # 在取值是，key不存在，则程序会报错
    print(xiaoming['name'])

    # 2. 增加/修改
    # key不存在 --> 新增，存在 --> 修改
    xiaoming['age'] = 17

    # 3. 删除
    # 删除不存在的key会出错
    xiaoming.pop('gender')
    print(xiaoming)

    # 常用操作:
    # 1.统计键值对数量
    print(len(xiaoming))
    # 2.合并字典
    temp_dict = {"sf": 12, 'age': 20}
    # 如果被合并时，有相同的会被覆盖
    xiaoming.update(temp_dict)
    # 3.清空字典
    xiaoming.clear()

    # 循环遍历
    xiaoming = {"name": "小明", "qq": "12234", "phone": "345"}

    # 迭代遍历
    # 变量k是每次获取的key值
    for k in xiaoming:
        print("%s - %s" % (k, xiaoming[k]))

    # 字典 描述一个物体的信息
    # 多个物体放到一个列表中
    card_list = [{"name": "张三",
                  "qq": "12345",
                  "phone": "110"},
                 {"name": "李四",
                  "qq": "54321",
                  "phone": "10086"},
                 {}]
    for card_info in card_list:
        print(card_info)
    # 定义字符串 -- 使用”
    # 字符串可以使用索引值索引
    # 可以使用for迭代循环遍历字符串

    # 常用的操作
    # len() 字符串的长度
    # string.count() 统计出现的字数
    # string.index("name") 判断自字符串出现的位置 --> 以第一个字母为位置
    # 使用index() 子字符串不存在，程序会报错
    #


if __name__ == "__main__":
    dict_learning()
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


if __name__ == "__main__":
    tuple_learning()


from tkinter import *


def first_test_listbox():

    root = Tk()

    # 创建listbox
    # 可以通过 selectmode -- 设置不同模式
    # SINGLE -- 单选
    # BROWSE -- 单选 但可以通过拖动鼠标切换选项 默认
    # MULTIPLE -- 多选
    # EXTENDED -- 多选 -- 可以通过 shift/ctrl + 鼠标实现选项选择
    the_lb = Listbox(root, selectmode=BROWSE)
    the_lb.pack()

    # 插入按钮
    # the_lb.insert(0, "你是猪吗？")
    # the_lb.insert(END, "fishx is foolish")
    # 可以通过列表实现
    for item in["鸡蛋", "鸭蛋", "鹅蛋", "李狗蛋"]:
        # END 表示在选项按钮列的最后面添加一个新的按钮
        the_lb.insert(END, item)

    # 删除参数（带有两个参数） -- 初始位置 -- 结束位置
    # 设置单个参数直接对应索引值位置的，变量删除
    # the_lb.delete(0)
    # ACTIVE -- 表示当前选中的值
    the_button = Button(root, text="删除它", command=lambda x=the_lb: x.delete(ACTIVE))
    the_button.pack()

    mainloop()


def test_listbox_more_selections():

    root = Tk()

    # 创建listbox
    # 修改height -- 设置显示行数
    the_lb = Listbox(root, selectmode=BROWSE, height=11)
    the_lb.pack()

    # 可以通过列表实现
    for item in range(11):
        # END 表示在选项按钮列的最后面添加一个新的按钮
        the_lb.insert(END, item)

    mainloop()


def test_listbox_more_selections_roll():

    root = Tk()

    sb = Scrollbar(root)
    sb.pack(side=RIGHT, fill=Y)

    # 创建listbox
    # 修改height -- 设置显示行数
    # yscrollcommand -- 必须如此设置
    the_lb = Listbox(root, yscrollcommand=sb.set)

    # 可以通过列表实现
    for item in range(110):
        # END 表示在选项按钮列的最后面添加一个新的按钮
        the_lb.insert(END, item)

    the_lb.pack(side=LEFT, fill=BOTH)

    # 这也需要设置
    sb.config(command=the_lb.yview)

    mainloop()


def scroller():

    root = Tk()

    # 设置滑块数值
    # tickinterval -- 设置显示
    # resolution -- 设置间隔
    # length -- 设置滚动条的长度
    s1 = Scale(root, from_=0, to=42, tickinterval=5, resolution=5, length=200)
    s1.pack()

    s2 = Scale(root, from_=0, to=200, resolution=10, orient=HORIZONTAL,length=600)
    s2.pack()

    def show():
        # 获取滚动条的位置参数
        print(s1.get(), s2.get())

    Button(root, text="获取位置", command=show).pack()

    mainloop()

if __name__ == '__main__':
    scroller()

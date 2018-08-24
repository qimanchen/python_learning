

from tkinter import *


def first_test():
    root = Tk()

    e = Entry(root)
    e.pack(padx=20, pady=20)

    e.delete(0, END)

    mainloop()


def entry_demo():
    """first example for entry in Tkinter"""

    root = Tk()
    # 设置两个文字窗口
    Label(root, text="作品：").grid(row=0, column=0)
    Label(root, text="作者：").grid(row=1, column=0)

    e1 = Entry(root)
    e2 = Entry(root)
    # 设置两个输入框
    e1.grid(row=0, column=1, padx=10, pady=5)
    e2.grid(row=1, column=1, padx=10, pady=5)

    # 设置“获取信息”按钮的执行函数
    def show():
        print("作品：《%s》" % e1.get())
        print("作者：《%s》" % e2.get())

    # 设置两个按钮 -- 获取信息 -- 退出(直接调用root内置的quit函数即可)
    # 注意IDLE会与这个窗口的退出冲突
    Button(root, text="获取信息", width=10, command=show).grid(row=3, column=0, sticky=W, padx=10, pady=5)
    Button(root, text="退出", width=10, command=root.quit).grid(row=3, column=1, sticky=E, padx=10, pady=5)

    mainloop()


def secret_code_set_entry():
    """first example for entry in Tkinter"""

    root = Tk()
    # 设置两个文字窗口
    Label(root, text="账号：").grid(row=0, column=0)
    Label(root, text="密码：").grid(row=1, column=0)

    # 设置两个变量存储对应的 -- 账号 -- 密码
    v1 = StringVar()
    v2 = StringVar()

    # 为两个窗口中的输入内容设置为变量
    e1 = Entry(root, textvariable=v1)
    # show参数设置密码的显示格式
    e2 = Entry(root, textvariable=v2, show="*")

    # 设置两个输入框
    e1.grid(row=0, column=1, padx=10, pady=5)
    e2.grid(row=1, column=1, padx=10, pady=5)

    # 设置“获取信息”按钮的执行函数
    def show():
        print("账号：%s" % e1.get())
        print("密码：%s" % e2.get())

    # 设置两个按钮 -- 获取信息 -- 退出(直接调用root内置的quit函数即可)
    # 注意IDLE会与这个窗口的退出冲突
    Button(root, text="获取账号信息", width=10, command=show).grid(row=3, column=0, sticky=W, padx=10, pady=5)
    Button(root, text="退出", width=10, command=root.quit).grid(row=3, column=1, sticky=E, padx=10, pady=5)

    mainloop()


def test_check_entry_content():
    root = Tk()

    # 添加一个字符变量用于存储输入的内容
    v = StringVar()

    # 设置输出验证函数
    def test(content, reason, name):
        if content == "小甲鱼":
            print("正确")
            print(content, reason, name)
            return True
        else:
            print("错误")
            print(content, reason, name)
            return False

    # 输出窗口注册
    testCMD = root.register(test)

    # 生成entry窗口
    # %P -- 输入框内最新的文本内容
    # %v -- 当前validate的值
    # %W -- 当前变量 -- 以变量名称注册 -- 一串数字
    e1 = Entry(root, textvariable=v, validate="focusout", validatecommand=(testCMD, '%P', '%v', '%W'))
    # 窗口参数设置
    e2 = Entry(root)

    # 设置窗口的位置 -- 防止窗口紧贴边沿
    e1.pack(padx=10, pady=10)
    e2.pack(padx=10, pady=10)

    # 设置窗口生成实现
    mainloop()


def entry_active_calculator_plus():
    root = Tk()

    # 添加一个窗口设置计算机
    frame = Frame(root)
    frame.pack(padx=10, pady=10)

    # 添加一个字符变量用于存储输入的内容
    v1 = StringVar()
    v2 = StringVar()
    v3 = StringVar()

    # 设置输出验证函数
    # 设置时知识显示
    def test(content):
        return content.isdigit()

    # 输出窗口注册
    testCMD = frame.register(test)

    # 生成entry窗口
    # %P -- 输入框内最新的文本内容
    # %v -- 当前validate的值
    # %W -- 当前变量 -- 以变量名称注册 -- 一串数字
    # 验证输入内容是否为数字
    # 窗口参数设置
    # 设置窗口的位置 -- 防止窗口紧贴边沿
    e1 = Entry(frame, width=10, textvariable=v1, validate="key", validatecommand=(testCMD, '%P')).grid(row=0, column=0)

    Label(frame, text="+").grid(row=0, column=1)

    # width -- 设置窗口的宽度
    e2 = Entry(frame, width=10, textvariable=v2, validate="key", validatecommand=(testCMD, '%P')).grid(row=0, column=2)

    Label(frame, text="=").grid(row=0, column=3)
    # 设置为只读 -- state 设置窗口状态
    e3 = Entry(frame, textvariable=v3, state='readonly').grid(row=0, column=4)

    # 增加计算窗口的函数
    def calc():
        result = int(v1.get()) + int(v2.get())

        # 设置计算结果 v3.set()
        v3.set(str(result))

    # 增加计算按钮
    Button(frame, text="计算结果", command=calc).grid(row=1, column=2, pady=5)

    # 设置窗口生成实现
    mainloop()


if __name__ == '__main__':
    entry_active_calculator_plus()



from tkinter import *
import webbrowser   # 测试连接
import hashlib  # 验证文本


def first_test_text():
    """first create a text input window by text entry"""
    root = Tk()

    # 创建一个text输入
    text = Text(root, width=30, height=2)
    text.pack()

    # 往text窗口中插入文字 -- 同时是可以修改编辑文本
    text.insert(INSERT, "I love \n")
    text.insert(END, "FishC.com!")

    mainloop()


def test_text_insert_button():
    root = Tk()

    # 创建一个text输入
    # width -- 窗体输入的宽度
    # height -- 行数
    text = Text(root, width=30, height=2)
    text.grid(row=0, column=0, padx=10, pady=5)

    # 往text窗口中插入文字 -- 同时是可以修改编辑文本
    # INSERT -- 文本插入区域
    text.insert(INSERT, "I love \n")
    text.insert(END, "FishC.com!")

    # 按钮的实现函数
    def show():
        print("哦， 我被点了一下")

    # 插入一个按钮 -- 插入到文本输入窗体内
    b1 = Button(text, text="点我点我", command=show)
    # 插入button组件
    text.window_create(INSERT, window=b1)

    Button(root, text="test out of text window", command=show).grid(row=3, column=0, padx=10, pady=5)
    mainloop()


def test_text_insert_photo():
    root = Tk()

    # 创建一个text输入
    # 注意窗口的大小会影响图像的显示
    text = Text(root, width=30, height=30)
    text.pack()
    # text.grid(row=0, column=0, padx=10, pady=5)

    # 插入图片
    photo = PhotoImage(file="te.gif")

    # 按钮的实现函数
    def show():
        # 插入图像图片
        text.image_create(END, image=photo)

    # 插入一个按钮 -- 插入到文本输入窗体内
    b1 = Button(text, text="点我点我", command=show)
    # 插入button组件
    text.window_create(INSERT, window=b1)

    # Button(root, text="test out of text window", command=show).grid(row=3, column=0, padx=10, pady=5)
    mainloop()


def test_text_indexes():
    """
        索引方式：
            "%d.%d" % (line, column) -- line 1 column 0
    :return:
    """
    pass


# 测试tag的使用
def test_text_tag():

    root = Tk()

    # 创建一个新的text窗口
    text = Text(root, width=30, height=10)
    text.pack()

    text.insert(INSERT, "I love FishC.com!")

    # 设置标签位置
    text.tag_add("tag1", "1.7", "1.12", "1.14")
    # 设置标签显示形式
    text.tag_config("tag1", background="yellow", foreground="red")
    # 新建的tag覆盖旧的tag

    mainloop()


def test_text_tag_repeat():

    root = Tk()

    # 创建一个新的text窗口
    text = Text(root, width=30, height=10)
    text.pack()

    text.insert(INSERT, "I love FishC.com!")

    # 设置标签位置
    text.tag_add("tag1", "1.7", "1.12", "1.14")
    # 设置标签显示形式
    # background -- 背景色
    # foreground -- 前景色
    text.tag_config("tag1", background="yellow", foreground="red")
    # 添加一个新的tag标签
    # 新的tag覆盖旧的
    text.tag_add("tag2", "1.7", "1.12", "1.14")
    text.tag_config("tag2", foreground="blue")
    # 新建的tag覆盖旧的tag

    mainloop()


def test_text_tag_event_binding():

    root = Tk()

    # 创建一个新的text窗口
    text = Text(root, width=30, height=10)
    text.pack()

    text.insert(INSERT, "I love FishC.com!")

    text.tag_add("link", "1.7", "1.16")
    text.tag_config("link", foreground="blue", underline=True)

    # 事件绑定
    def show_hand_cursor(event):
        text.config(cursor="arrow")

    def show_xterm(event):
        text.config(cursor="xterm")

    def click(event):
        # 绑定网址
        webbrowser.open("https://fishc.com.cn")

    text.tag_bind("link", "<Enter>", show_hand_cursor)
    text.tag_bind("link", "<Leave>", show_xterm)
    text.tag_bind("link", "<Button-1>", click)

    mainloop()


def test_text_check_content():

    root = Tk()

    # 创建一个新的text窗口
    text = Text(root, width=30, height=10)
    text.pack()

    text.insert(INSERT, "I love FishC.com!")
    contents = text.get("1.0", END)

    # 验证内容是否一致
    def get_sig(contents):
        m = hashlib.md5(contents.encode())
        return m.digest()

    sig = get_sig(contents)

    def check():
        ontents = text.get("1.0", END)

        if sig != get_sig(ontents):
            print("警报，内容发生变动")
        else:
            print("风平浪静")

    Button(root, text="检查", command=check).pack()

    mainloop()


def test_text_search():

    root = Tk()

    # 创建一个新的text窗口
    text = Text(root, width=30, height=10)
    text.pack()

    text.insert(INSERT, "I love FishC.com!")

    def getIndex(text, index):
        return tuple(map(int, str.split(text.index(index), ".")))

    start = "1.0"
    while True:
        pos = text.search("o", start, stopindex=END)
        if not pos:
            break
        print("找到了， 位置是", getIndex(text, pos))
        start = pos + "+1c"

    mainloop()


def test_text_reset():
    """测试撤销功能
    """
    root = Tk()

    # 创建一个新的text窗口
    text = Text(root, width=30, height=10, undo=True)
    text.pack()

    text.insert(INSERT, "I love FishC.com!")

    def show():
        text.edit_undo()

    Button(root, text="撤销", command=show).pack()

    mainloop()


def test_text_reset():
    """
        测试撤销功能
        撤销 -- 一次完整的工作
    """
    root = Tk()

    # 创建一个新的text窗口
    # autoseparators -- 设置是否通过一次性完整的工作来进行
    text = Text(root, width=30, height=10, undo=True, autoseparators=False)
    text.pack()

    text.insert(INSERT, "I love FishC.com!")

    # 设置通过用户自身设置来实现
    def callback(event):
        text.edit_separator()

    text.bind('<Key>', callback)

    def show():
        text.edit_undo()

    Button(root, text="撤销", command=show).pack()

    mainloop()


# 测试模块的实现
if __name__ == '__main__':
    test_text_reset()

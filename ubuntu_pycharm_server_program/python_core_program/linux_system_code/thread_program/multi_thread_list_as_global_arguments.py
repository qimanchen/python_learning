from threading import Thread
import time

def work1(nums):
    nums.append(44)
    print("--- in work1 ---",nums)

def work2(nums):
    time.sleep(1)
    print("--- in work2 ---",nums)

g_num = [11,22,33]

t1 = Thread(target=work1, args=(g_num,))
t1.start()

t2 = Thread(target=work2, args=(g_num,))
t2.start()

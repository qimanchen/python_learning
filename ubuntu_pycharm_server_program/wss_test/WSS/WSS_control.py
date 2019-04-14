#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 导入pyserial
import serial


"""
    波长选择器：通过pyserial模块进行控制
    主要为serial串口模块的熟悉
"""


# 端口控制
def test_serial():
    """
        测试serial模块相关功能
    :return:
    """
    ser = serial.Serial('/dev/ttyUSB0')  # 打开串口 serial port
    # 默认开启"9600,8,N,1" no timeout

    print ser.name      # 检查当前使用的串口
    ser.write(b'hello')     # 写入一段需要发送的数据
    ser.close()     # 关闭打开的相应串口

    # 设置"19200,8,N,1", timeout 1s
    with serial.Serial('/dev/ttyS1', 19200, timeout=1) as ser:
        x = ser.read()      # 读取一个字节
        s = ser.read(10)        # 读取十个字节（timeout）
        line = ser.readline()   # 读取一行

    ser.readline()      # 在timeout前会一直读取，直到timeout或\n
    ser.isOpen()       # 验证是否开启了当前端口
    ser.timeout = 10    # 设置read超时时间
    ser.writeTimeout = 20       # 设置写超时时间
    print ser       # 查看当前串口状态






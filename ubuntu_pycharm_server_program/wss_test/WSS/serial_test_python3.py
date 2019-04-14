#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import serial
from threading import Thread, Lock
import logging

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)


class SerialTest(object):
	"""
		测试serial模块的使用
	"""
	# 初始化端口
	
	# 检测链接状态
	
	# 检测接收数据，并返回相应的数据
	
	# 发送数据，同时检测返回信息
	
	def __init__(self, port="com2", baudrate=9600):
		self.serial = serial.Serial(port,baudrate=baudrate)
		
	def read(self):
		logger.info("*** 等待反馈信息 ***")
		response = self.serial.readall()
		return response
		
	def write(self):
		send_message = input("请输入需要传入的指令：").encode("utf-8")
		logger.info("*** 发送指令: {}" .format(send_message))
		self.serial.write(send_message)
		
	def loop_work(self):
		self.write()
		self.serial.timeout = 5
		response = self.read()
		if response.decode("utf-8") == "":
			logger.info("*** 目标主机无反馈信息 ***")
		else:
			logger.info("*** 反馈信息: \n{}".format(response.decode("utf-8")))
		
		

def str_to_hex(s):
	return ' '.join([hex(ord(c)).replace('0x', '') for c in s])
	
def hex_to_str(s):
	return ''.join([chr(i) for i in [int(b, 16) for b in s.split(' ')]])
	
def test():
	ser = serial.serial_for_url('com2', timeout=5)
	response = ser.readline()
	# mes = input("hello")
	# 将字符串转换成bytearray类型
	# mes = bytearray(mes, encoding="utf-8")
	# print(mes)
	# ser.write(mes)
	# 将串口发来的bytearray转换成字符串
	print(response.decode(encoding="utf-8"))
	
def as_byte_array(string):
	# 
	readstr = byarray.decode('utf-8')
	
	readstr = str(byarray)
	readstr = ' '.join(hex(x) for x in byarray)
	
def main(default_port=None, default_baudrate=9600):
	
	while True:

		serial_instance = serial.Serial("com2")

		miniterm = SerialTest(serial_instance)
		miniterm.start()

		miniterm.join()

		miniterm.close()
 
 
if __name__ == "__main__":
	test_ser = SerialTest()
	test_ser.loop_work()

	

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import logging
import serial
import serial.tools.list_ports
import threading

class WssControler(object):
	"""
		WSS的控制程序，通过RS232的通信方式
	"""
	
	def __init__(self, port="com3", baudrate=9600, timeout=None):
		self.logger = None		# 定义控制台信息
		self.ret = False		# 设定连接端口状态，默认是关闭的
		self.logger = self.set_logger()
		# 连接建立
		self.ser, self.ret = self.connect(port, baudrate, timeout)
		
		self.logger.info("连接串口{}".format(self.ser.port))
		self.logger.info("连接波特率 {}".format(self.ser.baudrate))
		self.bool = True	# 设置接收消息标志位
		
	@staticmethod
	def connect(port, baudrate, timeout):
		"""
			建立与设备的连接
			默认接收时间设置为None
		"""
		ret = False
		try:
			ser = serial.Serial(port, baudrate, timeout=timeout)
			
			# 判断是否成功打开
			if ser.isOpen():
				ret = True
		except Exception as e:
			logging.info("--程序异常：{}".format(e))
			
		return ser, ret
		
	@staticmethod
	def set_logger():
		"""
			设置通知类消息
		"""
		logging.basicConfig(level=logging.INFO, format='%(name)s - %(levelname)s - %(message)s ')
		logger = logging.getLogger(__name__)
		return logger
		
	def get_port_list(self):
		""" 获取当前设备可用串口 """
		port_list = list(serial.tools.list_ports.comports())
		if len(port_list) == 0:
			self.logger.info("无可用串口")
		else:
			self.logger.info("存在以下可用串口:  {}".format(port_list))
			
		return port_list
		
	# 关闭连接
	def close(self):
		self.bool = False
		self.ser.close()
		
	# 发送信息
	def write_cmd(self, cmd):
		result = self.ser.write(cmd.encode("utf-8"))
		return result
	
	# 接收信息
	def read_res(self):
		# 接收数据为死循环
		while self.bool:
			if self.ser.in_waiting:
				message = self.ser.read(self.ser.in_waiting).decode("utf-8")
				# 当设定OK时停止接收信息
				if message == "OK" or message == "OK\r\n" or message == "OK\n":
					break
				else:
					self.logger.info("返回的信息为：{}".format(message))
				
		
def main():
	# 简单的测试程序
	wss = WssControler("com3", 9600)
	cmd = input("请输入指令：")
	wss.write_cmd(cmd)
	wss.read_res()
	wss.close()


if __name__ == "__main__":
	main()
			
		
		
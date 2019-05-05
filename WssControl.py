#!/usr/bin/evn python2
# -*- coding: utf-8 -*-
import logging
import re
import serial
import time


BAUDRATE = 115200     # 与设备通信的波特率
WINDOWS_SERIALPORT = 'com3'      # windows操作系统下串口
LINUX_SERIALPORT = '/dev/ttyUSB0'       # linux操作系统下串口

# 设置logging信息
logging.basicConfig(level=logging.INFO, format='*** %(name)s - %(levelname)s - %(message)s')
Logger = logging.getLogger(__name__)


class WssControl(object):
    """
        调用serial模块中的相应的功能，
        得到或设置WSS的相关配置
    """
    def __init__(self, port='com3', baudrate=115200, timeout=None):
        """初始化，连接到相应设备"""
        self._ser = self.open_connect(port, baudrate, timeout)

    @staticmethod
    def open_connect(port, baudrate, timeout):
        """
            建立一个新的连接
            port: 设备通信串口
            baudrate：设备通信波特率
            timeout：读取response时间timeout
        """
        try:
            ser = serial.Serial(port, baudrate=baudrate, timeout=timeout)
            if not ser.isOpen():
                raise ValueError("*** 设备连接错误 ***")
            else:
                Logger.info("通过串口-{},波特率-{},连接到设备".format(port, baudrate))
            return ser
        except Exception as e:
            Logger.info(e)

    def response_len(self):
        """获取接收到的数据长度"""
        return self._ser.inWaiting()

    def check_connection_status(self):
        """查询设备的连接状态"""
        return self._ser.isOpen()

    def read_response(self, command_type):
        """读取相应command的响应信息"""

        pattern = re.compile("\s+")      # 定义分离模式
        data = ''
        data = data.encode('utf-8')
        n = self._ser.inWaiting()

        if n:
            data = data + self._ser.read(n)
        # 防止有数据未读取完全
        n = self._ser.inWaiting()
        if len(data) > 0 and n == 0:
            try:
                temp = data.decode("utf-8")
                temp = pattern.split(temp)

                # 去除最后的一个空白符
                temp = temp[0:-1]
                # 特殊处理 RES 命令
                if command_type == "RES":
                    set_check_status = temp[0]
                    command_type = False
                else:
                    set_check_status = temp[-1]

                # 检查命令设置状态
                if set_check_status == "OK":
                    Logger.info("命令设置成功")
                    # 返回响应信息
                    if command_type:
                        # 设备查询命令为True
                        # 设备设置命令为False
                        # 设备查询命令返回信息
                        return temp[0:-1]   # 去除查询命令后面的OK
                    # 返回设置命令的返回信息
                    return temp

                # 命令设置出现错误
                elif set_check_status == "CER":
                    Logger.info("命令行错误，请检查命令是否支持或书写正确")
                elif set_check_status == "AER":
                    Logger.info("命令参数错误，请检查参数是否书写正确及参数个数是否正确")
                elif set_check_status == "RER":
                    Logger.info("命令参数范围错误，请检查参数范围是否正确")
                elif set_check_status == "VER":
                    Logger.info("限定错误，请检查认证mode是否正确")
            except Exception as e:
                Logger.info("读取内容错误")

    def send_data(self, command, command_type):
        """
        发送指定指令到设备中
        :param command: 指定的指令
        :return:
        """
        try:
            self._ser.write("{}\n".format(command).encode("utf-8"))
            time.sleep(0.1)
            message = self.read_response(command_type)
            if message:
                Logger.info("指令-{}设置成功".format(command))
                return message
            else:
                Logger.info("指令-{}设置失败".format(command))
        except Exception as ex:
            Logger.info("指令发送异常")

    def close_connect(self):
        """关闭串口的连接"""
        if self._ser.isOpen():
            self._ser.close()
            Logger.info("串口连接关闭")
        else:
            Logger.info("串口连接已关闭")

    # 相应操作指令
    def sus(self):
        """
            查询设备当前状态
            设备指令 SUS?
            :return
            三种响应：
            SLS:  Start Last Saved
            SAB:  Start All Blocked
            SFD:  Start Factory Default
        """
        self._ser.write('SUS?\n'.encode("utf-8"))
        time.sleep(0.1)     # 给设备响应时间
        message = self.read_response(True)
        if message:
            Logger.info("SUS 查询到当前状态为{}".format(message))
            return message

    def mid_set(self, id_string):
        """
        MID <IDstring>\n
            设置设备的唯一id
        :return: id_string
        """
        self._ser.write('MID {}\n'.format(id_string).encode("utf-8"))
        time.sleep(0.1)
        message = self.read_response(False)
        if message:
            Logger.info("设置设备的唯一ID为: {}".format(id_string))
            return id_string
        else:
            Logger.info("MID 指令设置失败")

    def check_mid(self):
        """
        MID?
            查询设备的唯一Id
        :return: 设备Id string
        """
        self._ser.write('MID?\n'.encode("utf-8"))
        time.sleep(0.1)
        message = self.read_response(True)
        if message:
            Logger.info("查询到设备的唯一ID为: {}".format(message[0]))
            return message
        else:
            Logger.info("MID? 查询出错")

    def start_factory_default(self):
        """
        SFD
        设置以出厂设置为初始状态：恢复出厂设置
        :return: OK -- 设置成功
        None -- 设置出错
        """
        self._ser.write("SFD\n".encode("utf-8"))
        time.sleep(0.5)
        message = self.read_response(False)
        if message:
            Logger.info("SFD 设置成功")
            return message
        else:
            Logger.info("SFD 设置出错")

    def start_all_blocked(self):
        """
            SAB
            设置所有的Channels为Blocked状态
            :return: OK -- 设置成功
            None -- 设置出错
        """
        self._ser.write("SAB\n".encode("utf-8"))
        time.sleep(0.5)
        message = self.read_response(False)
        if message:
            Logger.info("SAB 设置成功")
            return message
        else:
            Logger.info("SAB 设置出错")

    def start_last_saved(self):
        """
            SLS
            设置上一次保存的状态作为开机状态
            :return: OK -- 设置成功
            None -- 设置出错
        """
        self._ser.write("SLS\n".encode("utf-8"))
        time.sleep(0.5)
        message = self.read_response(False)
        if message:
            Logger.info("SLS 设置成功")
            return message
        else:
            Logger.info("SLS 设置出错")

    def check_operational_status(self):
        """
        OSS?
        查询设备的运行状态
        :return: 十六进制数
        """
        pass

    def check_hardware_status(self):
        """
        HSS?
        查询设备软件的运行状态
        """
        pass

    def check_operational_latched_status(self):
        """
        LSS?
        查询设备软件锁存状态
        相应bit位对应HSS的bit位
        """
        pass

    def check_case_tempearture_status(self):
        """
        CSS?
        查询设备的范围温度
        温度不可高于70摄氏度
        :return: 返回的[temperature]
        """
        self._ser.write("CSS?\n".encode("utf-8"))
        time.sleep(0.1)
        message = self.read_response(True)
        if message:
            Logger.info("设备case温度为: {}".format(message[0]))
            if float(message[0]) > 50:
                Logger.info("设备温度过高，注意设备的休息")
            return message
        else:
            Logger.info("CSS? 查询出错")

    def check_internal_tempearture_status(self):
        """
        ISS?
        查询设备的内部温度
        :return:
        """
        self._ser.write("ISS?\n".encode("utf-8"))
        time.sleep(0.1)
        message = self.read_response(True)
        if message:
            Logger.info("设备case温度为: {}".format(message[0]))
            if float(message[0]) > 60:
                Logger.info("设备温度过高，注意设备的休息")
            return message
        else:
            Logger.info("ISS? 查询出错")

    def check_read_pending_array(self):
        """
        RPA?
        查询设备所有通道的可读状态
        :return:
        """
        pass

    def set_update_port_attenuation(self, out_port, port_attenuation):
        """
        UPA out_port,port_attenuation
        out_port: [1-9]
        port_attenuation: [0-20]
        设置所有可用通道唯一的输出端口和衰减值
        :return:
        """
        self._ser.write("UPA {},{}\n".format(out_port, port_attenuation).encode("utf-8"))
        time.sleep(0.5)
        message = self.read_response(False)
        if message:
            Logger.info("设置当前所有有效channel: out_port-{}, port_attenuation-{}".format(out_port, port_attenuation))
            return message
        else:
            Logger.info("UPA 设置出错")

    def check_custom_single_channel(self, channel_number):
        """
        RCS? channel_numbe
        查询某一通道的状态 -- out_port, channel_attenuation
        :param channel_number:
        :return: [channel_number, port_number, channel_attenuation
        """
        self._ser.write("RCS? {}\n".format(channel_number).encode("utf-8"))
        time.sleep(0.1)
        message = self.read_response(True)
        if message:
            response = re.split(',+', message[0])
            Logger.info("channel-{}, out_port-{}, attenuation-{}".format(response[0], response[1], response[2]))
            # response = ['channel_number', 'out_port', 'attenuation']
            return response
        else:
            Logger.info("RCS? 查询出错")

    def check_custom_all_channel(self):
        """
        RCA?
        查询所有可用通道的状态 -- out_port, channel_attenuation
        :return:
        """
        self._ser.write("RCA?\n".encode("utf-8"))
        time.sleep(0.1)
        message = self.read_response(True)
        if message:
            response = re.split(";+", message[0])
            channel_plan = []
            # 解析查询的信息
            for one_channel in response:
                mid_mes = re.split(",+", one_channel)
                channel_plan.append(mid_mes)
            # channel_plan = [['channel_num','out_port','channel_att'],....]
            Logger.info("查询到：[channel, out_port, attenuation] -- {}".format(channel_plan))
            return channel_plan
        else:
            Logger.info("RCA? 查询出错")

    def set_update_custom_array(self, channel_plan):
        """
        UCA channel_number,port_number,channel_attenuation;...
        设置一个或多个通道的状态
        :param channel_plan:
        channel_plan = [[channel_num, out_port, channel_att],....]
        :return:
        """
        # 处理传入参数
        mid_channel = []
        for channel_node in channel_plan:
            mid_channel.append(",".join(map(str, channel_node)))
        # 组合参数为一个字符串
        channel_string = ";".join(map(str, mid_channel))
        self._ser.write("UCA {}\n".format(channel_string).encode("utf-8"))
        time.sleep(0.5)
        message = self.read_response(False)
        if message:
            Logger.info("设置channel plan为{}".format(channel_string))
            return message
        else:
            Logger.info("UCA 设置出错")

    def set_channel_spacing_write(self, mode):
        """
        CHW mode[0|50|100]
        设置设备的通道模式
        :return:
        """
        if mode in [0, 50, 100]:
            self._ser.write("CHW {}\n".format(mode).encode("utf-8"))
            time.sleep(0.1)
            message = self.read_response(False)
            if message:
                Logger.info("设置设备的模式为: {}".format(mode))
                return message
            else:
                Logger.info("CHW 设置出错")
        else:
            Logger.info("CHW {}-模式不存在".format(mode))

    def check_channel_spacing_read(self):
        """
        CHR?
        查询设备的通道模式
        :return:
        """
        self._ser.write("CHR?\n".encode("utf-8"))
        time.sleep(0.1)
        message = self.read_response(True)
        if message:
            Logger.info("设备模式为: {}".format(message[0]))
            return message
        else:
            Logger.info("CHR? 查询出错")

    def trans_custom_list(self, custom_list, command_type):
        """
        转换DCC，DCR定制channel字典 to 字符串
        custome_list: {'channel_num':{'width':[start_slice,end_slice], 'range':[start_range,end_range]}}
        """
        if command_type == "DCC":
            custom_channel_string = ""
            for channel_num in custom_list.keys():
                custom_channel_string += str(channel_num) +\
                                         "=" \
                                         + ":".join(map(str, custom_list[channel_num]['width'])) \
                                         + ";"
                # "1=1:8;"
            return custom_channel_string
        elif command_type == "DCR":
            custom_channel_range = ""
            for channel_num in custom_list.keys():
                custom_channel_range += str(channel_num) \
                                        + "=" \
                                        + ":".join(map(str,custom_list[channel_num]['width'])) \
                                        + ',' \
                                        + ":".join(map(str, custom_list[channel_num]['range'])) \
                                        + ";"
            return custom_channel_range

    def trans_string_custom_list(self, custom_string, command_type):
        """
        将DCC或DCR的命令转换成相应的字符串
        custom_string:
        DCC? ==> channel_num=slice1:slice2;...
        DCR? ==>channel_num=slice1:slice2,range1:range2;...
        custome_list: {'channel_num':{'width':[start_slice,end_slice], 'range':[start_range,end_range]}}
        """
        channel_list = re.split(';+', custom_string)
        channel_plan_dict = {}

        if command_type == "DCC":
            for mid_channel in channel_list:
                mid_list = re.split('=+', mid_channel)
                slice_list = re.split(':+', mid_list[1])
                # 注意：这里的slice_list内为string类型
                channel_plan_dict[str(mid_list[0])] = {'width': slice_list}
        elif command_type == "DCR":
            for mid_channel in channel_list:
                mid_list = re.split('=+', mid_channel)
                slice_range_list = re.split(',+', mid_list[1])

                slice_list = re.split(':+', slice_range_list[0])
                range_list = re.split(':+', slice_range_list[1])
                # 注意：这里的slice_list内为string类型
                channel_plan_dict[str(mid_list[0])] = {'width': slice_list, 'range': range_list}
        return channel_plan_dict

    def set_define_custom_channel(self, custom_channel):
        """
        DCC channel_number=slice_range1:slice_range2;...
        注意slice范围不可超过40
        设置一个或多个自定义通道路由

        custom_channel = "channel_num=slice1:slice2;..."
        注意：sliece的范围受到设备当前设定的影响
        :return:
        """
        # 将custom字典转换成对应的字符串
        custom_string = self.trans_custom_list(custom_channel, 'DCC')
        self._ser.write("DCC {}\n".format(custom_string).encode("utf-8"))
        time.sleep(0.5)
        message = self.read_response(False)
        if message:
            Logger.info("定制的channel plane 为: {}".format(custom_channel))
            return message
        else:
            Logger.info("DCC 设置出错")

    def check_define_custom_channel(self):
        """
        DCC?
        查询定制通道路由

        :return:
        """
        self._ser.write("DCC?\n".encode("utf-8"))
        time.sleep(0.1)
        message = self.read_response(True)
        if message:
            channel_list = self.trans_string_custom_list(message[0], 'DCC')
            Logger.info("定制的channel plane 为: {}".format(channel_list))
            return channel_list
        else:
            Logger.info("DCC? 查询出错")

    def set_define_channel_range(self, custom_channel_range):
        """
        DCR channel_number=slice1:slice2,slice_range1:slice_range2;...
        自定义通道路由的同时，自定义相依的变化范围
        :return:
        """
        # 将custom字典转换成string
        custom_channel_range_string = self.trans_custom_list(custom_channel_range, "DCR")
        self._ser.write("DCR {}\n".format(custom_channel_range_string).encode("utf-8"))
        time.sleep(0.5)
        message = self.read_response(False)
        if message:
            Logger.info("定制的channel plane 为: {}".format(custom_channel_range))
            return message
        else:
            Logger.info("DCR 设置出错")

    def check_channel_range(self):
        """
        DCR?
        查询定义通道路由和通道slice变化范围
        :return:
        """
        self._ser.write("DCR?\n".encode("utf-8"))
        time.sleep(0.1)
        message = self.read_response(True)
        if message:
            channel_dic = self.trans_string_custom_list(message[0], 'DCR')
            Logger.info("定制的channel plane 为: {}".format(channel_dic))
            return channel_dic
        else:
            Logger.info("DCR? 查询出错")

    def set_change_custom_channel(self, channel_list):
        """
        CCC channel_number=slice1:slice2;
        注意slice一定要在slice range范围内
        :return:
        """
        # 将channel_list字典转换成string
        channel_string = self.trans_custom_list(channel_list, "DCC")
        self._ser.write("CCC {}\n".format(channel_string).encode("utf-8"))
        time.sleep(0.5)
        message = self.read_response(False)
        if message:
            Logger.info("定制的channel plane 为: {}".format(channel_string))
            return message
        else:
            Logger.info("CCC 设置出错")

    def set_channel_shape(self, string):
        """
        DCS channel_number=attenuations,attenuations;...
        设置通道内每个slice的shape -- 设置attenuation实现
        :param string:
        :return:
        """
        pass

    def check_channel_shape(self, channel_number=None):
        """
        DCS? {channel_number}
        查询所有或单个channel的shape
        :return:
        """
        pass

    def set_reset(self):
        """
        RES
        重新设置设备软件
        :return:
        """
        self._ser.write("RES\n".encode("utf-8"))
        time.sleep(0.5)
        message = self.read_response("RES")
        if message:
            Logger.info("存储当前设备重置成功")
            return message
        else:
            Logger.info("STR 设置出错")

    def set_store_data(self):
        """
        STR
        存储当前设备的状态 -- 配合SLS使用
        :return:
        """
        self._ser.write("STR\n".encode("utf-8"))
        time.sleep(0.5)
        message = self.read_response(False)
        if message:
            Logger.info("存储当前设备状态成功")
            return message
        else:
            Logger.info("STR 设置出错")

    def set_clear_error(self):
        """
        CLE
        清除设备中的错误 -- OSS？ 和 LSS？中查询到的
        :return:
        """
        self._ser.write("CLE\n".encode("utf-8"))
        time.sleep(0.5)
        message = self.read_response(False)
        if message:
            Logger.info("清除设备的软件错误 -- 通过OSS?和LSS?查询得到的")
            return message
        else:
            Logger.info("CLE 设置出错")


# 测试函数
def test():
    """测试类中函数的功能"""
    pass


if __name__ == "__main__":
    ser = WssControl()

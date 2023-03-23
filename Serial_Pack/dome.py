import serial
import time

class Tserial():


    # 模组串口配置，可以根据模组具体情况修改，使用的串口名字和波特率可以在程序启动参数指定
    def __init__(self,com,bu):
        # 端口与波特率要根据具体模组进行修改
        g_serial_port = com
        g_serial_baudrate = int(bu)
        g_serial_bytesize = serial.EIGHTBITS
        g_serial_parity = serial.PARITY_NONE
        g_serial_stopbits = serial.STOPBITS_ONE
        g_serial_timeout_s = 5

        # 连接串口
        self.serial_port = serial.Serial(g_serial_port, g_serial_baudrate, g_serial_bytesize, g_serial_parity,
                                         g_serial_stopbits,
                                         g_serial_timeout_s, rtscts=False)

    # 通过串口发送指令
    def into_data(self, data):
        # 输入的指令
        data_into = data
        time.sleep(10)
        datas = self.serial_port.write((data_into + '\r\n').encode('utf8'))
        print(f"已输入指令：{data},当前时间为："+time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))
        return datas


if __name__ == '__main__':
    s=Tserial("COM6",115200)
    data = ["insmod /kmod/aiw4201.ko","wpa_supplicant -iwlan0 -Dnl80211 -c/configs/wpa_supplicant.conf &",
            "echo wlan0 set_sta_pm_on 0 > /sys/wifisys/ccpriv","echo wlan0 alg_cfg tpc_mode 0 > /sys/wifisys/ccpriv",
            "wpa_cli -iwlan0 -p/configs/wpa_supplicant","scan","scan_results","add_n",
            'set_n 0 ssid "1234567890!@#$%^&*()asdfghjklzxc"',"set_network 0 key_mgmt WPA-PSK",'set_network 0 psk "12345678"',
            "select_n 0","q","udhcpc -i wlan0","ifconfig"]


    data_kill = ["killall udhcpc","ifconfig wlan0 down","rmmod aiw4201"]

    data_open = ["insmod /kmod/aiw4201.ko", "wpa_supplicant -iwlan0 -Dnl80211 -c/configs/wpa_supplicant.conf &",
            "echo wlan0 set_sta_pm_on 0 > /sys/wifisys/ccpriv", "echo wlan0 alg_cfg tpc_mode 0 > /sys/wifisys/ccpriv",
            "wpa_cli -iwlan0 -p/configs/wpa_supplicant", "scan", "scan_results", "add_n",
            'set_n 0 ssid "HUAWEI-AGG"', "set_n 0 key_mgmt NONE",
            "select_n 0", "q", "udhcpc -i wlan0", "ifconfig"]

    for i in data:
        s.into_data(i)

    l = input("是否需要ping包，Y/N？")
    if l == "Y":
        s.into_data("ping 192.168.99.1 -w 30")
        print("已开始ping包")

    l = input("是否需要关进驱动，Y/N？")
    if l == "Y":
        for i in data_kill:
            s.into_data(i)

    l = input("是否需要重置模组，Y/N？")
    if l =="Y":
        s.into_data("reboot")
        print("设备重启指令已输入")
    else:
        print("执行结束")
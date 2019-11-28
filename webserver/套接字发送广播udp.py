"""
1. 导入socket
2.创建socket对象
3.设置广播权限
4.发送广播  广播地址：xxx.xxx.xxx.255 或者 255.255.255.255
5.关闭套接字

"""
import socket


udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

udp_socket.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, True)

udp_socket.sendto("这是一条广播".encode("gbk"), ("192.168.0.255", 8080))

udp_socket.close()
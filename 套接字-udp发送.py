"""
1.导入socket包
2.创建socket对象 ipv4 协议模式
3.传输数据  数据内容.encode(),ip+port
4.关闭套接字对象

"""

import socket

UDP_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

UDP_socket.sendto("hello world".encode(), ("127.0.0.1", 8080))

UDP_socket.close()

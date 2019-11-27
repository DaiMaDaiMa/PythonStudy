"""
1.导入socket
2.创建socket对象
3.绑定端口号
4.发送消息
5.关闭套接字
"""

import socket

UDP_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

UDP_socket.bind(("127.0.0.1", 8888))  # ip地址可以穿空

UDP_socket.sendto("hello java".encode(), ("127.0.0.1", 8080))

UDP_socket.close()
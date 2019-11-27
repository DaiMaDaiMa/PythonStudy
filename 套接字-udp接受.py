"""
1.导入socket
2.创建socket对象 ipv4 协议模式
3.发送数据 encode 对方IP 和 port
4.接受数据
5.解码数据
6.关闭套接字
"""

import socket

UDP_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

UDP_socket.sendto("hello python".encode(), ("127.0.0.1", 8080))

recv = UDP_socket.recvfrom(1024)

# recv 接受的是一个元祖（消息，（ip，port）），第一个元素是接收到的消息二进制，第二个元素是对方的（ip，port）


recv_msg = recv[0].decode()
recv_addr = recv[1]
print("接受到来自:"+recv_addr+"的消息:"+recv_msg)

UDP_socket.close()

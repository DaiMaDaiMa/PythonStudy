"""
1.导入socket
2.创建socket对象
3.建立连接
4.发送数据
5.接收数据
6.关闭套接字

"""


import socket


tcp_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

tcp_socket.connect(("192.168.0.3", 7890))
 
tcp_socket.send("hellopython".encode())

recv_data = tcp_socket.recv(1024)

print(recv_data.decode("gbk"))

tcp_socket.close()
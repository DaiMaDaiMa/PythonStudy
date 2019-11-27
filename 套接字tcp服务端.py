"""
1.导入socket
2.创建socket对象
3.绑定端口
4.设置listen 主动变被动
5.等待客户端连接accept，返回新的socket，客户端ip和port
6.关闭所有的socket对象
"""


import socket


tcp_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

tcp_socket.bind(("", 8080))

tcp_socket.listen(128)

new_socket, ip_port = tcp_socket.accept()

recv_data = new_socket.recv(1024)

print("接收来自",str(ip_port),"的信息：",recv_data.decode("gbk"))

new_socket.close()

tcp_socket.close()
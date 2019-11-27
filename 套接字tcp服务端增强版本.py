"""
1.导入socket
2.创建socket对象
3.绑定端口
4.设置最大连接数
5.获取新的套接字对象
6.循环接收客户端信息
7.关闭所有套接字对象
"""


import socket

tcp_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

tcp_socket.bind(("", 8888))

tcp_socket.listen(128)


  
while True:  # 循环接收客户端连接
    new_socket, addr = tcp_socket.accept()
    while True:  # 循环处理当前客户端信息
        recv_data = new_socket.recv(1024)
        if len(recv_data) != 0:
            print("收到来自：",str(addr),"的消息：",recv_data.decode("gbk"))
        else:
            print("断开连接")
            break

    new_socket.close()

tcp_socket.close()


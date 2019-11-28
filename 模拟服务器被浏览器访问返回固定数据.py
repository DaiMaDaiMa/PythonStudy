"""
1.导入socket
2.创建socket对象
3.设置重复使用属性
4.绑定端口号
5.设置最大连接数
6.等待用户连接，并返回新的socket和客户端地址信息
7.判断客户端是否连接  未连接则提示并返回 连接则
8.拼接响应协议
9.发送数据给客户端
10.关闭套接字
"""

import socket

# 2.创建socket对象
tcp_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# 3.设置重复使用属性
tcp_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, True)
# 4.绑定端口号
tcp_socket.bind(("", 6789))
# 5.设置最大连接数
tcp_socket.listen(128)
# 6.等待用户连接，并返回新的socket和客户端地址信息
while True:
    new_socket, ip_port = tcp_socket.accept()
    # 7.判断客户端是否连接  未连接则提示并返回 连接则
    recv_data = new_socket.recv(1024)
    if not recv_data:
        print("客户端已断开连接")
        new_socket.close()

    # 8.拼接响应协议
    response_line = "HTTP/1.1 200 OK\r\n"
    response_heard = "Server:hello\r\n"
    response_blank = "\r\n"
    response_body = "Hello World"
    response_msg = response_line + response_heard + response_blank + response_body
    # 9.发送数据给客户端
    new_socket.send(response_msg.encode())
    # 10.关闭套接字
tcp_socket.close()

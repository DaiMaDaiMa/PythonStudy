"""
1.导入socket
2.创建socket对象
3.设置重复使用属性
4.绑定端口号
5.设置监听，最大连接数
6.等待客户端连接，返回新的socket和地址
7.获取客户端发来的信息，并判空
8.拼接响应协议
9.返回客户端信息
10.关闭套接字
"""
import socket
# 2.创建socket对象
tcp_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# 3.设置重复使用属性
tcp_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, True)
# 4.绑定端口号
tcp_socket.bind(("", 6788))
# 5.设置监听，最大连接数
tcp_socket.listen(128)
while True:
    # 6.等待客户端连接，返回新的socket和地址
    new_socket, ip_port =tcp_socket.accept()
    # 7.获取客户端发来的信息，并判空
    recv_data = new_socket.recv(1024)
    if not recv_data:
        print("客户端断开连接")
        new_socket.close()
    # 8.拼接响应协议
    response_line = "HTTP/1.1 200 OK\r\n"
    response_heard = "Server:hello\r\n"
    response_blank = "\r\n"

    with open("static/index.html", "rb") as file:
        response_body = file.read()

    response_msg = (response_line + response_heard + response_blank).encode() + response_body
    # 9.返回客户端信息
    new_socket.send(response_msg)
# 10.关闭套接字
tcp_socket.close()
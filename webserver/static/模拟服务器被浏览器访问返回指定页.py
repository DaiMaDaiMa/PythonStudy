"""
1.导入socket
2.创建socket对象
3.设置重复使用属性
4.绑定端口
5.设置监听，最大连接数
6.等待客户端连接，返回新的socket和地址
7.接收客户端信息并判空
8.获取客户端指定请求信息
9.拼接响应协议
10.返回信息给客户端
11.关闭套接字
"""

import socket
# 2.创建socket对象
tcp_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# 3.设置重复使用属性
tcp_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, True)
# 4.绑定端口
tcp_socket.bind(("", 7788))
# 5.设置监听，最大连接数
tcp_socket.listen(128)
while True:
    # 6.等待客户端连接，返回新的socket和地址
    new_socket, ip_port = tcp_socket.accept()
    # 7.接收客户端信息并判空
    recv_data =new_socket.recv(1024).decode()
    if not recv_data:
        print("客户端断开连接")
        new_socket.close()
    # 8.获取客户端指定请求信息
    # 第一次\r\n出现的位置
    first_index = recv_data.find("\r\n")
    # 获取第一行
    first_line = recv_data[0:first_index]
    # 以空格分割第一行
    first_list = first_line.split(" ")
    # 获取客户端的目的地址
    final_page = first_list[1]
    if final_page == "/":
        final_page = "/index.html"
    # 9.拼接响应协议
    response_line = "HTTP/1.1 200 OK\r\n"
    response_heard = "Server:hello\r\n"
    response_blank = "\r\n"
    try:
        with open("static"+final_page, "rb") as file:
            response_body = file.read()
    # 10.返回信息给客户端
    except Exception as e:
        response_line = "HTTP/1.1 404 NOT FOUND"
        response_body = "ERR"+str(e)
        response_body = response_body.encode()
       
    response_msg = (response_line + response_heard + response_blank).encode() + response_body
    new_socket.send(response_msg)
# 11.关闭套接字
tcp_socket.close()
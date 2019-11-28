"""
1.导入socket
2.创建socket对象
3.连接服务器
4.拼接请求协议 
  请求行  GET/POST / HTTP/1.1
  请求头  Host:www.baidu.com
  请求空行 \r\n
5.发送请求消息给服务器
6.接收返回的消息
7.保存消息
8.关闭套接字
"""

import socket

# 2.创建socket对象
tcp_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# 3.连接服务器
tcp_socket.connect(("www.baidu.com", 80))
# 4.拼接请求协议 
#   请求行  GET/POST / HTTP/1.1
request_line = "GET / HTTP/1.1\r\n"
#   请求头  Host:www.baidu.com
request_heard = "Host:wwww.baidu.com\r\n"
#   请求空行 \r\n
request_blank = "\r\n"

request_msg = request_line + request_heard + request_blank
# 5.发送请求消息给服务器
tcp_socket.send(request_msg.encode())
# 6.接收返回的消息
recv_data = tcp_socket.recv(1024).decode()
# print(recv_data)
# 7.保存消息
  # 截取信息
rn_4 = recv_data.find("\r\n\r\n")
recv_msg = recv_data[rn_4+4:]
  # 保存信息
with open("baidu.html", "w") as file:
    file.write(recv_msg)
print(recv_msg)
# 8.关闭套接字
tcp_socket.close()

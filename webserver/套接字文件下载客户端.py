"""
1.导入socket
2.创建socket对象
3.连接服务器
4.获取文件名
5.将文件名发送给服务端
6.接收返回的文件数据并保存
7.关闭socket
"""


import socket


# 1.导入socket
# 2.创建socket对象
tcp_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# 3.连接服务器
tcp_socket.connect(("192.168.0.3", 4567))
# 4.获取文件名
file_name = input("请输入您要下载的文件名:")
# 5.将文件名发送给服务端
tcp_socket.send(file_name.encode())

with open(file_name+"[复件]", "wb") as file:
    while True:
        file_data= tcp_socket.recv(1024)
        if file_data:
          file.write(file_data)
        else:
            break     
# 7.关闭socket
tcp_socket.close()


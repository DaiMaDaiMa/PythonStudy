"""
1.导入socket
2.创建socket对象
3.绑定端口号
4.设置最大连接数
5.等待客户端连接
6.获取文件名
7.打开文件并读取内容
8.发送内容给客户端
9.关闭socket
"""

# 1.导入socket
import socket
# 2.创建socket对象
tcp_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# 设置地址可以重用，目的是解决短时间内重启服务器时报的地址错误
tcp_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, True)
# 3.绑定端口号
tcp_socket.bind(("", 4567))
# 4.设置最大连接数
tcp_socket.listen(128)
while True:
    # 5.等待客户端连接
    new_socket, addr = tcp_socket.accept()
    try:
        # 6.获取文件名
        file_name = new_socket.recv(1024)

        with open(file_name, "rb") as file:
            while True:
                file_data = file.read()
                if file_data:
                    new_socket.send(file_data)
                else:
                    break
    except Exception as e:
        print("下载失败，%s" %file_name)
    else:
        print("下载成功，%s" %file_name)

        # 9.关闭socket
    new_socket.close()
tcp_socket.close()
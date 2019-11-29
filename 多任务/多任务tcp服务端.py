"""
1.导入socket 
2.创建socket对象
3.设置重复使用属性
4.绑定端口
5.设置监听
6.等待连接
7.接收消息
8关闭套接字

"""

import socket
import threading


def main():
    tcp_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    tcp_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, True)
    tcp_socket.bind(("", 9090))
    tcp_socket.listen(128)
    while True:

        new_socket, ip_port = tcp_socket.accept()
        # 每次有一个新连接，就创建一个新的线程，在子线程处理新的事务
        t = threading.Thread(target=recv_msg, args=(new_socket, ip_port))
        t.setDaemon(True)
        t.start()

        # recv_data = new_socket.recv(1024)
        # print("收到来自%s的消息：%s" % (str(ip_port), recv_data.decode("gbk"))

    tcp_socket.close()


def recv_msg(new_socket, ip_port):
    while True:
        recv_data = new_socket.recv(1024)
        if recv_data:
            print("收到来自%s的消息：%s" % (str(ip_port), recv_data.decode("gbk")))
        else:
            break
    new_socket.close()


if __name__ == "__main__":
    main()

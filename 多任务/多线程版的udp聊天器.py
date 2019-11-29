"""
1.创建子线程，在子线程中，完成数据的接收展示
2.主线程中，完成数据的发送
"""
import threading
import socket


def main():
    # 创建套接字对象
    udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    udp_socket.bind(("", 9090))
    # 创建多线程对象
    recv_thread = threading.Thread(target=recv_msg, args=(udp_socket, ))
    recv_thread.setDaemon(True)
    # recv_thread.setDaemon(True)
    recv_thread.start()

    while True:
        # 获取需要发送的消息
        send_msg = input()
        if not send_msg:
            udp_socket.close()
            break
        # 发送消息
        udp_socket.sendto(send_msg.encode("gbk"), ("192.168.0.3", 9999))


def recv_msg(udp_socket):
    # 获取发送过来的信息
    while True:
        recv_data = udp_socket.recvfrom(1024)
        if not recv_data:
            udp_socket.close()
            break
        msg = recv_data[0].decode("gbk")
        addr = recv_data[1]
        print("收到来自", str(addr), "回复：", msg)


if __name__ == "__main__":
    main()

import socket


def main():

    udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    udp_socket.bind(("", 8888))

    while True:

        print("*********************************")
        print("**********   1.发送消息  *********")
        print("**********   2.接收消息  *********")
        print("**********   3.退出系统  *********")
        print("*********************************")
        
        get_slect = int(input("请输入您的选择"))

        if get_slect == 1:
            send_msg(udp_socket)
        elif get_slect ==2:
            recv_msg(udp_socket)
        elif get_slect ==3:
            print("退出系统")
            break
        
    udp_socket.close()




def recv_msg(udp_socket):
    recv = udp_socket.recvfrom(1024)

# recv 接受的是一个元祖（消息，（ip，port）），第一个元素是接收到的消息二进制，第二个元素是对方的（ip，port）


    recv_msg = recv[0].decode("gbk")
    recv_addr = recv[1]
    print("接受到来自:"+str(recv_addr)+"的消息:"+recv_msg)


def send_msg(udp_socket):
    get_msg = input("请输入您要发送的信息：")
    get_ip = input("请输入您的ip:")
    get_port = int(input("请输入您的端口号："))

    udp_socket.sendto(get_msg.encode(), (get_ip, get_port))


if __name__ == "__main__":
    main()
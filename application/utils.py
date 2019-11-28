def creat_response(status, recv_data):
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
    response_line = "HTTP/1.1 %s\r\n" % status
    response_heard = "Server:hello\r\n"
    response_blank = "\r\n"

    return (final_page, response_line, response_heard, response_blank)

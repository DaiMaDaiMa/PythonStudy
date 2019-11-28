from application import utils


def fiel_path(status, recv_data):
    # # 8.获取客户端指定请求信息
    # # 第一次\r\n出现的位置
    # first_index = recv_data.find("\r\n")
    # # 获取第一行
    # first_line = recv_data[0:first_index]
    # # 以空格分割第一行
    # first_list = first_line.split(" ")
    # # 获取客户端的目的地址
    # final_page = first_list[1]
    # if final_page == "/":
    #     final_page = "/index.html"
    # # 9.拼接响应协议
    # response_line = "HTTP/1.1 200 OK\r\n"
    # response_heard = "Server:hello\r\n"
    # response_blank = "\r\n"
    response_info = utils.creat_response(status, recv_data)
    try:
        with open("static"+response_info[0], "rb") as file:
            response_body = file.read()

    # 10.返回信息给客户端
    except Exception as e:
        response_line = "HTTP/1.1 404 NOT FOUND"
        response_body = "ERR"+str(e)
        response_body = response_body.encode()

    response_msg = (response_info[1] + response_info[2] +
                    response_info[3]).encode() + response_body

    return response_msg

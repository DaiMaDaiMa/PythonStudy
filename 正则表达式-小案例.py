import re
# 1.验证手机号码，必须以1开头，第二位可以是34578，后面9位随意
text = "13345678901"
ret = re.match("1[34578]\d{9}", text)
print(ret.group())

# 2.验证邮箱：邮箱的规则是邮箱名称使用数字，下划线组成，然后是@符号，后面就是域名
text = "357086556@qq.com"
# ret = re.match("\d*@\w*.\w*", text)
ret = re.match("\w+@\w+.\w+", text)
print(ret.group())
# 3.验证URL：URL规则是前面是http或者https或者是ftp然后加上冒号，再加上一个斜杠。再后面就是任意的非空白字符
text = "http://wwww.baidu.com"
ret = re.match("(http|https|ftp)://[^\s]+", text)
print(ret.group())
# 4.验证身份证：规则是，总共18位，前面17位是数字，最后一位可以是数字，也可以说是小写的字母x也可以是大写的字母X
text = "320722199007258138"
ret = re.match("\d{17}(\d|x|X)", text)
print(ret.group())
# 5.匹配1-100之间的数字
text = "100"
ret = re.match("[1-9]\d?$|100$", text)
print(ret.group())
# 6.sub实例
text = "<hello>你好吗<hello>我很好<hello>"
ret = re.sub("<.+?>", "", text)  # 将所有的<>删除，只保留中文的部分
print(ret)

import re
# 1.match:匹配某个字符串
text = "hello"
ret = re.match("he", text)
print(ret.group())
# 2.点：匹配任意的一个字符，\n除外
text = "hello"
ret = re.match(".", text)
print(ret.group())
# 3.\d：匹配任意的一个数字（0-9）
text = "91"
ret = re.match("\d", text)
print(ret.group())
# 4.\D：匹配任意的一个非数字 
text = "hello"
ret = re.match("\D", text)
print(ret.group())
# 5.\S：匹配空白一个字符（\n, \t ,\r, 空格）
text = " \nhello"
ret = re.match("\s", text)
print(ret.group())
# 6.\w：匹配a-z.A-Z.数字和下划线
text = "hello"
ret = re.match("\w", text)
print(ret.group())
# 7.\W：与\w 相反
text = "+hello"
ret = re.match("\W", text)
print(ret.group())
# 8.[]:只要满足中括号中的字符
text = "025-8138"
ret = re.match("[\d\-]+", text)  # \- 是一个转义用法，+ 表示前面的字符匹配一次或多次
print(ret.group())
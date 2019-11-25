import re
# 9.* 匹配0或者任意多个字符
text = "hello"
ret = re.match("\w*", text)
print(ret.group())
# 10.+：匹配一个或者多个字符，如果第一个字符就不匹配，则为空
text = "hello"
ret = re.match("\w+", text)
print(ret.group())
# 11.？：匹配0个或者1个字符
text = "hello"
ret = re.match("\w?", text)
print(ret.group())
# 12.{m}：匹配m个字符
text = "hello"
ret = re.match("\w{3}", text)
print(ret.group())
# 13.{m,n}：匹配m-n个字符
text = "hello"
ret = re.match("\w{1,3}", text)  # 最多匹配到3个字符。最低一个字符
print(ret.group())
# 14.^：表示以。。。。开始  在【】中表示取反
text = "hello"  # match本身就是匹配第一个字符，search会在整个字符串内查找
ret = re.match("^h", text)
print(ret.group())
# 15.$：表示以。。。。结尾
text = "hello"
ret = re.search("lo$", text)
print(ret.group())
# 16.|：匹配多个字符串或表达式
text = "java"
ret = re.search("hello|java", text)
print(ret.group())
# 17：贪婪模式
text = "<hello><hello><hello>"
ret = re.search("<.+>", text)
print(ret.group())
# 18：非贪婪模式
text = "<hello><hello><hello>"
ret = re.search("<.+?>", text)
print(ret.group())
# 19:group 分组
text = "the apple price is $100,and python price is $200"
ret = re.match(".+(\$\d+).+(\$\d+)", text)
print(ret.group(1))  # 取出分组中的第一个子组
print(ret.group(2))  # 取出分组中的第二个子组
print(ret.group(0))  # 取出全部
print(ret.group())   # 取出全部
# 20:findall 找出所有符合条件的元素，以列表的形式返回
text = "the apple price is $100,and python price is $200"
ret = re.findall("\$\d+", text)
print(ret)
# 21:sub 替换
text = "the apple price is $100,and python price is $200"
ret = re.sub("\$\d+", "0", text)
print(ret)
# 22:split 以"""规则，分割字符串 返回一个列表
text = "the apple price is $100,and python price is $200"
ret = re.split(" ", text)
print(ret)
# 23:compile
text = "the apple price is $100.00,and python price is $100.00"
# r = re.compile("\d+.\d+")
# ret = re.search(r, text)
# print(ret.group())
r = re.compile(
    r"""
    \d+ # 小数点前面的数
    .  # 小数点
    \d+  # 小数点后面的数
    """, re.VERBOSE)
ret = re.search(r, text)
print(ret.group())

hello_str = "hello hello"

# 1. 统计字符串长度
print(len(hello_str))
# 2. 统计某一个小字符串穿线的次数
print(hello_str.count("llo"))
print(hello_str.count("laa"))

# 3. 某一个字符串出现的位置
print(hello_str.index("llo"))
# print(hello_str.index("lloo"))
# 要求：
# 1. 将字符串中的空白字符串全部去掉
# 2. 再使用个" "作为分隔符，拼接城一个整齐的字符串
poem_str = "登鹳雀楼\t王之涣\t白日依山尽\t\n黄海入海流\t\t欲穷千里目\t更上一层楼"

print(poem_str)
# 1. 拆分字符串
poem_list = poem_str.split()
print(poem_list)
# 2. 合并字符串
result = " ".join(poem_list)
print(result)
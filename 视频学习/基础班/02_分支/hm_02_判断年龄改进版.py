# 输入用户年龄
age = int(input("请输入年龄："))
# 判断是否满１８岁
if age >= 18:
    # 如果满１８岁，允许进网吧
    print("你已经成年，欢迎！")
else:
    # 如果未满１８岁，提示回家写作业
    print("你还没有成年，回家去！")
print("这句代码什么时候执行？")
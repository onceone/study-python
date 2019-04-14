xiaoming = {"name":"小明",
            "age":18}

# 1. 统计键值对数量
print(len(xiaoming))

# 2. 合并字典
temp = {"height":1.75,
        "age":20}
xiaoming.update(temp)

# 3. 清空字典
xiaoming.clear()

print(xiaoming)
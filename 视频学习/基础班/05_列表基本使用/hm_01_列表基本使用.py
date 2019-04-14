name_list = ["zhangsan","lisi","wangwu"]

# 1. 取值和取索引
print(name_list[1])

print(name_list.index("lisi"))

# 2. 修改
name_list[1] = "李四"

# 3. 增加
name_list.append("王小二")
name_list.insert(1,"小明")

temp_list = ["孙悟空","朱二哥","沙师弟"]

name_list.extend(temp_list)

# 4. 删除
name_list.remove("wangwu")

name_list.pop()

name_list.pop(3)

name_list.clear()





print(name_list)
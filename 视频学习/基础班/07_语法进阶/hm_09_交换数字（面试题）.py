a = 6
b = 100

#　解法１．使用其他变量
# c = a
# a = b
# b = c

# 解法２．不使用其他变量
# a = a + b
# b = a - b
# a = a -b

# 解法３．Python专有
# a,b = (b,a)
a,b = b,a

print(a)
print(b)
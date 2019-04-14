import random
player = int(input("请输入你要输入的拳石头（１）剪刀（２）布（３）："))
computer = random.randint(1,3)


print("玩家选择的拳头是%d-电脑出的拳头是%d"%(player,computer))

if((player ==1 and computer ==2)
        or (player ==2 and computer ==3)
        or(player ==3 and computer ==1)):

    print("恭喜玩家胜利！")

elif player == computer:
    print("平局！")

else:
    print("电脑赢了！")

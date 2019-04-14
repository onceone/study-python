has_ticket = True
knife_length = 10

if has_ticket:
    print("车票检查通过")

    if knife_length > 20:
        print("你携带的刀太长了,有%d公分"%knife_length)
        print("不允许上车!")

    else:
        print("安检通过！")
else:
    print("大哥，请先买票")
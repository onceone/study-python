class Cat:

    def eat(self):
        # 哪一个对象调用的方法，self就是哪一个对象的引用
        print("%s爱吃鱼"%self.name)

    def drink(self):
        print("%s要喝水"%self.name)

# 创建猫对象
tom = Cat()

# 可以使　.属性名，利用赋值语句就可以了
tom.name = "Tom"

tom.eat()
tom.drink()

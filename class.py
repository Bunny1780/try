# class Cat:
#     a = 123
#     def hi():
#         print("Hi there")

# Cat.hi() 
# print(Cat.a)

# Cat.hi # 類別方法
# kitty = Cat() # 實體/實例/instance
# kitty.hi() # 實體方法
# # 當使用實體方式去使用 hi() function, kitty就會成為 hi()的回傳值, 自己是自己的回傳值

# class Cat:
#     a = 123
#     def hi(self):
#         print(self)
#         print("Hi there")

# kitty = Cat() # 實體/實例/instance
# kitty.hi() # 實體方法

class Cat:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def say_hi(self):
        print(f"Hello {self.name}")

kitty = Cat("Kitty", 18)
kitty.say_hi()
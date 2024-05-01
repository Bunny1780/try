# if
# weather = "sunny"

# if weather == "rain":
#     print("下雨天")
# elif weather == "sunny":
#     print("出太陽")
# elif weather == "cloudy":
#     print("多雲")
# else:
#     print("不知道")

# match
# weather = "rain"

# match weather:
#     case "rain":
#         print("下雨天")
#     case "sunny":
#         print("出太陽")
#     case "cloudy":
#         print("多雲")
#     case something: # 就像 else只是在match會給個變數
#         print(f"我不知道 {something} 是什麼天氣")

# data = "123"
# match data:
#     case int() | float():
#         print("整數")
#     case str():
#         print("字串")
#     case _:
#         print("其他型別")

# user_data = [1, "悟空", 18]

# match user_data:
#     case [id, name, age]:
#         print(f"{id} - 我是{name}，我今年{age}")
#     case _:
#         print("HI")

# user_data = [99, "Leo", 18]
# match user_data:
#     case [id, _, _]:
#         print(f'會員編號{id}')
#     case _:
#         print("HI")

# user_data = {"name": "Kitty", "gender": "female"}
# match user_data:
#     case {"gender" : "male", "name" : name}:
#         print(f"{name}先生您好")
#     case {"gender" : "female", "name" : name}:
#         print(f"{name}小姐您好")

# number = [10, 0]
# match number:
#     case x, y if y != 0:
#         print(x / y)
#     case _:
#         print("第二個數字不能為零！")

# number = [1, 2, 3, 4, 5]
# match number:
#     case _, *other:
#         print(other)
#     case _:
#         print("Hello Python")

# 遞迴
def fib(n):
    match n:
        case n if n < 2:
            return n
        case _:
            return fib(n - 1) + fib(n - 2)
print(fib(6)) # 第 6 項 = 8
print(fib(8)) # 第 8 項 = 21


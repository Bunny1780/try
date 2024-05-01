
# import datetime
# the_date = datetime.date(2000, 8, 17)
# print(f"{the_date:%Y/%m/%d}")

message = "hellokitty"
a = message[:5]
print(message)
print(a)
print(a is message[:5]) # false

# a = 256
# b = 255
# print(a == b)
# print(a is b)


# num = [1, 2, 3]
# result = []
# for i in num:
#     result.append(i * 2)

# print(result)

# nums = [1, 2, 3, 4, 5]
# result = [n * 2 for n in nums]
# print(result)

# message = "hellokitty"
# a = message[:5]
# b = message[:]

# print("message", id(message))
# print("message_slice", id(message[:]))
# print("a", id(a))
# print("message[:5]", id(message[:5]))
# print("b", id(b))

original_str = "hellokitty"

# original_list = [1, 2, 3, 4, 5]
sliced_str = original_str[1:4]

print(original_str)  # 输出：[1, 2, 3, 4, 5]
print(sliced_str)    # 输出：[2, 3, 4]

print(original_str)  # 输出：[1, 2, 3, 4, 5]
print(sliced_str)    # 输出：[100, 3, 4]
# String unpacking
a, b, c, d, e = "Hello"
print(a, b, c, d, e)
# output: H e l l o

# *
heroes = ["悟空", "鳴人", "流川楓"]

name, *other = heroes
print(name)
print(other)

# *_ unpacking
data = ["弗利沙", [10, 20], (1, 23, 530000)]
name, *_, (*_, power) = data
print(name)
print(power)

# 開箱運算子 Unpacking Operator
print(list(range(5))) # [0, 1, 2, 3, 4]
print([*range(5)])    # [0, 1, 2, 3, 4]

# 用開箱運算子相加串列
comic_heroes = ["孫悟空", "魯夫", "宇智波佐助", "琦玉"]
marvel_heroes = ["金剛狼", "鋼鐵人", "奇異博士"]

all_heros = [*comic_heroes, *marvel_heroes]
print(all_heros)

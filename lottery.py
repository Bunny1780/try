# 1 ~ 49
# 不重複
# 由小到大
import random
def get_lottery(n):
    result = set()
    for i in range(n):
        result.add(random.randint(1,50))
    return sorted(result)

print(get_lottery(6)) # [1, 2, 3, 7, 10, 12]
print(get_lottery(3)) # [7, 10, 12]
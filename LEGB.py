# ----- global, enclosing, local -----
a = 0 # global

def fn_out():
    a = 1 # enclosing
    def fn_inner():
        a = 3 # local
        print(a)
    fn_inner()
fn_out()
# ----- global, enclosing, local -----

# ----- nonlocal -----

count = 1
def a():
    count = 100 # enclosing
    def b():
        nonlocal count # 指不在我這區域去enclosing找
        count += 1
        print(count)
    b()
a()

# ----- nonlocal -----

# ----- breakpoint -----
def add(x, y):
    breakpoint()
    return x + y
print(add(3, 4))
# ----- breakpoint -----



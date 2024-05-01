def print_stars(n):
    n *= 2
    for i in range(1, 10, 2):
        print(f"{'*' * i:^{n}}")
    print(f"{'*':^{n}}")
    print(f"{'*':^{n}}")
print_stars(5)
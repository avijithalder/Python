n = 5
def fact(n):
    if n == 0:
        return 1
    return n * fact(n - 1)


r = fact(5)
print(r)

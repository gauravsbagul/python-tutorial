def fact(n: object) -> object:
    if n == 0:
        return 1
    return n * fact(n - 1)


print(fact(5))

f = lambda a, b : a + b

print(f(5,4))

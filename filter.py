from functools import reduce

nums = [2, 3, 6, 8, 7, 5, 6, 9, 1]

evens = list(filter(lambda n: n % 2 == 0, nums))

print(evens)

doubles = list(map(lambda n: n * 2, evens))

print(doubles)

sum = reduce(lambda a, b: a + b, doubles)

print(sum)
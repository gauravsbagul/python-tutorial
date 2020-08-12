from typing import List

nums: List[int] = [12, 13, 18, 21, 26, 24]

for num in nums:
    if num % 5 == 0:
        print(num)
        break
else:
    print('not found')

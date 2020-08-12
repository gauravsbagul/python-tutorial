from numpy import *

vals: ndarray = array([5, 9, 8, 4, 2.4])
# print(vals)


arr = logspace(1, 40, 5)
# print('%.2f' % arr[4])

arr1  = array([
    [1, 2, 3, 6],
    [4, 5, 6, 7],
])

# print(arr1)

m1 = asmatrix('1 2 3; 6 4 5; 1 6 7')
m2 = asmatrix('1 2 3; 6 8 5; 1 6 7')

m3 = m1 * m2
print(m3)

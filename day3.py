import numpy as np
from functools import reduce

f = open('day3.data', 'r')
data = f.readlines()
data = np.array([list(d.rstrip()) for d in data])
data = np.tile(data, 500)
slopes = [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)]
answers = []
for right, down in slopes:
    row = down
    col = right
    num_trees = 0
    while row < data.shape[0]:
        loc = data[row, col]
        if loc == '#':
            num_trees += 1
        row += down
        col += right
    answers.append(num_trees)

print(reduce(lambda x, y: x * y, answers))

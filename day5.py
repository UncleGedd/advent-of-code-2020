import numpy as np

f = open('day5.data', 'r')
data = f.readlines()
data = [d.rstrip() for d in data]
NUM_ROWS = 127
NUM_COLS = 7

boarding_ids = []
seat_matrix = np.zeros((NUM_ROWS + 1, NUM_COLS + 1))
for boarding_pass in data:
    rows = range(0, NUM_ROWS + 1)
    for r in boarding_pass[:6]:
        rows = rows[:len(rows) // 2] if r == 'F' else rows[len(rows) // 2:]
    finalRow = min(rows) if boarding_pass[6] == 'F' else max(rows)

    cols = range(0, NUM_COLS + 1)
    for s in boarding_pass[NUM_COLS:-1]:
        cols = cols[:len(cols) // 2] if s == 'L' else cols[len(cols) // 2:]
    finalCol = min(cols) if boarding_pass[-1] == 'L' else max(cols)
    id = finalRow * 8 + finalCol
    boarding_ids.append(id)
    seat_matrix[finalRow, finalCol] = 1

print(max(boarding_ids))  # debug here and look at seat_matrix to find your seat!

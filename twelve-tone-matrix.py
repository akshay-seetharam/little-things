tone_row = []
for i in range(12):
    tone_row.append(int(input('Enter next pitch: ').strip()) % 12)

import numpy as np
matrix = np.zeros((12, 12))
matrix[0] = [i for i in tone_row]

i = 1
while i < 12:
    matrix[i][0] = (matrix[0][0] * 2 - matrix[0][i]) % 12
    j = 1
    while j < 12:
        matrix[i][j] = (matrix[i][0] + matrix[0][j] - matrix[0][0]) % 12
        j += 1
    i += 1

print(matrix)

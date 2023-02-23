import random

def preferred(opt1, opt2):
    result = int(input(f'Do you prefer {opt1} (enter 1) or {opt2} (enter 2)?'))
    while result != 1 and result != 2:
        result = input(f'Do you prefer {opt1} (enter 1) or {opt2} (enter 2)?')
    return result == 1

def mergeSort(arr):
    if len(arr) > 1:

        # Finding the mid of the array
        mid = len(arr) // 2

        # Dividing the array elements
        L = arr[:mid]

        # into 2 halves
        R = arr[mid:]

        # Sorting the first half
        mergeSort(L)
        print('peek behind the curtain', L)

        # Sorting the second half
        mergeSort(R)
        print('peek behind the curtain', R)

        i = j = k = 0

        # Copy data to temp arrays L[] and R[]
        while i < len(L) and j < len(R):
            if preferred(L[i], R[j]):
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[j]
                j += 1
            k += 1

        # Checking if any element was left
        while i < len(L):
            arr[k] = L[i]
            i += 1
            k += 1

        while j < len(R):
            arr[k] = R[j]
            j += 1
            k += 1


src = 'ts_songs.txt'
with open(src, 'r') as f:
    lines = f.readlines()

random.shuffle(lines)

i = 0
while i < len(lines):
    lines[i] = lines[i][:-1]
    i += 1

mergeSort(lines)
print(lines)

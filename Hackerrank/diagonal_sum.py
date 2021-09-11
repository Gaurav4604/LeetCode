def diagonalDifference(arr):
    # Write your code here
    index = 0
    total_left = 0
    total_right = 0
    for i in arr:
        total_left += i[index]
        total_right += i[-(index + 1)]
        index+= 1
    return abs(total_left - total_right)

arr = [
    [11, 2, 4],
    [4, 5, 6],
    [10, 8, -12]
]

print(diagonalDifference(arr))
# 회전 연습
arr = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]


def print_arr(arr):
    for i in range(len(arr)):
        print(arr[i])


print("시계방향")
print_arr(list(zip(*arr[::-1])))

print("반시계")
print_arr(list(zip(*arr))[::-1])

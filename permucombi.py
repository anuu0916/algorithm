# 순열 조합 연습
import itertools
arr = [1, 2, 3]
r = 2
n = len(arr)


def permutation(arr, r):
    arr = sorted(arr)
    used = [0] * n
    result = []

    def generate(chosen, used):
        if len(chosen) == r:
            result.append(chosen)
            return

        for i in range(n):
            if used[i] == 0:
                chosen.append(arr[i])
                used[i] = 1
                generate(chosen[:], used)
                used[i] = 0
                chosen.pop()

    generate([], used)
    return result


def combination(arr, r):
    arr = sorted(arr)
    result = []

    def generate(chosen):
        if len(chosen) == r:
            result.append(chosen)
            return

        start = arr.index(chosen[-1]) + 1 if chosen else 0
        for i in range(start, n):
            chosen.append(arr[i])
            generate(chosen[:])
            chosen.pop()

    generate([])
    return result


print(permutation(arr, r))
print(combination(arr, r))
print(list(itertools.permutations(arr, 2)))

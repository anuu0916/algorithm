# 15649 N과 M (1)
n, m = map(int, input().split())


def permutation(n, m):
    used = [0] * (n + 1)

    def generate(chosen, used):
        if len(chosen) == m:
            print(" ".join(map(str, chosen)))

        for i in range(1, n+1):
            if used[i] == 0:
                used[i] = 1
                chosen.append(i)
                generate(chosen, used)
                chosen.pop()
                used[i] = 0

    generate([], used)


permutation(n, m)

# 20437 문자열 게임 2
T = int(input())

for _ in range(T):
    w = input()
    k = int(input())

    if k == 1:
        print("1 1")
        continue
    
    cnt_dir = {
        "a":0, "b":0, "c":0, "d":0, "e":0, "f":0, "g":0,
        "h":0, "i":0, "j":0, "k":0, "l":0, "m":0, "n":0,
        "o":0, "p":0, "q":0, "r":0, "s":0, "t":0, "u":0,
        "v":0, "w":0, "x":0, "y":0, "z":0
    }

    dir = {
        "a":[], "b":[], "c":[], "d":[], "e":[], "f":[], "g":[],
        "h":[], "i":[], "j":[], "k":[], "l":[], "m":[], "n":[],
        "o":[], "p":[], "q":[], "r":[], "s":[], "t":[], "u":[],
        "v":[], "w":[], "x":[], "y":[], "z":[]
    }

    for i in range(len(w)):
        dir[w[i]].append(i)
        cnt_dir[w[i]] += 1

    if max(cnt_dir.values()) < k:
        print(-1)
        continue
    
    shortest = int(1e5)
    longest = 0
    for key, value in dir.items():
        if cnt_dir[key] < k:
            continue
        # print("----------%c--------"%key)
        # print(dir[key])
        for i in range(len(dir[key]) - (k-1)):
            # print(i, dir[key][i], dir[key][i+k-1])
            shortest = min(shortest, dir[key][i+k-1] - dir[key][i] + 1)
            longest = max(longest, dir[key][i+k-1] - dir[key][i] + 1)
    
    print(shortest, longest)
    
    

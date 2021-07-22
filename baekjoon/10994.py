#10994 별 찍기 - 19
num = int(input())
last = 4 * (num-1) + 1
middle = int(last/2) + 1
cnt = 1

for i in range(last, middle, -1):
    if i % 2 == 1:
        if i == last:
            print("*"*last)
        else:
            print("* " * cnt, end="")
            print("*" * (last - cnt * 4), end="")
            print(" *" * cnt)
            cnt += 1
    else:
        print("* "*cnt, end="")
        print(" "*(last - cnt * 4), end="")
        print(" *"*cnt)

print("* "*middle)

for i in range(middle+1, last+1):
    if i % 2 == 1:
        if i == last:
            print("*"*last)
        else:
            print("* " * cnt, end="")
            print("*" * (last - cnt * 4), end="")
            print(" *" * cnt)
    else:
        print("* "*cnt, end="")
        print(" "*(last - cnt * 4), end="")
        print(" *"*cnt)
        cnt -= 1

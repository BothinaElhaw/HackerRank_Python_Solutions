n = int(input())
arr = list(map(int, input().split()))
maximum=arr[0]
runner=-10000000
for x in arr:
    if x > maximum:
        runner=maximum
        maximum=x
    elif x!= maximum and x>runner:
        runner=x
print(runner)
        
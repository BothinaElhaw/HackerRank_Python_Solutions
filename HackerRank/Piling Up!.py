def check(arr):
    top = float('inf')
    while arr:
        if arr[0] >= arr[-1]:
            x = arr.pop(0)
        else:
            x = arr.pop()
        if x > top:
            return "No"

        top = x
    return "Yes"
t = int(input())

for i in range(t):
    n = int(input())
    arr = list(map(int, input().split()))
    print(check(arr))
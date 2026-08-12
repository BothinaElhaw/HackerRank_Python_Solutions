def average(array):
    s = set(array)
    total = sum(s)
    count = len(s)
    return total / count

if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    result = average(arr)
    print(result)
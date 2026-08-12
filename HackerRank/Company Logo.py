if __name__ == '__main__':
    s = input()

    count = {}

    for ch in s:
        if ch in count:
            count[ch] += 1
        else:
            count[ch] = 1

    items = list(count.items())

    items.sort(key=lambda x: (-x[1], x[0]))

    for i in range(3):
        print(items[i][0], items[i][1])
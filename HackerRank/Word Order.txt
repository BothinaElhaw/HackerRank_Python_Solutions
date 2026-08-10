n = int(input())

words_count = {}

for i in range(n):
    word = input().strip()
    
    if word in words_count:
        words_count[word] += 1
    else:
        words_count[word] = 1

print(len(words_count))

for count in words_count.values():
    print(count, end=" ")

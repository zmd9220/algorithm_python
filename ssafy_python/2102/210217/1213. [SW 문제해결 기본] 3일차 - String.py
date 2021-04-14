
for t in range(10):
    n = int(input())
    word = input()
    sentence = input()
    cnt = 0
    for i in range(len(sentence)):
        if sentence[i] == word[0]:
            found = True
            for j in range(1, len(word)):
                if i+j >= len(sentence) or sentence[i+j] != word[j]:
                    found = False
                    break
            if found:
                cnt += 1
    print(f'#{n} {cnt}')
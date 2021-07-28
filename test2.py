def solution(S):
    S1 = S.split('\n')
    answer = 0
    for i in range(len(S1)):
        words = S1[i].lstrip().split(' ')
        print(words)
        # K = 통과, M은 14이하, G는 무조건 통과 X
        if words[0][-1] == 'G':
            continue
        elif words[0][-1] == 'M':
            # print(int(words[0][:-1]))
            if int(words[0][:-1]) < 14:
                continue

        date = words[1].split('-')
        if int(date[0]) < 1990:
            continue
        # 1월은 위에 1990년 이후면 모두 1990년 1월 이후임
        # 즉 1990년 1월인데 31일 이전인 경우만 예외 (1990년 일때)
        if int(date[0]) == 1990 and int(date[1]) == 1 and int(date[2]) < 31:
            continue

        # 백업 파일 여부 tilde character
        if words[2][-1] != '~':
            continue
        answer += 1
    if answer == 0:
        return 'NO FILES'
    return str(answer)


s = """ 715K 2009-09-23 system.zip~
 179K 2013-08-14 to-do-list.xml~
 645K 2013-06-19 blockbuster.mpeg~
  536 2010-12-12 notes.html
 688M 1990-02-11 delete-this.zip~
  23K 1987-05-24 setup.png~
 616M 1965-06-06 important.html
  14M 1992-05-31 crucial-module.java~
 192K 1990-01-31 very-long-filename.dll~"""
# print(s.split('\n'))
# print(s)
ans = solution(s)
print(ans)

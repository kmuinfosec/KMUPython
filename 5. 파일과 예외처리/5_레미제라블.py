# 레 미제라블
# 리눅스
# f = open("파일 경로/Les_Miserables-Victor_Hugo.txt", "r", encoding="949")
# 윈도우
f = open("파일 경로/Les_Miserables-Victor_Hugo.txt", "r")
file = f.read()
f.close()

# 특수 기호 제거, 대문자로 통일, 공백 기준으로 나눔
words_arr = file.replace(",", "").replace(".", "").replace("?", "").replace("!", "").replace('"', '')\
            .replace("'", "").replace("#", "").replace("^", "").replace("&", "").replace("*", "").replace("(", "")\
            .replace(")", "").replace("-", "").replace(";", "").replace(":", "").replace("<", "").replace(">", "")\
            .replace("/", "").upper().split()

# 단어별 등장 횟수 기록
word_cnt = {}
for w in words_arr:
    if w in word_cnt:
        word_cnt[w] += 1
    else:
        word_cnt[w] = 1

# 등장 횟수 기준 정렬
sor = sorted(word_cnt.items(), key=lambda x: x[1], reverse=True)

# 10순위까지 출력
rank = 1
for w, cnt in sor:
    if rank > 10:
        break
    else:
        print("{R}순위) {W} : {Z}".format(R=rank, W=w, Z=cnt/sor[0][1]))
        rank += 1

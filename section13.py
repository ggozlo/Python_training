# Section 13 - 1
# 업그레이드 타이핑 게임 제작
# 타이핑 게임 제작 및 기본 완성 

import random
import time 
# 사운드 출력 모듈 
import winsound
import sqlite3
import datetime

# DB 생성 & auto 커밋
# 본인 DB 경로
conn = sqlite3.connect('E:/python/python_training/resource/records.db', isolation_level=None) #sql 파일을 연결 없으면 생성, 자동커밋 설정

# 커서 연결
cursor = conn.cursor() 

cursor.execute("CREATE TABLE IF NOT EXISTS records( id INTEGER PRIMARY KEY AUTOINCREMENT, cor_cnt INTEGER, record text, regdate text)") 
# 커서위치로 부터 sql 생성문 실행 id 는 정수형 프라이머리 키, 자동증가, cor_cnt 는 정수, record 는 텍스트, regdate는 텍스트로 테이블을 생성



words = [] #영어 단어 리스트 ( 1000개 로드)

n = 1 # 게임 시도 횠수
cor_cnt = 0 # 정답 갯수

with open('./resource/word.txt','r') as f: # 파일 오픈
    for c in f: # 파일 내용을 지역변수 c에 반복
        words.append(c.strip()) # 파일 내용을 리스트 에 좌우 공백을 제거하여 입력

input("Ready? Press Enter Key!") # Enter Game Start!

start = time.time() # 엔터키가 입력되어 시작시 시간을 기록

while n <=5 : # n 이 5 이하일떄 반복실행
    random.shuffle(words)  # 리스트를 자동으로 섞어줌
    q = random.choice(words)   # 랜덤 단어를 출력

    print()

    print("*Question # {}", format(n)) # 문제 번호 출력
    print(q) # 랜덤으로 선택된 단어를 출력

    x = input() # 타이핑 입력

    print()

    if str(q).strip() == str(x).strip(): # 랜덤 선택된 단어와 입력한 단어가 같다면
        print("Pass!")
        cor_cnt += 1 # 정답 카운터를 1 증가
        # 정답소리 재생
        winsound.PlaySound('./sound/good.wav', winsound.SND_FILENAME)
    else :
        print("Wrong!")
        # 오답소리 재생
        winsound.PlaySound('./sound/bad.wav', winsound.SND_FILENAME)

    n += 1  # 카운터 증가, 다음문제로 전환
    
end = time.time() # 와일문의 반복실행이 끝났을떄의 시간 기록
et = end - start # 게임 소요시간 계산
et = format(et,".3f") # 소요된 시간을 소숫점 3째 자리까지 출력

if cor_cnt >=3 :
    print("합격!")
else:
    print("불합격!")

# 기록 DB 삽입 
cursor.execute("INSERT INTO records('cor_cnt', 'record', 'regdate') VALUES(?,?,?)", (cor_cnt, et, datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')))

print("게임시간 : ", et, "초 ", f"정답 개수 : {cor_cnt}")

# 시작 지점
if __name__  == '__main__' :
    pass
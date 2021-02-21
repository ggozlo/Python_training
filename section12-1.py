  # 파이썬 데이터베이스 연동(SQLite)
  # 테이블 생성 및 삽입

import sqlite3 # 기본탑재
import datetime

# 삽입 날짜 생성
now = datetime.datetime.now()
print('now:',now)

nowdDatetime = now.strftime('%Y-%m-%d %H:%M:%S')
print('nowDatetime:',nowdDatetime)

print(" sqlite3 버전 :",sqlite3.version) # 버전확인
print(" sqlite3 엔진 버전 :",sqlite3.sqlite_version) #엔진버전 확인

# db 생성 & Auto Commit (Roleback)
conn = sqlite3.connect('E:/python/Python_training/resource/database.db', isolation_level=None) # 커밋 자동실행

# Cursor 
c = conn.cursor() # 커서 획득
print('Cursor Type', type(c))

# 테이블 생성(Date Type : TEXT, NUMERIC, INTEGER, REAL, BLOB)
c.execute("CREATE TABLE IF NOT EXISTS users(id INTEGER PRIMARY KEY, username text, email text, phone text, website text, regdate text)")

# 데이터 삽입 
c.execute("INSERT INTO users VALUES(1, 'Yang', 'ggozlo@naver.com', '010-4400-5041', 'ggozlo.com', ?)", (nowdDatetime,)) # ? 에 대한 매개변수를 튜플형태로 입력
c.execute("INSERT INTO users(id, username, email, phone, website, regdate) VALUES(?,?,?,?,?,?)", (2, 'Park', 'park@naver.com', '010-4400-5041', 'park.com', nowdDatetime)) # 튜플형식 인서트

# Many 삽입 (튜플, 리스트)
userList = (
    (3, 'LEE', 'LEE@naver.com','010-1111-1111', 'LEE.com',nowdDatetime),
    (4,'cho','cho@naver.com','101-1111-111','cho.com',nowdDatetime),
    (5,'jin','jin@naver.com','999-9999-9999','jin.net',nowdDatetime)
)

c.executemany("INSERT INTO users(id, username, email, phone, website, regdate) VALUES (?,?,?,?,?,?)", userList)

# 테이블 삭제 
# conn.execute("DELETE FROM users")
# print("users db deleted :", conn.execute("DELETE FROM users").rowcount) # 삭제한 행 수를 표시

# 커밋 : isolation_lever = None 일 경우 오토커밋 
# conn.commit()

# 롤백 - 마지막 커밋시점으로 원복
# conn.rollback() 

# 접속해제 
conn.close()
# 파이썬 데이터베이스 연동(SQLite)
# 테이블 조회

import sqlite3

# DB파일 조회
conn = sqlite3.connect('E:/python/Python_Training/resource/database.db') # 본인 db경로

# 커서 바인딩
c = conn.cursor()

# 데이터 조회(전체)
c.execute("SELECT * FROM users")

# 커서 위치가 변경 
# 1개 로우 선택

#print('One -> \n', c.fetchone()) # 커서의 위치가 첫 행이기에 첫 행을 출력 이후 커서가 넘어감

# 지정 로우 선택 
#print("Three -> \n", c.fetchmany(size=3)) # 커서 위치로부터 3 행을 출력
 
# 전체 로우 선택
#print('all -> \n', c.fetchall()) # 커서 위치부터 남은 행을 전부 출력시킴

#print('all -> \n', c.fetchall()) # 남은 행이 없어서 출력값이 없음

print()

# 순회 1 
# rows = c.fetchall() # rows 에 모든 행 정보 저장
# for row in rows : 
#     print('retrieve1 > ', row)

# 순회 2
# for row in c.fetchall():
#     print('retrieve2 > ', row)

# 순회 3 
# for row in c.execute('SELECT * FROM users ORDER BY id desc'):
#     print('retrieve3 >', row)

print()

# Where Retrieve1 
param1 = (3,)
c.execute('SELECT * FROM users WHERE id=?',param1) # 지정된 3번 아이디만 찾아서 출력
print('param1',c.fetchone()) 
print('param1',c.fetchall()) # 더이상 출력할 데이터 없음

# Where Retrieve2
param2 = 4 # 정수 4 저장
c.execute('SELECT * FROM users WHERE id="%s"'%param2)  # 정수를 문자열 형식으로 삽입하여 id 4을 찾는 명령으로 만듦
print('param2',c.fetchone()) 
print('param2',c.fetchall()) # 데이터 없음

# Where Retrieve3 
c.execute('SELECT * FROM users WHERE id=:Id', {"Id":5})  # 딕셔너리를 키값 Id 에 대한 밸류값 5를 넣음
print('param3',c.fetchone()) 
print('param3',c.fetchall()) # 데이터 없음

# WHERE Retrieve4
param4 = (3,5)
c.execute("SELECT * FROM users WHERE id IN(?,?)",param4) # 복수개의 id 찾기
print('param4',c.fetchall())

# WHERE Retrieve5
c.execute("SELECT * FROM users WHERE id IN(%d,%d)" % (3,4)) # 복수개의 id 찾기
print('param5',c.fetchall())

# WHERE Retrieve6
c.execute("SELECT * FROM users WHERE id=:id1 OR id=:id2", {"id1":2,"id2":5}) # 딕셔너리 복수 OR 를 사용해 다중 조건 출력
print('param6',c.fetchall())

# DUMP 출력 - SQL 작성에 사용된 명령어들 조회
with conn : # 기존 database 접근
    with open('E:/python/python_training/resource/dump.sql','w') as f : # 덤프파일 생성
        for line in conn.iterdump(): # 덤프를 줄단위로 반복
            f.write('%s\n'%line) # 줄단위로 문자열 형식 작성
        print('Dump print Complete') 

# f.close, conn.close 문은 with 명령어에 의하여 자동실행 되었음
# 파이썬 데이터 베이스 연동(SQLite)
# 테이플 데이터 수정 및 삭제

import sqlite3

# DB생성 (파일)
conn = sqlite3.connect('E:/python/Python_training/resource/database.db')

# Cursor 연결
c = conn.cursor()

# 데이터 수정1 
c.execute("UPDATE users SET username = ? WHERE id =?",('neceman',2))


# 데이터 수정 2
c.execute("UPDATE users SET username = :name WHERE id =:id",{"name" : 'goodman', "id":5})


# 데이터 수정 3
c.execute("UPDATE users SET username = '%s' WHERE id ='%s' " %('badboy', 3))

# 중간 데이터 확인1
for user in c.execute("SELECT * FROM users"):
    print(user)

# Row Delete1 
c.execute('DELETE FROM users WHERE id = ?',(2,))

# Row Delete2 
c.execute('DELETE FROM users WHERE id = :id',{"id":5})

# Row Delete3
c.execute("DELETE FROM users WHERE id = '%s'" %(4))

print()

#중간 데이터 확인2
for user in c.execute("SELECT * FROM users"):
    print(user)

# 테이블 전체 데이터 삭제
print("users db delete : ", conn.execute("DELETE FROM users").rowcount, " rows")
conn.commit()


# 접속해제
conn.close
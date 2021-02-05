# 자료형 데이터 타입 리스트 

# 리스트(순서 O), 중복 허용, 수정 가능, 삭제 가능) 
# 선언 

a = []
b = list()
c = [1, 2, 3, 4]
d = [10, 100, 'Pen', 'Banana', 'Orange']
e = [10, 100, ['Pen', 'Banana', 'Orange'] ]

# 인덱싱 
print(d[3])
print(d[-2])
print(d[0]+d[1])
print(e[2][1])
print(e[-1][-2])

# 슬라이싱
print(d[0:3])
print(e[2][1:3])

# 연산 
print(c + d )
print(c * 3)
print(str(c[0]) + 'hi')

# 리스트 수정 , 삭제
c[0] = 77
print(c)

c[1:3] = [100, 1000, 10000]
print(c)
c[1] = ['a','b','c']
print(c)

del c[1] # 인덱스 삭제
print(c)
del c[-1]
print(c)

# 리스트 함수 

y = [5,2,3,1,4]
print(y)
y.append(6)
print(y)
y.sort()
print(y)
y.reverse()
print(y)
y.insert(2 , 7)
print(y)
y.remove(2) # 값을 찾아서 삭제
y.remove(7)
print(y)
y.pop()  # LIFO  (last in first out)
print(y)
ex = [88,77]
y.extend(ex)
print(y)

# 삭제 : del, remove, pop

# tuple : 순서 있음, 중복 허용, 수정 안됨, 삭제 안됨

a = () 
b = (1, )  # 마지막엔 , 로 끝낼것
c = (1,2,3,4)
d = (10, 100, ('a','b','c'))

print(c[2])
print(c[3])
print(d[2][2])

print(d[2:])
print(d[2][0:2])

print(c + d) 
print(c * 3)

# 튜플 함수 
z = (5,2,1,3,4,1)

print(z)
print(3 in z)
print(z.index(3)) # index 3 번째의 값 호출
print(z.count(1)) # 1은 몇개가 있는가?
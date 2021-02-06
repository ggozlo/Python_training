# 파이썬 데이터 타입(자료형)
# 딕셔너리, 집합 자료형

# 딕셔너리(Dictionary) : 순서 없음, 중복 없음, 수정 가능, 삭제 가능

# Key, Value / Json -> MongoDB

# 선언
a = {'name' : 'Kim', 'Phone' : '010-7777-7777', 'birth' : 870214, }
b = {0 : 'Hello Python', 1 : 'Hello Coding'}
c = { 'arr' : [1,2,3,4,5]}


# 출력 
print(a['name'])
print(a.get('name'))
print(a.get('address'))
print(c['arr'][1:3])

# 딕셔너리 추가 
a['address'] = 'seoul'
print(a)
a['rank'] = [1,3,4]
a['rank2'] = (1,2,3)
print(a)

# Key, Value, Item
print(a.keys())
print(list(a.keys()))

temp = list(a.keys())
print(temp[1:3])

print(a.values())
print(list(a.values()))

print(a.items())
print(list(a.items()))
print(1 in b)
print('name' not in a)

# 집합 (set) 순서 x , 중복 x
a = set()
b = set([1,2,3,4])
c = set([1,2,3,6,5,6])

print(type(a))
print(c)

t = tuple(b)
print(t)
l = list(b)
print(l)

s1 = set([1, 2, 3, 4, 5, 6])
s2 = set([4,5,6,7,8,9])

print(s1.intersection(s2))
print(s1 & s2)

print(s1 | s2)
print(s1.union(s2))

print(s1 - s2)
print(s1.difference(s2))

# 추가 & 제거 
s3 = set([7,8,10,15])

s3.add(18)
s3.add(7)
print(s3)

s3.remove(15)
print(s3)
print(type(s3))

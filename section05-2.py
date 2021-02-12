# 흐름제어(반복문)

# 코딩의 핵심 -> 조건 해결 주용

# 기본 반복문 : for, while 

v1 = 1
while v1 < 11:
    print("v1 is :", v1)
    v1 += 1

for v2 in range(10):
    print("v2 is  :", v2)

for v3 in range(1, 100):
    print("v3 is", v3)

# 1 ~ 100 합

sum1 = 0
cnt1 = 1 

while cnt1 <= 100 : 
    sum1 += cnt1
    cnt1 += 1 

print('1 ~ 100 :', sum1)
print('1 ~ 100 :', sum(range(1, 101)))
print('1 ~ 100 :', sum(range(1, 101, 2)))

# 시퀀스(순서가 있는) 자료형 반복 
# 문자열, 리스트, 튜플, 집합, 사전 
# interable 리턴 함수 : range, reversed, enumerate, filter, map, zip 

names = ['kim', 'park', 'cho', 'choi', 'yoo']

for name in names :
    print("You are : ", name)

word = "dreams"

for dream in word :
    print("Word :", dream)

my_info = { 
    "name" : "Kim",
    "age" : 33, 
    "city" : "Seoul"
}

for key in my_info : 
    print("my_info", key)

for key in my_info.values() : 
    print("my_info", key)
    
for key in my_info.keys() : 
    print("my_info", key)
    
for key, v in my_info.items() : 
    print("my_info", key, v)
    


name = "KennRY"

for n in name:
    if n.isupper():
        print(n.lower(), end="")
    else:
        print(n.upper(), end="")


# break
numbers = [14, 3, 4, 7, 10, 24, 17, 2, 33, 15, 34, 36, 38]
for target in numbers : 
    if target == 33:
        print("found 33!")
        break
    else: 
        print("not found")
else: # 반복문이 완료시 else  블럭 실행 
    print("Not Found 33........")
# continue

lt = ["1", 2, 5, True, 4.3, complex(3)]


for v in lt : 
    if type(v) is float: 
        print("found!")
        continue
    print("타입 : ",type(v))

name = "Niceman"
print(reversed(name))
print(list(reversed(name)))
print(tuple(reversed(name)))
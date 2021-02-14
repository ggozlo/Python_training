# Section05-3
# 파이썬 흐름제어(제어문)
# 제어문 관련 퀴즈(정답은 영상)

# 1 ~ 5 문제 if 구문 사용
# 1. 아래 딕셔너리에서 '가을'에 해당하는 과일을 출력하세요.
q1 =  {"봄": "딸기", "여름": "토마토", "가을": "사과"}

for a1 in q1.keys() :
    if a1 == "가을" :
        print(q1[a1])
# 2. 아래 딕셔너리에서 '사과'가 포함되었는지 확인하세요.
q2 =  {"봄": "딸기", "여름": "토마토", "가을": "사과"}

for a2 in q2.values() : 
    if a2 == "사과" :
        print("included!")

# 3. 다음 점수 구간에 맞게 학점을 출력하세요.
# 81 ~ 100 : A학점
# 61 ~ 80 :  B학점
# 41 ~ 60 :  C학점
# 21 ~ 40 :  D학점
#  0 ~ 20 :  E학점

grade = 1
if grade > 80 :
    print("A학점")
elif grade > 60 :
    print("B학점")
elif grade > 40 :
    print("B학점")
elif grade > 20 :
    print("B학점")
else :
    print("E학점")

# 4. 다음 세 개의 숫자 중 가장 큰수를 출력하세요.(if문 사용) : 12, 6, 18
# numbers = [12, 6, 18]
# numbers.reverse()
# print(numbers[0])

n1, n2, n3 = 12, 6, 18 

best = n1 

if n2 > n1 : 
    best = n2 
if n3 > n2 :
    best = n3 
print(best)

# 5. 다음 주민등록 번호에서 7자리 숫자를 사용해서 남자, 여자를 판별하세요. (1,3 : 남자, 2,4 : 여자)

q5 = '990210-2183119'

if int(q5[7]) % 2 == 1 : 
    print("남자")
else: 
    print("여자")


# 6 ~ 10 반복문 사용(while 또는 for)

# 6. 다음 리스트 중에서 '정' 글자를 제외하고 출력하세요.
q6 = ["갑", "을", "병", "정"]

for a6 in q6 : 
    if a6 != "정" :
        print(a6, end=" ")
        print()
    else :
        continue

q11 = [ x for x in q6 if x != '정']
print(q11)
# 7. 1부터 100까지 자연수 중 '홀수'만 한 라인으로 출력 하세요.

# q7 = 0
# while q7 < 100 : 
#     q7 += 1 
#     if q7 % 2 == 1 : 
#         print(q7)
#     else : 
#         continue

for q7 in range(1, 101) : 
    if q7 % 2 == 1 : 
        print(q7)

q12 = [ x for x in range(1, 101) if x % 2 == 1]
print(q12)
    

# 8. 아래 리스트 항목 중에서 5글자 이상의 단어만 출력하세요.
q8 = ["nice", "study", "python", "anaconda", "!"]

for a8 in q8 : 
    if len(a8) >= 5 : 
        print(a8)
    else : 
        continue 

# 9. 아래 리스트 항목 중에서 소문자만 출력하세요.
q9 = ["A", "b", "c", "D", "e", "F", "G", "h"]

for a9 in q9 : 
    if a9.islower() :
        print(a9)
    else :
        continue 
print()
# 10. 아래 리스트 항목 중에서 소문자는 대문자로 대문자는 소문자로 출력하세요.
q10 = ["A", "b", "c", "D", "e", "F", "G", "h"]

for a10 in q10 : 
    if a10.isupper() : 
        print(a10.lower())
    elif a10.islower() : 
        print(a10.upper())
    else : 
        print("false")

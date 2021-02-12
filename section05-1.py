#파이썬 흐름제어(조건문)

print(type(True))
print(type(False))

if True:
    print("Yes")

if False:
    print("No")

if False:
    print("No")
else:
    print("Yes2")
    
# 관계연산자
# >, >=, ==, <, <=, !=

a = 10
b = 0

print(a == b)
print(a != b)
print(a > b)
print(a >=b)
print(a < b)
print(a <= b)

# 참거짓 종류
# 참 : "내용", [내용], (내용), {내용}, 1, True
# 거짓 : "", [], (), {}, 0, False

city = ""
if city : 
    print("True")
else : 
    print("-False")

# 논리 연산자
# and(곱연산) or(합연산) not(부정)

a = 100
b = 60 
c = 15

print('and:', a > b and b > c)
print('or:', a > b or c > b)
print('not:', not a > b)

 # 산술, 관계, 논리 연산자 
 # 산술 > 관계 > 논리 순서적용

print(5 + 10 > 0 and not 7 + 3 == 10)

score1 = 90 
score2 = 'A'

if score1 >= 90 and score2 == 'A':
    print("합격하셨습니다.")
else:
    print("불합격입니다")

# 다중 조건문 elif 

num = 90
if num >= 90:
    print("%d-등급 A" %num)
elif num >= 80:
        print("%d-등급 B" %(num))
elif num >= 70:
        print("%d-등급 C" %num)
else: 
    print("꽝")

# 중첩조건문 
age = 27 
height = 175

if age >= 20:
    if height >= 170:
        print("지원 가능")
    elif height >= 160:
        print("2지원가능") 
    else:
        print("지원불가")
else:
    print("20세 이상 지원 가능")


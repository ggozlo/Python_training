#파이썬 예외처리의 이해

# 예외 종류
# 문법적으로 에러가 없지만, 코드 실행(런타임)프로세스 에서 발생하는 예외 처리도 중요
# linter : 코드 스타일, 문법 체크 

# SyntaxError : 잘못된 문법
# print('test
# if True
#     pass
# x => y

# NameError = 참조변수 없음
a = 10 
b = 15 
#print(c)

# ZeroDivisionError : 0 나누기 에러
# print(10/0)

# IndexError : 인덱스 범위 오버 
x = [10,20,30]
print(x)
# print(x[3])

# KeyError 
dic = {'name': 'kim', 'age' : 33, 'City':'Seoul'}
#print(dic['hobby'])
print(dic.get('hobby'))

# AttributeError : 모듈 , 클래스에 있는 잘못된 속성 사용시에 예외
import time
print(time.time())
#print(time.month())

# ValuError : 참조 값이 없을 떄 발생
x = [ 1, 5, 9]
# x.remove(10)
# x.index(10)

# FileNotFiundError
# f = open('test.txt', 'r')

# TypeError 
x = [1,2]
y = (1,2)
z = 'test'
# print(x+y)
# print(x+z)
# print(x + list(y)) # 캐스팅

# 항상 예외가 발생하지 않을 것으로 가정하고 먼저 코딩 
# 런타임 예외 발생시 예외 처리 코딩 권장 ( EAFP 코딩 스타일 )

# 예외 처리 기본 
# try : 에러가 발생할 가능성이 있는 코드 실행
# except : 에러명 1
# except : 에러명 2 
# else : 에러가 발생하지 않았을 경우 실행
# finall : 항상 실행

# 예제 1번
name = ['kim', 'lee' , 'park']
# try: 
#     z = 'Kim'
#     x = name.index(z)
#     print('{} found if! in name'.format(z,x+1))
# except ValueError :
#     print('not found it! - occurred valueError!')
# else: # try 문이정상 실행되었을떄 ( except 문이 작동하지 않았을때 실행 )
#     print('OK! else!')


#예제 2 
# try: 
#     z = 'kim'
#     x = name.index(z)
#     print('{} found if! in name'.format(z,x+1))
# except : # 에러유형을 미지정시 모든 에러 포착
#     print('not found it! - occurred Error!')
# else: # try 문이정상 실행되었을떄 ( except 문이 작동하지 않았을때 실행 )
#     print('OK! else!')

# 예제 3
# try: 
#     z = 'Cho'
#     x = name.index(z)
#     print('{} found if! in name'.format(z,x+1))
# except :
#     print('not found it! - occurred valueError!')
# else: # try 문이정상 실행되었을떄 ( except 문이 작동하지 않았을때 실행 )
#     print('OK! else!')
# finally : # 에러 발생 유무에 관계 없이 실행
#     print('finall ok!')

# 예제 4 
# 예외 처리는 하지 않지만 무조건 수행되는 코딩 패턴
try : 
    print("try")
finally:
    print("ok Finally!")

# 예제 5
try: 
    z = 'jim'
    x = name.index(z)
    print('{} found if! in name'.format(z))
except ValueError as l : # 오류 출력 내용을 allias 를 이용하여 변수에 저장도 가능함
    print(l)
except IndexError :
    print("Error")
except Exception : # 모든 에러에 대해서 발생, 여러 종류의 except 문을 사용한다면 가장 하단에 위치해야함
    pass
else: # try 문이정상 실행되었을떄 ( except 문이 작동하지 않았을때 실행 )
    print('OK! else!')

# 예제6
# 예외 발생 : raise 
# raise 키워드로 예외 직접 발생
try : 
    a = 'kim'
    if a == 'kim':
        print('허가')
    else : 
        raise ValueError # 허가된 사용자가 아니라면 오류를 발생시킴 
except ValueError:
    print('문제 발생!')
except Exception as f:
    print(f)
else:
    print('ok!')
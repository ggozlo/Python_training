# 파이썬 함수식 및 람다(lambda)
# 
# 함수 정의 방법
# def 함수명(parameter(매개변수))
#   code

# 함수 호출 
# 함수명() 

# 함수 선언 위치 중요 

def hello(world) : 
    print("Hello", world)

hello("python!")
hello("7777")


def hello_return(world): 
    val = "Hello " + str(world)
    return val

string = hello_return("Python!!!")
print(string)

# 다중리턴 

def func_mul(x):
    y1 = x*100
    y2 = x*200
    y3 = x*300 
    return y1,y2,y3 

val1, val2, val3 = func_mul(100)
print(val1, val2, val3)

# 데이터 타입 반환

def func_list(x):
    y1 = x*100
    y2 = x*200
    y3 = x*300 
    return [y1,y2,y3]

lt = func_list(100)
print(lt, type(lt))


# *args , *kwargs 

def args_func(*args): # 튜플형 가변인자 
    # print(args)
    # for t in args:
    #     print(t)
    for i, v in enumerate(args):  # 인덱싱
        print(i, v)

args_func('kim', 'park', 'moon')

# kwargs 

def kwargs_func(**kwargs): #  사전형 가변인자
    for k, v in kwargs.items():
        print(k, v)

kwargs_func(name1='kim', name2='park', name3='lee')


# 전체 혼합

def example_mul(arg1, arg2, *args, **kwargs):
    print(arg1, arg2, args, kwargs)

example_mul(10, 20, 1,2,3,4,5, age= 20, age2=35)

# 중첩함수 (클로저)

def nested_func(num):
    def func_in_func(num):
        print(num)
    print("in func")
    func_in_func(num+10000)

nested_func(10000)

# 
def func_mul3(x : int) -> list :
    y1 = x*100
    y2 = x*200
    y3 = x*300 
    return [y1,y2,y3]

print(func_mul3(5))

# 람다식 
# 람다식 : 메모리 절약, 가독성 향상, 코드 간결 
# 함수는 객체 생성 -> 리소스(메모리) 할당 
# 람다는 즉시 실행(Heap 초기화) -> 메모리 초기화

# 일반함수 
def mul_10(num):
    return num * 10 

var_func = mul_10
print(var_func)
print(type(var_func))

print(var_func(10))

lambda_mul_10 = lambda x : x * 10
print(lambda_mul_10(10))

def func_fin(x, y, func):
    print(x * y * func(10))

func_fin(10,10,lambda_mul_10)

print(func_fin(10,10, lambda x : x * 1000))
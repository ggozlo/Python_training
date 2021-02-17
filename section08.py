# 기본제공 라이브러리,패키지 ( built-in pakage )
# 모듈들을 구조적으로 관리하는 것을 패키시 형 이라고 함
# ex ) 부엌 패키지내 식칼, 도마 모듈 

# 파이썬 모듈과 패키지 
# 상대경로
# .. : 부모 디렉토리
# .  : 현재 디렉토리 

# 사용1(클래스)
from pkg.fibonacci import Fibonacci # , 를 통한 다수의 모듈 호출가능

Fibonacci.fib(300)

print("ex1 : ", Fibonacci.fib2(400))
print("ex1 : ", Fibonacci().title)

# 사용 2(클래스) 비권장
from pkg.fibonacci import * # 모듈내 자료를 모두 가져옴 

print("ex2 : ", Fibonacci.fib2(400))
print("ex2 : ", Fibonacci().title)

# 사용3 클래스

from  pkg.fibonacci import Fibonacci as fb # allias - 축약어 지정

print("ex3 : ", fb.fib2(400))
print("ex3 : ", fb().title)

# 사용 4(함수)
import pkg.caculsations as c # 모듈 전체를 호출, c로 별칭

print("ex4 : ", c.add(10, 100))
print("ex4 : ", c.mul(10, 100))

# 사용 5(함수)

from pkg.caculsations import div as d # 필요한 함수만 호출

print("ex5 : ", int(d(100,10)))

# 사용 6 

import pkg.prints as p

p.prt1()
p.prt2()

import builtins
print(dir(builtins))
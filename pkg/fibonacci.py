class Fibonacci:
    def __init__(self, title = "fibonacci") : # title 변수값이 넘어온다면 그것을 사용, 아니라면 설정된 기본값 "fibonacci" 를 사요함
        self.title = title # 객체 명 지정
    
    def fib(n):
        a, b = 0 ,1 
        while a < n :   
            print(a, end=' ')
            a,b = b, a+b
        print()
    
    def fib2(n):
        result = []
        a, b = 0 ,1 
        while a < n : 
            result.append(a)
            a,b = b, a+b
        return result

    
# 파이썬 클래스 상세 이해 
# 상속, 다중상속

#상속 기본
#슈퍼클래스(부모) 및 서브클래스(자식) -> 모든 속성, 메소드 사용 

# ex) 라면 ( 종류 회사, 맛, 면, 종류, 이름) : 부모
# 
class Car: 
    ''' parent Class '''
    def __init__(self, tp, color ):
        self.type = tp
        self.color = color
    
    def show(self):
        return 'car class "show  Method!"'

class BMW(Car):
    '''sub class'''
    def __init__(self, car_name, tp, color):
        super().__init__(tp, color)
        self.car_name  = car_name

    def show_model(self) -> None:
            return 'your Car Name : %s' % self.car_name

class Benz(Car):
    '''sub class'''
    def __init__(self, car_name, tp, color):
        super().__init__(tp, color)
        self.car_name  = car_name

    def show_model(self) -> None:
            return 'your Car Name : %s' % self.car_name
    
    def show(self): # OverRiding
        print(super().show()) # Parent Method Call
        return 'car info %s %s %s' %(self.car_name, self.type, self.color)

#일반 사용
model1 = BMW('520d', 'sedan', 'red')
print(model1.color) # Super
print(model1.type)  # Super 
print(model1.car_name) # Sub
print(model1.show()) # Super
print(model1.show_model()) # Sub
print(model1.__dict__)

# Method Overriding(오버라이딩) 상속받은 내용을 덮어쓸수 있음
model2 = Benz('220d', 'suv', 'blcak')
print(model2.show())

# Parent Method Call
model3 = Benz('350s', 'sedan', 'silver')
print(model3.show())

# Inheritance Info (리스트형)
print(BMW.mro()) # 상속관계 출력
print(Benz.mro())

# 다중상속

class x():
    pass #미구현 함수의 넘김 가능

class y():
    pass

class z():
    pass

class A(x,y):
    pass

class B(y,z):
    pass

class M(B, A , z):
    pass

print(M.mro())
print(A.mro())
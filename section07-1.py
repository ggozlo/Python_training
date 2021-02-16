#파이썬 클래스 상세 이해
# self, 클래스, 인스턴스 변수 

# 클래스, 인스턴스 차이 중요 
# 네임스페이스 : 객체를 인스턴스화 할때 저장된 공간 
# 클래스 변수 : 직접 사용 가능, 객체 보다 먼저 생성 
# 인스턴스 변수 : 객체마다 별도로 존재, 인스턴스 생성후 사용  
#선언 
# class 클래스명 : 
    # 함수
    # 함수
    # 함수

class UserInfo:
    # 속성, 메소드 
    def __init__(self, name): #최초 초기화
        self.name = name # 인스턴스 변수 네임에 받은 변수를 입력
    def user_info_p(self):
        print("Name: ", self.name)

# 네임스페이스
user1 = UserInfo("kim")
print(user1.name)
user1.user_info_p()
user2 = UserInfo("park")
print(user2.name)
user2.user_info_p()

print(id(user1))
print(id(user2))
print(user1.__dict__)
print(user2.__dict__)

# sef 

# class SelfTest : 
#     def func1() : 
#         print('func1 called')
#     def func2(self) :
#         print(id(self))
#         print('func2 called')

# self_test = SelfTest()
# # self_test.func1() 
# SelfTest.func1()
# self_test.func2()
# SelfTest.func2(self_test)

# print(id(self_test))


# 

class WareHouse:
    # 클래스 변수 
    stock_num = 0 
    def __init__(self, name):
        self.name = name 
        WareHouse.stock_num += 1
    def __del__(self) :  # 인스턴스 삭제용
        WareHouse.stock_num -= 1

user1 = WareHouse('Kim')
user2 = WareHouse('Park')
user3 = WareHouse('Lee')

print(user1.__dict__)
print(user2.__dict__)
print(user3.__dict__)
print(WareHouse.__dict__) # 클래스 네임스페이스, 클래스 변수 공유 

print(user1.name)
print(user2.name)
print(user3.name)

print(user2.stock_num) # 자기 네임스페이스에서 찾아서 없으면 클래스 네임스페이스에서 찾음

del user1 
print(user2.stock_num)

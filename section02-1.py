# # 파이썬 기초 코딩
# print 구문의 이해 

# 기본출력 
print('Hello Python!')
print("Hello Python!")
print("""Hello Python!""")
print('''Hello Python!''')

print()

# separator 옵션
print ('T', 'E','S','T')
print ('T', 'E','S','T', sep='')
print ( 'T'+'E'+'S'+'T')
print('2019','02','19',sep='-')
print('niceman','google.com',sep='@')
# end 옵션 사용
print('Welcome to', end='-')
print(' the new paradise', end = "***")

print()
# format 사용
print('{} and {}'.format('I', 'You'))
print("{0} and {1} and {0}".format('You', 'Me'))
print("{a} are {b}".format(a = 'you',b='Me'))

print("%s favorite number is %d" %('My', 7)) # %s : 문자, %d : 정수, %f : 실수

print("Test1: %5d, Price: %4.2f" %(777, 6534.123) )
print("Test1: {0: 5d}, Prcie:{1: 6.2f}".format(776, 6534.123))
print("Test1: {a: 5d}, Price:{b: 4.2f}".format(a=776, b=6534.123))

# \n : 개행 ( 줄넘김 )
# \t : 탭   ( 간격 벌림 )
# \\ : 문자 \ 출력용
# \' : 문자 ' 출력용 
# \" : 문자 " 출력용

print("'you'")
print('\'you\'')
print('"you"')
print('\\you\\')

print('test\n')
print('test')

print('t\te\ts\tt ')

a = 10 
print(a)
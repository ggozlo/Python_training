# # 파이썬 기초 코딩
# print 구문의 이해 

# 기본출력 
print('Hello Python!')
print("Hello Python!")
print("""Hello Python!""")
print('''Hello Python!''')

print()

# separator 옵션
print ('T', 'E','S','T', sep='')
print('2019','02','19',sep='-')
print('niceman','google.com',sep='@')

# end 옵션 사용
print('Welcome to', end='')
print(' the black paradise', end='\n')
print('piano notes\n')

# format 사용
print('{} and {}'.format('I', 'You'))
print("{0} and {1} and {0}".format('You', 'Me'))
print("{a} are {b}".format(a = 'you',b='Me'))

print("%s favorite number is %d" %('My', 7)) # %s : 문자, %d : 정수, %f : 실수
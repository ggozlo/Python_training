# 파일 읽기, 쓰기
# 읽기모드 :r  쓰기모드(기존파일 삭제) : w , 추가 모드(파일 생성 또는 추가) : a 
# .. : 상대경로, . : 절대 경로'

# 파일 읽기 

print("예제 1번")

f = open('./resource/review.txt','r')
content = f.read()
print(content)
print(dir(f))
# 반드시 close로 리소스 반환
f.close 

# with 문 - close 생략 가능
print( "예제 2번")
with open('./resource/review.txt','r') as f: # = f = open('./Python_training/resource/review.txt','r')
    c = f.read()
    print(c)
    print(list(c)) # 배열출력시 char 단위로 리스트에 입력 ( 제어문도 같이 입력됨 )
    print(iter(c)) #  iteraotr 반환,  for 사용 가능 

print("예제 3번")

with open('./resource/review.txt','r') as f:
    for c in f: # 반복문으로 읽을시 한줄씩 가져옴
        print(c.strip()) #  줄간격 제거 가능
 
print("예제 4번")

with open('./resource/review.txt','r') as f:
        content = f.read()  
        print(">", content)
        content = f.read() # 읽기커서가 마지막에 가있기 떄문에 다시읽을 내용이 없음
        print(">", content)

print("예제 5번")

with open('./resource/review.txt','r') as f:
    line = f.readline() # 한줄씩 읽기
    # print(line)
    while line :  # 라인 변수에 값이 없을떄 까지 (더이상 읽어올것이 없을떄까지 반복)
        print(line, end='## ')
        line = f.readline()
print()
print("예제 6번")

with open('./resource/review.txt','r') as f:
    contents = f.readlines() # 라인별로 리스트 배열에 문자열로 저장함
    print(contents)
    for c in contents:
        print(c, end=' ***** ')

print()
print("예제 7번")
score = [] 
with open('./resource/score.txt','r') as f:
    for line in f:
        score.append(int(line)) # 기본형은 문자이기떄문에 int형으로 변환하여 받아야함
    print(score)
print('Average : {:6.3}'.format(sum(score)/len(score))) # 평균값 출력

#print("파일쓰기")
#print("예제 1번")

with open('./resource/text1.txt','w') as f:
    f.write('Goodman!\n')

#print("예제 2번")

with open('./resource/text1.txt','a') as f:
    f.write('niceman!\n')

# 예제 3번
from random import randint # 랜덤 라이브러리의 랜드인트 함수 지정

with open('./resource/text2.txt','w') as f:
    for cnt in range(6): # 6회 반복
        f.write(str(randint(1,51)))
        f.write('\n')

# 예제 4번 
# writelines : 리스트 -> 파일로 저장
with open('./resource/text3.txt','w') as f:
    list = ['kim\n','park\n','choi\n']
    f.writelines(list) # 리스트 내용을 줄별로 작성

# 예제 5번
with open('./resource/text4.txt','w') as f:
    print('Test Contests1!', file=f) # 파일로 바로 쓰기 가능
    print('Test Contests2!', file=f)
# 파이썬 외부 파일 처리
# 파이썬 Excel, CSV 파일 읽기 및 쓰기 

# CSV : MIME - text/csv 

import csv # csv 파일을 읽기위한 파이썬 기본제공 패키지

# 예제 1번 
with open('./resource/sample1.csv','r') as f:
    reader = csv.reader(f)
    next(reader) # 첫 컬럼(Header) 스킵을 위한 넘김
    #확인
    print(reader)
    print(type(reader))
    print(dir(reader)) #  __iter__ 가 존재한다면 반복문 가능

    for c in reader:
        print(c)

# 예제 2 
with open('./resource/sample2.csv','r') as f:
    reader = csv.reader(f, delimiter="|") # 구분을 컬럼이 아닌 다른문자로 되어있다면 지정해줄수 있다
    next(reader) # 첫 컬럼(Header) 스킵을 위한 넘김
    #확인
    print(reader)
    print(type(reader))
    print(dir(reader)) #  __iter__ 가 존재한다면 반복문 가능

    for c in reader:
        print(c)

# 예제 3 Dict 변환
with open('./resource/sample1.csv','r') as f:
    reader = csv.DictReader(f)

    for c in reader:
        for k,v in c.items():
            print(k ,v)
        print("-------------------")


# 예제 4 
w = [[1,2,3], [4,5,6],[7,8,9],[10,11,12],[13,14,15],[16,17,18]]

with open('./resource/sample3.csv','w', newline="") as f: # 다차원 배열에 대하여 자동 줄바꿈을 지원하지만 직접 설정도 가능함
    wt = csv.writer(f)

    for v in w: 
        wt.writerow(v)

# 예제5 
with open('./resource/sample4.csv','w', newline="\n") as f: # 다차원 배열에 대하여 자동 줄바꿈을 지원하지만 직접 설정도 가능함
    wt = csv.writer(f)
    wt.writerows(w) # 한번에 쓰기

# Xsl, Xlsx
# 열기용 오픈소스 openpyxl, xlsxwriter, xlrd, xlwt, xlutils
# pandas 를 주로 사용(openpyxl, xlrd 포함)
# pip install xlrd 
# pip install openpyxl
# pip install pandas 

import pandas as pd 

# sheetname = '시트명'(호출해올 시트명을 지정) 혹은 숫자, header=숫자(몇번쨰 행을 헤더로 지정할건지), skiprow=숫자(제외할 행을 지정)
xlsx = pd.read_excel('./resource/sample.xlsx')

# 상위 데이터 확인 
print(xlsx.head()) #첫줄부터 5줄
print()

# 데이터 확인
print(xlsx.tail()) # 뒤에서부터 5줄

# 데이터 확인
print(xlsx.shape) # 구조 확인, (행, 열)

# 엑셀 or CSV 다시쓰기 
xlsx.to_excel('./resource/result.xlsx',index=False)
xlsx.to_csv('./resource/result.csv',index=False)
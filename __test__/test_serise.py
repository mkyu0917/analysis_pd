import pandas as pd

price=[92600, 92400, 92100, 94300, 92300]
tuple =(1,2,3,4,5,6)
s = pd.Series(price) #엑셀처럼 인덱스와 열로 만들어줌
b = pd.Series(tuple)
print(b)
print(s)
print(s[0],s[1]) #인덱스로 출력

# index를 부여 할때는 반드시 데이터 개수와 같아야한다.
s = pd.Series(
    [92600, 92400, 92100, 94300, 92300],
    index=['2017-01-01','2017-02-02','2017-03-03','2017-04-04','2017-05-05']
)
print(s)
print(s[1], s['2017-03-03'])

#스칼라 값으로 초기화 할 때는 인덱스가 반드시 필요.
s1 = pd.Series(7, index=['a','b','c','d'])
print(s1)

#딕셔너리로 초 기 화 하 기
d ={'a':10,'b':20, 'c':30}
s1 = pd.Series(d)
print(s1)

s1=pd.Series(d, index=['A','B','C'])
print(s1)

#인덱스위에것보다 인덱스만 늘린경우 d는 비어있음

s1=pd.Series(d, index=['a','b','c','d'])
print(s1)


#순회 (index, values라는 속성을 통해 접근이 가능하다.)
for date in s.index:
    print(date, end=' ') #출력하고 스페이스 반복
else:
    print() #출력다하고 개행

for price in s.values:
    print(price, end=' ')  # 출력하고 스페이스 반복
else:
    print()  # 출력다하고 개행


#연산

#겹치지 않은 부분은 계산이 안된다!  A,D는 NaN으로 나옴
s1 =pd.Series([10,20,30], index=['A','B','C'])
s2 =pd.Series([10,20,30], index=['B','C','D'])

s3=s1+s2
print(s3, type(s3))

s3=s1-s2
print(s3, type(s3))

s3=s1*s2
print(s3, type(s3))

s3=s1/s2
print(s3, type(s3))

s3=s1*3
print(s3, type(s3))
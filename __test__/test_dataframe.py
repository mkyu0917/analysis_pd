import pandas as pd

# Serise와 dict 데이터를 사용한 DataFrame ,인덱스 필요
d = {
'one':pd.Series([1,2,3], index=['a','b','c']),
'two':pd.Series([10,20,30,40], index=['a','b','c','d'])
}

df = pd.DataFrame(d)
print(df)

#list와 dict를 활용

data= [
{'name':'둘리', 'age':10,'phone':'010-1111-1111'},
{'name':'마이콜', 'age':30,'phone':'010-2222-2222'},
{'name':'도우넛', 'age':20,'phone':'010-3333-3333'}
]



df = pd.DataFrame(data)
print(df)

df2 = pd.DataFrame(df, columns=['name','phone'])
print(df2)

# 데이터 추가 ( 열 추가) , 딕셔너리와 같음

df2['height'] = [150, 160 ,170]
print(df2)

df2 = pd.DataFrame(df, columns=('name', 'phone'))
df3 = df2.set_index('name')
print(df3)

# 인덱스 선택

df2['height'] = [150, 160, 170]
print(df2)

# 컬럼 선택
s = df2['name']

#merge
df4 = pd.DataFrame([{'sido': '서울'}, {'sido': '부산'}, {'sido': '전주'}])
df5 = pd.merge(df2, df4, left_index=True, right_index=True)
print(df5)


df1 = pd.DataFrame({
    '고객번호': [1001, 1002, 1003, 1004, 1005, 1006, 1007],
    '이름': ['둘리', '도우너', '또치', '길동', '희동', '마이콜', '영희']})

df2 = pd.DataFrame({
    '고객번호': [1001, 1001, 1005, 1006, 1008, 1001],
    '금액': [10000, 20000, 15000, 5000, 100000, 30000]})

# 공통 열인(column인) 고객번호를 기준으로 데이터를 찾아서 합친다.
# 이 때, 기본적으로 양쪽 데이터프레임에 모두 키가 존재하는
# 데이터만 합쳐지며, (inner join)방식이다.
df3 = pd.merge(df1,df2)
print(df3)
print()

#outer join 방식은 키값(인덱스) 한쪽에만 있어도 양쪽 데이터를 모두 합친다.
#(full)
df3 = pd.merge(df1, df2, how='outer')
print('outer',df3)
print()

#left, 두번째 파라미터의 데이터프레임의
#데이터를 전부 보여주는 방식
df3 = pd.merge(df1,df2,how='left')
print(df3)
print()




#right, 첫번째 파라미터의 데이터프레임의
#데이터를 전부 보여주는 방식
df3 = pd.merge(df1,df2,how='right')
print(df3)
print()

#기준열은 on 인수로 명시적 설정이 가능하다.
df1 = pd.DataFrame({'성별': ['남자', '남자', '여자'],
                    '연령': ['미성년자', '성인', '미성년자'],
                    '매출1': [1, 2, 3]})

df2 = pd.DataFrame({'성별': ['남자', '남자', '여자', '여자'],
                    '연령': ['미성년자', '미성년자', '미성년자', '성인'],
                    '매출2': [4, 5, 6, 7]})

df3=pd.merge(df1, df2)
print('머지',df3)
print()  

df3 = pd.merge(df1, df2, on=['성별', '연령'])# 기준을 성별과 연령으로 선택
print('기준:연령,성별',df3)
print()

df3 = pd.merge(df1, df2, on=['성별']) #기준을 성별로 선택
print(df3)
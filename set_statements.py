# set은 집합의 개념임.
# set의 특성은 딕셔너리와 마찬가지로 index가 없고 중복이 없다.

s1={'이름','나이','성별' }#몇개인가 ? 
# A, B, AB-> 3개
#b_type=set(lista)
#print(len(b_type))

# set의 값을 하나씩 출력하려면 ?
#for i in b_type :
#    print(i)

# 합집합 | or union() # |는 or을 의미한다.
s1={1,2,3,4,5,6}
s2={4,5,6,7,8}
s3=s1 | s2
print(s3)
s3=s1.union(s2)
print(s3) 

# 프로그래밍에서 & 는 and를 의미, 앰퍼샌드라고 부른다. 
s3 = s1 & s2
s3 = s1.intersection(s2)
print(s3)

#차집합
s3=s2-s1
print(s3)
s3=s2.difference(s1)
print(s3)

# 값 추가 
s1.add(159)
print(s1)

# 값 여러개 추가시 update함수 (딕셔너리와 동일)
s1.update(s2)
print(s1) ## {1, 2, 3, 4, 5, 6, 7, 8, 159} -> 중복제거하고 바뀜 

# 삭제 (remove, discard) discard는 없는거 없애믄 none 리턴함, remove는 에러발생
s1.remove(159)
print(s1)

s1.discard(156486)
print(s1) # key만 있다고 생각하면 됌.
# 리스트의 중복을 제거하기 위해서 리스트를 set으로 형변환 시키는 방식도 많이 사용
s1=set(['이름','나이','성별']) # 형변환 시킨거임
# 집합의 개수 구하는 함수 : len 
print(len(s1))
print(s1)
s2=set('test') # 중복제거 
print(s2)

# 인덱스로 접근 불가능 


lista =['A','A','A','B','B','AB','O']
# 이 반 학생들의 혈액형 종류는

# bool 형
# in, not in들은 interable한 자료형이 나온다  
# a in list , a not in lista, a not in dictionart.keys(), a not in set

# 비어있는 값들은 거짓, 값이 들어있으면 참이다.dd 
lista=[1,2,3]
while lista :
    print('참입니다')
    lista.pop()
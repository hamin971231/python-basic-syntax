#tuple 
# 튜플은 변경 불가능한 자료형으로서, ()통해 표현한다 BUT, 조회는 가능
# t1=(1,2,3,'a','b')
# print(t1)
# 인덱싱 슬라이싱 둘다 리스트와 동일하게 사용
# print(t1[0])
# 삭제, 수정할때 에러발생
# 더하기 곱하기가 가능한데 그 이유는 t1,t2를 수정하는 것이 아니라 재정의 하는 것이기 때문에 가능함. 
# del t1[0]
# print(t1) # typeError : 튜플 객체는 삭제지원 하지 않는다는 내용 나옴
# 튜플을 사용하는 이유는 개발자가 해당 자료를 수정하지 못하도록 
# 강제적으로 지정한 것. 
# 리스트에 비해 메모리 효율적 

# 딕셔너리 (자바에서는 Map or Hash Map, )

# 딕셔너리 자료형은 KEY와 VALUE로 이루어져있다.
# 영어사전에서 단어와 뜻으로 이루어져 있는 것에서 유래.

# 파이선에서의 dictionary는 
# 다른언어의 map 또는 hashmap과 유사한 자료형
# json이라는 자료형태와 유사하다.

# 딕셔너리의 특징-(1)
# KEY는 중복이 불가, 
# VALUE는 다른 키에도 존재할 수 있다.

# dic1={'이름':'조해민','나이':25,'성별':'남자','성별':'여자'}
# print(dic1)

# 딕셔너리의 기본 호출 방식은 변수명[key], 변수명.get(key)
# print(dic1['나이'])
# print(dic1.get('나이'))

# 리스트는 a=[value,...], 딕셔너리는 a={'key':value, ... }, 튜플은 a=(value,...)
# 리스트와 튜플은 a[index], 딕셔너리는 a[key]

# 딕셔너리의 특징-(2)
# key와 value로 이루어져 있다보니, 순서가 의미가 없다. index로 접근 불가


# key를 이용하여 값의 수정, 삭제, 추가 가능하다.
# 딕셔너리는 해시함수(암호생성기)를 통해 메모리 주소를 할당한다. 
# key값에 할당된 난수를 통해 value를 찾기 때문에 압도적을 빠름.
# key를 가지고 value를 검색할 떄 해시함수를 통해 index를 찾다보니 압도적으로 빠름. 

## 해시함수
## 딕셔너리의 메모리상 저장구조는?
## 딕셔너리의 동작원리 

# 딕셔너리에서 키를 이용한 key:value 추가 
dic1={'이름':'조해민','나이':25,'성별':'남자','몸무게':69}
print(dic1)
dic1['신분']='학생'
print(dic1)
# 딕셔너리에서 키를 이용한 key:value 삭제
del dic1['성별']
print(dic1)

# 딕셔너리에서 key목록만 뽑아낼떄
# iterable한 형태로 data가 뽑아져 나오므로 for문 ㄱㄱ 
# keyList=dic1.keys()
# print(keyList)

# 위의 keyList에서 각각의 값을 출력해보자
keyList=dic1.keys()
# print(keyList) ## --> dict_keys(['이름', '나이', '몸무게', '신분']) 리스트 형태 아님 !!!!!!!!!!
for i in keyList :
    ## key 값을 출력해주는 for 문안에서 value도 같이 출력하도록 해보자 
    print('key : ',i, ' , ','value : ',dic1[i])
# 위에 for 문을 활용해서 key가 담긴 list를 만들고 value가 담긴 list
# list_key=[]
# list_value=[]
# for i in keyList:
#     list_key.append(i)
#     list_value.append(dic1[i])
# print(list_key)
# print(list_value)
# # value 목록을 뽑아낼 때 .values()
# valueList=dic1.values()
# print(valueList)
# for i in dic1.values() :
#     print(i)
# # # # key & values 같이 뽑아 낼 때 
# for i in dic1.items() :
#     print(i)

# 딕셔너리의 확장 update()
dic1={'a':1,'b':2,'c':3}
dic2={'a':2,'e':4,'f':5}

dic1.update(dic2)
print(dic1)


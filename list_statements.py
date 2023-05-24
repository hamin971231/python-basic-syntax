# list는 변수마다 값을 할당해서 사용하기에 관리의 어려움이 있으므로
# 한 변수에 값을 집합시켜놓은것

# 하나의 변수로 여러개의 데이터를 관ㄹ;
# list 의경우 대괄호 []

# lista=['김돌쇠','김십돌','김갑순']

# print(lista)

# list 안의 각각의 값에 접근할 때에는 index 사용
# print(lista[0])
# print(lista[1])
# print(lista[2])

# 여러개의 데이터를 지정해서 가져오고 싶을 때는 slcing 사용 가능 
# 슬라이싱의 결과값은 같은 list로 출력
# 0~5번쨰 까지 출려
# lista=['a','b','c','d','e','f','g']
# print(lista[:5])
# 0~5번쨰 까지 출력한 결과물의 type 출력
# print(type(lista[:5]))

# 문자열은 메모리 리스트와 유사한 자료구조를 가지고 있음
# 문자열은 값을 추가하거나 수정할 수 없다. --> 불변 객체
# list는 값의 추가,삭제,수정이 가능한 구조를 가지고있다. 
# 

# 연습문제
# list안에 list값을 조회
# list_ex=['a','b','c',[1,2,3]]
# numbers=list_ex[-1]
# answer=list_ex[-1][0]+list_ex[-1][-1]
# print(answer)

# 리스트 더하기
# 리스트 2개 선언 + 하나의 리스트로 만들기

# list_a=[1,2,3,4,5,6]
# list_b=[7,8,9,10]
# result=list_a+list_b
# print(result)

# 리스트 길이구하기

# print(len(result))

# 한개의 값 수정하기
# -> 1개의 값만 바꿀땐 1개의 값으로
# -> 여러개의 값을 바꿀땐 다른 리스트로 대체

# lista=[1,3,5,6,7,9]
# lista[1]=4
# print(lista)
# lista[2]=[5,5,5]
# print(lista)

# lista=['1','2','3','4','1','1','3']
# print(lista.count('1'))

# 리스트 요소 삭제하기 
# del 리스트[인덱스]
# del 은 파이선에 내장되있는 삭제 방식
# 인덱스를 사용해서 지울려면 del 사용해야함 
# lista=[1,3,5,6,7,9,10]
# del lista[2]
# print(lista)
# del lista[3:5]
# print(lista)

# remove 로 삭제
# remove는 list에 내장된 함수
# 리스트.remove(값)
# 중복되어있을 때 앞에 있는걸 먼저 지움 

lista=[1,3,9,5,9,6,7,9,10]
# lista.remove(5)
# print(lista)


# 모든 특정한 숫자 9를 삭제


# 방법1
# count=0
# for i in range(len(lista)) :
#     if lista[i-count]==9:
#         del lista[i-count]
#         count=count+1
# print(lista)

# 방법2 
# listb=[]
# for i in range(0,len(lista)) :
#     if lista[i]!=9 :
#         listb.append(lista[i])
# print(listb)

# 방법3
# for i in range(len(lista)) :
#     if 9 in lista :
#         lista.remove(9)
#     else :
#         break
# print(lista)


# lista=[1,3,9,5,9,6,7,9,10]
# listb=[]
# for i in range(len(lista)) :
#     if lista[i]!=9 :
#         listb.append(lista[i])
# print(listb)

# for i in range(len(lista)) :
#     if 9 in lista :
#         lista.remove(9)
#     else :
#         break
# print(lista)

# count=0
# for i in range(len(lista)) :
#     if lista[i-count]==9 :
#         del lista[i-count]
#         count=count+1
# print(lista)



# 리스트값 추가하기 append
# lista=[1,3,5,7]
# 9,10 을 append + 출력
# lista.append(9)
# lista.append(10)

# print(lista)

# 리스트 insert 
# lista.insert(2,'abc') : 인덱스 2 위치에 abc 추가
# lista.insert(2,'abc')
# print(lista)

# 리스트 extend : iterable 객체를 list에 추가할떄 사용
# extend는 각 요소를 꺼내에 맨 뒤에 추가 
# 다른 리스트 요소들을 리스트 형태가 아닌 값의 형태로 추가하고 싶을 때 
# lista=[1,3,9,5,9,6,7,9,10]
# listb=[10,20,30]
# lista.extend(listb)
# print(lista)l

# 리스트 정력은 sort() 함수 사용
# sort()는 오름차순 정렬
# sort(reverse=True) : 내림차순임 
# numa=[5,3,18,4,2,1]
# numa.sort(reverse=True)
# print(numa)

# chlist=['brad','john','adam']
# # chlist.sort(reverse=True)
# # print(chlist)

# # list 뒤집기 
# chlist.reverse()
# print(chlist)

# 리스트 위치반환
# lista=['김돌쇠','감갑순','김철수']
# print(lista.index('김철수')+1)


# 리스트에서 요소 끄집에내기 
# 마지막 요소 끄집어내기 
# remove & return last value
# lista=['김돌쇠','감갑순','김철수']
# lastvalue=lista.pop()
# print(lastvalue)
# print(lista)
# 문자 리스트를 문자열로 만들기
lista=['hello','world','python']
st1=''
st2=st1.join(lista)
print(st2)

for i in lista :
    st1=st1+i
print(st1)
# 문자열을 문자 리스트로 만들기 
sta='hello world python'
mysta1=list(sta)
mysta2=sta.split()
print(mysta1) # ['h', 'e', 'l', 'l', 'o', ' ', 'w', 'o', 'r', 'l', 'd', ' ', 'p', 'y', 't', 'h', 'o', 'n']
print(mysta2) #['hello', 'world', 'python']

# 문자열뒤집기 문제 
# 방법1
# stlist=list(my_string)
# stlist.reverse()
# answer="".join(stlist)

# 방법2 [::-1] 뒤에서부터 조회하는거 
# answer=my_string[::-1]

# 방법3 
# revered(문자열)
# answer="".join(reversed(my_string))
# 방법4
# answer = ''
# my_string=list(my_string)
# for i in my_string:
#     answer= i+ answer

#짝수 홀수 갯수
# num_list=[1,2,3,4,5]
# answer=[]
# num1=0 # 짝수 개수
# num2=0 # 홀수 개수 
# for i in num_list:
#     if i%2==0 :
#         num1=num1+1
#     else :
#         num2=num2+1
# print(num1)
# print(num2)
# answer=[num1,num2]
# print(answer)

# even=0
# odd=0
# answer=[]
# for i in range(len(num_list)):
#     if num_list[i]%2==0 :
#         even=num_list.count(num_list[i])+even
#     else:
#         odd=num_list.count(num_list[i])+odd
# answer.append(even)
# answer.append(odd)


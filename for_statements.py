# while 문의 기본구조
# while 조건식 : # 조건식이 참인경우 반복 -> 무한반복이 기본전제
#     실행문

# 조건 체크 후 True이면 실행문을 1회 실행 시키고
# 다시 조건을 체크하러 돌ㄹ아온다. 그리고 True이면 또 다시 실행
# # 그러다 조건이 False 되면 while 문 종료
# a=0
# while a<5 :
#     print(str(a)+'번 반복')
#     a+=1
# # 1~1000까지만 
# a=1
# while a<1001 : 
#     print(a)
#     a+=1
# a=0
# snum=0
# while a<1000 :
#     a+=1
#     snum=snum+a
# print(a)
# print(snum)
# print(snum/1000)

# while문에서 반복을 진행하다가 break를 만나면 반복문 종료
# (1) if문을 써서 xx한 조건에 break

# a=1
# nsum=0
# while True :
#     nsum+=a
#     if a==1000 :
#         break
#     a+=2
    

# (2) 홀수만 더해서 
# a=1
# nsum=0
# while a<1000:
#     nsum+=a
#     a+=2
# print(nsum)

# continue : 이 구문을 만나면, 다시 반복문 조건으로 이동 
# 하단에 불필요한 로직을 수행하지 않고 다시 조건을 이동할수 있게 해준다 .
# a=0
# nsum=0
# while a<1000:
#     a+=1
#     if a % 2==0 :
        
#         continue
#     nsum+=a

# print(nsum)
############# 연습문제 ################
# 
# list_num=[]
# list_size=int(input('리스트의 크기를 입력하세요'))
# size_num=0
# while size_num<list_size :
#     size_num+=1
#     if list_size>10 :
#         list_size=int(input('리스트의 크기를 10 이하로 다시 할당하세요'))
#     else : 
#         nums=int(input('리스트에 값을 할당해 보아요 : '))
#         list_num.append(nums)
#         if len(list_num)==list_size :
#             break
# print(f'크기 {list_size}의 리스트 {list_num}이 할당 되었어요')

############## 로또번호 생성기 ################
# 랜덤의 값을 추출하는 파이선 라이브러리 -> random
# 리스트의 크기는 6개 
# import random

# lotto=[]
# ncount=0
# while ncount<7 :
#     ncount+=1
#     lotto.append(random.randint(1,45))
#     if ncount==6 :
#         break
 
        
# print(f'오늘의 로또 번호는 {lotto}')


    
# for문의 기본구조
# for 변수 in 반복가능한자료형:
#     실행문
# lista=[1,2,3,4,5,6,7,8,9,10]
# for i in lista :
#     print(i)

# # range 문법 : range(x,y) x이상 y미만
# range(y) :0이상 y미만

# for i in range(1,101) :
#     print(i)
# # range의 의미
# v1=list(range(1,10))
# print(v1)


# v1=list(range(10,20))
# # for a in 리스트

# for i in v1 :
#     print(i)

# # for a in range
# for i in range(len(v1)) :
#     print(v1[i])
# for a in list 구문으로는 원본리스트 데이터를 변경할 수 없다
# lista=[10,20,30,40]
# for a in lista :   ### 이런방식으론 추가 안댐
#     a=100
# 직접 리스트의 접급해야지 원본을 바꿀수 있다 .

# 리스트를 만드는 방법중에 리스트 컴프리핸션이라는 방법이 있다. 
# 리스트에 0~9까지 담는방법
# 방법(1)
# lista=[0,1,2,3,4,5,6,7,8,9]
# # 방법(2)
# lista=list(range(0,10))
# # 방법(3)
# lista=[]
# for a in range(10):
#     lista.append(a)
# # 방법(4) 리스트 컴프리핸션
# # 장점 : 간결하다 
# lista=[ i*2 for i in range(0,10) if i%2==1]
# print(lista)


# # 리스트 내포 


# arr=[5, 1, 4]
# for i in range(len(arr)) : 
#     arr[i]*arr[i]

# print(arr)



# a='abc'
# b='aabcc'
# print(a.count('a'))
# control="wsdawsdassw"
# answer = 0
# dict_con={}
# for i in control:
#     if i in dict_con :
#         dict_con[i]+=1
#     else : 
#         dict_con[i]=1
# print(dict_con)



# 한 반에 수학점수가 60점 넘으면 합, 미만이면 불
# 학생의 번호 순서대로 있을 때 
# listA=[90,25,67,45,80]
# # 출력 예 ) 1번 학생은 합격 입니다. 
# for i in range(len(listA)):
#     if listA[i]> 60 :
#         print(f'{i+1}번 학생은 합격입니다.')
#     else :
#         print(f'{i+1}번 학생은 불합격입니다.')
# num=0
# for i in listA :
#     num+=1
#     if i>60 :

#         print(f'{num}은 합격')
#     else :
#         print(f'{num}은 불합격')


# answer = ''
# myString="abstract algebra"
# for i in myString.inpdex() :
#     if myString[i] == 'a' :
#         myString[i]='A'

# for문과 break문 : for문에서 break를 반드시 써야하는 상황
# # 선착순 한명만 찾는 상황
# listA=['b','b','ab','a','b','a']

# 출력결과 : n번쨰 고객이 이벤트에 당첨되었습니다.
# for i in range(len(listA)) :
#     if listA[i]=='a':
#         print(f'{i+1}번째 고객이 이벤트에 당첨되었습니다')
#         break

# for 문을 이용한 구구단 
# 5단 출력 결과 구구단 
# for j in range(1,11) :
#     print(f'{nums} * {j} = {nums * j}')

# while True :
#     nums=int(input('구구단 몇단을 계산해드릴까요 : '  ))
#     for i in range(1,10):
#         print(f'{nums} * {i} = {nums * i}')


# 5단~9단까지 출력

# for i in range(5,10) :
#     for j in range(1,10)  :
#         print(f'{i} * {j} = {i * j}')

# num=5
# while num<10 :
#     for i in range(1,10):
#         print(f'{num} * {i} = {num * i}')
#     num+=1

# for 문으 이용한 정렬 알고리즘
# lista=[10,20,30,40]
# 리스트 0번쨰와 1번째 자리를 바꾸려면 
# 리스트 0의 값이 바껴서 교체가 안됌
# lista[0]=lista[1]
# lista[1]=lista[0]

# # 그래서 10이라는 숫자를 temp 에 킾해둠
# temp=lista[0]
# lista[0]=lista[1]
# lista[1]=temp
# print(lista)

# 파이선에서 지원하고있는 문법
# lista[0], lista[1]=lista[1],lista[0]
# print(lista)


# listA=[93,45,21,30,20,94,66,71,45]



# print(listA)
# 선택정렬 : 0번쨰 인덱스부터 가장 작은 값을 채워나가는방식
# 첫번쨰 for 문은 채워나가야할 인덱스를 의미 
# 두번쨰 for 문은 비교의 대상이 되는 인덱스를 의미 
## 오름차순으로 정렬하기 
# for i in range(len(listA)-1) : ## 마지막애는 비교대상이 없어서 있을필요없음. 
#     for j in range(i+1,len(listA)):
#         if listA[i]>listA[j] :
#             listA[i],listA[j]=listA[j],listA[i]
            # temp=listA[i]
            # listA[i]=listA[j]
            # listA[j]=temp



# 버블정렬
# 
# for i in range(len(listA)) :
#     # i가 0일때
#     # j는 9번반복
#     for j in range(len(listA)-1-i):
#         if listA[j]>listA[j+1]:
#             listA[j], listA[j+1] = listA[j+1], listA[j]

# print(listA)
# arr1=[[1,2],[2,3]]
# arr2=[[3,4],[5,6]]	
# answer = []
# # for i in range(len(arr1[] :
# #     for j in arr2:
# #         answer[i][j] = arr1[i][i]+arr2[j][j]

# for i in range(len(arr1)) :
#     temp=[]
#     for j in range(len(arr1[i])) : ## 각 요소들의 길이는 같기떄문에 0번쨰만알아도 댐
#         temp.append(arr1[i][j]+arr2[i][j])
#     answer.append(temp)



# print(answer)
# listA=[93,45,21,30,20,94,66,71,45]
# for i in range(len(listA)) :
#     for j in range(i+1,len(listA)-1) :
#         if listA[j]>listA[j+1] :
#             listA[i],listA[j]=listA[j],listA[i]
# print(listA)

## 버블정렬
# for i in range(len(listA)) :
#     for j in range(len(listA)-i-1) :
#         if listA[j]>listA[j+1] :
#             listA[j],listA[j+1]=listA[j+1],listA[j]
# print(listA)



# for i in range(len(listA)) :
#     for j in range(len(listA)-i-1) :
#         if listA[j]>listA[j+1] :
#             listA[j],listA[j+1]=listA[j+1],listA[j]
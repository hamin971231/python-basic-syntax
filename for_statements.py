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
lista=[0,1,2,3,4,5,6,7,8,9]
# 방법(2)
lista=list(range(0,10))
# 방법(3)
lista=[]
for a in range(10):
    lista.append(a)
# 방법(4) 리스트 컴프리핸션
# 장점 : 간결하다 
lista=[ i**2 for i in range(0,10)]
print(lista)


# 리스트 내포 


arr=[5, 1, 4]
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


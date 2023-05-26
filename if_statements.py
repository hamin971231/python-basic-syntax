
# # 괄호로 묶어주고 & 나 | 사용가능 

# a=10
# if (a>5) | (a>10) :
#     print('참입니다1')

# if a>5 or a>10 :
#     print('참입니다2')
# # 비트연산이란 2진법의 숫자를 or(|), and(&), xor(^) 등으로 cpu 내부적으로 계산하는 방식
# # 1111 and 1000 => 1000
# # 1111 or 1000 => 1111 

# # and는 &와 같고, or 은 | 와 같다, not은 부정의 의미
# # not True는 False가 되고, not False는 True가 된다.

# # 대입연산자
# # a=10
# # a=a+1로 해도 되고, a+=1 로 표현해도 된다. 
# # -=, /=, *= 도 있음
# # a/=5 = > a=a/5
# # 
# # 비교연산자 중에 chaining (범위로 표현할 수 있다.)
# # a=10
# # if a>5 and 100< a:
# #    print('참입니다')  
# a=10
# if 5 < a <100 :
#     print("참입니다")




# if 문의 기본 문법
# else 는 optional한 요소임, else 상단에 있는 if or elif에 종속된다
# elif도 마찬가지로 elif 상단 if에 종속된다.
# ~ 중 하나만 실행시키고자 할 때는 elif를 if 에 종속시키면됌 
# if 참조건 :
#     실행문
#     실행문
# else는 선택적인부분임

# a=int(input('숫자를 입력하세요'))
# if a>10:
#     print('a는 10보다 큽니다')
# else : 
#     print('a는 10보다 작습니다.')

# trueOrFalse=True
# if trueOrFalse:
#     print('참')
# else :
#     print('거짓입니다.')

# 실습문제 
# money=int(input("얼마를 가지고 있습니까?"))
# if money>=30000 :
#     print("택시를 타고 가시오")
# else :
#     print("걸어가시오")

# if문 한줄로 쓰기
# a=10

# if a >1: print('a는 1보다 큽니다') ;print('a는 1보다 큽니다')
# 삼항연산자 (간단한 식으로 표현)
# 먼저 if문의 실행문을 if 문 앞으로 옮기고, 세미콜론 필요없음
# a=10 
# print('a는 10보다 크다') if a>10    else  print('a는 10보다 작습니다.')

# 실행문을 실행하기 위해 사용한다기 보단, 참인경우에 어떤값, 거짓인 경우 어떤값을 쉽게 result에 담기위해 사용
# result='a는 10보다 큼' if a>10 else 'a는 10보다 작음'
# print(result)

# lista=[1,2,3,4,5,6,7,8,9,10]
# number=int(input('숫자입력'))

# if number in lista :
#     print('전재')
# else :
#     print('없음')

# 10이상부터 수수료, 수수료는 10의 배수단위로 10000증가

# weight=int(input('짐의 무게는 얼마입니까 ? '))
# money=0
# if weight >= 10 :
#     money=10000*(weight//10)
#     print('짐의 무게는 : %d kg 이며 수수료는 %d 입니다' %(weight,money)) 
# else :
#     money=0
#     print(f'짐의 무게는 : {weight} kg 이며 수수료는 {money} 입니다') 


# # f formating
# print(f'짐의 무게는 : {weight} kg 이며 수수료는 {money} 입니다')

# money=int(input('가진 돈이 얼마야'))
# hungry=input('배고픔? (Y or N) ')
# if money >= 10000 and hungry=='Y' :
#     print('저녁을 사먹으시오')
# else :
#     print('집에 가시오')

# a와 b와 같은지 비교하는 연산자 
# 객체타입의 경우에는 메모리 주소를 비교 
# 숫자, 문자, bool 기본타입의 경우 값을 비교한다. 
# 숫자 문자 bool 같은 경우에는 데이터 pool을 만들어서 재확용한다 .
# 그래서 값을 비교할 때 메모리 주소가 아니라, 데이터 pool에서 값을 직접 비교한다.
a=[10,20] 
b=[10,20]
if a is b : 
    print('참입니다 ')

a=10
b=10
################### pass #########################
if a==b :
    pass 
    # pass 시키는것

else : 
    print('안같음')

### 369 
## 방법(1)
for i in ['3','6','9'] :
    answer +=str(order).count(i)
## 방법(2) 


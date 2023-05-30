
# 람다함수 : 
# (1) 함수를 간편하게 표현하기 위한 방식
# (2) 함수를 변수에 담기 위한 방식 
# lambda 매개변수 : 실행문

# def add(a,b) :
#     return a+b
# print((add(1,2)))

add_lambda= lambda a, b : a+b


# 매개변수 a를 입력했을 때, a의 제곱이 출력되는 람다함수
square_lambda=lambda a : a**2

# 리스트에 람다함수를 담아서 사용가능

cal_list = [ lambda a,b : a+b, lambda a,b : a-b,lambda a,b : a*b,lambda a,b : a/b]
cal_dict={'plus':lambda a,b : a+b,
          'minus':lambda a,b : a-b,
          'multiply':lambda a,b : a*b,
          'divide':lambda a,b : a/b }

print(cal_dict['plus'](1,2))
print(cal_dict['minus'](5,6))

# 람다로 입력한 매개변수가 짝수이면 true, 홀수면 false 

oddOrNot = lambda x : True if x%2==0 else False

print(oddOrNot(1))

# lista=[1,2,4,6,7]
# def myIndex(list_input,number_input) :
    
#     for i in range(len(list_input)) :
#         if list_input[i]==number_input :
#            result=i
#            # break를 할 필요 없이, 바로 return을 해도된다.
#            # return 하게 되면 함수전체가 강제 종료된다.
#            break
#     return result

# map 함수
# 특정함수와 반복가능한 자료형을 입력받아, 특정함수가 수행한 결과값을 리턴하는 함수
# 사용예지 : map(함수, 리턴(또는 튜플 등등))

def two_times(x):
    return x*2
print(map(two_times,[1,2,3,4])) ## 계산결과가 리스트는 아니지만 리스트로 감싸줄수있음.
listb=list(map(two_times,[1,2,3,4]))
print(listb)

# map 함수와 람다를 사용해서 제곱하는 함수
# map의 역할 대상이 되는 리스트를 가지고 새로운 리스트를 만들어 내는 것. 
list_square=list(map(lambda x : x**2,[1,2,3,4]))
print(list_square)


# filter함수
# filter의 역할은 대상이 되는 리스트에서 함수를 적용하여 참/거짓 조건으로 값을 걸러내는것
def trueOrNot(x) :
    if x > 0 :
        return True 
    else :
        return False
lst=list(filter(trueOrNot,[-1,0,3,-2,5]))
print((lst))

lst_true=list(filter(lambda x: True if x>0 else False, [-1,0,3,-2,5]))
print(lst_true)

lst_true=list(filter(lambda x: True if x>0 else False, [-1,0,3,-2,5]))
print(lst_true)
# 만약 map을 쓰면
# 새로운 리스트에 담기게됨. map은 변환시키는 과정
# [False, False, True, False, True] 결과임

# 함수형 프로그래밍을 사용해서, 주어진 리스트에서 홀수만 추출
list_formal=[4,7,1,2,5,6,8]
list_odd=list(filter(lambda x: x if x%2==1 else False , list_formal))
list_new=list(map(lambda x: x**2,list(filter(lambda x: x if x%2==1 else False , list_formal))))
print(list_new)

# sum : 주어진 자료들의 총합
print(sum([1,2,3]))
# 예제
list_odd=list(filter(lambda x: x if x%2==1 else False , list_formal))
print(sum(list_odd))

# 문자를 아스키코드 변환 : ord()
print(ord('a'))
# 숫자 107이 의미하는 아스키코드상의 문자는?  : chr()
print(chr(97))

# 문자열이 주어질떄 숫자를 제외하고 문자값만 새로운 문자열로 만들어보아라
str1='123adsf23fd'
print(ord('z')) # 소문자 a~z : 97-122

print(ord('Z')) # 소문자 A~z : 65-90
new_str=''
for i in str1 :
    if (122 >= ord(i) >= 97) or (90 >= ord(i) >= 65) :
        new_str +=i
print(new_str)

# 절대값 구하기 : abs()

print(abs(-3))

# 주어진 리스트를 map을 사용해서 절대값으로 변환한 리스트를 출력해보자
list_minus=[-1,-5,12,-5]
list_ans=list(map(lambda x: abs(x), list_minus))
print(list_ans)


# 재귀함수
# 재귀함수란 함수내에서 자기자신을 호출하는 함수.
# 재귀함수는 반드시 재귀함수를 종료시키는 조건이 들어가야한다.
# 팩토리얼 
# def factorial_first(num1):
#     fact=1
#     for i in range(1,num1+1) :
#         fact=fact* i
#     return fact

# print(factorial_first(4))

# def test(n) :
#     if n==1 :
#         return 1 
#     return n+test(n-1)    
# result=test(10)
# print(result)
# def factorial(n) :
#     fact=1
#     if n==1 :
#         return 1
#     else:
#         fact=n*factorial(n-1)
        
#     return fact
# print(factorial(4))
       
# 재귀함수를 반드시 써야하는 상황 
# 반복의 횟수를 알 수 없을 때
# 다섯개의 숫자중에 2개씩 숫자를 추출하는 경우의 수를 구하고자한다.
# 2개씩 숫자를 추출해서 리스트에 담아 마지막에 모든 리스트를 출력
# [[10,20],[10,30][10,40]......]
# listA의 2개의 조합을 구하셈 
listA=[10,20,30,40,50]
listB=[]
count=0
for i in range(len(listA)):
    for j in range(i+1,len(listA)): 
        count+=1
        listB.append([listA[i],listA[j]])
print(count)

def combi(lista) :
    listb=[]
    if 





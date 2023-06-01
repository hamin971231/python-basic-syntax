# 특정한 input값이 있을 때, 해당 값을 복잡한 로직을 통해서 연산을 한다고 가정하자 
# 그런데, 해당 연산은 매우 빈번하기 사용이 된다고 가정하자.

# 복잡 로직의 연산을 함수화 시켜서 재사용할 수 있게 해보자.
# input값이 있어도 되고 없어도 된다. + return 값이 있어도 되고 없어도 된다 . 
# def myfunc(myinput) :
#     calc=(((myinput+10) * 20)/10) **2
#     return calc 
# 정의된 함수를 호출할떄는 함수명(input)의 형태로 호출하게된다
# ex) result=myfunc(200)

# 함수 직접 구현해보기
# myPlusFunc
# 함수의 로직은 사용자의 input을 받아 input값의 누적합을 더하는 하수
# ex) 1+2+...+100

# def myPlusFunc(input) :
#     calc=0
#     for i in range(input+1) :
#         calc=i+calc
#     return calc
# print(myPlusFunc(100))

# input값을 2개를 받아 더한 뒤 *2해서 리턴
# 그리고 해당함수를 호출하여 호출된 결과값을 result에 담아 출력
# def myCal(x,y) :
#     answer=(x+y)*2
#     return answer
# print(myCal(1,1))

# 리스트의 인덱스 함수를 for 문 혹은 while 문을 통해 함수로 구현
lista=[1,4,6,9]
# for i in range(len(lista)) :
#     if lista[i]==9 :
#         break
# print(i)
# print(f'{lista[i]}의 인덱스는 {i}입니다')

# 함수로 만들기 
# 인풋이 2개, 리스트하나 인덱스 찾고자하는 숫자 하나 

# 
# def myIndex(list_input,number_input) :
    
#     for i in range(len(list_input)) :
#         if list_input[i]==number_input :
#            result=i
#            break
#     return result

# print(myIndex(lista,9))

# mystring="cccCCC"
# for i in mystriㅍng :
#     print(i)
# num1=int(input('반지름의 길이를 구하시오'))
# def circle(circle_len) :
#     circle_size=circle_len**2*3.14
#     return circle_size ##     circle_size=circle_len**2*3.14  바로 리턴해도 됌


# print(f'원의 넓이 : {circle(num1)}')

# def hello1() :
#     ment=print('hello python')
#     return ment

# hello1()
# def hello2() :
#     return 'hello python'
# print(hello2())

# 입력값의 갯수가 정해져 있지 않고 multiple한 함수 
# *은 all의 의미로 사용됨
# def sum(*args) :
#     totalValue=0
#     for i in args :
#         totalValue+=i
#     return totalValue
# totalValue= sum(1,2,3,4,5)
# print(totalValue)

# 두개 이상의 리턴값이 있는 경우 : 튜플형태로 데이터 리턴된다. 

# def cal(a,b) :
#     result1=a+b
#     result2=a-b
#     result3=a*b
#     return result1, result2, result3

# calValue=cal(1,2)
# print(calValue)
# print(f'계산한 첫번쨰 결과: {calValue[0]}, 계산한 두번쨰 결과: {calValue[1]}, 계산한 세번째 결과: {calValue[2]} ')

# 함수에서 default값 미리 세팅 
# def cal(a,b,c='plus') :## 디폴트를 플러스로 세팅, 다른옵션을 주면 덮어쓴다
#     if c=='plus':
#         result=a+b
#     elif c=='minus':
#         result=a-b
#     elif c=='multiply':
#         result=a*b
#     return result

# calValue=cal(1,2)
# print(f'계산 결과 {calValue} ')

# 매개변수의 순서를 안맞추고도 원하는 매개변수의 자리에 값을 넣어 함수를 호출하는 방법

# def whoAreYou(name,age,gender):
#     print(f'제 이름은 {name}이고, 나이는 {age}, 성별은 {gender} 입니다. ')

# whoAreYou(age=19,name='길동',gender='남자')

# 파이선에서 디폴트값 세팅하는 대표적인 예시가 print함수
# print 2개를 사용해서 줄바꿈 없이 헬로월드 ㄱㄱ

# print('hello',end=' ')
# print('world')

# 지역변수와 전역변수
# 지역변수 : 함수내에서의 변수, 함수내에서만 유효
# # 전역변수 : 함수밖에서의 변수, 함수내에서도 인식가능 
# a=100
# def sum(a,b) :
    # 함수내에서 함수밖의 전역변수를 사용하려면 global 키워드 사용
    
    # 여기서 a의 값은 100인가 10인가
    # 전역변수인 a=100보다, 함수내에서 선언한 a=10을 우선적으로 인식
#     result=a+b
#     return result

# result=sum(10,20)
# print(result)

# 함수내의 result라는 변수는 함수 밖에서 인식불가
# 우리가 result 프린트 할 수 있었던 것은, 함수내에서 어떤 값을 return 해줬지 떄문
# for문마다 같은 변수를 사용하는 것은 전역변수이긴 하지만 재할당을 해서 사용하는 것이므로 어차피 reset되서 문제되지 않는다.
# print(a)


# lista=[10,20,30,40]
# for a in range(len(lista)) :
#     print(a)
# print(a)
# 이중 for 문을 사용할 때에는 문제가 될수있음
# 다중 for 문을 쓸 때는 상위의 for문의 변수를 잃어버리기 때문에, 다른 변수명 사용
# for a in range(len(lista)) :
#     for b in range(len(lista)) :
#         print(a)
#         print(b)




# 함수내에서 전여변수에 영향을 끼치는 방법 global
# 기본적으로 함수내에서 함수 밖의 전역변수를 수정할 수 없다.
# 그 이유는 저장되는 위치가 다르기떄문. 
# 
# result=10
# def sum(a):
#     global result
#     result += a
#     return result
# value =sum(10)
# print(value)

# 객체는 힙메모리 영역에 저장되는데, 함수내에서도 접근하여 추가/수정이 가능하다.
# 스택영역에 있는 지역변수는 함수가 끝나면 휘발되지만, 힙메모리는 휘발되지않는다. 

# lista=[2,3,4]
# def appendTest(input1,input2): 
#     input1.append(input2)

# appendTest(lista,5)
# print(lista)


# 만약에 지역변수가 함수호출이 끝난뒤에도 남아있다면 어떻게 될까 
# 함수에서 사용하는 지역변수가 계속 남아있으면 메모리 낭비 뿐만 아니라 
# 다른 함수에서 해당 변수명을 사용할 수 없는 불편함이 있음
# def test1(result):
#     result += 10
#     return result
# def test2(result) :
#     result += 100 
#     return result


# a=test1(20)
# b=test2()
# print(a)

# def sum(*args) :
#     totalValue=0
#     for i in args :
#         totalValue+=i
#     return totalValue
# totalValue= sum(1,2,3,4,5)
# print(totalValue)
# def mySort(list_input):
#     for i in range(len(list_input)-1) :
#         for j in range(i+1,len(list_input)) : 
#             if list_input[i]> list_input[j] :
#                 list_input[i],list_input[j] =list_input[j],list_input[i]
#     return lista




# lista=[5,1,2,3,6]

# print(mySort(lista))
# 리스트a에 리스트b를 담으면 객체의 주소가 복사된다
# 그래서 리스트b가 리스트a와 동일한 주소, 동일한 데이터를 갖게댐
# lista=[5,1,2]
# listb=lista
# # 주소 출력하는 함수 : id

# print(id(lista))
# print(id(listb))

# # lista와 값은 갖되, 동일한 메모리 주소가 아니게 할당하고싶으면, copy함수 사용
# # 얕은 복사 즉, 객체안의 객체의 값은 (메모리)주소로 복사가 된다.
# # 깊은 복사는 copy.deepcopy를 사용해서 객체의 객체도 모두 value로 복사


#     # for a in range(len(n))
#     #     answer.append(n[len(n)-a-1])


# import copy ## 해야함

# listb=copy.copy(lista)
# print(id(listb))

# n=12345

# answer = []
# for i in str(n) :
#     i=int(i)
#     answer.append(i)
# answer.reverse()


arr=[5,9,7,10]
divisor=5
answer = []
for i in arr :
    if (i%divisor) == 0 :
        answer.append(i)

    else :
        answer=[-1]
answer.sort()
print(answer)

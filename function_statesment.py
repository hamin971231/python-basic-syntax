# 특정한 input값이 있을 때, 해당 값을 복잡한 로직을 통해서 연산을 한다고 가정하자 
# 그런데, 해당 연산은 매우 빈번하기 사용이 된다고 가정하자.

# 복잡 로직의 연산을 함수화 시켜서 재사용할 수 있게 해보자.
# input값이 있어도 되고 없어도 된다. + return 값이 있어도 되고 없어도 된다 . 
def myfunc(myinput) :
    calc=(((myinput+10) * 20)/10) **2
    return calc 
# 정의된 함수를 호출할떄는 함수명(input)의 형태로 호출하게된다
# ex) result=myfunc(200)

# 함수 직접 구현해보기
# myPlusFunc
# 함수의 로직은 사용자의 input을 받아 input값의 누적합을 더하는 하수
# ex) 1+2+...+100

def myPlusFunc(input) :
    calc=0
    for i in range(input+1) :
        calc=i+calc
    return calc
# print(myPlusFunc(100))

# input값을 2개를 받아 더한 뒤 *2해서 리턴
# 그리고 해당함수를 호출하여 호출된 결과값을 result에 담아 출력
def myCal(x,y) :
    answer=(x+y)*2
    return answer
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
def myIndex(list_input,number_input) :
    
    for i in range(len(list_input)) :
        if list_input[i]==number_input :
           result=i
           break
    return result

print(myIndex(lista,9))




# # 클래스의 사용
# # 1) 같은 기능의 함수의 집합
# # 2) 객체를 만들기 위해 사용

# # 3) 사칙연산 함수가 있을떄, 같은 기능을 하므로, calculator라는 클래스에 모아둘수 있다.
# # 명명규칙: 일반적으로 클래스는 대문자로 시작, 변수명,함수명은 소문자로 시작 -> camelcase

# # 함수의 집합으로서의 클래스 -> 일반적이지 않은 형태

# class Calculator :
#     def plus(a,b) :
#         return a+b
#     def minus(a,b) :
#         return a-b
#     def multiply(a,b) :
#         return a*b
#     def divide(a,b) :
#         return a/b
# print(Calculator.plus(3,5))
# # 위 클래스의 문제점은 클래스 내에서 누적된 값을 변수로 갖고 있지 않다.

# class Calculator :
#     result=0
#     # 클래스명 변수 접근 가능 방법1 :  클래스.변수
#     # 방법2 : classmethod 데코레이터 사용
#     # 클래스 내에 선언된 함수는 메서드라고 부른다
#     @classmethod 
#     def plus(cls, a) :
#         # 클래스명.변수 를 쓰면 클래스 변수에 접근 가능
#         cls.result +=a
#     def minus(a) :
#         Calculator.result -=a
#     def multiply(a) :
#         Calculator.result *= a
#     def divide(a) :
#         Calculator.result /= a
# print(Calculator.result)
# Calculator.plus(5)
# print(Calculator.result)
# Calculator.plus(5)
# print(Calculator.result)

# # 객체란 클래스의 복제본, 인스턴스라 부르기도 한다. 
# # 객체의 사용이유
# # 클래스의 중복제거 : 변수와 함수의 재활용 어려움 해결
# # 객체 형식의 클래스의 기본구조
# class Calculator :
#     # 객체가 생성될때 init은 가장먼저 실행된다.
#     def __init__(self,result): # __init__ 은 생성자임
#                                # 생성자는 객체생성될때 객체변수를 초기화 (디폴트값)
#                                # result와 self.result 는 다른값이다
#         self.result=result ## 사용자에게 받아서 세팅하겠다 0이면 클래스 자체에서 0으로 세팅 
#     # 클래스 내의 함수의 메서드내의 첫번쨰 매개변수는 객체를 의미한다.

#     def plus(self,a) :
#         self.result += a
#     def minus(self,a) :
#         self.result -=a
#     def multiply(self,a) :
#         self.result *= a
#     def divide(self,a) :
#         self.result /= a
# # 클래스 생성시 매개변수를 통해 초기값 세팅가능

# aCompany = Calculator(516)
# aCompany.plus(100)
# bCompany = Calculator(2000)
# bCompany.plus(100)

# print(aCompany.result)

# print(bCompany.result)

# Person이라는 클래스를 만든다
# 생성자로 이름(name), 나이(age), 성별(gender), email라는 매개변수를 받아 각각의 객체변수를 만든다.
# register 이라는 메서드를 만들고, 해당 메서드에서는 myinfo라는 객체변수에 이름나이성별이메일을 문자열로 담는다.
# 실행: 2명의 person을 만들고, print(p1.myinfo),print(p2.myinfo)

# import datetime
# class Person :
#     def __init__(self,name,age,gender, email):
#         self.name=name
#         self.age=age
#         self.gender=gender
#         self.email=email
#         self.regDate=str(datetime.datetime.now())

#     def register(self) :
#         self.myinfo = self.name +" " + self.age +" " + self.gender+" "+self.email+" " +self.regDate

# p1=Person('조해민','27','Male','goaldl97123@naver.com')
# p2=Person('조한별','32','Female','hamin971231@gamil.com')
# p1.register()
# p2.register()
# print(p1.myinfo)
# print(p2.myinfo)

# 클래스의 상속
# 부모클래서에서의 기능을 자식클래스에서 물려받는것
# class 자식클래스명(부모클래스명) 이런형식으로 선언
class Calculator :
    def __init__(self):
        self.result=0
    def plus(self,a) :
        self.result += a
    def minus(self,a) :
        self.result -=a
    def multiply(self,a) :
        self.result *= a
# calculator 상속 후 divde 매서드 추가
class CalculatorChild(Calculator) :
    def __init__(self):
        self.result=0 # 자식클래스에서 생성자 설정하면 오버라이딩 됌
    def divide(self,a) :
        self.result /= a
    # 같은 함수명에 다른 매개변수를 추가한 매서드
    # 이러한 매서드 추가방식을 오버로딩(overloading)
    # 디바이드에 매개변수 하나가 입력되면 첫번쨰 디바이드, 
    # 두개가 입력되면 두번쨰 디바이드 
    
    def multiply(self, a):
        self.result *= (a+1)
    # 부모한테 있는 기능을 재선언하게되면, 
    # 부모의 기능보다 자식의 기능이 우선하게 되고, 이를 overriding이라고 한다
# if __name__ =='__main__' : ## class_statements 를 실행할 때는 정상적으로 출력하는데 다른 모듈에서 class_statements에서 import하면 실행이 안되게끔 통제
#     cc1=CalculatorChild()
#     cc1.plus(100)
#     cc1.divide(10)
#     print(cc1.result)
# print함수가 속해있는 클래스는 object 클래스를 상속받고있다
# 그런데 object클래스 안에는 list,dict 같은 파이썬에서 자주 사용되는 객체값을 value 형식으로 출력해주는 함수가 내장되어있다.

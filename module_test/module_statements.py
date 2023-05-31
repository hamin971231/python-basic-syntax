
class Calculator :
    def __init__(self):
        self.result=0
    def plus(self,a) :
        self.result += a
    def minus(self,a) :
        self.result -=a
    def multiply(self,a) :
        self.result *= a
class CalculatorChild(Calculator) :
    def __init__(self):
        self.result=100 # 자식클래스에서 생성자 설정하면 오버라이딩 됌
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


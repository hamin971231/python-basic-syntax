# # #표시는 프로그래밍에서 주석이라 말한다.
# # 주석은 파이썬의 인터프리터가 인식하지 못하도록 기호
# # 단축키는 컨트롤 슬래시 

# # 아래 a=1의 의미는 a와 1이 같다라는 의미가 아니라 
# # a라는 이름의 변수에 1을 담겠다라는 의미임. 
# a=1
# b='1'
# # print는 실행 후 결과값을 가시적으로 보여주기 위해 터미널창에 출력하는 것.
# # print(a)
# # print(b)


# # 변수명명규칙
# # 변수명을 지을떄는 숫자가 맨앞에 오면 안됌
# # 변수명 중간에 띄어쓰기, 특수기호 등을 일반적으로 쓰지않는다.
# # 특수기호는 별로 안사용하는데 언더바는 많이 사용한다
# # 변수 자료형 출력해보기
# # print(type(a))
# # print(type(b))

# # c=2.14353
# # print(type(c))

# # # 자료의 형변환 
# # # str(숫자)-> 문자, int(실수) -> 정수 

# # a=10
# # b=20
# # # 결과값이 1020이 나오도록 덧셈을 하여라
# # c=int(str(a)+str(b))
# # print(c)

# # # d의 소수부분을 잘라라 
# # d=2333.22316543542
# # print(int(d))


# # 문자 자료형
# # 문자는 "" or ''
# # 'a'라는 문자를 변수에 저장하면, 메모리에 어떤 숫자값으로 저장될까 ? 
# # y='a'
# # print(ord(y))
# # 아스키코드라는 문자와 매핑되는 테이블을 사용하여 약속된 숫자값으로 저장하고,
# # 현대에는 아스키코드와 표현범위의 한계로 인해, utf-8을 표준으로 지정하였음.

# # x='A'
# # print(ord(x))

# # multi line으로 문자열을 표현하고 싶으면, 쩜따옴표 3개를 사용하거나
# # 쌍따옴표 3개를 사용하면 된다
# # a='''hello
# # world'''
# # 이스케이프 문을 이용한 줄바꿈 
# # 이스케이프 문이란 '\n' or '\t' 등의 특수기호를 말한다.
# # \n은 줄바꿈, \t 는 tab키랑 동일 
# # 역슬래시 또 다른 활용 : 특수문자를 있는 그대로 표현하는 역할 
# #  a= "hello \n world"
# #  print(a)
# # # 그렇다면 python's easy 라는 문구 출력
# b="python's easy"
# print(b)

# c="쌍따옴표는(\") 파이선에서 문자를 의미한다"
# print(c)

# # 문자열 더하기 곱하기 
# # a라는 변수에 python, b에는 funny라는 문자열 담는다, c에는 a b 둘다 더한것 출력
# a='python '
# b='is funny'
# c=a+b
# print(c)

# # python 이라는 문자열이 두번 출력, is fun 은 한번
# c= a*2+b
# print(c)

# # 파이선에서 인덱스란, 특정위치를 가리키는 용도로 사용됌.
# # 인덱스의 사용방법은 원하는 대상의 [숫자값]
# # 프로그래밍에서는 대부분의 순서는 0부터 시작된다. 01234...
# # 문자 h를 출력하라 
# A="Python's fun Python's fun Python's fun"
# print(A[3])

# # 문자열의 마지막 문자를 출력하자
# print(A[-1])
# # 문자열의 길이를 출력
# print(len(A))
# print(A[len(A)-1])

# # 슬라이싱 
# # 몇번째부터 몇번째까지 잘라낸다.
# # 대상이 되는 값[시작:끝] -> 시작<= 값 < 끝 
# # python만 잘라내기
# a= "python is fun"
# b=a[:6]
# print(b)
# # x y 자리에 값이 없으면 처음부터 혹은 끝까지임. 
# # 6번째 부터 끝까지 잘라내서 b에 담아 출력
# c=a[6:]
# print(c) 

# # a[x:y:z] -> z는 z-1개씩 건너뛰고,
# # 2번째 이상 7번째 미만 문자열 중에 1개씩 건너뛰고 b에담아 출력.
# b=a[2:7:2]
# print(b)

# # a에서 슬라이싱 이용해 date에 날짜, day에 칠드런스데이
# a="20220505children's_day"
# date=a[:8]
# day=a[8:]
# print(date)
# print(day)

# 문자열 포맷팅이란 문자열 중간에 특정 문자(또는 숫자 등)를 삽입하는 방식
# %s : 문자열 , %d:정수, %f : 실수
# 포매팅 쓰는 이유 
# 1) 문자열을 직접 삽입하면 1회성으로 코딩할수 밖에 없지만, 
#    포맷팅은 변수값을 삽입할 수 있다.
# 2) 따옴표 여러번 안닫아도 된다.
# language=input('좋아하는 언어를 입력하세요')
# time=int(input('그 언어를 몇번이나 공부하셨나요?'))
# a="I studied %s %d times" % (language,time)
# print(a)

# 아래와 같이 코딩하면 따옴표로 열고 닫고를 너무  많이해서 귀찮음
# a='I studied ' + language + ' very hard ' + str(time) + ' time'
# print(a)

# 실습
# age=int(input("나이가 몇살이신가요? : "))
# weight=float(input("몸무게가 몇 키로그람 이신가요? : "))
# a='My age is %d, and weight is %f ' % (age, weight)
# print(a)

# 프로그램 중지 컨트롤+c

# 문자열 관련 주요 함수
# count : 대상 문자열에 지정한 문자가 몇개가 있는지 출력하는 함수
# a='python'
# countNum=a.count('o')
# print(countNum)
# # find : 대상 문자열에서 지정한 문자가 몇번째 index에 있는지 찾는 함수
# # index : find와 같은기능
# findNum=a.find('o')
# indexNum=a.index('o')
# print(findNum)
# print(indexNum)
# # 없는 문자 찾았을 때는 -1 return 해줌
# print(a.find('x'))

# whatyouwant=input('아무런 문자나 입력해주세요')
# search=input('찾고자하는 문자 1개만 입력해주세요')
# result=whatyouwant.find(search)
# if result == -1:
#     print("찾고자 하는 값이 없습니다.")
# else :
#     print('요청하신 문자는 %d 번째에 있습니다.' % result)

# 대소문자 변경 : upper() / lower()
a='heLLo'
print(a.upper())
print(a.lower())

# 문자열 양쪽 공백을 없애는 함수 : strip()
a='        hello world   '
print(a.strip())

# 문자열 대체 : replace()
# 특정 문자열을 특정 문자로 대체
a='I studied python'
b=a.replace('python','java')
print(b)

# 문자열 나누기 : split()
# 공백을 기준으로 자르는 함수
# 원하는 문자열을 기준으로 자를수 있음 
a='I studied python'
b=a.split()
print(b)

a= 'I      studied     python'
b=a.split(" ")
print(b)

a='I:studied:python'
b=a.split(':')
print(b)


# 2차방정식 

x=float(input('실수 x를 입력하시오 : '))
y=2.5*x**2+3.3*x+6
print(y)
# pow 써라
y=2.5*pow(x,2)+3.3*x+6
print(y)

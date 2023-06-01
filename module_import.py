# improt 하고싶은 모듈이 있으면 import 구문 사용
# from module_test import module_statements as ms
# from 패키지명 import 파일명 또는 import 패키지명.파일명
# as를 사용해서 약어로도 가능
# from module_test import module_statements as ms
# print(ms.plus(10,20))
import class_statements as cs
c1=cs.CalculatorChild()
c1.plus(10)
print(f'module_import 의 result : {c1.result}')



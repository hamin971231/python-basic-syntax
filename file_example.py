


# 파일 시스템 입출력 라이브러리 : open
# open 함수는 mode(w: write(덮어쓰기) ,r: read ,a: 추가') 갖고있음
# open을 했을 때 해당파일명이 없으면 자동생성



# f= open('test.txt','w')
# ,encoding='UTF-8'

# f = open('test.txt','w',encoding='UTF-8')
# for i in range(0,10) :
#     data = '%d 번쨰 줄입니다. \n' %i
#     f.write(data)
# f.close()

# f = open('test.txt','r',encoding='UTF-8')
# # 첫번째 줄만 가져오는 함수
# # while문 if문으로 readline()으로 전체출력
# 라인별로 출력을 하면 데이터를 뽑아내기 편하기 떄문 : 파싱을 원할하게 하기 위해
# while True :
#     line=f.readline()
#     print(line)
#     if not line :
#         break
# # print(line)
# f.close()

# f = open('test.txt','r',encoding='UTF-8')
# # readlines : 데이터를 리스트형태로 라인별로 담아준다.
# lines=f.readlines()
# print(lines)
# f.close()

# f = open('test.txt','r',encoding='UTF-8')
# # read : 데이터를 한꺼번에 문자열로 담아준다.
# lines=f.read()
# print(lines)
# f.close()

# a옵션으로 추가모드
# 0~9번쨰에서 -> 10~19번쨰 줄입니다.
# f = open('test.txt','a',encoding='UTF-8')
# for i in range(10,20) :
#     data='%d 번째 줄입니다 \n'%i
#     f.write(data)
# f.close()

# 파이선에서 객체를 생성하고 나면, 힙메모리에 객체 할당된다.
# 객체의 사용이 끝나면 객체를 close 해줘여하나  ?
# 그럴 필요 없음 : 파이선에는 GC(Garbage Collector)가 내장되어 자동으로 사용빈도가 낮은 데이터는 메모리에서 삭제를 해준다.
# 그러나 파일 시스템은 그렇지 못하기 때문에 직접 닫아줘야 메모리 낭비가 없다. 

import os
# os 라이브러리를 활용한 디렉토리 내에 파일 검색
# .py로 끝나는 파이선 확장파일을 검색
# 현재 폴더에서만 검색
# searchDir=r'C:\Users\hamin\조해민'
# # 파일 디렉토리 목록을 뽑아내는 listdir 함수사용
# dirList = os.listdir(searchDir)
# print(dirList)

# for dir in dirList :
#     dirTuple=os.path.splitext(dir)
#     if dirTuple[1]=='.py' :
#         fullPath = os.path.join(searchDir,dir)
#         print(fullPath)

# 그 다음 폴더까지 검색 

searchDir=r'C:\Users\hamin\조해민'

dirList = os.listdir(searchDir) # ['python-basic-syntax']

for dir in dirList:
    filename = os.path.join(searchDir, dir) #C:\Users\hamin\조해민\python-basic-syntax
    if os.path.isdir(filename):
        dirList2=os.listdir(filename)
        for dir2 in dirList2: ## dir2은  C:\Users\hamin\조해민\python-basic-syntax 안에 있는 파일들임
            dirTuple2 = os.path.splitext(dir2)
            if(dirTuple2[1]=='.py'):
                fullPath = os.path.join(filename, dir2)
                print(fullPath) # ex)  C:\Users\hamin\조해민\python-basic-syntax\variables.py 
    dirTuple = os.path.splitext(dir) #('python-basic-syntax', '')
    if(dirTuple[1]=='.py'):
        fullPath = os.path.join(searchDir, dir)
        print(fullPath)



# 모든 폴더까지 검색
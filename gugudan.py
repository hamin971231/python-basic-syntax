left=13
right=17
## 약수의 개수가 짝수인것은 더하고, 
## 약수의 개수가 올수인것은 뺸 수를 return

## 약수의 갯수
list_num=[]
# for i in range(left,right+1) :
#     count=0
#     for j in range(1,right+1) :
#         if i%j == 0:
#             count+=1
#             if count%2==0 :
#                 list_num.append(i)
#                 print(count)
#             else :
#                 i=-i
#                 list_num.append(i)
#                 print(count)

# n=2
# m=5
# list_return=[]

# ## 1 3     1,2,3,4,6,12

# div_n = []
# div_m = []
# for i in range(1,n+1) :
#     if n%i == 0 :
#         div_n.append(i)
# print(div_n)
# for j in range(1,m+1) :
#     if m%j == 0 :
#         div_m.append(j)
# print(div_m)

# div_ans=0
# num_div=0
# for i in div_m :
#     if i in div_n :
#         num_div=max(div_n)
# list_return.append(num_div)
# print(list_return)


## 1 2    1,2,5,10
# list_mult=[]
# for i in div_n :
#     list_mult.append(i*m)
# mult=min(list_mult)
# list_return.append(mult)
# print(list_return)

# arr=[5,9,7,10]
# divisor=5
# answer=[]
# for i in arr :
#     if i % divisor == 0:
#         answer.append(i)
# answer.sort()
# if len(answer) == 0 :
#     answer=[-1]

# print(answer)

# left=24
# right=27
# answer=[]
# for i in range(left,right+1):
#     count=0
#     for j in range(1,i+1):
#         if i % j == 0:
#             count+=1
#     if count%2==0 :
#         answer.append(i)
#     else :
#         answer.append(-i)
# print(answer)




# 약수부터 구하기
n=2
m=5
list_n=[]
list_m=[]
answer=[]
for i in range(1,n+1) :
    if n%i==0:
        list_n.append(i)
# print(list_n)
for j in range(1,m+1): 
    if m%j==0:
        list_m.append(j)
# print(list_m)

#최대공약수
max_div=0
for a in list_n :
    if a in list_m :
        if a > max_div :
            max_div=a
answer.append(max_div)
# print(max_div)

# 1  3
# 1 2 3 4 6 12 
# 최소공배수 
multi=[]
min_list=[]
for x in list_m :
    for y in list_n :
        multi.append(x*y)
for z in multi :
    if (z%m == 0) & (z%n == 0) :
        min_list.append(z)
min_multi=min(min_list)
# print(min_multi)
# answer.append(min_multi)
# print(answer)
#Hackerrank Finding Percentage

n=int(input())
# y=4*n
A=[]
B=[]
C=[]
# r=""
# v=input()
for i in range(n):
    t=input().split()
    A.append(t)
    # print(t)
v=input()
for j in A:
    # r=""
    for x in j:
        # print(x)
        B.append(x)
for i in range(len(B)):
    if B[i]==v:
        C.append(B[i+1])
        C.append(B[i+2])
        C.append(B[i+3])
list1=list(map(float,C))
# print(type(list1[0]))
n=sum(list1)
m=n/3
# print(round(m,2))
print(format(m, '.2f'))

# print(C)
        

# print(B)

#         r+=x
# print(list[r])

# for i in range(len(A)):
#     if A[i]==x:
#         A[i+1]=int(A[i+1])
# print(A[1])

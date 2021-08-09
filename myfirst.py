# Hackerrank # Runner up score
# n=int(input())
A=[]
# for i in range(n):
x=int(input())
# if 
#     input()
b=list(map(int, input().split()))
# print(b)
y= int(len(b))
for i in b:
    if i not in A:
        A.append(i)
# print(A)        
if y==x:
    # print(b)
    A.sort()
    c=int(len(A))
    print(A[c-2])
#     A.append(b)
#     # b=input().split()
#     # A.append(b)
# print(A)
# x=len(A)
# # print(A)
# # A.sort()
# # print(A)
# # print(A[n-1])
# print(A[x-2])
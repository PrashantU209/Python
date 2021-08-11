#Hackerrank Mutations
n=input()
p=input().split()
A=[]
for i in n:
    A.append(i)
# print(A)
# print(p)
# print(int(p[1]))
c=int(p[1])
# print(c)
# print(type(c))
for j in range(0,len(A)):
    if j==c:
        A[j]=p[0]
# print(A)
t=""
y=t.join(A)
print(y)
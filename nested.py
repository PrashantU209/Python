#Hackerrank#Nested Lists

n=int(input())
A=[]
m=[]
nondupm=[]
char1=[]
for i in range (n):
    new=input()
    marks=float(input())
    A.append([new,marks])
# print(A)
for val in A:
    m.append(val[1])
# print(m)
m.sort()
# print(m)
for i in m:
    if i not in nondupm:
        nondupm.append(i)
# print(nondupm)
x=int(nondupm[1])
# print(x)
for i in A:
    if i[1]==x:
        char1.append(i[0])
# print(char1)
char1.sort()
# print(char1)
for val in char1:
    print(val, end='\n')
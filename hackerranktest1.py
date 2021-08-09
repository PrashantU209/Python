#Hackerrank Test1

# Write your code here


s=input()
Alphabets=[]
Numbers=[]
# x=len(n)
# for i in range(x):
x=list(s)
# x.sort
# print(x)
for val in x:
    try:
        int(val)
        continue
    except ValueError:
        Alphabets.append(val)
# print(Alphabets)
for i in x:
    if i not in Alphabets:
        Numbers.append(i)
# print(Numbers)
y=sorted(Alphabets)            
# print(y)
for i in range(0,len(Numbers)):
    Numbers[i]=int(Numbers[i])
Numbers.sort()
print(Numbers)

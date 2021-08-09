#Hackerrank Capitalize

s=input()
x=list(s)
x[0]=x[0].upper()
y=""
# print(x)
for i in range(len(x)):
    if x[i]==" ":
        x[i+1]=x[i+1].upper()
        # print(x[i+1])
    # print(x[i])
# print(x)
t=y.join(x)
print(t)


# y=""
# for i in range(0,len(x)):
#     x[0]==x[0].capitalize()
    # elif i==" ":
    #     x[i+1]==x[i+1].upper()
# print(x)
# for j in x:
#     y=y+j
# print(y)
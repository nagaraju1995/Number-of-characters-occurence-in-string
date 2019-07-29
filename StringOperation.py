a= input("Enter the String which you want to perform operation")
b=list(a)
c=len(a)
i=0
j=1
e=""
d= input("Enter the character for which you need to search")
for i in range(c):
    if b[i] == d:
         s = str(j)
         b[i] = s
         j+=1
    e+=b[i]
    i+=1

print(e)


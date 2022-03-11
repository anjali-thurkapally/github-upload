n=int(input())//2
l=list(map(int,input().split()))

l1=[]

for i in range(0,len(l),2):
    l1.append([l[i],l[i+1]])

x=[]
y=[]
s=[]

for i in range(0,len(l1)-1):
    a=abs(l1[i][0]-l1[i+1][0])
    x.append(a)

for i in range(0,len(l1)-1):
    a=abs(l1[i][1]-l1[i+1][1])
    y.append(a)

for i in range(0,len(x)):
    a=y[i]/x[i]
    s.append(a)

s1=set(s)

if len(s1)==1:
    p=l1[0]
    q=l1[1]
    a=q[0]-p[0]
    b=q[1]-p[1]
    c=(-b*p[0])+(a*p[1])
    print(str(b)+'x'+'-'+str(a)+'y'+'+'+str(c)+"=0")

else:
    print("No Line")



    
#print(n)
#print(l1)
#print(x)
#print(y)
#print(s)
#print(s1)

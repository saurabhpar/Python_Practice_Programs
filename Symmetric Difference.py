# Enter your code here. Read input from STDIN. Print output to STDOUT
M=int(input())
x=input()
a=x.split(" ")
alist=[]
for k in a:
    alist.append(int(k))
a=set(alist)

N=int(input())
y=input()
b=y.split(" ")
blist=[]
for j in b:
    blist.append(int(j))
b=set(blist)
G=list(a.symmetric_difference(b))
F=sorted(G)
for i in F:
    print(i)
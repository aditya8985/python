#author: aditya
#sort tuple by total digits
lis = [(1,2), (1,2,3,4), (1,2,3,4,5), (1,2,3)]
x=[]
for i in lis:
    x.append(len(i))
sorts=sorted(x,reverse=False)
ans=[0]*len(lis)
#print(x)
#print(sorts)
for j in range(len(lis)):
    ans[j]=lis[x.index(sorts[j])]
print(ans)

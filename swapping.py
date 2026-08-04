'''s1="hello"
s2="worldd"
s1,s2=s2,s1
print(s1,s2)'''

'''n=10
m=200
n,m=m,n
print(n)
print(m)'''

'''n=[1,2,3,4,5]
l=len(n)
n[0],n[l-1]=n[l-1],n[0]
print(n)'''

'''s="hello"
k=list(s)
k[1],k[3]=k[3],k[1]
n="".join(k)
print(n)'''

'''n=[1,2,3,4,5,6,7,8,9,10]
for i in  range(0,len(n)-1,2):
    n[i],n[i+1]=n[i+1],n[i]

print(n)'''

'''n = [1, 2, 3, 4, 5, 6]
for i in  range(0,len(n)-1,2):
    n[i],n[i+1]=n[i+1],n[i]
n.reverse()
print(n)'''

'''l=[1,2,3,4,5]
m=["a","b","c","d","e"]
if len(l)%2!=0:
    k=len(l)//2
    l[k],m[k]=m[k],l[k]

print(l,m)
'''

'''n=[1,2,3,4,5]
k=len(n)
for i in range(k//2):
    n[i],n[k-i-1]=n[k-i-1],n[i]

print(n)
    '''




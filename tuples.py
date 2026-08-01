#first and last occurence of a specific element
'''t=(1,2,3,4,5,6,2,3)
c=2
for i in t:
    if c==i:
        print(t.index(i))
        break
for i in range(len(t)-1,-1,-1):
    if c==t[i]:
        print("last index",i)
        break
    '''

#concatenate two tuples
t'''1=(2,3,4)
t2=(5,6,7)
t3=t1+t2
print(t3)
print(type(t3))'''

'''t=(1,2,3,2,2,2,3,7)
print(t.count(2))
    '''

#found
'''t=(1,2,3,2,2,2,3,7)
n=2
for i in t:
    if n==i:
        print("found")
        break'''
#revrse of tuple
'''t=(1,2,3,4,5)
rev=()
for i in range(len(t)-1,-1,-1):
    rev=rev+(t[i],)

print(rev)
'''
#max and min in tuple
'''t=(3,4,3,6,8,0,99,3)
l=t[0]
s=t[0]
for i in t:
    if i>l:
        l=i
    if i<s:
        s=i

print(l)
print(s)'''


'''t = (5, 5, 2, 5)

for i in t:
    if i != t[0]:
        print("Not all elements are same")
        break
else:
    print("All elements are same")'''


#sum of elements
'''t=(3,4,2,1,4,6)
print(sorted(t))
sm=0
for i in t:
    sm+=i
print(sm)'''

'''#multiply tuple
t=(1,2,3)
print(t*3)'''

#unique elements
'''t=(1,4,3,5,6)
for i in range(len(t)):
    for j in range(i+1,len(t)):
        if t[i]==t[j]:
            print("elements are not unique")
            break
    else:
        continue
    break
else:
    print("elemts are unique ")
'''

'''#string to tuple
s="udaysimhadri"
l=tuple(s)
print(l)'''


#create a new tuple using old tuple
'''
t=(1,2,3,4,5,6,7,8)
k=()
for i in t:
    if i%2==0:
        k=k+(i,)
print(k)'''

'''t1=(1,2,3,4,5)
t2=(2,3,4,6)
for i in t2:
    if i not in t1:
        print("t2 is not subset t1")'''

'''t1=(1,2,3,4,5)
t2=(2,3,4,2,3,5,7,98,74)
for i in t1:
    for j in t2:
        if i==j:
            print(j)

        
'''
'''
#unpack tuple
t=(1,2,3,4,5)
a,b,c,d,e=t
print(a,b,c,d,e)'''

'''g=("uday","sim","king")
l=" ".join(g)
print(l)

'''

'''
t=()
if t==():
    print("no")'''


#new tuple
'''t=(1,2,3,4,5)
k=t[: :-1]
print(k)'''

'''t=(1,2,"uh",4)
for i in t:
    if not isinstance(i,(int,float)):
        print("tuple contains not numeric valuse")
        break
else:
    print("only numeric values")
'''


#palindrome
'''t=(1,2,3,4,5,4,3,2,1)
let=0
ret=len(t)-1
while let<ret:
    if t[let]!=t[ret]:
        print("tuple is not palindrome")
        break
    let+=1
    ret-=1
else:
    print("palindrome")'''


#max sum of tuples
'''t=[(1,3),(4,7),(2,3)]
s=0
max=0
res=0
for i in t:
    s=sum(i)
    if s>max:
        max=s
        res=i
print(res)'''


#rotate the tuple by using k steps
'''t=(2,3,4,8,9)
k=2
k=k%len(t)
l=t[-k:]+t[:-k]
print(l)'''

#kth samll and large
'''t=(3,4,2,89,5,7,8)
k=4
l=sorted(t)
print("kth small",l[k-1])
print("kth small",l[len(l)-k])'''



#brute force of finding sub arrays
'''t = (3, -4, 2, -3, -1, 7, -5)
min=t[0]

for i in range(len(t)):
    s=0
    for j in range(i,len(t)):
        s+=t[j]
        if s<min:
            min=s
print(min)'''





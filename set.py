#creata a empty set
'''a=set()
a.add(2)
a.add(7)
a.add(8)
print(a)
a.remove(7)
print(a)'''

'''a={1,2,5,4,7,100,3}
k=100
if k in a:
    print("TRUE")
else:
    print("false")'''
'''
a={1,2,3,4,5}
b={6,8,94}
print(b.issubset(a))
print(b.isdisjoint(a))

'''

'''a={1,3,443,4,5}
print(max(a))
print(min(a))
k=[3,4,6,8432,12,1,2,1,1]
print(set(k))
'''

'''a={1,3,443,4,5}
k=90
if k in a:
    a.remove(k)
else:
    print("do nothing")'''

'''a={1,2,4,7,8996,2}
if a==set():
    print("emptty")
else:
    print("ehfuh")'''

'''print("uday")'''
'''s={1,2,3,4}
e={5,6,2,3}
print(s)
print(sum(s))
print(sum(s)//len(s))
print(s.union(e))
print(s.intersection(e))
print(s.difference(e))
'''

#longest consecutive sequence of elements
'''s = {100, 4, 200, 1, 3, 2}
l=list(s)
l.sort()
c=1
m=1
for i in range(1,len(l)):
    if l[i]==l[i-1]+1:
        c+=1
    else:
        c=1
    if c>m:
        m=c

print(m)'''


#
    

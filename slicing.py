'''m="Vcude"
print(m[:3])

n=[1,2,3,4]
print(n[::-1])

c=(1,2,3,4,5,6)
print(c[1:3])'''

'''a=[100,200,300,400]
a[2]=80000
print(a)'''

'''n="Vcube Solutions"
print(n[::2])'''

'''l=[[1,2,3],4,5,6]
m=[l[0][2],l[1]]
print(m)

str="Vcube"
print(str[::-1])'''

'''s="python"
print(s[::3])'''

'''l = ["vcube", "python", "java"]
res=[word[::-1] for word in l]
print(res[::-1])'''

'''n="Vcube Solution"
print(n[::3])'''

'''n="udayadu"
if n[::]==n[::-1]:
    print("palindrome")'''

'''l=[1,2,3]
m=[2,5,7]
res=l[::]+m[::]
print(res)'''

'''l1=[1,2,3,1,4,5,2]
m=[]
for i in range(len(l1)):
    if l1[i] not in l1[:i]:
        m.append(l1[i])

print(m)'''

'''m="python"
print(m[::-1])
'''

'''l=[[1,2],[3,5],[89,45]]
res=l[0][:]+l[1][:]+l[2][:]
print(res)'''

'''l=[10,11,12,13,14,15,2]
sm=l[0]
for i in l[::]:
    if i>sm:
        sm=i

print(sm)
    '''

'''s="udaysimhaydri"
ss="ay"
c=0
for i in range(len(s)-len(ss)+1):
    if (s[i:i+len(ss)]==ss):
        c+=1
print(c)'''

'''d1={'a':1,'b':2,'c':3}
d2={'x':10,'y':20,'z':30}
res=dict(list(d1.items())[:]+list(d2.items())[:])
print(res)'''


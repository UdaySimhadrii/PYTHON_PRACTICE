#reverse of list
'''n=[89,34,90,"uday","kiddo","kone"]
k=n[::-1]
print(k)'''

#remove duplicates
'''n=[4,5,3,2,5,4,"kid","kid"]
k=[]
for i in n:
    if i not in k:
        k.append(i)
print(k)'''

'''n=[4,5,3,2,5,4,"kid","kid"]
k=list(dict.fromkeys(n))
print(k)
'''

#max and min
'''n=[4,2,9,1,6,8]
a=n[0]
for i in n:
    if i>a:
        a=i
print("max",a)
for i in n:
    if i<a:
        a=i
print("min",a)'''

'''n=[4,2,9,1,6,8]
print(max(n))
print(min(n))'''

'''n=[4,2,9,1,6,8]
print(sorted(n))'''

'''n=[4,2,9,1,6,8]
n.sort(reverse=True)
print(n)
'''

#list.index(element) and count
'''n=[4,2,9,1,6,8,6,9,43]
a=1
for i in n:
    if a==i:
        print(i,n.index(i))
b=9
c=0
for i in n:
    if b==i:
        c+=1
print(c)'''

#extend is used to merge two lists
#append is add another list is element to first list
'''n=[2,3,57,87]
k=["uday",'toyy']
n.extend(k)
print(n)
n.append(k)
print(n)'''

#sum of all elements
'''n=[1,2,3,4]
k=0
for i in n:
    k+=i
print(k)'''    


#remove element from its value
'''n=[1,2,3,4,5]
k=3
if k in n:
    n.remove(k)
else:
    print("element not found")'''


#slice length add iterate  insert 
'''n=[34,66,8,9,2,3,5,2,1,4,8,9]
k=n[1:4]
print(k)
print(len(k))
n.insert(2,400)
print(n)'''

'''
n=[45,78,43,2344]
l=n.copy()
print(l)'''

'''
revrse of list
k=[5,6,7,8,9]
k.reverse()
print(k)
'''

#find the first occurence of string
'''n=[45,63,67,43,9,53,221,567,43,23,22,124]
l=n.index(43,4)
print(l)
m=n.pop()
print(m)
p=n.index(22,-1)
print(p)'''

#second largest element in the listt
'''m=[34,3,1,7,8,9,56,345,677]
l=m[0]
s=0
for i in m:
    if i>l:
        s=l
        l=i
    elif i>s and i!=l:
        s=i

print(s)'''


#remove elements at even indices
'''k=[1,2,3,4,5,6,7,8,9,10]
for i in range(1,len(k)+1):
    if i%2==0:
        k.remove(i)
print(k)'''

'''l1=[1,2,3,4,5,6,7,8,9]
l2=[4,5,6,7]
for i in l1:
    if i in l2:
        print(i)

#union
union=[]
for i in l1:
    if i not in union:
        union.append(i)
for i in l2:
    if i not in union:
        union.append(i)

print(union)
'''
#palindrome

'''
l1 = [1, 2, 3, 2, 1]

flag = True

for i in range(len(l1) // 2):
    if l1[i] != l1[len(l1) - 1 - i]:
        flag = False
        break

if flag:
    print("Palindrome")
else:
    print("Not Palindrome")'''

#frequency of each element
'''k=[3,4,5,2,3,4,5,3,4,5,3,4,5]
d={}
for i in k:
    if i in d:
        d[i]+=1
    else:
        d[i]=1
print(d)

l={}
for i in k:
    l[i]=k.count(i)

print(l)'''


#stack implementation
'''stack=[]
stack.append(450)
stack.append(43)
stack.append(2)
stack.append(350)
stack.append(90)

print(stack.pop())
print(stack.pop())
print(stack.pop())'''

#queue implementation
'''stack1=[]
stack2=[]
stack1.append(450)
stack1.append(43)
stack1.append(2)
stack1.append(350)

while stack1:
    stack2.append(stack1.pop())

print("remover",stack2.pop())

while stack2:
    stack1.append(stack2.pop())

print(stack1)'''


#except one list
'''l1=[1,2,3,5]
n=5
ex=n*(n+1)//2
actual=sum(l1)
print(ex-actual)
'''


'''import random
k=[5,3,8,2,1,3334,22,2]
random.shuffle(k)
print(k)'''


#generate all subsets
'''from  itertools import combinations
l1=[23,45,67,23,2,4,6,7]
for i in range(len(l1)+1):
    for j in combinations(l1,i):
        print(list(j))'''

#sum of all equal parts
'''l1=[1,1,3,4]
left=0
total=sum(l1)
for i in l1:
    left+=i
    if left==total-left:
        print("cand be divided:")
        break
else:
    print("cant be divided")'''

#count all n/2 elements
'''n=[2,3,45,77,33,2,2,23,34,1,2,2,2,2,2,2,2,2,2,2,2,2]
for i in n:
    if n.count(i)>len(n)//2:
        print("greater tahnnn")
        break
else:
    print("noo")'''

#longest consecutive number
'''l = [100, 4, 200, 1, 3, 2]

l.sort()

count = 1
max_count = 1

for i in range(len(l) - 1):
    if l[i] + 1 == l[i + 1]:
        count += 1
    else:
        count = 1

    if count > max_count:
        max_count = count

print("Length:", max_count)'''









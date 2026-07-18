#print 10 numbers using for loop
'''for i in range(10):
    print(i)'''

#sum of first 10 numbers using for loop
'''sum = 0 
for i in range(10):
    sum += i
print("Sum of first 10 numbers is:", sum)'''

#print even numbers between 1 to 20 using for loop
'''for i in range(1, 21):
    if i % 2 == 0:
        print(i)''' 
#print odd numbers between 1 to 20 using for loop
'''for i in range(1, 21):               
    if i % 2 != 0:
        print(i)''' 

#calculate factorial of a number using for loop
'''num = int(input("Enter a number: "))
factorial = 1           
for i in range(1, num + 1):
    factorial *= i
print("Factorial of", num, "is:", factorial)'''

#print pattern using nexted for loops
'''n=4
for i in range(0,4):
    for j in range(0,4):
        if i==0 or i==3:
            print("*",end="")
        else:
            if j==0 or j==3:
                print("*",end="")
            else:
                print(" ",end="")

    print("")'''

#sum of all even numbers in 1-100
'''sum=0
for i in range(2,101):
    if i%2==0:
        sum=sum+i

print(sum)'''


#fibinoccis series
'''a=0
b=1
for i in range(11):
   print(a)
   c=a+b
   a=b
   b=c'''

#common elements in two lists
'''a=[23,6,4,3,89,54,22]
b=[5,4,3,90]
for i in b:
    for j in a:
        if i==j:
            print(j)'''

#factorial of a number
'''n=10
fact=1
for i in range(1,n+1):
    fact=fact*i

print(fact)'''


#reverse of string
'''name="udaysimahdri"

rev=""
for i in range(len(name)-1,-1,-1):
    rev=rev+name[i]
    
print(rev)'''

#list of squares
'''n=10
l=[]
for i in range(1,11):
    l.append(i**2)

print(l)'''

#numbers of words in sentence
'''m="I AM good person  and bad one"
count=0
for ch in m:
    if ch==" ":
        count+=1

print(count)'''

#sum of digits in number
'''n=input("enter a number=")
s=0
for digit in n:
    s+=int(digit)

print(s)'''

# generate a list of prime numbers
'''n=20
l=[]
for i in range(2,n+1):
    for k in range(2,i):
        if i%k==0:
            break
    else:
        l.append(i)

print(l)'''

#power of a number
'''b=2
k=1
p=3
for i in range(p):
    k=k*b

print(k)'''

#reverse of a list
'''l=[45,"ikihi",90,56,43,222]
k=[]
for i in range(len(l)-1,-1,-1):
    print(l[i])'''

#largest element number in list
'''m=[56,78,34,5678,44,67,99]
a=m[0]
for i in m:
    if i>a:
        a=i
print(a)'''

#average of number
'''m=[56,78,34,5678,44,67,99]
sum=0
for i in m:
    sum+=i

k=sum//len(m)
print(k)'''

#countdown
'''n=5
for i in range(n,0,-1):
    print(i)'''

#product of list
'''n=[1,2,3,4,5,6,7,8,9,10]
k=5
for i in n:
    if k==i:
        print("element found")
        print(n.index(i))'''

#* of a triangle
''''n=5
for i in range(5):
    print(i*"*")'''

#lcm of two numbers
'''a=4
b=6
for i in range(max(a,b),a*b+1):
    if i%a==0 and i%b==0:
        print(i)
        break'''

#prime numbers for 1 to given number
'''n=10
count=0
for i in range(2,n+1):
    for j in range(2,i):
        if i%j==0:
            break
    else:
        count+=1

print(count)'''


#reverse of words in sentece
'''m="I LOve pythonnn"
words=m.split()
rev=[]
for i in range(len(words)-1,-1,-1):
    rev.append(words[i])

print(" ".join(rev))'''

#factorial of given number
'''n=10
fact=1
for i in range(n,0,-1):
    fact*=i

print(fact)'''

#diamond pattern
'''n=5
for i in range(1,n+1):
    print(" "*(n-i),end=" ")
    print("*"*(2*i-1))
for i in range(n-1,0,-1):
    print(" "*(n-i),end=" ")
    print("*"*(2*i-1))'''



















    


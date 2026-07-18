#first prime number after 100
'''for i in range(101,200):
    if i>=100:
        for j in range(2,i):
            if i%j==0:
                break

        else:
            print("the first prime number after 100",i)
            break'''

#sum is divible by 3 and 5
'''sum=0
for i in range(1,101):
    if i%3==0 and i%5==0:
        continue
    sum+=i

print(sum)'''

#find and print all factors of a given number
'''n=int(input("enter a  number="))
for i in range(1,n+1):
    if n%i==0:
        print(i)'''

#sum of all list of numbers
'''nm=[1,2,3,4,-1,-2,-5,6]
sum=0
for i in nm:
    if i<0:
        continue
    sum+=i
print(sum)'''

#basic login system
'''user="uday"
password="Uday1408"
count=3
while True:
    k=input("enter the username:")
    m=input("enter the password=")
    if password==m:
        print("password is correct")
        break
    else:
        count-=1
    if count==0:
        break'''

#first 10 even numbers
'''n=10
cn=0
for i in range(2,100):
    if i%2==0:
        if i%3==0:
            continue
        print(i)
        cn+=1
    if cn==n:
        break
'''

#fibinocci seris
'''a=0
b=1
for i in range(20):
    if a<100:
        print(a)
    else:
        break
    c=a+b
    a=b
    b=c'''

#list of summ digit
'''n=[]
while True:
    i=int(input("enter the number="))
    if i<0:
        break
    else:
        n.append(i)
sum=0
for i in n:
    sum+=i

print(sum//len(n))'''


#count the voewls
'''name="udayioe"
count=0
for ch in name:
    if ch.lower() not in "aeiou":
        continue
    count+=1
print(count)'''



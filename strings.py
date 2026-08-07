#reverse of a string
'''str="udaysimhadri"
rev=""
for ch in str:
    rev=ch+rev
print(rev)

print(str[::-1])'''

#count vowels in string
'''str="akilmonu"
c=0
for i in str:
    if i in "aeiou":
        c=c+1

print(c)'''

'''str="i am udasy simhadri you are welcome to the house of mine"
w=str.split()
for i in range(len(w)):
    w[i]=chr(ord(w[i][0])-32)+w[i][1:]

m=" ".join(w)

print(m)
'''
'''str="i am udasy simhadri you are welcome to the house of mine"
print(str.title())'''


#palindrome of given string checks
'''str="udayyadu"
for i in range(len(str)//2):
    if str[i]!=str[len(str)-i-1]:
        print("not palindrome")
        break
else:
    print("palindrome")'''

'''str="kinghgfnik"
flag=True
for i in range(len(str)//2):
    if str[i]!=str[len(str)-i-1]:
        flag=False

if flag:
    print("palindrom")
else:
    print("nottt")'''


'''str="udaysimhadri"
c=0
for i in str:
    c=c+1
print(c)'''


#upper case to lower and vice verse
'''str="uDaYsImHaDrI"
res=""
for ch in str:
    if 'a'<=ch<='z':
        res+=chr(ord(ch)-32)
    else:
        res+=chr(ord(ch)+32)

print(res)
print(str.swapcase())'''

#concatenate
'''a="uday"
b="simhadri"
c=a+" "+b
print(c)'''


#count the occurences of substring
'''s="udayudghudknirnud"
n="ud"
print(s.count(n))'''

'''s="udayudghudknirnud"
n="ud"
c=0
for i in range(len(s)-len(n)+1):
    if s[i:i+len(n):]==n:
        c+=1

print(c)'''

#check if character is given in string or not
'''str="udaysimhadri"
flag=False
for i in range(len(str)):
    if str[i]=="h":
        flag=True     

if flag:
    print("found")
else:
    print("not found")'''

#first and last character
'''str="udaysimhadri"
print(str[0])
print(str[len(str)-1])'''

'''str="udaysimhadri"
c=0
k=0
for ch in str:
    if ch not in "aeiou":
        c+=1
    else:
        k+=1

print(c,k)'''

#old and new string
'''a="banana"
o='n'
n='l'
res=" "
for ch in a:
    if ch==o:
        res=res+n
    else:
        res=res+ch
print(res)'''

'''k="program"
c=0
for i in range(len(k)):
    for j in range(i+1,len(k)):
        if k[i]==k[j]:
            c=c+1

if c==0:
    print("not repeat")
else:
    print("repeat")
'''

'''lm="nurses run"
temp=""
for i in lm:
    if i!=" ":
        temp+=i
print(temp)
flag=True
for i in range(len(temp)//2):
    if temp[i]!=temp[len(temp)-1-i]:
        flag=False
        break

if flag:
    print("palindrome")
else:
    print("not palindrome")'''

'''s = "PYTHON"

for i in range(len(s)):
    for j in range(len(s)-i-1):
        print(" ", end="")
    for k in range(i+1):
        print(s[k], end="")
    print()'''


#encoding the stringg
'''n="xyzabc"
res=""
for i in n:
    if i=='z':
        res+='a'
    elif i=='Z':
        res+='A'
    else:
        res+=chr(ord(i)+1)

print(res)
'''


'''#vhecking the anagrammm
s1="lismten"
s2="silent"
if len(s1)!=len(s2):
    print("NOT ANAGRAMM")
else:
    flag=True
    c1=0
    c2=0
    for ch in s1:
        for i in s1:
            if i==ch:
                c1+=1
            
        for j in s2:
            if j==ch:
                c2+=1

        if c1!=c2:
            flag=False
            break

    if flag:
        print("ANAGRAM")
    else:
        print("NOT ANAGRAM")
'''

        
        


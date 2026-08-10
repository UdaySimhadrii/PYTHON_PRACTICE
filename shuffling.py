import random


#shuffle rnadomly arrange elements return to same variable
'''a= [1, 2, 3, 4, 5, 6, 7, 8, 9, 10] 
random.shuffle(a)
print(a)'''

#sample will return a new variable
'''k=random.sample(a,len(a))
print(k)'''

#given a sentence shuffle its words
'''s = "This is a sample sentence to shuffle." 
k=s.split()
random.shuffle(k)
ne=" ".join(k)
print(ne)'''

#suffle eve and odd numbers in list
A = [1,2,3,4,5,6,7,8,9,10]
'''l=[i for i  in A if i%2==0]
m=[i for i in A if i%2!=0]
random.shuffle(l)
random.shuffle(m)
n=[]
for i in range(len(m)):
    n.append(l[i])
    n.append(m[i])

print(n)'''

'''names = ["Uday", "Ram", "Kiran", "Ravi", "Sai", "Ajay"]
random.shuffle(names)
print(names)
k=[(names[i],names[i+1]) for i in range(0,len(names),2)]
print(k)'''





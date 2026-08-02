'''d={k:k**2 for k in range(1,21)}
print(d)'''


'''n=["uday","padhu","king"]
a=[23,20,18]
d={n[i]:a[i] for i in range(len(n))}
print(d)'''

'''n=["udaysimha","padhu","kingkong"]
m={n[i]:len(n[i]) for i in range(len(n)) if len(n[i])>5}
print(m)'''

'''t1=("uday","lily","kinggkongg")
t2=(3,4,5)
k={t1[i]:t2[i] for i in range(len(t1))}
print(k)'''

'''words = ["apple", "banana", "cat", "dog", "elephant", "flower", "grape", "house", "ice", "jungle"]
k={ch:len(ch) for ch in words if ch[0] in "aeiou"}
print(k)'''

'''sn = [
    "Python is a powerful programming language.",
    "I enjoy solving coding problems every day.",
    "The sun rises in the east.",
    "Artificial intelligence is transforming technology."]

m={i:len(sn[i].split()) for i in range(len(sn))}
print(m)'''

'''k={i:i**2 for i in range(1,11) if i%3==0}
print(k)'''


'''words = ["apple", "banana", "cat", "dog", "elephant", "flower", "grape", "house", "ice", "jungle"]
m={i:len(i) for i in words if len(i)%2==0}
print(m)'''

'''n=[1,2,3,4,6,8]
m=["uday","p","kij","koff","lol","lodee"]
k={n[i]:m[i] for i in range(len(m))}
print(k)'''

'''emails = [
    "uday@gmail.com",
    "rahul@yahoo.com",
    "priya@outlook.com",
    "kiran@icloud.com"
]

d={i.split("@")[0]:i.split("@")[1] for i in emails }
print(d)'''



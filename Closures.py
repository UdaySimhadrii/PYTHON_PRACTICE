#nested function
'''def x():
    def y():
        print("hello")
    y()
x()
'''
#return nested function
'''def x(n):
    def y():
        print(n)
    return y()
x(5)'''

#modifiying non local
'''def x():
    n=60
    def y():
        nonlocal n
        n+=10
        print(n)
    return y()
x()'''


#closure with mutable state
'''def nm():
    n=[]
    def mn(a):
        n.append(a)
        print(n)
    return mn
k=nm()
k(70)'''


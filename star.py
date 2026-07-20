'''for i in range(10):
    print("*"*i)

for i in range(10,0,-1):
    print("*"*i)
n=5
for i in range(n+1):
    print(" "*(n-i),end=" ")
    print("*"*(i-1))

n=5
for i in range(n+1):
    print("*"*(i),end=" ")
    print(" "*(i-1))'''


'''n=5
for i in range(n,0,-1):
    print(" "*(n-i),end=" ")
    print("*"*(2*i-1))'''


'''n=6
for i in range(n+1):
    print(" "*(n-i),end=" ")
    print("*"*(2*i-1))
n=6
for i in range(n,0,-1):
    print(" "*(n-i),end=" ")
    print("*"*(2*i-1))

n=6
for i in range(n+1):
    print("*"*(i-1))
'''

#hollow pyramid
'''n=5
for i in range(n+1):
    for j in range(1,i+1):
        if i==j or j==1 or i==n:
            print("*",end=" " )
        else:
            print(" ", end=" ")
    print(" ")'''


#hollow diamond
'''n=5
for i in range(1,n+1):
    print("  "*(n-i),end=" ")
    k=2*i-1
    for j in range(1,k+1):
        if j==1 or j==k:
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()
for i in range(n-1,0,-1):
    print("  "*(n-i),end=" ")
    k=2*i-1
    for j in range(1,k+1):
        if j==1 or j==k:
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print(" ")'''


#hollow square
'''n=5
for i in range(n+1):
    for j in range(n+1):
        if i==0 or i==n or j==0 or j==n:
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()'''

#hourglass
'''
n=5
for i in range(n,0,-1):
    print(" "*(n-i),end=" ")
    print("*"*(i))
for i in range(2,n+1):
    print(" "*(n-i),end=" ")
    print("*"*(i))
'''

#checkered diagram
n = 6

for i in range(n):
    if i % 2 == 0:
        print("* " * n)
    else:
        print(" *" * n)

    
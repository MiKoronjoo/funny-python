import os
print(os.sys.getrecursionlimit())
os.sys.setrecursionlimit( 1000000000)
print(os.sys.getrecursionlimit())

input()
class A:
    counter =0 
    def __init__(self, data):
        self.data = data
    def __eq__(self, other):
        print(A.counter)
        A.counter += 1
        return self.data == other.data
a=A(1)
b=A(1)
a.data=b
b.data=a

a==b

a = 1
def f():
    global a
    print(a)
    if False:
        a = 2
f()
print(a)

def external():
    x = 10
    def internal():
        nonlocal x
        x += 1
        print(x)
    internal()
 
external()
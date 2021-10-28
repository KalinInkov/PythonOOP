x=5
y=-1
ll = []

def f1():
    print(f"from f1: {x}")
def f2():
    global x
    x = 6
    ll.append(2)

    print(f"from f2: {x}")
    print(ll)

def f3():

    x=7
    def f31():
        print(f"from f31: {x}")
        print(f"from f31: y  {y}")
    def f32():
        nonlocal x
        x = 8
        print(f"from f32: {x}")

    print(f"from f3: {x}")
    f31()
    f32()



f1()
f2()
print(f'from Global: {x}')
f3()
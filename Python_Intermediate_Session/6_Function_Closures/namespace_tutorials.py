x = 100


def f():
    x = 30

    def g():
        nonlocal x
        x = 40
        print(locals())
        print(globals())
        print()

    g()
    print(x)
    print()


f()
print(x)
print()
print(globals())

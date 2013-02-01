##globaName = 'xyz'
##def foo():
##    global globaName
##    globaName = 'def'
##    localName = 'abc'
##    print localName + globaName

def foo1():
    m = 3
    def bar():
        n = 4
        print m + n
    print m
    bar()

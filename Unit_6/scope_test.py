#   Scope of Variable
#   Scope global, local

# g = 10  # global variable


# def testFun(n):

#     # if we want to use like global variable we have to use global
#     global g
#     g = 30  # local variable
#     v = g ** n
#     return v


# print(testFun(5))
# print(f"this is global g: {g}.")
# -----------------------------------------------------------------------------

# Non Local
def outerFun():
    d = 'green'

    def innerFun():
        d = 'Python'
        print(f'this is from innerfun: {d}')
    innerFun()
    print(f"this is from outerFun: {d}")


outerFun()

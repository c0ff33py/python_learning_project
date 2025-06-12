# function annotation

def myFun(a: "annotation of a", b: "annotation of b") -> "return of function":
    return a * b


print(myFun(2, 6))
print(myFun.__annotations__)


def greet(name: str) -> str:
    return f"Hello, {name}!"


def add_number(a: int, b: int) -> int:
    return a+b


print(greet("John"))
print(add_number(3, 8))

print(greet.__annotations__)

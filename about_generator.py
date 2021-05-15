import inspect
def is_generator():
    yield 1
    yield 2
    yield 3

def is_not_generator():
    return 1

# isgeneratorfunction()は、ジェネレータかどうかを調べる関数
print(inspect.isgeneratorfunction(is_generator))
print(inspect.isgeneratorfunction(is_not_generator))

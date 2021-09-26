# def some_function(a, b, c, *args, **kwargs):
#     print(kwargs.get('abcde'))
#     print(type(args))
#     print(type(kwargs))
#     print(a, b, c, args, kwargs)

# some_function(1, 2, 3, 4, 5, abcde=4312)
# some_function(1, 2, 3, 4)
# some_function(1, 2, 3)

def function(b):
    return a + b

a = 5
function = lambda *args: max(args)

print(function(0,3,5,6,7,8,9,0,0))

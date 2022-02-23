# # Define the function
# def add_two(x):
#     """Increase x by 2.""" 
#     x += 2 
#     return x
# print(add_two(2))

def f(*args, **kwargs):
    x = args[0] 
    y = kwargs.get("y") 
    print (f"x: {x}, y: {y}") 
f(5, y=2)

#Lambda
def identity(x):
    return x
# Can be rewrite as
    lambda x: x         # Keyword: lambda, bound variable: x, body: x
# Another example
y=(lambda x: x + 1)(2)
print(y)
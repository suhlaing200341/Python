def total_numbers(num1, num2):
    print("total numbers.....", num1 + num2)

total_numbers(4, 6)

def myfunction(*num):
    print("*args......", num)
    
myfunction(2, 3, 4, 5)

def afunction(**char):
    print("**kwargs......", char)
    
afunction(first="Su", last="Hlaing")

# =============Lambda function============
"""
A lambda function is a small anonymous function.
A lambda function can take any number of arguments, but can only have one expression.
"""
result = lambda c, b: c + b
    
print("lambda result.......", result(4, 6))

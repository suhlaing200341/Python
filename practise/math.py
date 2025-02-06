import math

def calculate(x, y, z):
    total = sum(item for item in x)
    print("Total.....", total)
    
    sqrt = math.sqrt(y)
    print("Sqrt.....", sqrt)
    
    abs_val = abs(z)
    print("Abs.....", abs_val)
    
    min_val = min(x)
    print("Min.....", min_val)
    
calculate([1, 2, 3, 4, 5], 16, -10)
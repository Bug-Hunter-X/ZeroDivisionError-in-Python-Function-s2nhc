def function(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        return "Division by zero"

result = function(10, 0)
print(result) # Output: Division by zero

result2 = function(10,2)
print(result2) # Output: 5.0
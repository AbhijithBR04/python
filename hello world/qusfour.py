def calculate_reciprocals(numbers):
    reciprocals = []
    
    for num in numbers:
        if num == 0:
            reciprocals.append("Cannot calculate reciprocal of zero")
        else:
            reciprocals.append(1 / num)
    
    return reciprocals

# Example usage
numbers = [1, 2, 3, 0, -4, 5]
result = calculate_reciprocals(numbers)
print("Reciprocals:", result)
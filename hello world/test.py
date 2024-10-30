def square_numbers(numbers):

    # if not isinstance(numbers, list):
    #     return "Error: Input must be a list."

    if len(numbers) == 0:
        return {}
    
    result = {}

    for num in numbers:
        try:

            squared_num = float(num) ** 2
            
            result[num] = squared_num
        except ValueError:
            print(f"Warning: '{num}' is not a valid number.")
    
    return result

input_list = [4, 1, 8, 7, 2]
result = square_numbers(input_list)
print(result)
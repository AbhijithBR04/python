def find_common_elements(A, B):
    return A & B

A = {1, 2, 3}
B = {3, 4, 5}

common_elements = find_common_elements(A, B)
print("Common elements:", common_elements)
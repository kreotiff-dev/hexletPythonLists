# lesson 2 - Concept of lists
# Реализуйте функцию is_list(), которая проверяет, является ли значение списком.

def is_list(value):
    return isinstance(value, list)

print(is_list([1, 2, 3]))
print(is_list(1))
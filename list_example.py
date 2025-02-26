# Creating a list
my_list = [1, 2, 3, 4, 5]

# Adding elements to the list
my_list.append(6)
my_list.insert(0, 0)

# Removing elements from the list
my_list.remove(3)
popped_element = my_list.pop()

# Iterating through the list
for element in my_list:
    print(element)

# List comprehension
squared_list = [x**2 for x in my_list]
print(squared_list)

def find_in_list(lst, element):
    """
    Find the index of an element in the list.
    Returns the index if found, otherwise returns -1.
    """
    try:
        return lst.index(element)
    except ValueError:
        return -1

# Example usage of find_in_list
index = find_in_list(my_list, 2)
print(f"Index of 2: {index}")

index = find_in_list(my_list, 10)
print(f"Index of 10: {index}")

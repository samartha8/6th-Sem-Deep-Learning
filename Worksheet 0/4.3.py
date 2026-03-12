# 1. Flatten a Nested List
def flatten(lst):
    result = []
    for item in lst:
        if isinstance(item, list):
            result.extend(flatten(item))
        else:
            result.append(item)
    return result


# 2. Accessing Nested List Elements
def access_nested_element(lst, indices):
    element = lst
    for i in indices:
        element = element[i]
    return element


# 3. Sum of All Elements in a Nested List
def sum_nested(lst):
    total = 0
    for item in lst:
        if isinstance(item, list):
            total += sum_nested(item)
        else:
            total += item
    return total


# 4. Remove Specific Element from a Nested List
def remove_element(lst, elem):
    result = []
    for item in lst:
        if isinstance(item, list):
            result.append(remove_element(item, elem))
        elif item != elem:
            result.append(item)
    return result


# 5. Find Maximum Element in a Nested List
def find_max(lst):
    max_value = None
    for item in lst:
        if isinstance(item, list):
            value = find_max(item)
        else:
            value = item
        
        if max_value is None or value > max_value:
            max_value = value
    return max_value


# 6. Count Occurrences of an Element in a Nested List
def count_occurrences(lst, elem):
    count = 0
    for item in lst:
        if isinstance(item, list):
            count += count_occurrences(item, elem)
        elif item == elem:
            count += 1
    return count


# 7. Deep Flatten (List of Lists of Lists)
def deep_flatten(lst):
    result = []
    for item in lst:
        if isinstance(item, list):
            result.extend(deep_flatten(item))
        else:
            result.append(item)
    return result


# 8. Nested List Average
def average_nested(lst):
    flat = deep_flatten(lst)
    return sum(flat) / len(flat)


# Example Tests
print("Flatten:", flatten([[1, 2], [3, 4], [5]]))
print("Access Element:", access_nested_element([[1,2,3],[4,5,6],[7,8,9]], [1,2]))
print("Sum Nested:", sum_nested([[1,2],[3,[4,5]],6]))
print("Remove Element:", remove_element([[1,2],[3,2],[4,5]], 2))
print("Find Max:", find_max([[1,2],[3,[4,5]],6]))
print("Count Occurrences:", count_occurrences([[1,2],[2,3],[2,4]], 2))
print("Deep Flatten:", deep_flatten([[[1,2],[3,4]],[[5,6],[7,8]]]))
print("Average Nested:", average_nested([[1,2],[3,4],[5,6]]))
def search_data(sorted_list, target):
    left, right = 0, len(sorted_list) - 1

    while left <= right:
        mid = (left + right) // 2
        if sorted_list[mid] == target:
            return mid
        elif sorted_list[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    return -1

# Example sorted list
xyz_data = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]

# Input target value to search
target_value = int(input("Enter the value to search: "))

# Search for the target value in the sorted list
result_index = search_data(xyz_data, target_value)

if result_index != -1:
    print(f"Value {target_value} found at index {result_index}.")
else:
    print(f"Value {target_value} not found in the list.")

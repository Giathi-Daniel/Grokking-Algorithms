def binary_search(arr, item):
    # Keep track of which part of the list you'll search in
    low = 0;
    high = len(arr) - 1;

    while low <=high:
        mid = (low + high) // 2 # check the middle element
        guess = arr[mid]
        if guess == item: # Found item
            return mid
        elif guess > item: # The guess was too high
            high = mid - 1
        else: # The guess was too low
            low = mid + 1
    return None # The item was not found

my_list = [1, 3, 5, 7, 9]
print(binary_search(my_list, 3))
print(binary_search(my_list, -1))
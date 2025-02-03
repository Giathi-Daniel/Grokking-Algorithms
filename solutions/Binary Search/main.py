def binary_search(arr, name):
    low = 0
    high = len(arr) - 1

    while low <= high:
        mid = (low + high) // 2
        guess = arr[mid]

        if guess == name:
            return mid
        elif guess > name:
            high = mid - 1
    return None
my_names = [1,128]
print(binary_search(my_names, 128))

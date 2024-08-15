def length(arr):
    count = 1
    for num in arr:
        count += 1
    return count

arr = [1, 2, 3, 4, 5]

# this should be 5 but it prints 6. can you find what is wrong and fix it?
print(length(arr))
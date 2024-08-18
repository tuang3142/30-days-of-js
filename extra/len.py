def length(arr):
    count = 0 #change 1 to 0 
    for num in arr:
        count += 1
    return count

arr = [1, 2, 3, 4, 5]

# this should be 5 but it prints 6(WHY IT PRINTS 6 INSTEAD OF 4). can you find what is wrong and fix it?
# IT'S WORK
print(length(arr))

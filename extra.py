#EXTRA EXERCISE
#excercise 1 
arr = [1,2,3,4,5,7]
avg = sum(arr) / len(arr)
print(int(avg)) 

#execise 2
def length(arr):
    count = 0
    for num in arr:
        count += 1
    return count

arr = [1, 2, 3, 4, 5]

# this should be 5 but it prints 6. can you find what is wrong and fix it?
print(length(arr))

#I think count(line 9) should start from 0, so just replace 1 to 0  
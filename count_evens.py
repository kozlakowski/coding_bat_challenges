def count_evens(nums):

    evens = []
    
    for num in nums:
        if (num % 2) == 0:
            evens.append(num)
        else:
            pass

    return len(evens)

print(count_evens([1,3,5]))


        

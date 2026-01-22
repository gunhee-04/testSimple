def add_many(args):
    result = 0
    for i in args:
        result += i 

    return result

nums=[2,3,4]
sum = add_many(nums)
print(sum)
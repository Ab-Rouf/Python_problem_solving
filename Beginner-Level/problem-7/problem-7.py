def find_missing_number(nums):
    n = len(nums) + 1  
    expected_sum = n * (n + 1) // 2  
    a_sum = sum(nums)  
    m = expected_sum - a_sum  
    return m


l = [1, 2, 4, 5]
print(find_missing_number(l))  

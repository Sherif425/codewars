def sum_two_smallest_numbers(numbers):
    return sum(sorted(numbers)[:2])

nums = [10, 343445353, 3453445, 3453545353453]
print(sum_two_smallest_numbers(nums))   #correct result 3453455
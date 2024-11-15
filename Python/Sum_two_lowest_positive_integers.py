def sum_two_smallest_numbers(numbers):
    """
    Create a function that returns the sum of the two lowest positive numbers given
    an array of minimum 4 positive integers. No floats or non-positive integers will be
    passed.
    For example, when an array is passed like [19, 5, 42, 2, 77], the output should be 7.
    """
    lowest_num = numbers[0]
    sum = 0
    for i in numbers:
        if 0 < i < lowest_num:
            lowest_num = i
    sum += lowest_num
    numbers.remove(lowest_num)
    print(numbers, sum)
    lowest_num2 = numbers[0]
    for i in numbers:
        if 0 < i < lowest_num2:
            lowest_num2 = i
    sum += lowest_num2
    return sum


nums = [10, 343445353, 3453445, 3453545353453]
print(sum_two_smallest_numbers(nums))

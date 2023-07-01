#1.Given a list A of size N. You need to find the sum of Maximum and Minimum element in the given list Input Format First argument A is an integer list. Output Format Return the sum of maximum and minimum element of the list
A = [-2, 1, -4, 5, 3]
def solve(A):
    sum=max(A)+min(A)
    return(sum)

#Run the function
answer=solve(A)
print(answer)

#2.Given a list A. You have some integers given in the list B.For the i-th number, find the frequency of B[i] in the list A and return a list containing all the frequencies. Input Format First argument A is a list of integers.Second argument B is a list of integers denoting the queries. Output Format Return an array of integers containing frequency of the each element in B.
def find_frequencies(A, B):
    frequency_list = []
    for num in B:
        frequency = A.count(num)  # Count the frequency of num in list A
        frequency_list.append(frequency)  # Append the frequency to the result list
    return frequency_list
    
A = [1, 2, 3, 2, 4, 1, 2]
B = [1, 2, 5]
result = find_frequencies(A, B)
print(result)  # Output: [2, 3, 0] (frequency of 1 is 2, frequency of 2 is 3, frequency of 5 is 0)

#3.Given an integer list A of size N, find the first repeating element in it. We need to find the element that occurs more than once and whose index of the first occurrence is the smallest. If there is no repeating element, return -1. Input Format The first and only argument is an integer list A of size N. Output Format Return an integer denoting the first repeating element.
def find_first_repeating_element(A):
    frequency_map = {}
    min_index = float('inf')  # Initialize the minimum index to positive infinity
    repeating_element = -1  # Initialize the repeating element as -1

    for i, num in enumerate(A):
        if num in frequency_map:
            # If the element is already in the frequency map, it is a repeating element
            # Check if its index is smaller than the current minimum index
            if frequency_map[num] < min_index:
                min_index = frequency_map[num]
                repeating_element = num
        else:
            # If the element is not in the frequency map, add it with its index
            frequency_map[num] = i

    return repeating_element
my_list = [2, 5, 3, 2, 4, 3, 1, 5]
result = find_first_repeating_element(my_list)
print(result)  # Output: 2 (the first repeating element is 2)

#4.Given a number A, find if it is COLORFUL number or not. If number A is a COLORFUL number return 1 else, return 0. What is a COLORFUL Number: A number can be broken into different consecutive sequence of digits. The number 3245 can be broken into sequences like 3, 2, 4, 5, 32, 24, 45, 324, 245 and 3245. This number is a COLORFUL number, since the product of every consecutive sequence of digits is different Input Format The first and only argument is an integer A. Output Format Return 1 if integer A is COLORFUL else return 0. Explanation 2: Possible Sub-sequences: [2, 3, 6, 23, 36, 236] where 2 -> 2 3 -> 3 6 -> 6 23 -> 6 (product of digits) 36 -> 18 (product of digits) 236 -> 36 (product of digits) This number is not a COLORFUL number since the product sequence 23 and sequence 6 is same.

def is_colorful_number(A):
    digits = list(map(int, str(A)))  # Convert the number to a list of digits
    product_set = set()

    for i in range(len(digits)):
        product = 1
        for j in range(i, len(digits)):
            product *= digits[j]
            if product in product_set:
                return 0  # If the product is already in the set, it's not COLORFUL
            product_set.add(product)

    return 1  # If no repetitions are found, the number is COLORFUL
number = 3245
result = is_colorful_number(number)
print(result)  # Output: 1 (3245 is a COLORFUL number)


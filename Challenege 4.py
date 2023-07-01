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


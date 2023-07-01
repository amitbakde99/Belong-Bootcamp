#1.Given a list A of size N. You need to find the sum of Maximum and Minimum element in the given list Input Format First argument A is an integer list. Output Format Return the sum of maximum and minimum element of the list
A = [-2, 1, -4, 5, 3]
def solve(A):
    sum=max(A)+min(A)
    return(sum)

#Run the function
answer=solve(A)
print(answer)

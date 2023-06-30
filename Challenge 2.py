#4.You are given an integer A. You have to tell whether it is a perfect number or not. Perfect number is a positive integer which is equal to the sum of its proper positive divisors. A proper divisor of a natural number is the divisor that is strictly less than the number. Return 1 if A is a perfect number and 0 otherwise.
A=4
def solve(A):
    if A <= 0:
        return 0

    divisors_sum = 0
    for i in range(1, A):
        if A % i == 0:
            divisors_sum += i

    if divisors_sum == A:
        return 1
    else:
        return 0
answer=solve(A)
print(answer)


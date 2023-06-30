#1.Given an integer A, you need to find the count of it's factors.Factor of a number is the number which divides it perfectly leaving no remainder.Example : 1, 2, 3, 6 are factors of 6
#2.Given a number A. Return 1 if A is prime and return 0 if not.
#3.Given a number A. Return square root of the number if it is perfect square otherwise return -1. Note: A number is a perfect square if its square root is an integer.
#4.You are given a number N, write a program that calculates the sum of it’s digits.
    
#5. You are given an integer A. You have to tell whether it is a perfect number or not. An Perfect number is a positive integer that is equal to the sum of its proper positive divisors. A proper divisor of a natural number is the divisor that is strictly less than the number. Return 1 if A is a perfect number and 0 otherwise.
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

#6. You will be given an integer n. You must return the count of prime numbers less than or equal to n.
n=19
def solve(n):
    is_prime = [True] * (n+1)
    is_prime[0] = is_prime[1] = False  

   
    p = 2
    while p * p <= n:
        
        if is_prime[p]:
            
            for i in range(p * p, n+1, p):
                is_prime[i] = False
        p += 1

    count = sum(is_prime)

    return count

answer=solve(n)
print(answer)

#7..You are given an integer A. You need to print all the Armstrong Numbers between 1 to A as a list. If sum of cubes of each digit of the number is equal to the number itself, then the number is called an Armstrong number. For example, 153 = ( 1 * 1 * 1 ) + ( 5 * 5 * 5 ) + ( 3 * 3 * 3 ).
A=153
def solve(A):
    digit_sum = 0
    temp = A
    while temp > 0:
        digit = temp % 10
        digit_sum += digit ** 3
        temp //= 10

    if A == digit_sum:
        return True
    else:
        return False
def find_armstrong_numbers(A):
    armstrong_numbers = []
    for A in range(1, A + 1):
        if is_armstrong_number(A):
            armstrong_numbers.append(A)
    return armstrong_numbers

#Run the function
answer=solve(A)
print(answer)

#8.Given two integers A and B. A represents the count of mangoes and B represent the count of slices of mangoes. Mango can be cut into three slices of mangoes. A glass of mango shake can be formed by two slices of mangoes. Find the maximum number of glasses of mango shakes you can make with A mangoes and B slices of mangoes initially.
A=19
B=0
def solve(A,B):
    slices=(B+3*A)
    n=int(slices/2)
    return n

#Run the function
answer=solve(A,B)
print(answer)


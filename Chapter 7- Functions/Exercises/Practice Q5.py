# 5. Python program to check if a number is prime using a function
def is_prime_v2(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

# Example usage:
check_number_v2 = 23
if is_prime_v2(check_number_v2):
    print(f"{check_number_v2} is a prime number.")
else:
    print(f"{check_number_v2} is not a prime number.")

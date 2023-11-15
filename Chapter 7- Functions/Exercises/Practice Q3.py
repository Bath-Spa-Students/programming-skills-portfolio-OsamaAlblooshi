# 3. Python program to check if a number is prime using a function
def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

# Example usage:
check_number = 17
if is_prime(check_number):
    print(f"{check_number} is a prime number.")
else:
    print(f"{check_number} is not a prime number.")

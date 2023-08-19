#String manipulation
#This is solved using only chatGPT and some ideas...

import pyperclip

input_string = pyperclip.paste()

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def classify_numbers(s):
    numbers = [int(c) for c in s if c.isdigit() and c != '0' and c != '1']
    composite_sum = 0
    prime_sum = 0

    for num in numbers:
        if is_prime(num):
            prime_sum += num
        else:
            composite_sum += num

    return composite_sum, prime_sum

def increment_ascii(c):
    if not c.isdigit():
        return chr(ord(c) + 1)
    return c

def solve_challenge(input_string):
    composite_sum, prime_sum = classify_numbers(input_string)
    product = composite_sum * prime_sum

    non_numeric_characters = [c for c in input_string if not c.isdigit()]
    modified_characters = [increment_ascii(c) for c in non_numeric_characters[:25]]

    answer = ''.join(modified_characters) + str(product)
    return answer

answer = solve_challenge(input_string)
print(answer)
pyperclip.copy(answer)
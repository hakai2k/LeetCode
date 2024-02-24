def check_prime(num):
    for i in range(2, num): 
        if num % i == 0: return False
    else: return True
print(list(filter(check_prime, list(range(2, 2024)))))
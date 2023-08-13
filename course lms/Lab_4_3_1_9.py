def is_prime(num):
    if num % 2 == 0 and num // 2 != 1:
        return False
    elif num % 3 == 0 and num // 3 != 1:
        return False
    elif num % 5 == 0 and num // 5 != 1:
        return False
    elif num % 7 == 0 and num // 7 != 1:
        return False
    else:
        return True

for i in range(1, 50):
	if is_prime(i + 1):
			print(i + 1, end=" ")
print()

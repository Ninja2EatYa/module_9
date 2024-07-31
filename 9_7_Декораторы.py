def is_prime(func):
    def wrapper(*args):
        res = func(*args)
        is_prime = 0
        for i in range(2, (res // 2) + 1):
            if res % i == 0:
                is_prime += 1
        if is_prime == 0:
            print('Простое')
        else:
            print('Составное')
        return res
    return wrapper


@is_prime
def sum_three(*args):
    return sum(args)


result = sum_three(2, 3, 6)
print(result)

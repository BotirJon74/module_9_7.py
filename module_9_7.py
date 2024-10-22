def is_prime(func):
    def wrapper(*args):
        res = func(*args)
        for i in range(2, int(res ** 0.5) + 1):
            if res % i == 0:
                print('Составное')
            else:
                print('Простое')
            return res
    return wrapper


@is_prime
def sum_three(a, b, c):
    return a + b + c


result = sum_three(2, 3, 6)
print(result)

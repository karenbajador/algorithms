''' 
    Get module of a huge fibonacci number 
'''

def get_fibonacci_huge_naive(n, m):
    if n <= 1:
        return n

    previous = 0
    current = 1

    for _ in range(n - 1):
        previous, current = current, previous + current % m

    return current % m


def pisano(modulo):
    ''' 
        Get the repeating pattern for fibonacci given the modulo
        Checking for first repetition of the starting signature "0, 1"
    '''
    if modulo == 1:  # exception
        return 1
    if modulo == 2:  # exception
        return 3

    previous = 1
    current = 1
    result = 1
    while not (previous == 0 and current == 1):
        previous, current = current, (previous + current) % modulo  # 2
        result += 1
    return result


def calc_fib_last_digit(n, m):
    '''
        Get the module of fib
    '''

    if n <= 1:
        return n

    previous = 0
    current = 1

    for _ in range(n - 1):
        previous, current = current, previous + current % m
    return current % m


def get_fibonacci_huge_optimized(n, m):

    if n <= 1:
        return n

    return calc_fib_last_digit(n % pisano(m), m)


def test_pisano():
    assert pisano(1) == 1
    assert pisano(2) == 3
    assert pisano(3) == 8
    assert pisano(4) == 6
    assert pisano(5) == 20
    assert pisano(6) == 24
    assert pisano(10) == 60


def test_fib():
    n, m = 1000, 100
    assert get_fibonacci_huge_naive(n, m) == get_fibonacci_huge_optimized(n, m)
    n, m = 1000000, 9973
    assert get_fibonacci_huge_naive(n, m) == get_fibonacci_huge_optimized(n, m)
    n, m = 1000, 10
    assert get_fibonacci_huge_naive(n, m) == get_fibonacci_huge_optimized(n, m)
    n, m = 99, 2
    assert get_fibonacci_huge_naive(n, m) == get_fibonacci_huge_optimized(n, m)





    



if __name__ == '__main__':
    n, m = input().split()

    print('***')
    print(get_fibonacci_huge_naive(int(n), int(m)))
    print('***')
    print(get_fibonacci_huge_optimized(int(n), int(m)))


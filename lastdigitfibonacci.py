'''
 Get only the last digit of fibonacci number given n
'''


def get_fibonacci_last_digit(n):
    '''
       Complexity: O(N)
       No need to handle large numbers
       Trick is to compute only the remainder
    '''
    if n <= 1:
        return n

    PREV = 0
    CURR = 1

    for _ in range(2, n+1):
        PREV, CURR = CURR, PREV + CURR % 10

    return CURR % 10


if __name__ == '__main__':
    n = int(input('Enter number:'))
    print(get_fibonacci_last_digit(n))

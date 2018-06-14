'''
 Get the fibonacci number given n
'''


def calc_fib(n):
    '''
       Complexity: O(N)
       No need to store all values in array
    '''
    if n <= 1:
        return n

    PREV = 0
    CURR = 1

    for _ in range(n-1):      
        PREV, CURR = CURR, PREV + CURR
        # print(f'i: {i}, PREV: {PREV}, CURR: {CURR}')
        
    return CURR


if __name__ == "__main__":
    n = int(input('Enter number:'))
    print(calc_fib(n))


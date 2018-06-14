'''
 Get Greatest Commond Divisor (GCD) of two digits
'''


def gcd_naive(a, b):
    '''
        Complexity: O(N) of lesser digit
    '''
    current_gcd = 1
    # loop until the lesser digit
    for d in range(2, min(a, b) + 1):
        # Check if divisor of both digits
        if a % d == 0 and b % d == 0:
            # if current divisor greater that last gcd, replace gcd
            if d > current_gcd:
                current_gcd = d

    return current_gcd


def gcd_euclid(a, b):
    '''
        Using Euclid theorem
        Complexity: some log ???
    '''    

    # a should be the bigger number
    a, b = (b, a) if b > a else (a, b)

    # Getting a'; remainder of a / b
    a_prime = a % b

    if a_prime == 0:
        # If no remainder, then b is the greatest divisor
        return b
    else:
        return gcd_euclid(a=b, b=a_prime)


if __name__ == "__main__":

    a, b = input().split()
    # print('naive: {}'.format(gcd_naive(int(a), int(b))))
    # print('euclid: {}'.format(gcd_euclid(int(a), int(b))))
    print(gcd_euclid(int(a), int(b)))

'''
Input: an integer
Returns: an integer
'''

def eating_cookies(n):

    cookie_memo = {}

    # base cases
    if n < 0:
        return 0
    elif n == 0:
        return 1
    elif n <= 2:
        return n
    elif n == 3:
        return 4

    # # non  base case
    elif n not in cookie_memo:
        cookie_memo[n] = eating_cookies(n-1) + eating_cookies(n-2) + eating_cookies(n-3)
        
    return cookie_memo[n]

if __name__ == "__main__":
    # Use the main function here to test out your implementation
    num_cookies = 5

    print(f"There are {eating_cookies(num_cookies)} ways for Cookie Monster to each {num_cookies} cookies")

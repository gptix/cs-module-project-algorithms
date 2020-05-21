'''
Input: a List of integers in which every int, except one,
shows up twice.

Returns: the only integer that shows up once.'''

def single_number(list_of_integers):
    my_integers = {}
    for integer in list_of_integers:
        if (integer in my_integers.keys()):
            del my_integers[integer]
        else: 
            my_integers[integer] = True
    return list(my_integers)[0]

if __name__ == '__main__':
    # Use the main function to test your implementation
    arr = [1, 1, 4, 4, 5, 5, 3, 3, 9, 0, 0]

    print(f"The integer that occurs once is: '{single_number(arr)}'")
    
arr = [1, 1, 4, 4, 5, 5, 3, 3, 9, 0, 0]

single_number(arr)

"""for i in range(len(arr)): products[i] = product_so_far product_so_far *= arr[i] """
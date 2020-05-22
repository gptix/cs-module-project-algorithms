'''
Input: a List of integers.
Returns: a List of integers,with all '0' to the right.
'''
def moving_zeroes(lst):
    # find leftmost zero
    length  = len(lst)
    last_index = length - 1
    left_pointer = 0
    right_pointer = 0
    
    # find leftmost zero
    while (left_pointer <= last_index) and (lst[left_pointer] is not 0):
        left_pointer += 1
    
    # we might have gotten to the end of the list
    if left_pointer == last_index:
        return lst
    
    else: # we have found a zero before the end of the list
        # if the read index gets beyond the list, GAME OVER MNA
        right_pointer = left_pointer + 1
        while left_pointer < last_index and right_pointer <= last_index:
            lst[left_pointer] = lst[right_pointer]
            lst[right_pointer] = 0
            right_pointer += 1
            if lst[left_pointer] is not 0:
                left_pointer += 1
                
    return lst


if __name__ == '__main__':
    # Use the main function here to test out your implementation
    arr = [0, 3, 1, 0, -2]

    print(f"The resulting of moving_zeroes is: {moving_zeroes(arr)}")
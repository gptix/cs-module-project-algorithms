'''
Input: a List of integers.
Returns: a List of integers,with all '0' to the right.
'''
def moving_zeroes(lst):
    length = len(lst)
    zero_count = lst.count(0)
    lst = [i for i in lst if i is not 0]
    return lst + [0]*zero_count


if __name__ == '__main__':
    # Use the main function here to test out your implementation
    arr = [0, 3, 1, 0, -2]

    print(f"The resulting of moving_zeroes is: {moving_zeroes(arr)}")
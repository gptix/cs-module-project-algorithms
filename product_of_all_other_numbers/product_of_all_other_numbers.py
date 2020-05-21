# '''
# Input: a List of integers
# Returns: a List of integers
# '''
from functools import reduce

def product_of_all_other_numbers(lst):
    # cases:
    # empty list
    # list with one element
    # list with more than one zero
    # list with only one zero
    # list with no zeroes


    # if list is empty
    if lst == []:
            return lst

    lst_length = len(lst)
    # if list has only one element:
    if lst_length == 1:
        return [0]


    # zero_count = sum([1 for i in lst if i == 0])

    # if zero_count > 0:
    #     basic_lst = [0]*lst_length

    #     # in this case, only the element at the zero is non-zero
    #     if zero_count == 1:
    #         index_of_non_zero_element = lst.index(0)
    #         lst[index_of_non_zero_element] = 1
    #         prod = reduce( (lambda x, y: x*y) , lst)
    #         basic_lst[index_of_non_zero_element] = prod

    #     # (if the count of zeroes is > 1, all products remain zero)
    #     return basic_lst

    # basic case:
    answer_list = []
    for idx in range(lst_length):
        answer_list.append( reduce(  (lambda x, y: x * y),   lst[:idx] + lst[idx+1:]  ))

    return answer_list
    
    # test_list = [1, 7, 3, 4]
    # product_of_all_other_numbers(test_list)


if __name__ == '__main__':
    # Use the main function to test your implementation
    # arr = [1, 2, 3, 4, 5]
    arr = [2, 6, 9, 8, 2, 2, 9, 10, 7, 4, 7, 1, 9, 5, 9, 1, 8, 1, 8, 6, 2, 6, 4, 8, 9, 5, 4, 9, 10, 3, 9, 1, 9, 2, 6, 8, 5, 5, 4, 7, 7, 5, 8, 1, 6, 5, 1, 7, 7, 8]

    print(f"Output of product_of_all_other_numbers: {product_of_all_other_numbers(arr)}")

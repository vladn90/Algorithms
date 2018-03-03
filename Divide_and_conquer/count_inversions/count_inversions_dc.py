""" Count inversions in an array. Divide and conquer algorithm based
on merge sort.
Algorithm description:
1) Base case: length(array) <= 1, i.e. only 1 element in the array,
no need to sort and no need to count inversions.
2) Divide array in two halves: left array and right array.
3) Sort recursively and count inversions in left and right array.
4) Combine sorted arrays and count inversions between elements from different
arrays.
5) Return total number of inversions in left array, right array and in-between.
"""


def sort_count_split(left_arr, right_arr):
    # pointers to the beginning of the left and right arrays
    i, j = 0, 0
    comb_arr = []  # resulting sorted array
    inv = 0  # inversions count
    # choose the minimum element from left and right array,
    # count inversions if needed
    while i < len(left_arr) and j < len(right_arr):
        # min element in the left array, no inversions needed
        if left_arr[i] <= right_arr[j]:
            comb_arr.append(left_arr[i])
            i += 1
        # min element in right array, number of inversions needed is equal to
        # number of elements left in the left array, including current element
        else:
            comb_arr.append(right_arr[j])
            j += 1
            inv += len(left_arr) - i

    # add whatever's left from left or right array to resulting sorted array
    while i < len(left_arr):
        comb_arr.append(left_arr[i])
        i += 1
    while j < len(right_arr):
        comb_arr.append(right_arr[j])
        j += 1
    return comb_arr, inv


def sort_count(array):
    """ Returns sorted array and number of inversions.
    """
    # base case, empty array or an array with 1 element
    if len(array) <= 1:
        return array, 0

    mid = len(array) // 2
    # recursively sort left and right array and count inversions
    left_arr, left_inv = sort_count(array[:mid])
    right_arr, right_inv = sort_count(array[mid:])
    # merge sorted arrays and count inversions between elements in arrays
    array, split_inv = sort_count_split(left_arr, right_arr)
    return array, (left_inv + right_inv + split_inv)


def count_inv(array):
    """ Returns number of inversions in array.
    """
    return sort_count(array)[1]

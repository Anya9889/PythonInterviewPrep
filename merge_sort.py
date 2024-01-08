def merge_sort(arr):
    # splitting the original array into two smaller ones (half length) until its length is not equal to 1.

    if len(arr) <= 1:
        return arr

    else:

        # diving the array into two parts
        left_arr = arr[:len(arr) // 2]
        right_arr = arr[len(arr) // 2:]

        # recursion

        left = merge_sort(left_arr)
        right = merge_sort(right_arr)

    return merge_two_sorted_arrays(left, right)

def merge_two_sorted_arrays(left_arr, right_arr):
        # comparing each element from the first array with the one from the second, and appending the smaller one
        # to the final result. Increasing the index as we do it.

        result = []

        # this it the left array index
        i = 0
        # this is the right array index
        j = 0
        # this is the final merged array index
        k = 0

        # merging
        while i < len(left_arr) and j < len(right_arr):
            if left_arr[i] < right_arr[j]:
                result.append(left_arr[i])
                i += 1

            else:
                result.append(right_arr[j])
                j += 1

            k += 1

        while i < len(left_arr):
            result.append(left_arr[i])
            i += 1
            k += 1

        while j < len(right_arr):
            result.append(right_arr[j])
            j += 1
            k += 1

        return result


def merge_sort_two(arr):

        # splitting the original array into two smaller ones (half length) until its length is not equal to 1.
        # Then comparing each element from the first array with the one from the second, and appending the smaller one
        # to the original array. Increasing the index as we do it. If the length of the array is greater than 1, we'll
        # keep applying this function to the left and right array.

        if len(arr) > 1:


            # diving the array into two parts
            left_arr = arr[:len(arr)//2]
            right_arr = arr[len(arr)//2:]

            #recursion

            merge_sort(left_arr)
            merge_sort(right_arr)

            # this it the left array index
            i = 0
            # this is the right array index
            j = 0
            # this is the final merged array index
            k = 0

            #merging
            while i < len(left_arr) and j < len(right_arr):
                if left_arr[i] < right_arr[j]:
                    arr[k] = left_arr[i]
                    i += 1

                else:
                    arr[k] = right_arr[j]
                    j += 1

                k += 1

            while i < len(left_arr):
                arr[k] = left_arr[i]
                i += 1
                k += 1

            while j < len(right_arr):
                arr[k] = right_arr[j]
                j += 1
                k += 1

        return arr

print(merge_sort_two([5,6,4,3]))
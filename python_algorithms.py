class Solution:
    def minOperationsNumber(self, n):
        # the function that return the minimum number of operations to reduce a number to 0
        # by adding or subtracting the power of 2.

        if n == 1 or n == 2:
            return 1
        meter = 0

        while n != 0:
            degree = 0
            delta = 0
            while n - delta > 0:
                delta = 2 ** degree
                degree += 1

            if n - (delta // 2) < delta - n:
                n = n - (delta // 2)
            else:
                n = delta - n
            meter += 1

        return meter




    def isPalindrome(self, s):
        # checking if a string is a palindrome (reading the same from the beginning to end and from end to beginning

        new_string = ''.join(char.lower() for char in s if char.isalnum())

        if new_string == new_string[::-1]:
            return True



    def isSubsequence(self, s, t):
        #  checking if a string is a subsequence of another

        position = 0

        for char in s:
            if char not in t[position:] or position > len(t):
                return False
            else:
                position = t.find(char, position) + t.find(char, 0, position) + 1



        return True




    def k_smallest_element(self, arr, k):
        # return the Kth smallest element from the array

        arr.sort()

        return arr[k - 1]



    def quick_sort(self, n):
        # sort the numbers by choosing a pivot point and comparing each number with that pivot and appending each number to either
        # greater array or lower array.
        # Then reapply the same function to each list (greater and lower array).


        if len(n) == 1:
            return n

        if len(n) == 0:
            return []

        pivot = n.pop()
        greater_array = []
        lower_array = []

        for i in n:
            if i < pivot:
                lower_array.append(i)

            else:
                greater_array.append(i)


        return self.quick_sort(lower_array) + [pivot] + self.quick_sort(greater_array)



    def bubble_sort(self, nums):
        # sorting an array by comparing each number with the one next to it and swapping them if the one on the left
        # is bigger than the one on the right.


        l = len(nums)
        swapped = False
        for i in range(l - 1):
            # 0,1,2,3,4,5
            for j in range(l - i - 1):
                # 0,1,2,3,4,5
                if nums[j+1] < nums[j]:
                    swapped = True
                    nums[j + 1], nums[j] = nums[j], nums[j + 1]
                    print(nums)


            if not swapped:
                return nums

        return nums



    def n_fibonacci(self, n):
        # write a fibonacci sequence for a given number n. Fibonacci sequence always starts with 0, 1, and then each next
        # number is the sum of the two previous ones.

        if n == 1:
            return 1

        if n == 0:
            return 0

        a = 0
        b = 1

        fib = [0]

        for i in range(n):
            a, b = b, a+b
            fib.append(a)

        return fib



    def merge_sort(self, arr):

        # splitting the original array into two smaller ones (half length) until its length is not equal to 1.
        # Then comparing each element from the first array with the one from the second, and appending the smaller one
        # to the original array. Increasing the index as we do it. If the length of the array is greater than 1, we'll
        # keep applying this function to the left and right array.

        if len(arr) > 1:


            # diving the array into two parts
            left_arr = arr[:len(arr)//2]
            right_arr = arr[len(arr)//2:]

            #recursion

            self.merge_sort(left_arr)
            self.merge_sort(right_arr)

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



    def anagram(self, s1, s2):
        # given two strings, check if the are anagrams (can be written using the same letters, can be in different order)

        if len(s1) != len(s2):
            return False

        count = {}

        for char in s1:
            if char in count:
                count[char] += 1

            else:
                count[char] = 1

        for char in s2:
            if char in count:
                count[char] -= 1

            else:
                count[char] = 1

        for k in count:
            if k != 0:
                return False

        return True




    def pair_sum(self, nums, k):
        # given an array of integers and an integer k, return all unique pairs of integers from the array
        # that will sum up to k.

        if len(nums) < 2:
            return print('Too small')

        seen = set()
        output = set()

        for num in nums:
            target = k - num

            if target not in seen:
                seen.add(num)
            else:
                output.add((min(num, target), max(num, target)))

        return output



    def largest(self, nums):
        # function that returns a largest sum of a contiguous subarray.

        if len(nums) < 2:
            return print('Too small')

        current_sum = max_sum = nums[0]

        for num in nums[1:]:
            current_sum = max(current_sum + num, num)
            max_sum = max(max_sum, current_sum)

        return max_sum

# now create an instance of a class Solution and check any of the following functions with an example to see how they work.

example = Solution()
# print(example.merge_sort(([5,6,4,3,7,8,1,2])))



def reversed_string(text):
    # the most simple way to reverse a string
    result = ""
    for char in text:
       result = char + result
    return result



def reversed_string_2(s):
    # more complicated step by step way to reverse a string

    l = len(s)
    i = 0
    new_string = []


    while i < len(s):
        # checking if an element is not a space
        if s[i] != ' ':
            word_start = i

            while i < len(s) and s[i] != ' ':
                i += 1

            new_string.append(s[word_start:i])

        i += 1

    return ' '.join(reversed(new_string))




def reverse_string_3(s):
    # another way to reverse a string by using negative indexing

    return ' '.join(word[::-1] for word in s.split())




def rotation(num1, num2):
    # functon that checks if one array is a rotation of the other.

    if len(num1) != len(num2):
        return False

    key_1 = num1[0]

    key_2 = 0

    for i in range(len(num2)):
        if num2[i] == key_1:
            key_2 = i

            break

    if key_2 == 0:
        return False

    for x in range(len(num1)):
        index2 = (x + key_2) % len(num1)
        if num1[x] != num2[index2]:
            return False

    return True



def common_elements(a, b):
    # function that returns a list of common elements between two lists of integers sorted in a ascending order.

    i1 = 0
    i2 = 0

    result = []

    while i1 < len(a) and i2 < len(b):

        if a[i1] == b[i2]:
            result.append(a[i1])
            i1 += 1
            i2 += 1

        elif a[i1] < b[i2]:
            i1 += 1

        else:
            i2 += 1

    return result




def mine_sweeper(bombs, num_rows, num_cols):
    # a function that takes three arguments: bomb locations, number of rows and columns. The task is to return
    # the matrix of a given size that is going to have -1 where the bomb is, 0 if there are no bombs in the given
    # matrix range (using 3 x 3 in this example), or another value which is going to be equal the sum of the bombs
    # in the given row and column range. So if there are two bombs in the cells adjacent to the current one, return two.
    # If there are none, keep it as 0.

    field = [[0 for i in range(num_cols)] for j in range(num_rows)]

    for bomb_location in bombs:
        (bomb_row, bomb_col) = bomb_location
        field[bomb_row][bomb_col] = -1

        row_range = range(bomb_row - 1, bomb_row + 2)
        col_range = range(bomb_col - 1, bomb_col + 2)

        for row in row_range:
            for col in col_range:
                if row >= 0 and col >= 0 and field[row][col] != -1:
                    field[row][col] += 1

    return field


def most_frequent(nums):
    # return the most frequently occurring element in the list

    count = {}
    max_item = None
    max_count = 0

    for num in nums:
        if num in count:
            count[num] += 1

        else:
            count[num] = 1

        if count[num] > max_count:
            max_count = count[num]
            max_item = num

    return max_item

def unique(s):
#     given a string, return True or False depending on uniqueness of all elements

    s = s.replace(' ','')
    return len(set(s)) == len(s)

def unique_2(s):

    s = s.replace(' ', '')
    characters = set()

    for letter in s:
        if letter in characters:
            return False
        else:
            characters.add(letter)

    return True


def non_repeating(s):

    s = s.replace(' ', '').lower()

    count = {}

    for letter in s:
        if letter in count:
            count[letter] += 1

        else:
            count[letter] = 1


    all_uniqies = []

    result = sorted(count.items(), key = lambda x : x[1])

    print(result)

    for i in result:
        if i[1] == 1:
            all_uniqies.append(i[0])

    return all_uniqies


    # for item in count:
    #     if count[item] == 1:
    #         return item
    #
    # return None

import re

def word_in_text(word, text):
    word = word.lower()
    text = text.lower()
    match = re.search(word, text)

    if match:
        return True
    return False

print(word_in_text('Anya', 'anya went for a walk'))





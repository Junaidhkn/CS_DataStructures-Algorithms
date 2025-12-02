# ---------------------------------------------------------------------
# ---------------------------------------------------------------------
#                             Basics
# ---------------------------------------------------------------------
# ---------------------------------------------------------------------


import numpy as np
import array

my_array = array.array("I", [1, 2, 4, 54])
print("Printing the array using the array package :\n", my_array)

my_array1 = np.array([1, 34, 4, 5, 5, 6], dtype=int)
print("Printing the array using the array package :\n", my_array1)

# When creating an empty array the time and space complexity is constant O(1), but when array is initialized with elements of size of n, its time and space complexity is O(n)

# Insertion operation: When inserting an element in the end of the array its time and space complexity is O(1), where as at the start or any given index its time complexity is O(n) and space complexity is O(1)
my_array.insert(0, 666)
print(my_array)


# Searching an element in an Array - Time complexity is O(n) and space complexity is O(1)
def linear_Search(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i, True
    return -1, False


my_array1 = np.array([1, 34, 4, 5, 6], dtype=int)
print(linear_Search(my_array1, 6))


# Removing the last element from the array is O(1) time complexity, removing any other element from the array is the O(n) time complexity,space complexity would remain same and that is O(1)


# List insertion
def list_insert(lst, index, value):
    if index < 0:
        index = 0
    if index > len(lst):
        index = len(lst)
    lst.append(None)
    for i in range(len(lst) - 1, index, -1):
        lst[i] = lst[i - 1]
    lst[index] = value


lst = [10, 20, 30, 40]
print("List Before the insertion", lst)
list_insert(lst, 2, 99)
print("list after the insertion", lst)
# ---------------------------------------------------------------------
# ---------------------------------------------------------------------
#                             Problems
# ---------------------------------------------------------------------
# ---------------------------------------------------------------------


# Given two integer lists, num1 and num2, of size m and n, respectively , sorted in nondecreasing order.Merge nums1 and nums2 into a single list sorted in nondecreasing order.


def merge_lists(nums1, nums2):
    result = [None] * (len(nums1) + len(nums2))
    p1 = 0
    p2 = 0
    p3 = 0

    # Traverse both lists until the end of either list is reached
    while (p1 < len(nums1)) and (p2 < len(nums2)):
        # If the value at p1 is smaller than the value at p2, store the value at p3 and increment p1 and p3
        if nums1[p1] < nums2[p2]:
            result[p3] = nums1[p1]
            p1 += 1
            p3 += 1
        # Otherwise, store the value at p2 into p3 and increment p2 and p3
        else:
            result[p3] = nums2[p2]
            p2 += 1
            p3 += 1
    # If elements remain in nums1, store them in result
    while p1 < len(nums1):
        result[p3] = nums1[p1]
        p1 += 1
        p3 += 1
    # If elements remain in nums2, store them in result
    while p2 < len(nums2):
        result[p3] = nums2[p2]
        p2 += 1
        p3 += 1
    return result


nums1 = [
    [23, 33, 35, 41, 44, 47, 56, 91, 105],
    [1, 2],
    [1, 1, 1],
    [6],
    [12, 34, 45, 56, 67, 78, 89, 99],
]
nums2 = [[32, 49, 50, 51, 61, 99], [7], [1, 2, 3, 4], [-99, -45], [100]]

# for i in range(len(nums1)):
#     print(i + 1, ".\tFirst list: ", nums1[i])
#     print("\tSecond list: ", nums2[i])
#     print("\tMerged list: ", merge_lists(nums1[i], nums2[i]))
#     print("-" * 25)

# Bubble Sort Algorithm Notes:

# Bubble Sort is a simple comparison-based sorting algorithm.
# It repeatedly steps through the list, compares adjacent items, and swaps them if they are in the wrong order.
# This process continues until no more swaps are needed, meaning the list is sorted.

# Time Complexity:
# - Best Case: O(n) -> When the array is already sorted (with an optimization check)
# - Average Case: O(n^2)
# - Worst Case: O(n^2) -> When the array is sorted in reverse
# Space Complexity: O(1) -> In-place sorting algorithm (no extra space required)

# Stability: Yes (does not change the relative order of equal elements)
# Adaptive: Yes (if modified with a flag to detect swaps)


def bubble_sort(my_list):
    for i in range(len(my_list) -1 ,0,-1):
        for j in range(i):
            print('i :',i,'->\tj :',j, '\tj+1:',j+1)
            print('List before:', my_list)
            print('values under consideration:', my_list[j],'<->',my_list[j+1] )
            if my_list[j] > my_list[j+1]:
                my_list[j], my_list[j + 1] = my_list[j + 1], my_list[j]
                print('Values swapped!!!')
                print(my_list)
    return my_list





print(bubble_sort([5, 3, 8, 4, 2]))



# Example:
# Initial:
# [5, 3, 8, 4, 2]

# Pass 1:
# Compare 5 and 3 → swap → [3, 5, 8, 4, 2]
# Compare 5 and 8 → OK
# Compare 8 and 4 → swap → [3, 5, 4, 8, 2]
# Compare 8 and 2 → swap → [3, 5, 4, 2, 8] ✅

# Pass 2:
# Compare 3 and 5 → OK
# Compare 5 and 4 → swap → [3, 4, 5, 2, 8]
# Compare 5 and 2 → swap → [3, 4, 2, 5, 8] ✅

# Pass 3:
# Compare 3 and 4 → OK
# Compare 4 and 2 → swap → [3, 2, 4, 5, 8] ✅

# Pass 4:
# Compare 3 and 2 → swap → [2, 3, 4, 5, 8] ✅

# Pass 5:
# No swaps → algorithm ends early ⛔

# ✅ Final Sorted Output:
# [2, 3, 4, 5, 8]


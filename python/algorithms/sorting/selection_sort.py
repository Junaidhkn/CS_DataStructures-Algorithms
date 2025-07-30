# --------------------------------------------
# 📘 Selection Sort - Python Notes in Comments
# --------------------------------------------

# Selection Sort is a simple comparison-based sorting algorithm.
# It divides the list into a sorted and an unsorted part.
# The smallest element is repeatedly selected from the unsorted part
# and moved to the beginning (sorted part).

# ❗ Not a stable sorting algorithm by default
# ✅ In-place (no extra space needed)

# Time Complexity:
#   Best case   -> O(n^2)
#   Average case-> O(n^2)
#   Worst case  -> O(n^2)
# Space Complexity: O(1)  (no additional storage)

# Algorithm Steps:
# 1. Start from the first element.
# 2. Find the smallest element in the unsorted part of the list.
# 3. Swap it with the current position.
# 4. Move to the next position and repeat until the list is sorted.

# Example usage:
# Input: [64, 25, 12, 22, 11]
# Step-by-step:
# 1st pass: smallest is 11 -> [11, 25, 12, 22, 64]
# 2nd pass: smallest is 12 -> [11, 12, 25, 22, 64]
# 3rd pass: smallest is 22 -> [11, 12, 22, 25, 64]
# 4th pass: already sorted
# Output: [11, 12, 22, 25, 64]

def selection_sort(arr):
    for i in range(len(arr) - 1):
        min_index = i
        print('i',i)
        for j in range(i+1,len(arr)):
            print('j',j)
            if arr[j] < arr[min_index]:
                min_index = j
        if i != min_index:
          arr[i],arr[min_index] = arr[min_index],arr[i]
    return arr






print(selection_sort([22,24,25,21,1]))
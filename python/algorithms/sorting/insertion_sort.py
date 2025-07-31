# --------------------------------------------
# 📘 Insertion Sort - Python Notes in Comments
# --------------------------------------------

# Insertion Sort is a simple sorting algorithm that builds the final sorted list one element at a time.
# It is much like sorting playing cards in your hands.

# ✅ Stable sorting algorithm
# ✅ In-place sorting (does not require extra space)
# ❗ Inefficient for large datasets

# Time Complexity:
#   Best Case (already sorted): O(n)        ← Only comparisons, no swaps
#   Average Case:              O(n^2)
#   Worst Case (reverse sorted): O(n^2)
# Space Complexity:            O(1)

# 🔄 Algorithm Steps:
# 1. Start from the second element (index 1), assume the first element is already sorted.
# 2. Compare the current element (key) with the elements in the sorted part.
# 3. Shift all elements greater than the key to one position ahead to make space.
# 4. Insert the key at its correct position.
# 5. Repeat for all elements in the list.

# 🔍 Example usage and steps:
# Input: [5, 3, 4, 1, 2]
# Step-by-step:
# i = 1, key = 3 → shift 5 → [5, 5, 4, 1, 2] → insert 3 → [3, 5, 4, 1, 2]
# i = 2, key = 4 → shift 5 → [3, 5, 5, 1, 2] → insert 4 → [3, 4, 5, 1, 2]
# i = 3, key = 1 → shift 5, 4, 3 → [3, 4, 5, 5, 2] → insert 1 → [1, 3, 4, 5, 2]
# i = 4, key = 2 → shift 5, 4, 3 → [1, 3, 4, 5, 5] → insert 2 → [1, 2, 3, 4, 5]



def insertion_sort(arr):
    for i in range(1,len(arr)):
        key = arr[i]
        j = i-1
        while key < arr[j] and j >= 0:
            arr[j],arr[j+1] = arr[j+1],arr[j]
            j-=1
    return arr

print(insertion_sort([5, 3, 4, 1, 2]))  # Output: [1, 2, 3, 4, 5]
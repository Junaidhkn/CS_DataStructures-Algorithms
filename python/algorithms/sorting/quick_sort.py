# ----------------------------------------
# 🧠 QUICK SORT – DETAILED NOTES
# ----------------------------------------

# ✅ DEFINITION:
# Quick Sort is a **Divide and Conquer** sorting algorithm.
# It works by selecting a 'pivot' element from the array,
# and partitioning the other elements into two sub-arrays:
# one with elements less than the pivot and one with elements greater.
# The process is then recursively applied to the sub-arrays.

# 📌 MAIN STEPS IN QUICK SORT:
# 1. Choose a pivot element from the array.
# 2. Partition the array:
#    - Elements smaller than pivot go to the left.
#    - Elements greater than or equal to pivot go to the right.
# 3. Recursively apply the above steps to the left and right sub-arrays.
# 4. Combine the results to form the sorted array.

# 📌 COMMON STRATEGIES TO CHOOSE PIVOT:
# - First element
# - Last element (common in implementations)
# - Random element (to reduce chances of worst-case)
# - Median of first, middle, and last (median-of-three heuristic)

# 📉 TIME COMPLEXITY:
# - Best Case:      O(n log n) → when the pivot divides the array evenly
# - Average Case:   O(n log n)
# - Worst Case:     O(n²) → occurs when the smallest or largest element is always chosen as the pivot (unbalanced partition)

# 🧠 SPACE COMPLEXITY:
# - In-place version: O(log n) for recursive stack space
# - Non-in-place version (using extra arrays): O(n) due to storage of left and right partitions

# 🔄 STABILITY:
# - Quick Sort is **NOT a stable** sorting algorithm.
#   Equal elements may change their relative order during partitioning.
#   Stability can be achieved with modified versions (but at the cost of performance/memory).

# ⚡ ADVANTAGES OF QUICK SORT:
# - Very fast in practice for large datasets.
# - Outperforms many other algorithms like Bubble, Insertion, and Selection sort.
# - In-place version requires little additional memory.

# ⚠️ DISADVANTAGES:
# - Not stable by default.
# - Worst-case time complexity is O(n²), though rare if pivot is chosen well.
# - Recursive implementation can cause stack overflow on large lists without optimization.

# 💡 OPTIMIZATIONS:
# - Use "median-of-three" pivot selection to avoid worst-case partitioning.
# - Tail recursion optimization can reduce stack usage.
# - For small subarrays (e.g., <10 elements), switch to Insertion Sort (hybrid approach used in Timsort).

# ✅ COMMON APPLICATIONS:
# - Used in system libraries (like C's qsort() for non-stable sorting).
# - Efficient for large datasets where memory usage is a concern.
# - Good default choice for general-purpose, fast, non-stable sorting.

# 🚀 FUN FACT:
# - Quick Sort was invented by Tony Hoare in 1959.
# - Despite its worst-case time complexity, it's often faster than other O(n log n) algorithms like Merge Sort due to better cache performance and low constant factors.


def swap(arr, i, j):
    arr[i], arr[j] = arr[j], arr[i]

def pivot(arr,pivot_index,end_index):
    swap_index = pivot_index

    for i in range(pivot_index + 1, end_index + 1):
        if arr[i] < arr[pivot_index]:
            swap_index += 1
            swap(arr,swap_index,i)
    swap(arr,pivot_index,swap_index)

    return swap_index

def quick_sort(arr,left,right):
    if left < right:
        pivot_index = pivot(arr ,left, right)
        quick_sort(arr, left ,pivot_index - 1)
        quick_sort(arr,pivot_index + 1, right)
    return arr




print(quick_sort([5, 3, 4, 1, 2 ,23,34,53,122],0,len([5, 3, 4, 1, 2 ,23,34,53,122])-1))












# ----------------------- Merge Sort - Python Notes -----------------------

# Merge Sort is a Divide and Conquer algorithm.
# It divides the input array into two halves, recursively sorts each half,
# and then merges the two sorted halves to produce the sorted array.

# ----------------------- Why Merge Sort? -----------------------
# Merge Sort is more efficient than Bubble Sort, Selection Sort, and Insertion Sort
# for large datasets due to its better time complexity.
# It guarantees O(n log n) time complexity in all cases (worst, best, average).

# ----------------------- Steps of Merge Sort -----------------------
# 1. Divide: Split the array into two halves.
# 2. Conquer: Recursively sort both halves.
# 3. Combine: Merge the two sorted halves into a single sorted array.

# ----------------------- Key Properties -----------------------
# - Time Complexity:
#     - Best Case: O(n log n)
#     - Average Case: O(n log n)
#     - Worst Case: O(n log n)
# - Space Complexity: O(n) due to the temporary arrays used during merging.
# - Stable Sort: Yes (maintains the relative order of equal elements).
# - Not In-Place: Requires extra space for merging.

# ----------------------- Example -----------------------
# Input: [6, 3, 9, 5, 2, 8]
# Step 1: Divide → [6, 3, 9] and [5, 2, 8]
# Step 2: Divide again → [6], [3, 9] → [3], [9] → merge → [3, 9] → merge with 6 → [3, 6, 9]
#         and [5], [2, 8] → [2], [8] → merge → [2, 8] → merge with 5 → [2, 5, 8]
# Step 3: Merge [3, 6, 9] and [2, 5, 8] → [2, 3, 5, 6, 8, 9]
# Output: [2, 3, 5, 6, 8, 9]

# ----------------------- Optimal Use Cases -----------------------
# - When working with large datasets that don’t fit into memory (external sorting).
# - When stable sorting is required.
# - When you want consistent performance (no worst-case degradation).

# ----------------------- Drawbacks -----------------------
# - High space consumption (O(n) extra space).
# - Slower on small datasets compared to Insertion Sort due to overhead.

# ------------------------------------------------------------------



def merge(list1,list2):
    combined =[]
    i = 0
    j = 0
    while i < len(list1) and j < len(list2):
        if list1[i] < list2[j]:
            combined.append(list1[i])
            i += 1
        else:
            combined.append(list2[j])
            j += 1
    while i < len(list1):
        combined.append(list1[i])
        i += 1
    while j < len(list2):
        combined.append(list2[j])
        j += 1
    return combined


print(merge([2, 14, 15, 365], [3, 223, 442]))



















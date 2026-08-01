"""

# Kadane's Algorithm (DSA Pattern)

---

# What is Kadane's Algorithm?

Kadane's Algorithm is a **greedy algorithm** used to find the **maximum (or minimum) sum of a contiguous subarray** in **linear time**.

Instead of checking every possible subarray (which takes **O(n²)** time), Kadane's Algorithm determines at every index:

> **"Is it better to continue the current subarray or start a new one?"**

This simple decision allows it to solve the problem in a single pass.

---

# The Core Idea

At every element, you have only **two choices**:

1. **Extend the current subarray**
2. **Start a new subarray from the current element**

Choose whichever gives the larger sum.

Mathematically:

```text
current_sum = max(nums[i], current_sum + nums[i])
```

Then update the answer:

```text
max_sum = max(max_sum, current_sum)
```

The algorithm repeats this process until the end of the array.

---

# When is Kadane's Algorithm Useful?

Kadane's Algorithm is useful whenever a problem asks about a **contiguous subarray** and involves **optimizing a cumulative value**, such as:

- Maximum sum
- Minimum sum
- Maximum profit
- Maximum score
- Largest gain
- Largest difference
- Best continuous segment

It is specifically designed for **contiguous** ranges.

---

# How to Recognize When to Apply Kadane's Algorithm

Look for these clues in the problem statement.

## 1. The word "contiguous"

Examples:

- Contiguous subarray
- Consecutive elements
- Continuous segment
- Continuous sequence

Example:

> Find the maximum sum of a contiguous subarray.

Immediately think:

> **Kadane's Algorithm**

---

## 2. Optimize a Running Sum

The problem asks for:

- Largest sum
- Smallest sum
- Maximum score
- Minimum cost
- Maximum profit
- Maximum gain

over a **continuous section**.

---

## 3. Every Element is Used at Most Once

Kadane scans from left to right.

Each element is processed once.

If the problem naturally fits a single pass, Kadane is often applicable.

---

## 4. Previous Sum Affects Current Decision

Ask yourself:

> Does the previous accumulated value help me?

If yes, Kadane may work.

---

## 5. Local Decision Leads to Global Answer

Kadane is a **Greedy Algorithm**.

At each index it decides:

```text
Continue
or
Restart
```

without reconsidering previous choices.

---

# When NOT to Use Kadane

Kadane is **not** suitable when:

- Elements are **not contiguous**
- The problem asks for **subsets** instead of subarrays
- Multiple disjoint segments are allowed
- The window size is fixed
- The problem requires considering many future possibilities (traditional Dynamic Programming may be needed)

---



# Why Does Kadane Work?

Suppose your running sum becomes negative.

Example:

```text
Current Sum = -8
Next Number = 6
```

Continuing gives:

```text
-8 + 6 = -2
```

Starting fresh gives:

```text
6
```

Clearly:

```text
6 > -2
```

A negative running sum only makes future sums smaller.

Therefore:

> If the running sum is worse than starting over, discard it.

This greedy observation is the key to Kadane's Algorithm.

---

# Time Complexity

Only one traversal.

```text
O(n)
```

---

# Space Complexity

Only two variables are needed.

```text
O(1)
```

---

# Benefits of Kadane's Algorithm

- Simple implementation
- Optimal **O(n)** runtime
- Constant **O(1)** extra space
- Eliminates unnecessary subarray comparisons
- Easy to adapt for related optimization problems
- Forms the basis for several advanced interview questions

---

# Common Problems Solved Using Kadane

## 1. Maximum Subarray Sum

The classic Kadane problem.

**Example**

> Find the maximum sum of any contiguous subarray.

---

## 2. Minimum Subarray Sum

Replace `max()` with `min()`.

Useful in:

- Minimum loss
- Minimum cost
- Minimum temperature interval

---

## 3. Maximum Circular Subarray Sum

The array wraps around.

Example:

```text
[5, -3, 5]
```

Solution combines:

- Standard Kadane
- Total array sum
- Minimum subarray sum

---

## 4. Best Time to Buy and Sell Stock

Convert prices into daily differences:

```text
difference[i] = prices[i] - prices[i - 1]
```

Then finding the maximum profit becomes finding the maximum subarray sum.

---

## 5. Maximum Sum Rectangle (2D Kadane)

Compress rows into a 1D array and run Kadane repeatedly.

Time Complexity:

```text
O(rows² × cols)
```

---

## 6. Maximum Product Subarray

A variation of Kadane.

Track both:

- Maximum product
- Minimum product

because multiplying by a negative number swaps them.

---

## 7. Flip Binary String

Convert:

```text
0 → +1
1 → -1
```

Run Kadane to find the best segment to flip.

---

## 8. Maximum Difference Between Prefixes

Many interval optimization problems reduce to maintaining a running value and repeatedly making the "continue or restart" decision.

---

# General Kadane Template

```python
def kadane(nums):
    current = nums[0]
    best = nums[0]

    for i in range(1, len(nums)):
        current = max(nums[i], current + nums[i])
        best = max(best, current)

    return best
```

---

# Minimum Subarray Template

```python
def minimum_subarray(nums):
    current = nums[0]
    best = nums[0]

    for i in range(1, len(nums)):
        current = min(nums[i], current + nums[i])
        best = min(best, current)

    return best
```

---

# How Kadane Compares to Other DSA Patterns

| Pattern | Main Goal | Typical Clue |
|----------|-----------|--------------|
| Sliding Window | Fixed or expandable contiguous window | "Longest", "Smallest", "At most K", "Exactly K" |
| Prefix Sum | Fast range-sum queries | Many range sum queries |
| Two Pointers | Two moving indices | Sorted arrays, pairs, partitions |
| Dynamic Programming | Overlapping subproblems | Multiple state transitions |
| **Kadane's Algorithm** | Maximum or minimum value over a contiguous subarray | "Maximum/minimum contiguous subarray", "Best continuous segment", "Largest gain" |

---

# Recognition Checklist

Ask yourself:

- Is the answer based on a **contiguous subarray**?
- Is the goal to **maximize or minimize** a cumulative value?
- At each position, can I choose between:
  - Continuing the current subarray?
  - Starting a new one?
- Can a **single left-to-right traversal** solve the problem?

If the answer is **yes** to most of these questions, Kadane's Algorithm is likely the correct pattern.

---

# One-Sentence Summary

> **Kadane's Algorithm is a greedy, linear-time technique for finding the maximum or minimum value of a contiguous subarray by deciding at every element whether to extend the current subarray or start a new one.**

"""

##! Question 1 : Maximum Subarray
"""

Given an integer array nums, find the subarray with the largest sum, and return its sum.

Example 1:

Input: nums = [-2,1,-3,4,-1,2,1,-5,4]
Output: 6
Explanation: The subarray [4,-1,2,1] has the largest sum 6.

Example 2:

Input: nums = [1]
Output: 1
Explanation: The subarray [1] has the largest sum 1.

Example 3:

Input: nums = [5,4,-1,7,8]
Output: 23
Explanation: The subarray [5,4,-1,7,8] has the largest sum 23.
 

Constraints:

1 <= nums.length <= 105
-104 <= nums[i] <= 104
 

Follow up: If you have figured out the O(n) solution, try coding another solution using the divide and conquer approach, which is more subtle.

"""


# Brute Force Approach
def max_sum_subarray_bruteforce(nums):
    n = len(nums)
    max_sum = float("-inf")

    for start in range(n):
        current_sum = 0

        for end in range(start, n):
            current_sum += nums[end]
            max_sum = max(max_sum, current_sum)

    return max_sum


# Time complexity : O(n²)
# Space Complexity : O(1)


# Optimal Approach
def max_sum_subarray_optimal(nums):
    best_ending = nums[0]
    answer = nums[0]

    for i in range(1, len(nums)):
        best_ending = max(best_ending + nums[i], nums[i])
        answer = max(answer, best_ending)

    return answer


print(
    "printing solution :\n",
    max_sum_subarray_optimal([-2, 1, -3, 4, -1, 2, 1, -5, 4]),
)
# Time complexity : O(n)
# Space Complexity : O(1)


##! Question 2 : Minimum Sum Subarray


"""

Given an array arr[], find the sub-array containing at least one number which has the minimum sum and return its sum.

Examples :

Input: arr[] = {3,-4, 2,-3,-1, 7,-5}
Output: -6
Explanation: The subarray is {-4,2,-3,-1} = -6
Input: arr[] = {2, 6, 8, 1, 4}
Output: 1
Explanation: The sub-array is {1} = 1
Constraints:
1 ≤ N ≤ 10^6
-10^7 ≤ A[i] ≤ 10^7


"""


# Brute Force Approach
def min_sum_subarray_bruteforce(nums):
    n = len(nums)
    min_sum = float("inf")

    for start in range(n):
        current_sum = 0

        for end in range(start, n):
            current_sum += nums[end]
            min_sum = min(min_sum, current_sum)

    return min_sum


# Time complexity : O(n²)
# Space Complexity : O(1)


# Optimal Approach
def min_sum_subarray_optimal(nums):
    best_ending = nums[0]
    answer = nums[0]

    for i in range(1, len(nums)):
        best_ending = min(best_ending + nums[i], nums[i])
        answer = min(answer, best_ending)

    return answer


# Time complexity : O(n)
# Space Complexity :  O(1)

##! Question 3 : Maximum Product Subarray


"""

Given an integer array nums, find a subarray that has the largest product, and return the product.

The test cases are generated so that the answer will fit in a 32-bit integer.

Note that the product of an array with a single element is the value of that element.


Example 1:

Input: nums = [2,3,-2,4]
Output: 6
Explanation: [2,3] has the largest product 6.

Example 2:

Input: nums = [-2,0,-1]
Output: 0
Explanation: The result cannot be 2, because [-2,-1] is not a subarray.
 

Constraints:

1 <= nums.length <= 2 * 104
-10 <= nums[i] <= 10
The product of any subarray of nums is guaranteed to fit in a 32-bit integer.

"""


# Brute Force Approach
def max_product_subarray_bruteforce(nums):
    n = len(nums)
    answer = float("-inf")

    for start in range(n):
        current_product = 1

        for end in range(start, n):
            current_product *= nums[end]
            answer = max(answer, current_product)

    return answer


# Time complexity : O(n²)
# Space Complexity : O(1)


# Optimal Approach
def max_product_subarray_optimal(nums):
    max_ending = nums[0]
    min_ending = nums[0]
    answer = nums[0]
    n = len(nums)

    for i in range(1, n):
        num = nums[i]

        temp_max = max(
            num,
            max_ending * num,
            min_ending * num,
        )

        temp_min = min(
            num,
            max_ending * num,
            min_ending * num,
        )

        max_ending = temp_max
        min_ending = temp_min

        answer = max(answer, max_ending)

    return answer


# Time complexity : O(n)
# Space Complexity : O(1)


## If asked to return the subarray along with the maximum


def max_product_subarray_with_indices(nums):
    max_ending = nums[0]
    min_ending = nums[0]
    answer = nums[0]
    n = len(nums)

    max_start = 0
    min_start = 0
    best_start = 0
    best_end = 0

    for i in range(1, n):
        num = nums[i]

        c1 = num
        c2 = max_ending * num
        c3 = min_ending * num

        temp_max = max(c1, c2, c3)
        if temp_max == c1:
            new_max_start = i
        elif temp_max == c2:
            new_max_start = max_start
        else:
            new_max_start = min_start

        temp_min = min(c1, c2, c3)
        if temp_min == c1:
            new_min_start = i
        elif temp_min == c2:
            new_min_start = max_start
        else:
            new_min_start = min_start

        max_ending, min_ending = temp_max, temp_min
        max_start, min_start = new_max_start, new_min_start

        if max_ending > answer:
            answer = max_ending
            best_start = max_start
            best_end = i

    return answer, nums[best_start : best_end + 1]


# Time complexity : O(n)
# Space Complexity : O(1)

##! Question 4 : Maximum Subarray Sum with One Deletion

"""
Given an array of integers, return the maximum sum for a non-empty subarray (contiguous elements) with at most one element deletion. In other words, you want to choose a subarray and optionally delete one element from it so that there is still at least one element left and the sum of the remaining elements is maximum possible.

Note that the subarray needs to be non-empty after deleting one element.

Example 1:

Input: arr = [1,-2,0,3]
Output: 4
Explanation: Because we can choose [1, -2, 0, 3] and drop -2, thus the subarray [1, 0, 3] becomes the maximum value.

Example 2:

Input: arr = [1,-2,-2,3]
Output: 3
Explanation: We just choose [3] and it's the maximum sum.

Example 3:

Input: arr = [-1,-1,-1,-1]
Output: -1
Explanation: The final subarray needs to be non-empty. You can't choose [-1] and delete -1 from it, then get an empty subarray to make the sum equals to 0.
 

Constraints:

1 <= arr.length <= 105
-104 <= arr[i] <= 104

"""

# Brute Force Approach


# Time complexity :
# Space Complexity :

# Optimal Approach


# Time complexity :
# Space Complexity :
##! Question 5 : Maximum Absolute Sum of Any Subarray

"""

You are given an integer array nums. The absolute sum of a subarray [numsl, numsl+1, ..., numsr-1, numsr] is abs(numsl + numsl+1 + ... + numsr-1 + numsr).

Return the maximum absolute sum of any (possibly empty) subarray of nums.

Note that abs(x) is defined as follows:

If x is a negative integer, then abs(x) = -x.
If x is a non-negative integer, then abs(x) = x.
 

Example 1:

Input: nums = [1,-3,2,3,-4]
Output: 5
Explanation: The subarray [2,3] has absolute sum = abs(2+3) = abs(5) = 5.

Example 2:

Input: nums = [2,-5,1,-4,3,-2]
Output: 8
Explanation: The subarray [-5,1,-4] has absolute sum = abs(-5+1-4) = abs(-8) = 8.
 

Constraints:

1 <= nums.length <= 105
-104 <= nums[i] <= 104

"""


# Brute Force Approach


# Time complexity :
# Space Complexity :

# Optimal Approach


# Time complexity :
# Space Complexity :

##! Question 6 :   Maximum Sum Circular Subarray
"""

Given a circular integer array nums of length n, return the maximum possible sum of a non-empty subarray of nums.

A circular array means the end of the array connects to the beginning of the array. Formally, the next element of nums[i] is nums[(i + 1) % n] and the previous element of nums[i] is nums[(i - 1 + n) % n].

A subarray may only include each element of the fixed buffer nums at most once. Formally, for a subarray nums[i], nums[i + 1], ..., nums[j], there does not exist i <= k1, k2 <= j with k1 % n == k2 % n.

 

Example 1:

Input: nums = [1,-2,3,-2]
Output: 3
Explanation: Subarray [3] has maximum sum 3.

Example 2:

Input: nums = [5,-3,5]
Output: 10
Explanation: Subarray [5,5] has maximum sum 5 + 5 = 10.

Example 3:

Input: nums = [-3,-2,-3]
Output: -2
Explanation: Subarray [-2] has maximum sum -2.
 

Constraints:

n == nums.length
1 <= n <= 3 * 104
-3 * 104 <= nums[i] <= 3 * 104

"""
# Brute Force Approach


# Time complexity :
# Space Complexity :

# Optimal Approach


# Time complexity :
# Space Complexity :

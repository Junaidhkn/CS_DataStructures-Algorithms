"""
Sliding Window Pattern: Explained

1. Definition
The Sliding Window is a technique used to solve problems that involve contiguous segments or subarrays of a given array or string.
It involves maintaining a window (a range or segment) defined by two pointers(usually start and end) that slide over the input data.
The window can either be fixed size or variable size.
Instead of recalculating everything for every window, it efficiently updates results as the window moves forward by adding the new element and removing the old element.

2. Where it can apply?
The sliding window pattern applies mainly when:
You need to find something about subarrays or substrings of contiguous elements.
You want to calculate or track a property over a range that moves forward step-by-step.
Problems involving sums, counts, average, maximum/minimum,atmost k, atleast k or exactly k, frequency of elements inside a window.
Fixed-size windows (e.g., "find max sum of subarray of size k")
Variable-size windows where the window expands or shrinks based on some condition
(e.g., "smallest subarray with sum >= target")


3. How to apply the Sliding Window pattern?
There are generally two types of sliding windows:

a) Fixed-Size Sliding Window
Window size is fixed (say k).
Move the window from the start to the end by sliding one element at a time.
For each move, update the result by adding the new element and removing the element that slides out.
Example steps:
Initialize sum, frequency map, or required tracking variable for the first k elements.
Slide the window by one element forward:
->Remove the leftmost element from the window.
->Add the new rightmost element.
Update your result or answer for the current window.

b) Variable-Size Sliding Window
Window size changes dynamically based on a condition.
Use two pointers: start and end.
Move end forward to expand the window until a condition is met.
Move start forward to shrink the window to satisfy constraints or optimize the solution.
Example steps:
Initialize start and end to 0.
Expand end to include new elements and update your tracking variables.
When the condition is met (e.g., window sum >= target), try shrinking the window by moving start forward while maintaining the condition.
Keep track of the best (minimum, maximum, count, etc.) window found so far.

4. How to check which type of questions sliding window can apply to?
Look for these clues in the problem:
The problem deals with subarrays or substrings.
You need to find something like:
-> Maximum/minimum sum of a subarray of size k.
-> Longest/shortest substring/subarray meeting some criteria.
-> Count of distinct elements or frequencies in a substring/subarray.
-> Any problem involving "continuous" or "contiguous" segments.
The problem hints at "window", "substring", "subarray", or "contiguous".
Naive solution would involve nested loops iterating over all subarrays; sliding window offers optimization.
Constraints are large (like 10^5 elements) where brute force O(n^2) is not feasible.

5. Benefits of Sliding Window
Efficiency: Reduces time complexity from O(n^2) (nested loops) to O(n).
Simplicity: Easy to implement once understood.
Memory: Uses constant or linear extra space, depending on implementation.
Versatility: Works for fixed-size and variable-size problems.
Ideal for real-time streaming data and online algorithms where data is processed
sequentially.

"""

## ! Question 1: Max Sum Subarray of size K

"""

Given an array of integers arr[] and a number k. Return the maximum sum of a subarray of size k.
Note: A subarray is a contiguous part of any given array.

Examples:

Input: arr[] = [100, 200, 300, 400], k = 2
Output: 700
Explanation: arr2 + arr3 = 700, which is maximum.

Input: arr[] = [1, 4, 2, 10, 23, 3, 1, 0, 20], k = 4
Output: 39
Explanation: arr1 + arr2 + arr3 + arr4 = 39, which is maximum.

Input: arr[] = [100, 200, 300, 400], k = 1
Output: 400
Explanation: arr3 = 400, which is maximum.

Constraints:
1 ≤ arr.size() ≤ 106
0 ≤ arr[i] ≤ 106
1 ≤ k ≤ arr.size()

"""
# Brute Force


def MaxSumSubarrayBruteForce(nums: list[int], k: int):
    n = len(nums)
    maximum = float("-inf")
    for i in range(n - k + 1):
        current_sum = 0
        for j in range(i, i + k):
            current_sum += nums[j]
        maximum = max(maximum, current_sum)

    return maximum


result = MaxSumSubarrayBruteForce([1, 4, 2, 10, 23, 3, 1, 0, 20], 4)
print(" BF solution for question 1:\n", result)

# Time complexity : O(n^2) Space Complexity : O(1)


# Optimal Solution
def MaxSumSubarray(nums, k):
    n = len(nums)
    current_sum = 0
    for i in range(k):  # Or current_sum = sum(arr[:k])
        current_sum += nums[i]
    maximum = current_sum

    for j in range(k, n):
        current_sum = current_sum + nums[j] - nums[j - k]
        maximum = max(current_sum, maximum)

    return maximum


result = MaxSumSubarray([1, 4, 2, 10, 23, 3, 1, 0, 20], 4)
print("Optimized solution for question 1:\n", result)

# Time complexity : O(n) Space Complexity : O(1)


## ! Question 2: Minimum size subarray sum


"""
Given an array of positive integers nums and a positive integer target, return the minimal length of a subarray whose sum is greater than or equal to target. If there is no such subarray, return 0 instead.

Example 1:

Input: target = 7, nums = [2,3,1,2,4,3]
Output: 2
Explanation: The subarray [4,3] has the minimal length under the problem constraint.

Example 2:

Input: target = 4, nums = [1,4,4]
Output: 1

Example 3:

Input: target = 11, nums = [1,1,1,1,1,1,1,1]
Output: 0
 

Constraints:

1 <= target <= 109
1 <= nums.length <= 105
1 <= nums[i] <= 104
 

Follow up: If you have figured out the O(n) solution, try coding another solution of which the time complexity is O(n log(n)).
"""

# Brute Force solution:


def minSubArrayLenBF(target, nums):
    n = len(nums)
    min_length = float("inf")
    for i in range(n):
        current_sum = 0
        for j in range(i, n):
            current_sum += nums[j]
            if current_sum >= target:
                min_length = min(min_length, j - i + 1)
                break

    return 0 if min_length == float("inf") else min_length


print(
    "printing BF solution for minsubarraylen:\n",
    minSubArrayLenBF(7, [2, 3, 1, 2, 4, 3]),
)


# Sliding window : O(n) solution
def minSubArrayLen(target, nums):
    left = 0
    curr_sum = 0
    min_len = float("inf")
    n = len(nums)

    for right in range(n):
        curr_sum += nums[right]

        while curr_sum >= target:
            min_len = min(min_len, right - left + 1)
            curr_sum -= nums[left]
            left += 1

    return 0 if min_len == float("inf") else min_len


print(
    "printing SW solution for minsubarraylen:\n",
    minSubArrayLen(7, [2, 3, 1, 2, 4, 3]),
)

# Time Complexity : O(n)
# Space Complexity : O(1)


## ! Question 3: Longest Substring with K Uniques
"""
You are given a string s consisting only lowercase alphabets and an integer k. Your task is to find the length of the longest substring that contains exactly k distinct characters.

Note : If no such substring exists, return -1. 

Examples:

Input: s = "aabacbebebe", k = 3
Output: 7
Explanation: The longest substring with exactly 3 distinct characters is "cbebebe", which includes 'c', 'b', and 'e'.

Input: s = "aaaa", k = 2
Output: -1
Explanation: There's no substring with 2 distinct characters.

Input: s = "aabaaab", k = 2
Output: 7
Explanation: The entire string "aabaaab" has exactly 2 unique characters 'a' and 'b', making it the longest valid substring.

Constraints:
1 ≤ s.size() ≤ 105
1 ≤ k ≤ 26

"""


# Brute Force Approach
def longestKSubstr(s, k):
    n = len(s)
    longest = -1

    for i in range(n):
        distinct = set()

        for j in range(i, n):
            distinct.add(s[j])

            if len(distinct) == k:
                longest = max(longest, j - i + 1)

            elif len(distinct) > k:
                break

    return longest


# Time Complexity : O(n^2) and Space Complexity : O(1)


# Optimal Sliding Window Pattern
def longestKSubstrOptimal(s, k):
    left = 0
    longest = -1
    freq = {}

    for right in range(len(s)):
        freq[s[right]] = freq.get(s[right], 0) + 1

        while len(freq) > k:
            freq[s[left]] -= 1

            if freq[s[left]] == 0:
                del freq[s[left]]

            left += 1

        if len(freq) == k:
            longest = max(longest, right - left + 1)

    return longest


# Time Complexity : O(n) and Space Complexity : O(1)

## ! Question 4: Fruit Into Baskets
"""
You are visiting a farm that has a single row of fruit trees arranged from left to right. The trees are represented by an integer array fruits where fruits[i] is the type of fruit the ith tree produces.

You want to collect as much fruit as possible. However, the owner has some strict rules that you must follow:

You only have two baskets, and each basket can only hold a single type of fruit. There is no limit on the amount of fruit each basket can hold.
Starting from any tree of your choice, you must pick exactly one fruit from every tree (including the start tree) while moving to the right. The picked fruits must fit in one of your baskets.
Once you reach a tree with fruit that cannot fit in your baskets, you must stop.
Given the integer array fruits, return the maximum number of fruits you can pick.

 

Example 1:

Input: fruits = [1,2,1]
Output: 3
Explanation: We can pick from all 3 trees.

Example 2:

Input: fruits = [0,1,2,2]
Output: 3
Explanation: We can pick from trees [1,2,2].
If we had started at the first tree, we would only pick from trees [0,1].

Example 3:

Input: fruits = [1,2,3,2,2]
Output: 4
Explanation: We can pick from trees [2,3,2,2].
If we had started at the first tree, we would only pick from trees [1,2].
 

Constraints:

1 <= fruits.length <= 105
0 <= fruits[i] < fruits.length

"""


## ! Question 5: Longest substring without repeating characters


"""
Given a string s, find the length of the longest substring without duplicate characters.

Example 1:

Input: s = "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3. Note that "bca" and "cab" are also correct answers.

Example 2:

Input: s = "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.

Example 3:

Input: s = "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3.
Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.
 

Constraints:

0 <= s.length <= 5 * 104
s consists of English letters, digits, symbols and spaces.
"""


def longestSubstring(s):
    seen = set()
    left = 0
    max_length = 0

    for right in range(len(s)):
        while s[right] in seen:
            seen.remove(s[left])
            left += 1
        seen.add(s[right])
        max_length = max(max_length, right - left + 1)

    return max_length


# Time Complexity: O(n)
# Space Complexity: O(min(n, charset))


# print("printing longest substring", longestSubstring("wpwqewkew"))


## ! Question 6: Maximum sum of distinct subarrays with length K
"""
You are given an integer array nums and an integer k. Find the maximum subarray sum of all the subarrays of nums that meet the following conditions:

The length of the subarray is k, and
All the elements of the subarray are distinct.

Return the maximum subarray sum of all the subarrays that meet the conditions. If no subarray meets the conditions, return 0.

A subarray is a contiguous non-empty sequence of elements within an array.

Example 1:

Input: nums = [1,5,4,2,9,9,9], k = 3
Output: 15
Explanation: The subarrays of nums with length 3 are:
- [1,5,4] which meets the requirements and has a sum of 10.
- [5,4,2] which meets the requirements and has a sum of 11.
- [4,2,9] which meets the requirements and has a sum of 15.
- [2,9,9] which does not meet the requirements because the element 9 is repeated.
- [9,9,9] which does not meet the requirements because the element 9 is repeated.
We return 15 because it is the maximum subarray sum of all the subarrays that meet the conditions

Example 2:

Input: nums = [4,4,4], k = 3
Output: 0
Explanation: The subarrays of nums with length 3 are:
- [4,4,4] which does not meet the requirements because the element 4 is repeated.
We return 0 because no subarrays meet the conditions.
 

Constraints: 

1 <= k <= nums.length <= 105
1 <= nums[i] <= 105
"""


# Brute force approach
def maximumSubarraySumBrute(nums, k):
    n = len(nums)
    max_sum = 0

    for i in range(n - k + 1):
        valid = True
        for j in range(i, i + k):
            for x in range(j + 1, i + k):
                if nums[j] == nums[x]:
                    valid = False
                    break
            if not valid:
                break

        if valid:
            curr_sum = 0
            for j in range(i, i + k):
                curr_sum += nums[j]
            max_sum = max(max_sum, curr_sum)

    return max_sum


# Time Complexity: O(n* k^2)
# Space Complexity: O(1)


# Brute force approach using set
def maximumSubarraySumBruteSET(nums, k):
    n = len(nums)
    max_sum = 0

    for i in range(n - k + 1):
        seen = set()
        curr_sum = 0
        valid = True

        for j in range(i, i + k):
            if nums[j] in seen:
                valid = False
                break
            seen.add(nums[j])
            curr_sum += nums[j]

        if valid:
            max_sum = max(max_sum, curr_sum)

    return max_sum


# time complexity: O(n * k)
# Space complexity: O(k)

# result = maximumSubarraySumBrute([1, 5, 4, 4, 6, 7, 9, 9, 9], 3)
# print("priting brute force result", result)


# Using Hash Map
def maxSubarraySum(nums, k):
    left = 0
    curr_sum = 0
    max_sum = 0
    freq = {}

    for right in range(len(nums)):
        freq[nums[right]] = freq.get(nums[right], 0) + 1
        curr_sum += nums[right]
        while freq[nums[right]] > 1:
            freq[nums[left]] -= 1
            curr_sum -= nums[left]
            if freq[nums[left]] == 0:
                del freq[nums[left]]
            left += 1
        if right - left + 1 > k:
            freq[nums[left]] -= 1
            curr_sum -= nums[left]
            if freq[nums[left]] == 0:
                del freq[nums[left]]
            left += 1
        if right - left + 1 == k:
            max_sum = max(max_sum, curr_sum)

    return max_sum


# Using Hash-set solution
def maximumSubarraySum(nums, k):
    window = set()
    left = 0
    current_sum = 0
    max_sum = 0

    for right in range(len(nums)):
        while nums[right] in window:
            window.remove(nums[left])
            current_sum -= nums[left]
            left += 1
        window.add(nums[right])
        current_sum += nums[right]
        if right - left + 1 == k:
            max_sum = max(max_sum, current_sum)
            window.remove(nums[left])
            current_sum -= nums[left]
            left += 1

    return max_sum


# print("solution for Question 1: \n", maximumSubarraySum([1, 5, 4, 2, 9, 9, 9], 3))


# Time complexity : O(n)
# Space Complexity : O(k)

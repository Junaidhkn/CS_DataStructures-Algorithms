"""
1. What is the Prefix Sum Pattern?
The Prefix Sum of an array is a technique where you create a new array (or use a data structure) to store cumulative sums of elements from the start up to each index. Formally, for an array arr[] of size n, its prefix sum array prefix[] is defined as:

prefix[i] = arr[0]+arr[1]+...+arr[i]
for 0≤i<n0

2. Why use Prefix Sum?
Prefix sums help quickly compute the sum of elements in any contiguous subarray in     O(1) time after an O(n) preprocessing step.
Without prefix sums:Sum of elements from index i to j is computed by looping from i to j, which is O(j - i + 1).
With prefix sums: Sum of elements from index i to j is:
sum(i,j)=prefix[j]−prefix[i−1]. (i>0)
or simply
prefix[j] (i=0)
which is O(1).

3. How to Compute Prefix Sum?
Given an array arr of size n:

int[] prefix = new int[n];
prefix[0] = arr[0];
for (int i = 1; i < n; i++) {
prefix[i] = prefix[i - 1] + arr[i];
}

4. Where can Prefix Sum be applied?
Prefix sums are useful in many types of problems such as:
Range sum queries: Quickly compute sum of elements in subarrays multiple times.
Number of elements in a range satisfying a condition.
Finding subarrays with a certain sum.
2D prefix sums for matrix sub-rectangle sums.
Difference arrays and range update queries.
Problems involving cumulative frequencies, histograms, or quick summation checks.

5. How to identify problems where Prefix Sum applies?
Look for questions that:
Ask for sum of elements in a range/subarray multiple times.
Need fast repeated sum queries after an initial array is given.
Need to find number of subarrays satisfying certain sum-related properties.
Involve checking sums quickly without recalculating sums for overlapping parts.
Deal with prefix-based conditions, such as count of elements or cumulative constraints.

6. Benefits of Prefix Sum Pattern
Reduces repeated work in sum calculations.
Transforms O(n^2) range sum queries into O(n) preprocessing + O(1) query.
Simplifies problem logic by leveraging precomputed cumulative data.
Helps in solving problems related to subarray sums, histogram calculations, and range queries efficiently.

Prefix Sum Flowchart:

             Arrays / Subarrays
                                    Sum of left / right
                                    pivot / equilibrium

             Sum of Subarrays/negative Numbers
                                    Sum(i...j) == K      (Hashmap)
                                    Sum(i...j)%k = 0     (Hashmap)
             Shortest Window with Sum >= K    (Deque)
             Range Sum   ->>>>   Merge Sort on prefix Array



prefix[i] = prefix[i-1] + a[i-1]
means prefix[2] = prefix[1] + a[1] and prefix[1] = a[0]

Suff[i] = Suff[i+1] + a[i+1]
as suff[2] = a[3] + a[4]
and suff[1]  = suff[2] + a[2]
"""

##! Question 1: Find pivot index


"""
Given an array of integers nums, calculate the pivot index of this array.

The pivot index is the index where the sum of all the numbers strictly to the left of the index is equal to the sum of all the numbers strictly to the index's right.

If the index is on the left edge of the array, then the left sum is 0 because there are no elements to the left. This also applies to the right edge of the array.

Return the leftmost pivot index. If no such index exists, return -1.

 

Example 1:

Input: nums = [1,7,3,6,5,6]
Output: 3
Explanation:
The pivot index is 3.
Left sum = nums[0] + nums[1] + nums[2] = 1 + 7 + 3 = 11
Right sum = nums[4] + nums[5] = 5 + 6 = 11

Example 2:

Input: nums = [1,2,3]
Output: -1
Explanation:
There is no index that satisfies the conditions in the problem statement.

Example 3:

Input: nums = [2,1,-1]
Output: 0
Explanation:
The pivot index is 0.
Left sum = 0 (no elements to the left of index 0)
Right sum = nums[1] + nums[2] = 1 + -1 = 0
 

Constraints:

1 <= nums.length <= 10^4
-1000 <= nums[i] <= 1000

"""


## Brute Force
def pivot_index_brute_force(nums):
    n = len(nums)

    for i in range(n):
        left_sum = 0
        right_sum = 0

        for j in range(i):
            left_sum += nums[j]

        for j in range(i + 1, n):
            right_sum += nums[j]

        if left_sum == right_sum:
            return i

    return -1


# Time Complexity: O(n²)
# Space Complexity : O(1)


## prefix Sum Array
def pivot_index_prefix(nums):
    n = len(nums)

    prefix = [0] * n
    prefix[0] = nums[0]

    for i in range(1, n):
        prefix[i] = prefix[i - 1] + nums[i]

    total = prefix[-1]

    for i in range(n):

        left_sum = prefix[i - 1] if i > 0 else 0
        right_sum = total - prefix[i]

        if left_sum == right_sum:
            return i

    return -1


# Time Complexity: O(n)
# Space Complexity : O(n)


## Optimized Approach - Running Sum
def pivotIndex(nums):
    total = sum(nums)
    leftSum = 0
    n = len(nums)

    for i in range(n):
        rightSum = total - leftSum - nums[i]  # As total = leftSum + nums[i] + rightSum
        if rightSum == leftSum:
            return i
        leftSum += nums[i]

    return -1


# Time Complexity: O(n)
# Space Complexity : O(1)

print(
    "Results for pivot index:\n", pivotIndex([1, 7, 3, 6, 5, 6]), pivotIndex([2, 1, -1])
)


##! Question 2: Subarray sum equals K

"""
Given an array of integers nums and an integer k, return the total number of subarrays whose sum equals to k.

A subarray is a contiguous non-empty sequence of elements within an array.

Example 1:

Input: nums = [1,1,1], k = 2
Output: 2

Example 2:

Input: nums = [1,2,3], k = 3
Output: 2
 

Constraints:

1 <= nums.length <= 2 * 104
-1000 <= nums[i] <= 1000
-107 <= k <= 107
"""
# brute force appraoch


def subarraySumEqualsKBrute(nums, k):
    count = 0
    n = len(nums)
    for i in range(n):
        sum = 0
        for j in range(i, n):
            sum += nums[j]
            if sum == k:
                count += 1

    return count


print("subarraySumEqualsK()", subarraySumEqualsKBrute([-1, 2, 1, 2, -1], 5))

# Time Complexity : O(n^2)
# Space Complexity : O(1)


def subarraySum(nums, k):

    prefix_sum = 0
    count = 0
    freq = {0: 1}

    for num in nums:

        prefix_sum += num

        if (prefix_sum - k) in freq:
            count += freq[prefix_sum - k]

        freq[prefix_sum] = freq.get(prefix_sum, 0) + 1

    return count


# Time and space complexity : O(n)


##! Question 3: Continuous Subarray Sum


"""
Given an integer array nums and an integer k, return true if nums has a good subarray or false otherwise.

A good subarray is a subarray where:

its length is at least two, and
the sum of the elements of the subarray is a multiple of k.
Note that:

A subarray is a contiguous part of the array.
An integer x is a multiple of k if there exists an integer n such that x = n * k. 0 is always a multiple of k.
 

Example 1:

Input: nums = [23,2,4,6,7], k = 6
Output: true
Explanation: [2, 4] is a continuous subarray of size 2 whose elements sum up to 6.

Example 2:

Input: nums = [23,2,6,4,7], k = 6
Output: true
Explanation: [23, 2, 6, 4, 7] is an continuous subarray of size 5 whose elements sum up to 42.
42 is a multiple of 6 because 42 = 7 * 6 and 7 is an integer.

Example 3:

Input: nums = [23,2,6,4,7], k = 13
Output: false
 

Constraints:

1 <= nums.length <= 105
0 <= nums[i] <= 109
0 <= sum(nums[i]) <= 231 - 1
1 <= k <= 231 - 1
"""


def checkSubarraySum(nums, k):
    prefix_sum = 0
    remainder_map = {0: -1}  # remainder 0 at index -1

    for i, num in enumerate(nums):
        prefix_sum += num
        remainder = prefix_sum % k

        if remainder in remainder_map:
            if i - remainder_map[remainder] >= 2:
                return True
        else:
            remainder_map[remainder] = i

    return False


# Time Complexity: O(n)
# Space Complexity: O(min(n, k))


##! Question 4: Subarray Sums Divisible by K


"""

Given an integer array nums and an integer k, return the number of non-empty subarrays that have a sum divisible by k.

A subarray is a contiguous part of an array.

Example 1:

Input: nums = [4,5,0,-2,-3,1], k = 5
Output: 7
Explanation: There are 7 subarrays with a sum divisible by k = 5:
[4, 5, 0, -2, -3, 1], [5], [5, 0], [5, 0, -2, -3], [0], [0, -2, -3], [-2, -3]

Example 2:

Input: nums = [5], k = 9
Output: 0
 

Constraints:

1 <= nums.length <= 3 * 10^4
-10^4 <= nums[i] <= 10^4
2 <= k <= 10^4

"""


##! Question 5: Contiguous Array

"""

Given a binary array nums, return the maximum length of a contiguous subarray with an equal number of 0 and 1.

Example 1:

Input: nums = [0,1]
Output: 2
Explanation: [0, 1] is the longest contiguous subarray with an equal number of 0 and 1.

Example 2:

Input: nums = [0,1,0]
Output: 2
Explanation: [0, 1] (or [1, 0]) is a longest contiguous subarray with equal number of 0 and 1.

Example 3:

Input: nums = [0,1,1,1,1,1,0,0,0]
Output: 6
Explanation: [1,1,1,0,0,0] is the longest contiguous subarray with equal number of 0 and 1.
 

Constraints:

1 <= nums.length <= 105
nums[i] is either 0 or 1.

"""


##! Question 6: Shortest Subarray with Sum at Least K


"""

Given an integer array nums and an integer k, return the length of the shortest non-empty subarray of nums with a sum of at least k. If there is no such subarray, return -1.

A subarray is a contiguous part of an array.

Example 1:

Input: nums = [1], k = 1
Output: 1

Example 2:

Input: nums = [1,2], k = 4
Output: -1

Example 3:

Input: nums = [2,-1,2], k = 3
Output: 3
 

Constraints:

1 <= nums.length <= 10^5
-10^5 <= nums[i] <= 10^5
1 <= k <= 10^9

"""


##! Question 7: Count of Range Sum

"""

Given an integer array nums and two integers lower and upper, return the number of range sums that lie in [lower, upper] inclusive.

Range sum S(i, j) is defined as the sum of the elements in nums between indices i and j inclusive, where i <= j.


Example 1:

Input: nums = [-2,5,-1], lower = -2, upper = 2
Output: 3
Explanation: The three ranges are: [0,0], [2,2], and [0,2] and their respective sums are: -2, -1, 2.

Example 2:

Input: nums = [0], lower = 0, upper = 0
Output: 1
 
Constraints:

1 <= nums.length <= 105
-231 <= nums[i] <= 231 - 1
-105 <= lower <= upper <= 105
The answer is guaranteed to fit in a 32-bit integer.

"""

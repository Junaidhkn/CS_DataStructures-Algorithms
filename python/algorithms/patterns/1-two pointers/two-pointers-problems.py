"""
What is the Two Pointers Pattern?
The Two Pointers technique involves using two indices (pointers) to iterate over a data structure (usually an array or a string) to solve problems efficiently by avoiding nested loops.

When to Use Two Pointers?
When you need to find pairs, triplets, or subarrays meeting certain conditions.
When the data is sorted or can be sorted.
When you want to optimize brute force solutions that use nested loops (On2)) to linear or near-linear time (O(n)).
{
    array / linkedlist
    sorted / sort
    merge / remove duplicates / rearrange
    detect cycle in linked list
    finding pair / triplets / quadruple
}

How It Works?
You maintain two pointers that move through the data structure according to certain rules:
One pointer starts at the beginning, the other at the end (common in problems like finding pairs with a sum).
Or, both pointers start at the beginning, with one moving faster than the other (useful for sliding window problems).
Move pointers towards each other or forward depending on the problem condition.

Typical Approach:
Initialize two pointers, left and right.
Check condition based on the current pointers.
Move pointers accordingly:
If condition not met, move left or right pointer to try to satisfy the condition.
If condition met, record the answer or move pointers to find more solutions.
Repeat until pointers cross or reach the end.
"""

#! Question 1: Two sum II: Input Array is sorted

"""
Given a 1-indexed array of integers numbers that is already sorted in non-decreasing order, find two numbers such that they add up to a specific target number. Let these two numbers be numbers[index1] and numbers[index2] where 1  <= index1 < index2 <= numbers.length.

Return the indices of two numbers, index1 and index2, added by one as an integer array [index1,index2] of length 2.

The same element cannot be used twice, and solution must only be constant extra space

Example 1:
Input: numbers = [2,7,11,15] , target = 9
Output: [1,2]
Explanation: The sum of 2 and 7 is 9. Therefore, index1 = 1, index2 = 2. We return [1,2]

"""


# Brute force Approach:Problem is that its time complexity is O(n^2)
def twoSumIIBruteForce(lst, target):
    n = len(lst)
    for i in range(n):
        for j in range(i + 1, n):
            if lst[i] + lst[j] == target:
                return [i + 1, j + 1]


# resultTwoSumII = twoSumIIBruteForce([8, 7, 11, 15], 19)
# print("Bruteforce question 1:\n", resultTwoSumII)


# HashMap Approach: Problem is that its takes alot of space: O(n)
def twoSumIIHashmap(lst, target):
    seen = {}
    for i in range(len(lst)):
        complement = target - lst[i]
        if complement in seen:
            print("printing seen[complement]", seen[complement])
            return [seen[complement] + 1, i + 1]
        seen[lst[i]] = i
        print("printing seen:", seen[lst[i]])


# resultTwoSumII = twoSumIIHashmap([2, 7, 11, 15], 9)


# Optimal approach -> two pointers
def twoSumII(lst, target):
    left = 0
    right = len(lst) - 1

    while left < right:
        num = lst[left] + lst[right]

        if num == target:
            return [left + 1, right + 1]
        elif num > target:
            right -= 1
        else:
            left += 1

    return []


# resultTwoSumII = twoSumII([2, 7, 11, 15], 9)

# print("printing result for question 1: Optimal two pointers\n", resultTwoSumII)

# Time Complexity : O(n)
# Space Complexity : O(1)


#! Question 2: Remove Duplicates from Sorted Array

"""
Given an integer array nums sorted in non-decreasing order, remove the duplicates in-place such that each unique element appears only once. The relative order of the elements should be kept the same.

Consider the number of unique elements in nums to be k. After removing duplicates, return the number of unique elements k.

The first k elements of nums should contain the unique numbers in sorted order. The remaining elements beyond index k - 1 can be ignored.

Custom Judge:

The judge will test your solution with the following code:

int[] nums = [...]; // Input array
int[] expectedNums = [...]; // The expected answer with correct length

int k = removeDuplicates(nums); // Calls your implementation

assert k == expectedNums.length;
for (int i = 0; i < k; i++) {
    assert nums[i] == expectedNums[i];
}
If all assertions pass, then your solution will be accepted.

 

Example 1:

Input: nums = [1,1,2]
Output: 2, nums = [1,2,_]
Explanation: Your function should return k = 2, with the first two elements of nums being 1 and 2 respectively.
It does not matter what you leave beyond the returned k (hence they are underscores).

Example 2:

Input: nums = [0,0,1,1,1,2,2,3,3,4]
Output: 5, nums = [0,1,2,3,4,_,_,_,_,_]
Explanation: Your function should return k = 5, with the first five elements of nums being 0, 1, 2, 3, and 4 respectively.
It does not matter what you leave beyond the returned k (hence they are underscores).
 

Constraints:

1 <= nums.length <= 3 * 104
-100 <= nums[i] <= 100
nums is sorted in non-decreasing order.
"""


# Brute force approach for sorted array
def removeDuplicates_bruteforce(nums):
    unique = []
    for num in nums:
        found = False
        for u in unique:
            if u == num:
                found = True
                break
        if not found:
            unique.append(num)
    return len(unique), unique


# Time Complexity: O(n²)
# Space Complexity : O(n) (if we store results in another list)


# Optimal Solution for sorted array according to the question : Two pointers approach
def removeDuplicates(nums):
    slow = 1
    for fast in range(1, len(nums)):
        if nums[fast] != nums[slow - 1]:
            nums[slow] = nums[fast]
            slow += 1
    return slow, nums[:slow], nums


# here we are starting with slow = 1, because the first one is not duplicate
# result = removeDuplicates([0, 0, 1, 1, 1, 2, 2, 3, 3, 4])

# print("Printing result for question 2:\n", result)


# Time Complexity : O(n)
# Space Complexity : O(1) but when returning array rather than length it would be O(n)

# If unsorted array is given: Optimal method is to use hash set


def removeDuplicates_unsorted(nums):
    seen = set()
    k = 0

    for num in nums:
        if num not in seen:
            seen.add(num)
            nums[k] = num
            k += 1

    return k, nums[:k], nums


# print(removeDuplicates_unsorted([3, 1, 3, 2, 4, 1, 5]))
# Time Complexity: O(n)
# Space Complexity : O(n)


#! Question 3: Valid Palindrome
"""
A phrase is a palindrome if, after converting all uppercase letters into lowercase letters and removing all non-alphanumeric characters, it reads the same forward and backward. Alphanumeric characters include letters and numbers.

Given a string s, return true if it is a palindrome, or false otherwise.

 

Example 1:

Input: s = "A man, a plan, a canal: Panama"
Output: true
Explanation: "amanaplanacanalpanama" is a palindrome.

Example 2:

Input: s = "race a car"
Output: false
Explanation: "raceacar" is not a palindrome.

Example 3:

Input: s = " "
Output: true
Explanation: s is an empty string "" after removing non-alphanumeric characters.
Since an empty string reads the same forward and backward, it is a palindrome.
 

Constraints:

1 <= s.length <= 2 * 105
s consists only of printable ASCII characters.
"""


def isPalindrome(s):
    left = 0
    right = len(s) - 1
    while left < right:
        while left < right and not s[left].isalnum():
            left += 1
        while left < right and not s[right].isalnum():
            right -= 1
        if s[left].lower() != s[right].lower():
            return False

        left += 1
        right -= 1

    return True


# result = isPalindrome("m,,a.dam")

# print("Printing result from question 3:\n", result)


#! Question 4: Container with most water

"""
You are given an integer array height of length n. There are n vertical lines drawn such that the two endpoints of the ith line are (i, 0) and (i, height[i]).

Find two lines that together with the x-axis form a container, such that the container contains the most water.

Return the maximum amount of water a container can store.

Notice that you may not slant the container.

 

Example 1:

Input: height = [1,8,6,2,5,4,8,3,7]
Output: 49
Explanation: The above vertical lines are represented by array [1,8,6,2,5,4,8,3,7]. In this case, the max area of water the container can contain is 49.

Example 2:

Input: height = [1,1]
Output: 1
 

Constraints:

n == height.length
2 <= n <= 105
0 <= height[i] <= 104
"""


"""
Notes:
a) left and right, there are two pointers
b) Keep track of the items in the left and right indices, and store the area, and it can only be replaced with the next higher area
c) Considering only the heights, the one with the smaller number between left and right, would only be moved, and it would cause the width to get less with each movement
d) amoung the left and right only the height with the lower number would be considered in calculations

"""


def maxArea(height):
    n = len(height)
    left = 0
    right = n - 1
    max_area = 0
    while left < right:
        width = right - left
        area = min(height[left], height[right]) * (width)
        max_area = max(max_area, area)
        if height[left] < height[right]:
            left += 1
        else:
            right -= 1

    return max_area


# result = maxArea([1, 8, 6, 2, 5, 4, 8, 3, 7])

# print("Printing result from question 4:\n", result)


# Time Complexity: O(n)
# Space Complexity : O(1)


#! Question 5: Squares of a Sorted Array

"""
Given an integer array nums sorted in non-decreasing order, return an array of the squares of each number sorted in non-decreasing order.

Example 1:

Input: nums = [-4,-1,0,3,10]
Output: [0,1,9,16,100]
Explanation: After squaring, the array becomes [16,1,0,9,100].
After sorting, it becomes [0,1,9,16,100].

Example 2:

Input: nums = [-7,-3,2,3,11]
Output: [4,9,9,49,121]
 

Constraints:

1 <= nums.length <= 104
-104 <= nums[i] <= 104
nums is sorted in non-decreasing order.
 

Follow up: Squaring each element and sorting the new array is very trivial, could you find an O(n) solution using a different approach?
"""


#  Brute force approach
def sortedSquares(nums: list[int]) -> list[int]:
    return sorted(x * x for x in nums)


# Two Pointers Optimal Solution
def sortedSquaresOptimal(nums: list[int]) -> list[int]:
    n = len(nums)
    result = [0] * n
    left, right = 0, n - 1
    pos = n - 1
    while left <= right:
        left_sq = nums[left] ** 2
        right_sq = nums[right] ** 2
        if left_sq > right_sq:
            result[pos] = left_sq
            left += 1
        else:
            result[pos] = right_sq
            right -= 1
        pos -= 1
    return result


# result = sortedSquaresOptimal([-4, -1, 0, 3, 10])

# print("Printing result from question 5:\n", result)


#! Question 6: Triplet Sum to Zero (medium)

"""

Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.

Notice that the solution set must not contain duplicate triplets.

Example 1:

Input: nums = [-1,0,1,2,-1,-4]
Output: [[-1,-1,2],[-1,0,1]]
Explanation: 
nums[0] + nums[1] + nums[2] = (-1) + 0 + 1 = 0.
nums[1] + nums[2] + nums[4] = 0 + 1 + (-1) = 0.
nums[0] + nums[3] + nums[4] = (-1) + 2 + (-1) = 0.
The distinct triplets are [-1,0,1] and [-1,-1,2].
Notice that the order of the output and the order of the triplets does not matter.

Example 2:

Input: nums = [0,1,1]
Output: []
Explanation: The only possible triplet does not sum up to 0.

Example 3:

Input: nums = [0,0,0]
Output: [[0,0,0]]
Explanation: The only possible triplet sums up to 0.
 

Constraints:

3 <= nums.length <= 3000
-105 <= nums[i] <= 105

"""


## Brute Force Solution


# time complexity : O(n^3) , space complexity: O(n)
def tripletSumZero(nums: list[int]) -> list[int]:
    triplets = []
    seen = set()
    n = len(nums)
    for i in range(n - 2):
        for j in range(i + 1, n - 1):
            for k in range(j + 1, n):
                if nums[i] + nums[j] + nums[k] == 0:
                    triplet = tuple(sorted([nums[i], nums[j], nums[k]]))
                    if triplet not in seen:
                        seen.add(triplet)
                        triplets.append(list(triplet))

    if len(triplet) != 0:
        return triplets
    else:
        return []


# result = tripletSumZero([-1, 0, 1, 2, -1, -4])

# print("**********Brute Force for question 6:************\n", result)


# Two Pointers: Optimized Solution
def tripletSumZeroOptimized(nums: list[int]) -> list[int]:
    nums.sort()
    triplets = []
    n = len(nums)

    for i in range(n):
        if i > 0 and nums[i] == nums[i - 1]:
            continue
        if nums[i] > 0:
            break

        left, right = i + 1, n - 1
        target = -nums[i]

        while left < right:
            current_sum = nums[left] + nums[right]

            if current_sum == target:
                triplets.append([nums[i], nums[left], nums[right]])
                left += 1
                right -= 1
                while left < right and nums[left] == nums[left - 1]:
                    left += 1
                while left < right and nums[right] == nums[right + 1]:
                    right -= 1

            elif current_sum < target:
                left += 1
            else:
                right -= 1

    return triplets


# result = tripletSumZeroOptimized([-1, 0, 1, 2, -1, -4])

# print("**********Optimal solution for question 6:************\n", result)

# Time Complexity : O(n^2)
# Space Complexity : O(1)

### Optimal Solution Without Sorting


def tripletSumZeroWithoutSort(nums: list[int]) -> list[int]:
    n = len(nums)
    result = set()

    for i in range(n):
        seen = set()
        target = -nums[i]
        for j in range(i + 1, n):
            complement = target - nums[j]
            if complement in seen:
                triplet = tuple(sorted([nums[i], nums[j], complement]))
                result.add(triplet)
            seen.add(nums[j])

    return [list(t) for t in result]


# result = tripletSumZero([-1, 0, 1, 2, -1, -4])
# print("Printing result if input is unsorted \n", result)  # [[-1, -1, 2], [-1, 0, 1]]

#! Question 7: 	Triplet Sum Close to Target (medium)

"""

Given an integer array nums of length n and an integer target, find three integers at distinct indices in nums such that the sum is closest to target.

Return the sum of the three integers.

You may assume that each input would have exactly one solution.

Example 1:

Input: nums = [-1,2,1,-4], target = 1
Output: 2
Explanation: The sum that is closest to the target is 2. (-1 + 2 + 1 = 2).

Example 2:

Input: nums = [0,0,0], target = 1
Output: 0
Explanation: The sum that is closest to the target is 0. (0 + 0 + 0 = 0).
 

Constraints:

3 <= nums.length <= 500
-1000 <= nums[i] <= 1000
-104 <= target <= 104

"""


#! Question 8: 	Triplets with Smaller Sum (medium)


"""

Given an array arr[] of distinct integers and a value sum, find the count of triplets (i, j, k), having (i<j<k) with the sum of (arr[i] + arr[j] + arr[k]) smaller than the given value sum.

Examples :

Input: sum = 2, arr[] = [-2, 0, 1, 3]
Output:  2
Explanation: Triplets with sum less than 2 are (-2, 0, 1) and (-2, 0, 3). 
Input: sum = 12, arr[] = [5, 1, 3, 4, 7]
Output: 4
Explanation: Triplets with sum less than 12 are (1, 3, 4), (5, 1, 3), (1, 3, 7) and (5, 1, 4).


Constraints:
1 ≤ sum ≤ 105
3 ≤ arr.size() ≤ 103
-103 ≤ arr[i] ≤ 103

"""

# Brute force solution


def tripletSmallerSum(nums: list[int], target) -> list[int]:
    triplets = []
    seen = set()
    n = len(nums)
    for i in range(n - 2):
        for j in range(i + 1, n - 1):
            for k in range(j + 1, n):
                if nums[i] + nums[j] + nums[k] < target:
                    triplet = tuple(sorted([nums[i], nums[j], nums[k]]))
                    if triplet not in seen:
                        seen.add(triplet)
                        triplets.append(list(triplet))

    if len(triplet) != 0:
        return triplets, len(triplets)
    else:
        return []


result = tripletSmallerSum([5, 1, 3, 4, 7], 12)

print("**********Brute Force for question 8:************\n", result)


# Optimized Solution
def tripletSmallerSumOptimized(nums: list[int], sum) -> list[int]:
    nums.sort()
    triplets = []
    n = len(nums)

    for i in range(n):
        if i > 0 and nums[i] == nums[i - 1]:
            continue
        if nums[i] > sum:
            break

        left, right = i + 1, n - 1

        while left < right:
            current_sum = nums[left] + nums[right] + nums[i]
            if current_sum < sum:
                triplets.append([nums[i], nums[left], nums[right]])
                left += 1
                right -= 1
                while left < right and nums[left] == nums[left - 1]:
                    left += 1
                while left < right and nums[right] == nums[right + 1]:
                    right -= 1
            elif current_sum >= sum:
                right -= 1

    return triplets, len(triplets)


result = tripletSmallerSumOptimized([5, 1, 3, 4, 7], 12)

print("***Optimized solution for question 8:************\n", result)

#! Question 9: 	Sort Colors (medium)

"""

Given an array nums with n objects colored red, white, or blue, sort them in-place so that objects of the same color are adjacent, with the colors in the order red, white, and blue.

We will use the integers 0, 1, and 2 to represent the color red, white, and blue, respectively.

You must solve this problem without using the library's sort function.

 

Example 1:

Input: nums = [2,0,2,1,1,0]
Output: [0,0,1,1,2,2]

Example 2:

Input: nums = [2,0,1]
Output: [0,1,2]
 

Constraints:

n == nums.length
1 <= n <= 300
nums[i] is either 0, 1, or 2.
 

Follow up: Could you come up with a one-pass algorithm using only constant extra space?

"""


#! Question 10:  4Sum (medium)


"""

Given an array nums of n integers, return an array of all the unique quadruplets [nums[a], nums[b], nums[c], nums[d]] such that:

0 <= a, b, c, d < n
a, b, c, and d are distinct.
nums[a] + nums[b] + nums[c] + nums[d] == target
You may return the answer in any order.

 

Example 1:

Input: nums = [1,0,-1,0,-2,2], target = 0
Output: [[-2,-1,1,2],[-2,0,0,2],[-1,0,0,1]]

Example 2:

Input: nums = [2,2,2,2,2], target = 8
Output: [[2,2,2,2]]
 

Constraints:

1 <= nums.length <= 200
-109 <= nums[i] <= 109
-109 <= target <= 109

"""


#! Question 11:  Backspace String Compare (Easy)

"""

Given two strings s and t, return true if they are equal when both are typed into empty text editors. '#' means a backspace character.

Note that after backspacing an empty text, the text will continue empty.

 

Example 1:

Input: s = "ab#c", t = "ad#c"
Output: true
Explanation: Both s and t become "ac".

Example 2:

Input: s = "ab##", t = "c#d#"
Output: true
Explanation: Both s and t become "".

Example 3:

Input: s = "a#c", t = "b"
Output: false
Explanation: s becomes "c" while t becomes "b".
 

Constraints:

1 <= s.length, t.length <= 200
s and t only contain lowercase letters and '#' characters.
 

Follow up: Can you solve it in O(n) time and O(1) space?

"""


#! Question 12:  Shortest Unsorted Continuous Subarray (Medium)


"""

Given an integer array nums, you need to find one continuous subarray such that if you only sort this subarray in non-decreasing order, then the whole array will be sorted in non-decreasing order.

Return the shortest such subarray and output its length.

 

Example 1:

Input: nums = [2,6,4,8,10,9,15]
Output: 5
Explanation: You need to sort [6, 4, 8, 10, 9] in ascending order to make the whole array sorted in ascending order.

Example 2:

Input: nums = [1,2,3,4]
Output: 0

Example 3:

Input: nums = [1]
Output: 0
 

Constraints:

1 <= nums.length <= 104
-105 <= nums[i] <= 105
 

Follow up: Can you solve it in O(n) time complexity?

"""


#! Question 13:  Subarray Product Less Than K (Medium)

"""

Given an array of integers nums and an integer k, return the number of contiguous subarrays where the product of all the elements in the subarray is strictly less than k.

 

Example 1:

Input: nums = [10,5,2,6], k = 100
Output: 8
Explanation: The 8 subarrays that have product less than 100 are:
[10], [5], [2], [6], [10, 5], [5, 2], [2, 6], [5, 2, 6]
Note that [10, 5, 2] is not included as the product of 100 is not strictly less than k.

Example 2:

Input: nums = [1,2,3], k = 0
Output: 0
 

Constraints:

1 <= nums.length <= 3 * 104
1 <= nums[i] <= 1000
0 <= k <= 106

"""


#! Question 14:  Trapping Rain Water (Hard)

"""

Given n non-negative integers representing an elevation map where the width of each bar is 1, compute how much water it can trap after raining.

Example 1:
Input: height = [0,1,0,2,1,0,1,3,2,1,2,1]
Output: 6
Explanation: The elevation map is represented by the array above.
In this case, 6 units of rain water are being trapped.

Example 2:
Input: height = [4,2,0,3,2,5]
Output: 9
Constraints:
n == height.length
1 <= n <= 2 * 10^4
0 <= height[i] <= 10^5

"""


#! Question 15:  Minimum Window Substring (Hard)


"""

Given two strings s and t of lengths m and n respectively, return the minimum window substring of s such that every character in t (including duplicates) is included in the window. If there is no such substring, return the empty string "".
The testcases will be generated such that the answer is unique.

Example 1:
Input: s = "ADOBECODEBANC", t = "ABC"
Output: "BANC"
Explanation: The substring "BANC" includes 'A', 'B', and 'C' from string t.

Example 2:
Input: s = "a", t = "a"
Output: "a"
Explanation: The entire string s is the minimum window.

Example 3:
Input: s = "a", t = "aa"
Output: ""
Explanation: Both 'a's from t must be included in the window.
Since the largest window of s only has one 'a', return empty string.
Constraints:
m == s.length
n == t.length
1 <= m, n <= 10^5
s and t consist of uppercase and lowercase English letters.

"""

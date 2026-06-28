"""
What is the Two Pointers Pattern?
The Two Pointers technique involves using two indices (pointers) to iterate over a data structure
(usually an array or a string) to solve problems efficiently by avoiding nested loops.

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
Or, both pointers start at the beginning, with one moving faster than the other (useful for
sliding window problems).
Move pointers towards each other or forward depending on the problem condition.

Typical Approach:
Initialize two pointers, left and right.
Check condition based on the current pointers.
Move pointers accordingly:
If condition not met, move left or right pointer to try to satisfy the condition.
If condition met, record the answer or move pointers to find more solutions.
Repeat until pointers cross or reach the end.
"""

# Question 1: Two sum II: Input Array is sorted

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


resultTwoSumII = twoSumIIBruteForce([8, 7, 11, 15], 19)
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


resultTwoSumII = twoSumIIHashmap([2, 7, 11, 15], 9)


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


resultTwoSumII = twoSumII([2, 7, 11, 15], 9)

print("printing result for question 1: Optimal two pointers\n", resultTwoSumII)

# Time Complexity : O(n)
# Space Complexity : O(1)


# Question 2: Remove Duplicates from Sorted Array

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


result = removeDuplicates([0, 0, 1, 1, 1, 2, 2, 3, 3, 4])

print("Printing result for question 2:\n", result)


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


print(removeDuplicates_unsorted([3, 1, 3, 2, 4, 1, 5]))
# Time Complexity: O(n)
# Space Complexity : O(n)


# Question 3: Valid Palindrome
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


result = isPalindrome("m,,a.dam")

print("Printing result from question 3:\n", result)


# Question 4: Container with most water

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


result = maxArea([1, 8, 6, 2, 5, 4, 8, 3, 7])

print("Printing result from question 4:\n", result)


# Time Complexity: O(n)
# Space Complexity : O(1)


# Question 5: Squares of a Sorted Array

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


# Brute force approach


# Two Pointers Optimal Solution

"""
What is the Two Pointers Pattern?
The Two Pointers technique involves using two indices (pointers) to iterate over a data structure
(usually an array or a string) to solve problems efficiently by avoiding nested loops.

When to Use Two Pointers?
When you need to find pairs, triplets, or subarrays meeting certain conditions.
When the data is sorted or can be sorted.
When you want to optimize brute force solutions that use nested loops (O(n2)) to linear or
near-linear time (O(n)).


How It Works?
You maintain two pointers that move through the data structure according to certain rules:
One pointer starts at the beginning, the other at the end (common in problems like
finding pairs with a sum).
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

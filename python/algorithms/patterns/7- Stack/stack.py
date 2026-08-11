"""
============================================================
STACK DSA PATTERN
============================================================

WHAT IS A STACK?
----------------
A Stack is a data structure that follows:

    LIFO = Last In, First Out

The last element added to the stack is the first one removed.

Think of it like a stack of plates:

    Add plate -> put it on top
    Remove plate -> take the top plate

Main operations:

    push(x)  -> add x
    pop()    -> remove and return the top element
    peek()   -> look at the top element
    empty()  -> check whether stack is empty


PYTHON IMPLEMENTATION
---------------------

Python's list can be used as a stack:

    stack = []

    stack.append(10)    # push
    stack.append(20)
    stack.append(30)

    stack.pop()         # 30
    stack[-1]           # peek -> 20

Time complexity:

    append() -> O(1)
    pop()    -> O(1)
    peek     -> O(1)


============================================================
THE CORE IDEA
============================================================

A stack is useful when the problem requires us to remember
previous elements and process them in reverse order.

The most important question to ask is:

    "Do I need to go back to something I saw earlier?"

If YES, a stack may be useful.


============================================================
WHEN SHOULD I THINK OF A STACK?
============================================================

Look for these patterns:

1. Matching / nested structures
--------------------------------

Examples:

    ()
    {}
    []
    ({[]})

You need to remember the most recent opening bracket.

Example:

    stack = []

    for char in s:
        if char in "([{":
            stack.append(char)

        elif char in ")]}":
            if not stack:
                return False

            if stack.pop() != matching_opening_bracket:
                return False

    return not stack


2. "Previous" or "Next" greater/smaller element
------------------------------------------------

These are classic STACK problems.

Examples:

    Next Greater Element
    Previous Greater Element
    Next Smaller Element
    Previous Smaller Element

Instead of repeatedly searching backward/forward,
we maintain useful candidates inside a stack.

These commonly use a:

    MONOTONIC STACK


3. Remove/cancel previous elements
-----------------------------------

If the current element can make a previous element invalid,
a stack is often useful.

Example:

    Remove Adjacent Duplicates

    "abbaca"

Processing:

    a -> stack = [a]
    b -> stack = [a, b]
    b -> remove b
    a -> remove a
    c -> stack = [c]
    a -> stack = [c, a]

Result:

    "ca"


4. Nested problems
-------------------

Whenever something is nested inside something else:

    (a(b(c)))
    directories
    expressions
    function calls
    HTML/XML tags

A stack can represent the currently active/nested items.


5. Undo / Backtracking-like behavior
-------------------------------------

A stack naturally remembers previous states/actions.

Examples:

    Undo operations
    Browser history
    DFS
    Backtracking states


============================================================
THE MOST IMPORTANT STACK PATTERN:
MONOTONIC STACK
============================================================

A Monotonic Stack is a stack whose elements are maintained
in increasing or decreasing order.

Example:

    [2, 5, 7]

Increasing stack:

    2 < 5 < 7

If a new value violates the desired ordering, we pop elements.

Example:

    nums = [2, 1, 5]

We want the Next Greater Element.

Process:

    2 -> stack = [2]

    1 -> stack = [2, 1]

    5 ->

    5 > 1
    Therefore 1's next greater element is 5.

    pop 1

    5 > 2
    Therefore 2's next greater element is 5.

    pop 2

This allows us to solve the problem in O(n).


============================================================
WHY IS MONOTONIC STACK O(N)?
============================================================

This is one of the most important things to understand.

At first glance, we are using a loop inside a loop:

    for num in nums:
        while stack:
            stack.pop()

It LOOKS like O(n²).

But it is actually O(n).

Why?

Every element can:

    1. Be pushed onto the stack once.
    2. Be popped from the stack once.

Therefore:

    Maximum pushes = n
    Maximum pops   = n

Total work:

    O(n) + O(n)
    = O(n)


============================================================
HOW TO RECOGNIZE THE OPTIMAL STACK APPROACH
============================================================

Ask these questions:

Question 1:
    Am I repeatedly searching for the previous/next
    greater/smaller element?

If YES:
    Think MONOTONIC STACK.


Question 2:
    Do I need to match opening and closing elements?

If YES:
    Think STACK.


Question 3:
    Does the current element invalidate/remove a
    previously processed element?

If YES:
    Think STACK.


Question 4:
    Is there a nested structure?

If YES:
    Think STACK.


Question 5:
    Does the problem require processing something in
    reverse order?

If YES:
    Consider STACK.


============================================================
BRUTE FORCE vs STACK
============================================================

Suppose we need:

    Next Greater Element

Input:

    [2, 1, 5, 3, 4]

Brute force:

    For every element:
        search to the right
        find the first greater element

This can take:

    O(n²)


Stack approach:

    Process elements once.
    Maintain candidates in a monotonic stack.

Complexity:

    Time  -> O(n)
    Space -> O(n)


The important optimization idea is:

    Don't repeatedly search elements that we already know
    cannot be useful.

The stack stores only useful candidates.


============================================================
CLASSIC STACK PROBLEMS
============================================================

1. Valid Parentheses
2. Min Stack
3. Evaluate Reverse Polish Notation
4. Next Greater Element
5. Previous Greater Element
6. Next Smaller Element
7. Daily Temperatures
8. Stock Span
9. Largest Rectangle in Histogram
10. Trapping Rain Water
11. Remove K Digits
12. Remove Adjacent Duplicates
13. Decode String
14. Asteroid Collision
15. Basic Calculator
16. Browser History
17. DFS


============================================================
STACK + INDEX
============================================================

A very important technique is storing INDICES instead of
values.

Instead of:

    stack = [2, 5, 7]

we may store:

    stack = [0, 2, 4]

Then we can access:

    nums[stack[-1]]

Why?

Because many problems require both:

    value
    position

Example:

    Next Greater Element
    Daily Temperatures
    Largest Rectangle in Histogram


============================================================
EXAMPLE: DAILY TEMPERATURES
============================================================

Problem:

    temperatures = [73, 74, 75, 71, 69, 72, 76, 73]

For each day, find how many days we need to wait
until a warmer temperature.

We can use a decreasing monotonic stack.

The stack stores indices whose warmer day has not
yet been found.

Example:

    stack = []

    for i, temperature in enumerate(temperatures):

        while stack and temperature > temperatures[stack[-1]]:
            previous = stack.pop()
            answer[previous] = i - previous

        stack.append(i)

Each index:

    gets pushed once
    gets popped once

Therefore:

    Time  -> O(n)
    Space -> O(n)


============================================================
GENERAL MONOTONIC STACK TEMPLATE
============================================================

For NEXT GREATER:

    stack = []

    for i, num in enumerate(nums):

        while stack and nums[stack[-1]] < num:
            index = stack.pop()

            # nums[index]'s next greater element is num

        stack.append(i)


For NEXT SMALLER:

    while stack and nums[stack[-1]] > num:
        index = stack.pop()


The comparison determines the monotonic behavior.


============================================================
COMMON STACK TEMPLATES
============================================================

1. MATCHING / NESTING
---------------------

    stack = []

    for item in items:

        if opening(item):
            stack.append(item)

        else:
            if not stack:
                return False

            previous = stack.pop()

            if not matches(previous, item):
                return False

    return not stack


2. MONOTONIC STACK
------------------

    stack = []

    for i, num in enumerate(nums):

        while stack and condition(stack[-1], num):
            previous = stack.pop()

            # Process previous

        stack.append(i)


3. REMOVE PREVIOUS ELEMENT
---------------------------

    stack = []

    for num in nums:

        while stack and should_remove(stack[-1], num):
            stack.pop()

        stack.append(num)


============================================================
STACK vs QUEUE
============================================================

STACK:

    LIFO
    Last In -> First Out

    Useful for:
        nested structures
        previous elements
        DFS
        undo
        monotonic problems


QUEUE:

    FIFO
    First In -> First Out

    Useful for:
        BFS
        scheduling
        level-order traversal
        processing things in arrival order


============================================================
STACK vs TWO POINTERS
============================================================

If the problem asks about relationships between elements
and requires searching for:

    next greater
    next smaller
    previous greater
    previous smaller

a monotonic stack is often better.

If the problem involves:

    left boundary
    right boundary
    sorted array
    shrinking from both ends

two pointers may be better.


============================================================
STACK vs HASHMAP
============================================================

HASHMAP is mainly for:

    "Have I seen this?"
    "How many times?"
    "What value belongs to this key?"

STACK is mainly for:

    "What was the most recent unresolved element?"
    "What previous element should I process/remove?"
    "What is nested inside what?"


They can also be combined.

Example:

    frequency map + stack


============================================================
INTERVIEW CHECKLIST
============================================================

When reading a problem, ask:

    1. Is there nesting?
    2. Do I need the most recent unresolved element?
    3. Am I looking for next/previous greater/smaller?
    4. Can the current element invalidate a previous one?
    5. Am I repeatedly scanning backward/forward?
    6. Can I remove useless candidates as I process?
    7. Would each element be pushed and popped at most once?

If several answers are YES:

    STACK is a strong candidate.


============================================================
THE BIGGEST INSIGHT
============================================================

A stack is NOT just:

    "a data structure where we push and pop."

In DSA problems, the deeper idea is:

    "Maintain the elements that are still relevant,
     and remove elements as soon as they become useless."

This is why stacks can turn:

    O(n²) repeated searching

into:

    O(n) single-pass processing.


============================================================
MEMORIZE THIS
============================================================

STACK
    ↓
LIFO
    ↓
Recent / unresolved elements
    ↓
Nested structures
    ↓
Previous / next relationships
    ↓
Monotonic Stack
    ↓
Remove useless candidates
    ↓
Often O(n)


The strongest pattern to remember:

    "If I am repeatedly looking for the next or previous
     greater/smaller element, think MONOTONIC STACK."
"""

"""
============================================================
STACK — TYPES
============================================================

A Stack follows:

    LIFO = Last In, First Out

The last element inserted is the first element removed.

Example:

    push(10)
    push(20)
    push(30)

    Stack:
        [10, 20, 30] <- TOP

    pop() -> 30


============================================================
1. NORMAL / LINEAR STACK
============================================================

The basic stack.

Operations:

    push()  -> add element
    pop()   -> remove top element
    peek()  -> view top element

Python:

    stack = []

    stack.append(10)     # push
    stack.append(20)
    stack.pop()           # removes 20
    stack[-1]             # peek

Time:

    push -> O(1)
    pop  -> O(1)
    peek -> O(1)


============================================================
2. STATIC STACK
============================================================

A stack with a fixed maximum capacity.

Example:

    capacity = 5

    [10, 20, 30, 40, 50]

You cannot add another element once the capacity
is reached.

Commonly implemented using:

    Fixed-size arrays

Important concept:

    Stack Overflow
        -> trying to push into a full stack

    Stack Underflow
        -> trying to pop from an empty stack


============================================================
3. DYNAMIC STACK
============================================================

A stack that can grow/shrink dynamically.

Python's list is commonly used as a dynamic stack:

    stack = []

    stack.append(10)
    stack.append(20)
    stack.append(30)

The underlying storage can grow when necessary.

In Python:

    list + append() + pop()

is the standard way to implement a stack.


============================================================
4. MONOTONIC STACK ⭐
============================================================

A stack that maintains elements in a particular order.

There are two major types:

    1. Monotonic Increasing Stack
    2. Monotonic Decreasing Stack

The purpose is NOT simply storing elements.

The purpose is:

    Remove elements that can no longer be useful.


============================================================
5. MONOTONIC INCREASING STACK
============================================================

Elements are maintained in increasing order.

Example:

    [1, 3, 5, 8]

Whenever a new element violates the ordering,
we pop elements.

Usually useful for:

    Next Smaller Element
    Previous Smaller Element
    Histogram problems
    Finding boundaries


Example:

    nums = [2, 4, 1]

    Process 2:
        stack = [2]

    Process 4:
        stack = [2, 4]

    Process 1:

        1 < 4 -> pop 4
        1 < 2 -> pop 2

        stack = [1]


============================================================
6. MONOTONIC DECREASING STACK
============================================================

Elements are maintained in decreasing order.

Example:

    [9, 7, 5, 2]

Usually useful for:

    Next Greater Element
    Previous Greater Element
    Daily Temperatures
    Stock Span


Example:

    nums = [5, 3, 7]

    Process 5:
        stack = [5]

    Process 3:
        stack = [5, 3]

    Process 7:

        7 > 3 -> pop 3
        7 > 5 -> pop 5

        stack = [7]


============================================================
7. TWO-STACK TECHNIQUE
============================================================

Sometimes one problem uses two stacks.

Example:

    Min Stack

We can maintain:

    stack      -> actual values
    min_stack  -> minimum values

Example:

    push(5)
    push(3)
    push(7)

    stack:
        [5, 3, 7]

    min_stack:
        [5, 3, 3]

Now the minimum can be obtained in:

    O(1)


============================================================
8. STACK + HASHMAP
============================================================

A stack can be combined with a hashmap when we need:

    Stack:
        ordering / unresolved elements

    HashMap:
        fast lookup / frequency / mapping


Example use cases:

    Frequency-based problems
    Decode String
    Matching relationships
    Some monotonic-stack problems


============================================================
IMPORTANT DSA STACK PATTERNS
============================================================

Normal Stack
    ↓
    Matching / nesting / reverse processing

Monotonic Increasing Stack
    ↓
    Smaller-element relationships

Monotonic Decreasing Stack
    ↓
    Greater-element relationships

Two Stacks
    ↓
    Maintain two related states

Stack + HashMap
    ↓
    Ordering + fast lookup


============================================================
HOW TO RECOGNIZE A MONOTONIC STACK
============================================================

Look for phrases such as:

    "Next greater element"
    "Next smaller element"
    "Previous greater element"
    "Previous smaller element"
    "First greater element to the right"
    "First smaller element to the left"
    "Days until a warmer temperature"
    "Nearest smaller/greater element"

These are strong signals for:

    MONOTONIC STACK


============================================================
TIME COMPLEXITY OF MONOTONIC STACK
============================================================

Usually:

    Time  -> O(n)
    Space -> O(n)

Why O(n)?

Each element is:

    pushed at most once
    popped at most once

Therefore:

    n pushes + n pops
    = O(n)


============================================================
MOST IMPORTANT THING TO REMEMBER
============================================================

Do NOT memorize stacks only as:

    "LIFO data structure"

For DSA, think:

    STACK
      ↓
    Remember unresolved elements
      ↓
    Process them when a useful future element appears
      ↓
    Remove elements that are no longer useful
      ↓
    Often converts O(n²) → O(n)


============================================================
INTERVIEW CHEAT SHEET
============================================================

Need matching / nesting?
    → Normal Stack

Need next/previous greater?
    → Monotonic Stack

Need next/previous smaller?
    → Monotonic Stack

Need nearest greater/smaller?
    → Monotonic Stack

Need to maintain minimum/maximum?
    → Stack / Two Stacks

Need ordering + frequency/lookup?
    → Stack + HashMap

Need reverse-order processing?
    → Stack


============================================================
PRIORITY FOR DSA
============================================================

Learn in this order:

    1. Normal Stack
    2. Stack using Python list
    3. Matching Parentheses
    4. Monotonic Stack
    5. Increasing Monotonic Stack
    6. Decreasing Monotonic Stack
    7. Stack + HashMap
    8. Two-Stack problems
    9. Advanced problems

The MOST IMPORTANT stack pattern for array problems:

    MONOTONIC STACK ⭐
"""


##! Question 1: Remove All Adjacent Duplicates In String

"""

You are given a string s consisting of lowercase English letters. A duplicate removal consists of choosing two adjacent and equal letters and removing them.

We repeatedly make duplicate removals on s until we no longer can.

Return the final string after all such duplicate removals have been made. It can be proven that the answer is unique.

Example 1:

Input: s = "abbaca"
Output: "ca"
Explanation: 
For example, in "abbaca" we could remove "bb" since the letters are adjacent and equal, and this is the only possible move.  The result of this move is that the string is "aaca", of which only "aa" is possible, so the final string is "ca".
Example 2:

Input: s = "azxxzy"
Output: "ay"
 

Constraints:

1 <= s.length <= 10^5
s consists of lowercase English letters.

"""


##! Question 2: Valid Parentheses

"""

Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
Every close bracket has a corresponding open bracket of the same type.
 

Example 1:

Input: s = "()"

Output: true

Example 2:

Input: s = "()[]{}"

Output: true

Example 3:

Input: s = "(]"

Output: false

Example 4:

Input: s = "([])"

Output: true

Example 5:

Input: s = "([)]"

Output: false

 

Constraints:

1 <= s.length <= 104
s consists of parentheses only '()[]{}'.

"""
##! Question 3: Next Greater Element I

"""

The next greater element of some element x in an array is the first greater element that is to the right of x in the same array.

You are given two distinct 0-indexed integer arrays nums1 and nums2, where nums1 is a subset of nums2.

For each 0 <= i < nums1.length, find the index j such that nums1[i] == nums2[j] and determine the next greater element of nums2[j] in nums2. If there is no next greater element, then the answer for this query is -1.

Return an array ans of length nums1.length such that ans[i] is the next greater element as described above.

 

Example 1:

Input: nums1 = [4,1,2], nums2 = [1,3,4,2]
Output: [-1,3,-1]
Explanation: The next greater element for each value of nums1 is as follows:
- 4 is underlined in nums2 = [1,3,4,2]. There is no next greater element, so the answer is -1.
- 1 is underlined in nums2 = [1,3,4,2]. The next greater element is 3.
- 2 is underlined in nums2 = [1,3,4,2]. There is no next greater element, so the answer is -1.
Example 2:

Input: nums1 = [2,4], nums2 = [1,2,3,4]
Output: [3,-1]
Explanation: The next greater element for each value of nums1 is as follows:
- 2 is underlined in nums2 = [1,2,3,4]. The next greater element is 3.
- 4 is underlined in nums2 = [1,2,3,4]. There is no next greater element, so the answer is -1.
 

Constraints:

1 <= nums1.length <= nums2.length <= 1000
0 <= nums1[i], nums2[i] <= 10^4
All integers in nums1 and nums2 are unique.
All the integers of nums1 also appear in nums2.
 

Follow up: Could you find an O(nums1.length + nums2.length) solution?

"""


##! Question 4: Next Greater Element II

"""

Given a circular integer array nums (i.e., the next element of nums[nums.length - 1] is nums[0]), return the next greater number for every element in nums.

The next greater number of a number x is the first greater number to its traversing-order next in the array, which means you could search circularly to find its next greater number. If it doesn't exist, return -1 for this number.

 

Example 1:

Input: nums = [1,2,1]
Output: [2,-1,2]
Explanation: The first 1's next greater number is 2; 
The number 2 can't find next greater number. 
The second 1's next greater number needs to search circularly, which is also 2.
Example 2:

Input: nums = [1,2,3,4,3]
Output: [2,3,4,-1,4]
 

Constraints:

1 <= nums.length <= 10^4
-10^9 <= nums[i] <= 10^9

"""


##! Question 5: Daily Temperatures


"""

Given an array of integers temperatures represents the daily temperatures, return an array answer such that answer[i] is the number of days you have to wait after the ith day to get a warmer temperature. If there is no future day for which this is possible, keep answer[i] == 0 instead.

Example 1:

Input: temperatures = [73,74,75,71,69,72,76,73]
Output: [1,1,4,2,1,1,0,0]

Example 2:

Input: temperatures = [30,40,50,60]
Output: [1,1,1,0]

Example 3:

Input: temperatures = [30,60,90]
Output: [1,1,0]
 
Constraints:

1 <= temperatures.length <= 10^5
30 <= temperatures[i] <= 100

"""


##! Question 6: Previous greater element

"""

Given an array arr[], find the Previous Greater Element (PGE) for every element in the array.

The Previous Greater Element of an element x is defined as the first element to its left in the array that is greater than x.
If no such element exists for a particular position, the PGE should be considered as -1.
Examples: 

Input: arr[] = [10, 4, 2, 20, 40, 12]
Output: [-1, 10, 4, -1, -1, 40]
Explanation:
For 10 → No elements on the left → -1
For 4 → Previous greater element is 10 → 10
For 2 → Previous greater element is 4 → 4
For 20 → No element on the left greater than 20 → -1
For 40 → No element on the left greater than 40 → -1
For 12 → Previous greater element is 40 → 40

Input: arr[] = [10, 20, 30, 40]
Output: [-1, -1, -1, -1]
Explanation: Since the array is strictly increasing, no element has a greater element before it. Hence, all positions are assigned -1.

"""


##! Question 7: Remove Nodes From Linked List

"""

You are given the head of a linked list.

Remove every node which has a node with a greater value anywhere to the right side of it.

Return the head of the modified linked list.


Example 1:

Input: head = [5,2,13,3,8]
Output: [13,8]
Explanation: The nodes that should be removed are 5, 2 and 3.
- Node 13 is to the right of node 5.
- Node 13 is to the right of node 2.
- Node 8 is to the right of node 3.
Example 2:

Input: head = [1,1,1,1]
Output: [1,1,1,1]
Explanation: Every node has value 1, so no nodes are removed.
 

Constraints:

The number of the nodes in the given list is in the range [1, 105].
1 <= Node.val <= 10^5

"""


##! Question 8: Remove All Adjacent Duplicates in String II

"""

You are given a string s and an integer k, a k duplicate removal consists of choosing k adjacent and equal letters from s and removing them, causing the left and the right side of the deleted substring to concatenate together.

We repeatedly make k duplicate removals on s until we no longer can.

Return the final string after all such duplicate removals have been made. It is guaranteed that the answer is unique.

 

Example 1:

Input: s = "abcd", k = 2
Output: "abcd"
Explanation: There's nothing to delete.
Example 2:

Input: s = "deeedbbcccbdaa", k = 3
Output: "aa"
Explanation: 
First delete "eee" and "ccc", get "ddbbbdaa"
Then delete "bbb", get "dddaa"
Finally delete "ddd", get "aa"
Example 3:

Input: s = "pbbcggttciiippooaais", k = 2
Output: "ps"
 

Constraints:

1 <= s.length <= 10^5
2 <= k <= 104
s only contains lowercase English letters.

"""

##! Question 9: Simplify Path

"""

You are given an absolute path for a Unix-style file system, which always begins with a slash '/'. Your task is to transform this absolute path into its simplified canonical path.

The rules of a Unix-style file system are as follows:

A single period '.' represents the current directory.
A double period '..' represents the previous/parent directory.
Multiple consecutive slashes such as '//' and '///' are treated as a single slash '/'.
Any sequence of periods that does not match the rules above should be treated as a valid directory or file name. For example, '...' and '....' are valid directory or file names.
The simplified canonical path should follow these rules:

The path must start with a single slash '/'.
Directories within the path must be separated by exactly one slash '/'.
The path must not end with a slash '/', unless it is the root directory.
The path must not have any single or double periods ('.' and '..') used to denote current or parent directories.
Return the simplified canonical path.

 

Example 1:

Input: path = "/home/"

Output: "/home"

Explanation:

The trailing slash should be removed.

Example 2:

Input: path = "/home//foo/"

Output: "/home/foo"

Explanation:

Multiple consecutive slashes are replaced by a single one.

Example 3:

Input: path = "/home/user/Documents/../Pictures"

Output: "/home/user/Pictures"

Explanation:

A double period ".." refers to the directory up a level (the parent directory).

Example 4:

Input: path = "/../"

Output: "/"

Explanation:

Going one level up from the root directory is not possible.

Example 5:

Input: path = "/.../a/../b/c/../d/./"

Output: "/.../b/d"

Explanation:

"..." is a valid name for a directory in this problem.


Constraints:

1 <= path.length <= 3000
path consists of English letters, digits, period '.', slash '/' or '_'.
path is a valid absolute Unix path.

"""


##! Question 10: Remove K Digits

"""

Given string num representing a non-negative integer num, and an integer k, return the smallest possible integer after removing k digits from num.

 

Example 1:

Input: num = "1432219", k = 3
Output: "1219"
Explanation: Remove the three digits 4, 3, and 2 to form the new number 1219 which is the smallest.
Example 2:

Input: num = "10200", k = 1
Output: "200"
Explanation: Remove the leading 1 and the number is 200. Note that the output must not contain leading zeroes.
Example 3:

Input: num = "10", k = 2
Output: "0"
Explanation: Remove all the digits from the number and it is left with nothing which is 0.
 

Constraints:

1 <= k <= num.length <= 10^5
num consists of only digits.
num does not have any leading zeros except for the zero itself.

"""

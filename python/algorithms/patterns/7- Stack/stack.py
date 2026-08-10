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

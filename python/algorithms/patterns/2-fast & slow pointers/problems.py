"""
What is the Fast and Slow Pointers Pattern?
The Fast and Slow Pointers pattern (also known as Floyd's Cycle Detection Algorithm or the Tortoise and Hare technique) is a two-pointer strategy used to efficiently traverse data structures where:
Elements are connected in a sequence (e.g., linked list, number transformations, circular arrays).
You can "move" step by step through the structure.

You use:
Slow Pointer: moves 1 step at a time.
Fast Pointer: moves 2 steps at a time.

Where is this pattern useful?
This pattern is typically used in problems involving:
Cycle detection (in linked lists, number sequences, etc.)
Finding the middle of a list
Detecting palindromes in linked lists
Finding the start of a loop
Math-based problems that create a repetitive cycle (e.g., Happy Number)

How to Recognize When to Apply Fast and Slow Pointers
Look for these signs:
Repetition :You're repeatedly transforming or traversing values (e.g., linked list traversal, square-sum of digits).

Cycle possibility:The structure or transformation could lead to a loop (like a cycle in a linked list or in a number chain).

Need for midpoint: You need to find the middle element in one pass.

O(1) space required:You're asked to solve in constant space — fast & slow pointers do not use extra memory.

How to Apply the Pattern – Step-by-Step

Step 1: Initialize two pointers
slow = head;
fast = head;

Step 2: Traverse the structure
Move slow one step.
Move fast two steps.

while (fast != null && fast.next != null) {
slow = slow.next;
fast = fast.next.next;
...
}

Step 3: Watch for a meeting point
If slow == fast → there is a cycle (for detection problems).
If fast hits null → no cycle (or list has ended).

Step 4: Additional logic
Depending on the goal:
If looking for cycle start, reset slow and move both one step until they meet.
If looking for middle, return slow when fast hits end.
If looking for cycle in transformations (e.g., Happy Number), treat transformation as “next” movement.

Benefits of Fast and Slow Pointers

O(n): Time Linear traversal — no nested loops needed
O(1): Space Only two pointers used — no hashmap or extra storage
No modification: Works on original structure without altering it
Midpoint access: Efficient way to find middle of list
Cycle detection: Elegant way to detect loop existence or entry point

Example Use Case Patterns

Detect cycle: Linked List : Traverse nodes, check if slow == fast
Find loop start: Linked List : After meeting, reset slow to head
Find middle : Linked List : Stop when fast == null
Happy Number : Integer Problem : Apply next-transform function repeatedly
Circular array loop : Array + Modulo : Move with (i + nums[i]) % n, apply cycle logic

"""

# Question 1 : Linked List Cycle

"""
Given head, the head of a linked list, determine if the linked list has a cycle in it.

There is a cycle in a linked list if there is some node in the list that can be reached again by continuously following the next pointer. Internally, pos is used to denote the index of the node that tail's next pointer is connected to. Note that pos is not passed as a parameter.

Return true if there is a cycle in the linked list. Otherwise, return false.

Example 1:
Input: head = [3,2,0,-4], pos = 1      => Here in this example -4 again points to 2
Output: true
Explanation: There is a cycle in the linked list, where the tail connects to the 1st node (0-indexed).

Example 2:
Input: head = [1], pos = -1     => Here in this example -1 denotes 1 points to null
Output: false
Explanation: There is no cycle in the linked list.
 
Constraints:

The number of the nodes in the list is in the range [0, 104].
-105 <= Node.val <= 105
pos is -1 or a valid index in the linked-list.
"""


def linkedListCycleDetection(head):
    slow = head
    fast = head
    while fast is not None and fast.next is not None:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            return True
    return False


# test code
class node:
    def __init__(self, value):
        self.value = value
        self.next = None


# creating nodes
n1 = node(3)
n2 = node(2)
n3 = node(0)
n4 = node(-4)

# connecting nodes
n1.next = n2
n2.next = n3
n3.next = n4
n4.next = n1

head = n4
print(linkedListCycleDetection(head))


# Question 2: Linked List cycle II

"""
Given the head of a linked list, return the node where the cycle begins. If there is no cycle, return null.

There is a cycle in a linked list if there is some node in the list that can be reached again by continuously following the next pointer. Internally, pos is used to denote the index of the node that tail's next pointer is connected to (0-indexed). It is -1 if there is no cycle. Note that pos is not passed as a parameter.

Do not modify the linked list.

Constraints:

The number of the nodes in the list is in the range [0, 104].
-105 <= Node.val <= 105
pos is -1 or a valid index in the linked-list.
"""


def detectCycle(head):
    slow = head
    fast = head

    # Phase 1: Detect cycle
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next

        if slow == fast:
            # Phase 2: Find cycle start
            slow = head
            while slow != fast:
                slow = slow.next
                fast = fast.next
            return slow  # start of cycle

    return None


# test code

# creating nodes
n1 = node(3)
n2 = node(2)
n3 = node(0)
n4 = node(1)
n5 = node(-4)

# connecting nodes
n1.next = n2
n2.next = n3
n3.next = n4
n4.next = n5
n5.next = n2

head = n1
print(detectCycle(head))

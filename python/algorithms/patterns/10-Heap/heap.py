"""
============================================================
                    HEAP — DSA PATTERN
============================================================

A Heap is a specialized tree-based data structure used when
we repeatedly need access to the smallest or largest element.

The two main types are:

1. Min Heap
   -> Smallest element is always at the top.

2. Max Heap
   -> Largest element is always at the top.

The most important idea:

    Heap = Efficient access to an extreme element.

If a problem repeatedly asks:

    - smallest element
    - largest element
    - remove smallest
    - remove largest
    - K smallest
    - K largest
    - Kth smallest/largest
    - highest/lowest priority
    - next minimum/maximum
    - scheduling by priority

then a Heap should immediately come to mind.


============================================================
                    WHY DO WE NEED HEAPS?
============================================================

Suppose we have:

    nums = [8, 2, 5, 1, 9, 3]

If we want the smallest element, we could sort:

    nums.sort()

But sorting costs:

    O(n log n)

A Heap allows us to access the minimum in:

    O(1)

and insert/remove elements in:

    O(log n)

This becomes extremely useful when we repeatedly insert and
remove elements.

For example:

    Insert 5
    Insert 2
    Insert 8
    Remove minimum
    Insert 1
    Remove minimum
    ...

Sorting the entire collection after every operation would be
wasteful.

A Heap maintains enough ordering to efficiently give us the
minimum or maximum without completely sorting everything.


============================================================
                    HEAP PROPERTY
============================================================

A Heap is a Complete Binary Tree.

A Complete Binary Tree means:

    - Every level is completely filled
      except possibly the last level.

    - The last level is filled from left to right.


MIN HEAP:

                    1
                  /   \
                 3     2
                / \
               7   5

The rule is:

    parent <= children

Therefore:

    The smallest element is always at the root.


MAX HEAP:

                    10
                  /    \
                 7      8
                / \
               3   5

The rule is:

    parent >= children

Therefore:

    The largest element is always at the root.


IMPORTANT:

A Heap is NOT a fully sorted data structure.

For example, a valid Min Heap could be:

    [1, 3, 2, 7, 5, 8]

This does NOT mean:

    1 <= 3 <= 2 <= 7 ...

The entire array is not sorted.

The only guarantee is:

    Every parent <= its children

Therefore, the root is guaranteed to be the minimum.


============================================================
                    HEAP AS AN ARRAY
============================================================

Although a Heap is conceptually a binary tree, it is usually
stored inside an array.

Example:

                    1
                  /   \
                 3     2
                / \   /
               7   5 8

Array representation:

    [1, 3, 2, 7, 5, 8]


For an element at index i:

    Left child:

        2 * i + 1

    Right child:

        2 * i + 2

    Parent:

        (i - 1) // 2


Example:

    heap = [1, 3, 2, 7, 5, 8]

Index 1 contains 3.

Left child:

    2 * 1 + 1 = 3

    heap[3] = 7

Right child:

    2 * 1 + 2 = 4

    heap[4] = 5

Parent:

    (1 - 1) // 2 = 0

    heap[0] = 1


============================================================
                    PYTHON HEAP
============================================================

Python provides the built-in heapq module.

    import heapq

Python's heapq implements a:

    MIN HEAP

by default.


Basic example:

"""

import heapq

heap = []

heapq.heappush(heap, 5)
heapq.heappush(heap, 2)
heapq.heappush(heap, 8)
heapq.heappush(heap, 1)

print(heap[0])  # 1


"""
The smallest element is always available at:

    heap[0]

Important:

    heap[0] gives the minimum.

    heapq.heappop(heap)
    removes and returns the minimum.


============================================================
                    HEAP OPERATIONS
============================================================

1. heappush()
----------------

Insert an element into the heap.

    heapq.heappush(heap, value)

Time:

    O(log n)


Why?

The element may need to move upward to restore the Heap
property.

This process is commonly called:

    Sift Up
    Bubble Up


2. heappop()
----------------

Remove and return the smallest element.

    heapq.heappop(heap)

Time:

    O(log n)


The root is removed and another element is moved to the root.
The Heap is then repaired.

This process is commonly called:

    Sift Down
    Bubble Down


3. Get minimum
----------------

    heap[0]

Time:

    O(1)

No removal happens.


4. Build a heap
----------------

If we already have a list:

    nums = [5, 2, 8, 1, 3]

we can convert it into a heap:

    heapq.heapify(nums)

Time:

    O(n)

Important:

    heapify() is O(n)

It is NOT O(n log n).


============================================================
                    TIME COMPLEXITIES
============================================================

Operation                  Time

Get minimum               O(1)

Insert                    O(log n)

Remove minimum            O(log n)

Build heap                O(n)

Search arbitrary value    O(n)

Remove arbitrary value    O(n)

"""


heap = [5, 2, 8, 1, 3]

heapq.heapify(heap)

print(heap)

"""
After heapify(), the list satisfies the Min Heap property.

Do NOT expect the list to be sorted.

The important guarantee is:

    heap[0] == minimum


============================================================
                    MAX HEAP IN PYTHON
============================================================

Python's heapq is a Min Heap.

To simulate a Max Heap, negate the values.

Example:

    Original:

        10, 5, 20

    Negated:

        -10, -5, -20

The Min Heap considers:

    -20 < -10 < -5

So -20 comes first.

But:

    -(-20) = 20

Therefore, we can use a Min Heap as a Max Heap by storing
negative values.

"""


max_heap = []

heapq.heappush(max_heap, -10)
heapq.heappush(max_heap, -5)
heapq.heappush(max_heap, -20)

largest = -heapq.heappop(max_heap)

print(largest)  # 20


"""
============================================================
              THE MOST IMPORTANT HEAP PATTERN
============================================================

Ask yourself:

    "What element do I repeatedly need?"

If the answer is:

    smallest

use:

    MIN HEAP


If the answer is:

    largest

use:

    MAX HEAP


This is the fundamental Heap decision.


============================================================
                    HOW TO RECOGNIZE A HEAP PROBLEM
============================================================

Look for words like:

    - minimum
    - maximum
    - smallest
    - largest
    - Kth smallest
    - Kth largest
    - Top K
    - K smallest
    - K largest
    - most frequent
    - least frequent
    - highest priority
    - lowest priority
    - next available
    - closest K elements
    - merge K sorted structures
    - continuously changing minimum/maximum
    - scheduling
    - priority queue


Especially pay attention when the problem says:

    "Repeatedly remove the smallest..."

or:

    "Repeatedly remove the largest..."


That is a very strong Heap signal.


============================================================
                  WHEN IS HEAP OPTIMAL?
============================================================

A Heap is usually useful when:

    1. We repeatedly need the minimum/maximum.

    2. New elements are continuously arriving.

    3. Elements are continuously being removed.

    4. We only need the Top K elements.

    5. Fully sorting the data would be unnecessary.

    6. We need a Priority Queue.

    7. We need to merge multiple sorted collections.

    8. We need to efficiently choose the next best candidate.


The key question is:

    "Do I need the entire collection sorted,
     or do I only need the current smallest/largest element?"


If you need everything sorted:

    Sorting may be better.


If you repeatedly need only the smallest/largest:

    Heap is often better.


============================================================
                 HEAP VS SORTING
============================================================

Suppose:

    nums = [10, 2, 7, 5, 1, 8]

If you need:

    "Return the entire array sorted"

Use:

    nums.sort()

because you actually need all elements ordered.


But if you need:

    "Repeatedly remove the smallest element"

A Heap is usually better.

Sorting:

    O(n log n)

Heap:

    Build heap: O(n)

    n removals:
        O(n log n)

Both can end up O(n log n), but the Heap has an important
advantage:

    It maintains the structure dynamically.

You can insert new elements while processing.


============================================================
                PATTERN 1 — K LARGEST
============================================================

Problem:

    Find the K largest elements.

Example:

    nums = [3, 2, 1, 5, 6, 4]
    k = 2

Answer:

    [5, 6]


A common mistake is to think:

    "K largest -> Max Heap"

But for the Top-K pattern, we usually use:

    K largest -> MIN HEAP


Why?

Suppose:

    k = 2

We want to maintain only the two largest numbers.

Imagine our heap contains:

    [5, 6]

The smallest among our current candidates is:

    5

If a new number 10 arrives:

    [5, 6, 10]

We now have 3 candidates but only need 2.

Who should leave?

    5

Therefore, we want the smallest candidate to be immediately
available.

A Min Heap gives us exactly that.

So:

    K largest -> Min Heap of size K


Code:
"""


def k_largest(nums: list[int], k: int) -> list[int]:
    heap = []

    for num in nums:
        heapq.heappush(heap, num)

        if len(heap) > k:
            heapq.heappop(heap)

    return heap


"""
Time:

    O(n log k)

Space:

    O(k)


Compare with sorting:

    O(n log n)

If k is much smaller than n, the Heap solution is better.


============================================================
                PATTERN 2 — K SMALLEST
============================================================

Now suppose:

    Find the K smallest elements.

Example:

    nums = [7, 10, 4, 3, 20, 15]
    k = 3

Answer:

    [3, 4, 7]


For K smallest, use:

    MAX HEAP of size K


Why?

Suppose our current candidates are:

    [3, 4, 7]

The largest among our K candidates is:

    7

If a new number 1 arrives:

    [3, 4, 7, 1]

We only want 3 elements.

The worst candidate is:

    7

Therefore, we need quick access to the largest candidate.

That is exactly what a Max Heap provides.


Important pattern:

    K largest  -> Min Heap
    K smallest -> Max Heap


============================================================
             WHY IS THE HEAP OPPOSITE FOR TOP K?
============================================================

This is one of the most important Heap concepts.

For K largest:

    We keep the K largest numbers.

    The WORST candidate is the smallest one.

    Therefore:

        Min Heap


For K smallest:

    We keep the K smallest numbers.

    The WORST candidate is the largest one.

    Therefore:

        Max Heap


Think:

    "What candidate should be kicked out
     when a better candidate arrives?"

That element should be at the root.


============================================================
                PATTERN 3 — KTH LARGEST
============================================================

Problem:

    nums = [3, 2, 1, 5, 6, 4]
    k = 2

Find:

    2nd largest

Sorted:

    [1, 2, 3, 4, 5, 6]

Answer:

    5


Instead of sorting everything:

    Maintain a Min Heap of size K.


The heap contains:

    The K largest numbers seen so far.


At the end:

    heap[0]

is the Kth largest element.


Code:
"""


def kth_largest(nums: list[int], k: int) -> int:
    heap = []

    for num in nums:
        heapq.heappush(heap, num)

        if len(heap) > k:
            heapq.heappop(heap)

    return heap[0]


"""
Time:

    O(n log k)

Space:

    O(k)


============================================================
                PATTERN 4 — TOP K FREQUENT
============================================================

Many problems first require a frequency map and then a Heap.

Example:

    nums = [1, 1, 1, 2, 2, 3]

Frequency:

    1 -> 3
    2 -> 2
    3 -> 1

Top 2:

    [1, 2]


General pattern:

    Step 1:
        Count frequencies using a dictionary.

    Step 2:
        Maintain a Heap of size K.

    Step 3:
        Remove the least useful candidate when
        heap size becomes greater than K.


This pattern is useful for:

    - Top K frequent elements
    - Top K frequent words
    - Top K most common values
    - Top K scores
    - Top K recommendations


============================================================
             PATTERN 5 — PRIORITY QUEUE
============================================================

A Priority Queue is a data structure where the next element
to process is determined by priority rather than insertion
order.

Normal Queue:

    A -> B -> C

    First in -> First out


Priority Queue:

    A -> priority 5
    B -> priority 1
    C -> priority 10

Processing order:

    C
    A
    B


A Heap is commonly used to implement a Priority Queue.


Typical applications:

    - CPU scheduling
    - Job scheduling
    - Task management
    - Network packet processing
    - Event simulation
    - Dijkstra's algorithm
    - A* search


Example:
"""


tasks = [
    (5, "Task A"),
    (1, "Task B"),
    (3, "Task C"),
]

heap = []

for priority, task in tasks:
    heapq.heappush(heap, (priority, task))

while heap:
    priority, task = heapq.heappop(heap)
    print(task)


"""
The task with the smallest priority value is processed first.


============================================================
          PATTERN 6 — MERGE K SORTED LISTS
============================================================

Suppose we have:

    [1, 4, 7]
    [2, 5, 8]
    [3, 6, 9]

We want:

    [1, 2, 3, 4, 5, 6, 7, 8, 9]


At any moment, we only care about:

    The smallest currently available element.


Put the first element from every list into a Min Heap:

    1
    2
    3


Remove 1.

Then insert the next element from the list containing 1:

    4


Heap now represents:

    2
    3
    4


Remove 2.

Insert 5.

Continue.

This is why Heap is ideal for:

    "Find the smallest element among K sources."


This pattern appears in:

    - Merge K sorted arrays
    - Merge K sorted linked lists
    - External sorting
    - Multi-way merge


============================================================
              PATTERN 7 — TWO HEAPS
============================================================

Two Heaps are often used when we need to maintain a dynamic
median.

We divide the numbers into two halves:

                Numbers
                   |
          ---------------------
          |                   |
     Smaller half         Larger half
          |                   |
      MAX HEAP            MIN HEAP


Max Heap:

    Gives the largest number from the smaller half.


Min Heap:

    Gives the smallest number from the larger half.


Example:

    Numbers:

        [1, 2, 3, 4, 5, 6]


Smaller half:

        [1, 2, 3]

Larger half:

        [4, 5, 6]


Max Heap:

        [3, 2, 1]

Min Heap:

        [4, 5, 6]


The two middle values are:

        3 and 4

Median:

        (3 + 4) / 2


This pattern is called:

    TWO HEAPS


Common problem:

    Find Median from Data Stream


============================================================
                PATTERN 8 — DIJKSTRA
============================================================

Dijkstra's shortest path algorithm repeatedly needs:

    The unprocessed node with the smallest distance.


That is exactly:

    MIN HEAP


Instead of scanning all nodes to find the minimum:

    O(V)

we use a Heap to efficiently retrieve the next smallest
distance.

With an adjacency list and binary Heap:

    O((V + E) log V)


This is one of the most important algorithmic applications
of a Heap.


============================================================
                 PATTERN 9 — SCHEDULING
============================================================

Many scheduling problems involve:

    "Which task should happen next?"


If the answer depends on:

    earliest finishing time
    smallest processing time
    highest priority
    earliest deadline
    smallest cost

a Heap may be useful.


Typical pattern:

    1. Add available tasks to Heap.

    2. Heap chooses the best task.

    3. Process it.

    4. Add newly available tasks.

    5. Repeat.


This is commonly combined with:

    Sorting + Heap


============================================================
             HEAP + SORTING COMBINATION
============================================================

A very common advanced pattern is:

    SORT first

then:

    USE HEAP while processing.


For example, scheduling problems may require:

    1. Sort jobs by start time.

    2. Add all currently available jobs
       to a Min Heap.

    3. Select the job with the smallest
       end time / priority / cost.

    4. Continue.


This combination is extremely common in:

    - Meeting room problems
    - CPU scheduling
    - Job scheduling
    - Event scheduling


============================================================
               HEAP VS OTHER DATA STRUCTURES
============================================================

Array:

    Good for:
        Direct indexing.

    Bad for:
        Repeated min/max extraction.


Sorted Array:

    Good for:
        Searching/order.

    Bad for:
        Frequent insertion.


Hash Map:

    Good for:
        Key/value lookup.

    Bad for:
        Maintaining minimum/maximum ordering.


Stack:

    Good for:
        Last In First Out.


Queue:

    Good for:
        First In First Out.


Heap:

    Good for:
        Repeated minimum/maximum extraction.


============================================================
               HEAP VS HASHMAP
============================================================

A HashMap answers:

    "Do I have this key?"

A Heap answers:

    "What is the smallest/largest current element?"


Example:

    nums = [5, 2, 8, 1]


HashMap:

    Can efficiently answer:

        Does 8 exist?


Heap:

    Can efficiently answer:

        What is the minimum?


These solve completely different problems.


============================================================
             HEAP VS TWO POINTERS
============================================================

Two pointers are generally useful when:

    - Data is sorted.
    - We process elements from both ends.
    - We have a monotonic structure.


Heap is useful when:

    - We dynamically need min/max.
    - Elements arrive or disappear.
    - We need Top K.
    - We need a Priority Queue.


============================================================
                HEAP VS SORTING
============================================================

Use SORTING when:

    You need the entire data ordered.


Use HEAP when:

    You only repeatedly need the minimum/maximum.


Example:

    "Return the 10 largest elements."

Could use:

    Sorting:
        O(n log n)

or:

    Min Heap:
        O(n log 10)
        = O(n log k)


If k is small compared to n, Heap is usually preferable.


============================================================
             HOW TO DETERMINE IF HEAP IS OPTIMAL
============================================================

Ask these questions:


QUESTION 1:

    Do I repeatedly need the minimum or maximum?

If YES:

    Think Heap.


QUESTION 2:

    Do I only need K elements instead of all elements?

If YES:

    Think Top-K Heap.


QUESTION 3:

    Are elements continuously being inserted?

If YES:

    Heap may be useful.


QUESTION 4:

    Are elements continuously being removed based
    on priority?

If YES:

    Think Priority Queue / Heap.


QUESTION 5:

    Am I repeatedly choosing the "best" next candidate?

If "best" means:

    smallest
    largest
    earliest
    cheapest
    highest priority

then:

    Think Heap.


QUESTION 6:

    Am I merging multiple sorted sources?

If YES:

    Think Min Heap.


QUESTION 7:

    Do I need a dynamic median?

If YES:

    Think Two Heaps.


============================================================
                 IMPORTANT TOP-K RULE
============================================================

MEMORIZE THIS:

    K LARGEST
        ↓
    MIN HEAP


    K SMALLEST
        ↓
    MAX HEAP


Why?

Because the root should represent the WORST candidate
currently inside our K candidates.

K largest:

    Worst = smallest

    Therefore:
        Min Heap


K smallest:

    Worst = largest

    Therefore:
        Max Heap


This single idea solves many Top-K problems.


============================================================
                  COMMON HEAP PROBLEMS
============================================================

Beginner / Intermediate:

    1. Kth Largest Element
    2. Kth Smallest Element
    3. K Largest Elements
    4. K Smallest Elements
    5. Top K Frequent Elements
    6. Last Stone Weight
    7. K Closest Points to Origin
    8. Relative Ranks
    9. Sort Characters By Frequency


Intermediate / Advanced:

    10. Merge K Sorted Lists
    11. Meeting Rooms II
    12. Task Scheduler
    13. Find Median from Data Stream
    14. Sliding Window Median
    15. IPO
    16. Smallest Range Covering Elements from K Lists
    17. Dijkstra's Algorithm
    18. A* Search


============================================================
                 K CLOSEST POINTS PATTERN
============================================================

Suppose:

    points = [
        [1, 3],
        [-2, 2],
        [5, 8],
        [0, 1]
    ]

We want:

    K closest points to the origin.


Distance can be calculated using:

    x² + y²


We don't actually need the square root because:

    sqrt(a) < sqrt(b)

whenever:

    a < b


For Top K closest:

    We want the K SMALLEST distances.

Therefore:

    Max Heap of size K


Why Max Heap?

Because among our current K closest points, the worst point
is the one with the largest distance.

That point should be at the root so we can remove it when a
closer point arrives.


============================================================
                 HEAP WITH TUPLES
============================================================

Python's heapq can compare tuples.

Example:

    heapq.heappush(heap, (distance, point))


The Heap first compares:

    distance

If distances are equal, Python compares:

    point


This is very useful for:

    Priority Queues
    Dijkstra
    Scheduling
    K closest points
    K frequent elements


Example:
"""


heap = []

heapq.heappush(heap, (10, "A"))
heapq.heappush(heap, (3, "B"))
heapq.heappush(heap, (7, "C"))

print(heapq.heappop(heap))

# (3, "B")


"""
The smallest priority/distance comes out first.


============================================================
                 IMPORTANT PYTHON TRICK
============================================================

For a Max Heap with tuples:

    heapq.heappush(heap, (-priority, value))


Example:
"""


heap = []

heapq.heappush(heap, (-10, "A"))
heapq.heappush(heap, (-5, "B"))
heapq.heappush(heap, (-20, "C"))

priority, value = heapq.heappop(heap)

print(-priority, value)

# 20 C


"""
============================================================
                  HEAP COMMON MISTAKES
============================================================

MISTAKE 1:

Thinking the Heap is sorted.

Wrong.

A Heap only guarantees the Heap property.


MISTAKE 2:

Using a Max Heap for K largest.

Usually wrong for the Top-K pattern.

Correct:

    K largest -> Min Heap


MISTAKE 3:

Calling heap.sort()

A Heap does not need to be sorted.

The purpose is efficient min/max access.


MISTAKE 4:

Assuming searching is O(log n).

Heap search for an arbitrary value is:

    O(n)


Only the root is guaranteed to be min/max.


MISTAKE 5:

Using a Heap when you need the entire sorted order.

If the problem says:

    "Return all elements sorted"

then sorting is usually more appropriate.


MISTAKE 6:

Forgetting that Python heapq is a Min Heap.

Python:

    heapq -> Min Heap


Max Heap:

    Store negative values.


============================================================
                    HEAP CHEAT SHEET
============================================================

Python:

    import heapq


Create:

    heap = []


Insert:

    heapq.heappush(heap, value)

    O(log n)


Get minimum:

    heap[0]

    O(1)


Remove minimum:

    heapq.heappop(heap)

    O(log n)


Convert list into Heap:

    heapq.heapify(nums)

    O(n)


Max Heap:

    heapq.heappush(heap, -value)

    maximum = -heapq.heappop(heap)


============================================================
                    PATTERN CHEAT SHEET
============================================================

Problem                          Approach

Minimum repeatedly               Min Heap

Maximum repeatedly               Max Heap

K largest                        Min Heap of size K

K smallest                       Max Heap of size K

Kth largest                      Min Heap of size K

Kth smallest                     Max Heap of size K

Top K frequent                   Heap + frequency map

K closest                        Max Heap of size K

Merge K sorted lists             Min Heap

Priority Queue                   Heap

Scheduling                       Heap

Dijkstra                         Min Heap

Dynamic Median                   Two Heaps

Smaller half                     Max Heap

Larger half                      Min Heap


============================================================
                    THE CORE INTUITION
============================================================

The most important thing to remember:

    A Heap does NOT give you complete ordering.

    It gives you FAST ACCESS to one extreme.


Min Heap:

                    MIN
                     ↓
                    root

Max Heap:

                    MAX
                     ↓
                    root


Therefore:

    If the problem repeatedly asks:

        "What is the smallest?"

            -> Min Heap


        "What is the largest?"

            -> Max Heap


        "What are the K largest?"

            -> Min Heap of size K


        "What are the K smallest?"

            -> Max Heap of size K


        "What is the Kth largest?"

            -> Min Heap of size K


        "What is the Kth smallest?"

            -> Max Heap of size K


============================================================
                    FINAL DECISION TREE
============================================================

When you see a problem, ask:

                Do I need
              min / max repeatedly?
                       |
                +------+------+
                |             |
               YES            NO
                |             |
             HEAP          Probably not
                |
        +-------+--------+
        |                |
      Min?              Max?
        |                |
    Min Heap          Max Heap


If the problem asks:

            "Top K?"

                |
                v

        +-------+--------+
        |                |
     K largest        K smallest
        |                |
    Min Heap          Max Heap
    size K            size K


If the problem asks:

    "Dynamic median?"

        ↓

    Two Heaps

        Max Heap
        smaller half

        Min Heap
        larger half


If the problem asks:

    "Merge K sorted sources?"

        ↓

    Min Heap


If the problem asks:

    "Choose next task based on priority?"

        ↓

    Priority Queue / Heap


============================================================
                    BIG-O SUMMARY
============================================================

Operation:

    Get min/max:
        O(1)

    Insert:
        O(log n)

    Remove min/max:
        O(log n)

    Build Heap:
        O(n)

    Search arbitrary element:
        O(n)


Top K:

    Sorting:
        O(n log n)

    Heap:
        O(n log k)


This is why Heap is especially powerful when:

    k << n


============================================================
                    ONE-LINE MEMORY RULES
============================================================

    MIN HEAP
        -> smallest comes out first.


    MAX HEAP
        -> largest comes out first.


    K LARGEST
        -> Min Heap of size K.


    K SMALLEST
        -> Max Heap of size K.


    KTH LARGEST
        -> Min Heap of size K.


    KTH SMALLEST
        -> Max Heap of size K.


    TOP K FREQUENT
        -> Frequency Map + Heap.


    K CLOSEST
        -> Usually Max Heap of size K.


    MERGE K SORTED
        -> Min Heap.


    PRIORITY QUEUE
        -> Heap.


    DYNAMIC MEDIAN
        -> Two Heaps.


    DIJKSTRA
        -> Min Heap.


============================================================
                    CORE IDEA TO REMEMBER
============================================================

Don't memorize Heap problems individually.

Instead, recognize the underlying requirement:

        "I repeatedly need the best/worst
         element according to some ordering."


If "best" means:

        smallest
        largest
        earliest
        cheapest
        highest priority
        closest

then ask:

        "Can a Heap give me that element efficiently?"


If YES:

        Heap is likely the correct pattern.


The deepest Heap intuition is:

        HEAP = KEEP THE BEST CANDIDATE
               EASILY ACCESSIBLE

and for Top-K problems:

        KEEP ONLY K CANDIDATES

while the root stores the candidate that should be
removed first when a better candidate appears.
"""

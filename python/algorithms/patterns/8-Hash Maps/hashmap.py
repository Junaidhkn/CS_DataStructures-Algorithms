"""
============================================================
                    HASHMAP DSA PATTERN
============================================================

1. WHAT IS A HASHMAP?
------------------------------------------------------------

A HashMap is a data structure that stores data in the form:

    KEY -> VALUE

In Python, the built-in `dict` is a HashMap.

Example:

    freq = {
        "a": 3,
        "b": 2,
        "c": 1,
    }

Here:

    "a" -> 3
    "b" -> 2
    "c" -> 1

The main power of a HashMap is that it allows us to find,
insert, and update information very quickly.

Average time complexity:

    Insert:    O(1)
    Lookup:    O(1)
    Delete:    O(1)

This is why HashMaps are extremely useful in DSA.

Instead of repeatedly searching through an array:

    O(n)

we can often store information in a HashMap and retrieve it
in approximately:

    O(1)


============================================================
2. THE CORE IDEA
============================================================

The fundamental idea behind the HashMap pattern is:

    "Store information that you have already seen so that
     you can retrieve it quickly later."

Think of it as creating a memory for your algorithm.

Without a HashMap:

    "Have I seen this before?"
        -> Search the entire array
        -> O(n)

With a HashMap:

    "Have I seen this before?"
        -> dictionary lookup
        -> O(1) average


Example:

    nums = [2, 7, 11, 15]
    target = 9

We need to find two numbers whose sum is 9.

Brute force:

    2 + 7
    2 + 11
    2 + 15
    7 + 11
    ...

This takes O(n²).

HashMap idea:

    For every number, calculate:

        complement = target - current_number

    Then ask:

        "Have I already seen complement?"

For 2:

    complement = 9 - 2 = 7

    Have we seen 7?
        No.

Store:

    2 -> index 0


For 7:

    complement = 9 - 7 = 2

    Have we seen 2?
        Yes!

Therefore:

    [2, 7]

The HashMap acts as our memory.


============================================================
3. WHY IS IT CALLED A HASHMAP?
============================================================

A HashMap uses a hashing mechanism internally to determine
where a key should be stored.

Conceptually:

    key
     |
     v
   HASH FUNCTION
     |
     v
  storage location

This allows the data structure to jump close to the location
where the key's value is stored instead of scanning every
element.

You normally do NOT need to implement the hashing mechanism
yourself in DSA problems.

In Python:

    dict

already provides this functionality.


============================================================
4. HASHMAP VS ARRAY
============================================================

Suppose:

    nums = [10, 20, 30, 40]

If we want to find whether 30 exists:

Array:

    Search -> 10 -> 20 -> 30

Worst case:

    O(n)

HashMap:

    nums_map = {
        10: True,
        20: True,
        30: True,
        40: True,
    }

Lookup:

    nums_map[30]

Average:

    O(1)


This is the main reason we trade:

    SPACE

for:

    TIME


We use additional memory to avoid repeated searching.


============================================================
5. THE MOST IMPORTANT HASHMAP PATTERN
============================================================

The most common pattern is:

    SEE SOMETHING
        |
        v
    STORE IT
        |
        v
    USE IT LATER


For example:

    for num in nums:

        if num in seen:
            ...

        seen[num] = ...


The exact information we store depends on the problem.

We may store:

    number -> index

or:

    number -> frequency

or:

    prefix_sum -> frequency

or:

    character -> frequency

or:

    value -> last_seen_index

or:

    value -> some calculated information


============================================================
6. WHEN SHOULD I THINK "HASHMAP"?
============================================================

HashMap should immediately come to mind when you see
questions involving:

    - "Have I seen this before?"
    - "Find duplicates"
    - "Count frequencies"
    - "How many times?"
    - "Find a pair"
    - "Find a complement"
    - "Find matching values"
    - "First occurrence"
    - "Last occurrence"
    - "Index of previous occurrence"
    - "Group similar items"
    - "Count subarrays"
    - "Count pairs"
    - "Store previously calculated information"


A particularly strong signal is:

    "Find something that has already appeared."


============================================================
7. HASHMAP FOR FREQUENCY COUNTING
============================================================

One of the most common uses of a HashMap is counting.

Example:

    nums = [1, 2, 2, 3, 3, 3]

We want:

    1 -> 1
    2 -> 2
    3 -> 3


Python:

    freq = {}

    for num in nums:
        freq[num] = freq.get(num, 0) + 1


Why does this work?

Initially:

    {}

Read 1:

    freq[1] = 0 + 1

    {1: 1}

Read 2:

    {1: 1, 2: 1}

Read another 2:

    {1: 1, 2: 2}

Read 3 three times:

    {1: 1, 2: 2, 3: 3}


This converts a repeated-search/counting problem into a
single O(n) traversal.


============================================================
8. HASHMAP FOR "TWO SUM"
============================================================

Problem:

    Given an array, find two numbers whose sum equals target.


Example:

    nums = [2, 7, 11, 15]
    target = 9


Brute force:

    Check every pair.

Time:

    O(n²)

HashMap:

    seen = {}

    for i, num in enumerate(nums):

        complement = target - num

        if complement in seen:
            return [seen[complement], i]

        seen[num] = i


Step-by-step:

    num = 2

    complement = 7

    7 not seen.

    Store:

        2 -> 0


Next:

    num = 7

    complement = 2

    2 IS seen.

    Therefore:

        [0, 1]


Complexity:

    Time:  O(n)
    Space: O(n)


This is a classic example of trading:

    O(n) SPACE

for:

    O(n²) -> O(n) TIME


============================================================
9. HASHMAP FOR DUPLICATES
============================================================

Problem:

    Determine whether an array contains duplicates.


Example:

    nums = [1, 2, 3, 1]

Approach:

    seen = set()

    for num in nums:

        if num in seen:
            return True

        seen.add(num)

    return False


Notice something important:

We don't necessarily need a dictionary here.

A SET is essentially the HashMap pattern when we only care
about whether a key exists.

Therefore:

    HashMap pattern
        |
        +---- dict  -> key + value
        |
        +---- set   -> key only


Complexity:

    Time:  O(n)
    Space: O(n)


============================================================
10. HASHMAP FOR LAST SEEN POSITION
============================================================

Sometimes we don't care about frequency.

We care about:

    "Where did I see this value last?"


Example:

    s = "abcabcbb"

We can store:

    character -> last index


Initially:

    {}

Read:

    a -> 0

    {
        "a": 0
    }

Read:

    b -> 1

    {
        "a": 0,
        "b": 1
    }

Read:

    c -> 2

    {
        "a": 0,
        "b": 1,
        "c": 2
    }

Read another a:

    a was previously at index 0.

    Move its recorded position:

    {
        "a": 3,
        "b": 1,
        "c": 2
    }


This pattern is heavily used in:

    Longest Substring Without Repeating Characters


The HashMap is answering:

    "Where was the previous occurrence?"


============================================================
11. HASHMAP + SLIDING WINDOW
============================================================

HashMaps frequently work together with the Sliding Window
pattern.

Example:

    Longest Substring Without Repeating Characters


Input:

    "abcabcbb"


We maintain:

    left
    right
    last_seen


HashMap:

    character -> most recent index


When a duplicate appears, we can move `left` directly to
the correct position instead of moving it one step at a time.


Conceptually:

    right
      |
      v
    a b c a
    ^     ^
    |     |
   left  duplicate


If:

    last_seen["a"] = 0

and current index is:

    3

then:

    left = last_seen["a"] + 1

    left = 1


This allows the algorithm to remain O(n).


============================================================
12. HASHMAP + PREFIX SUM
============================================================

This is one of the MOST IMPORTANT HashMap patterns.

Consider:

    Subarray Sum Equals K


Example:

    nums = [1, 1, 1]
    k = 2


We want to count subarrays whose sum is 2.

The important mathematical relationship is:

    prefix_sum[j] - prefix_sum[i] = k

Therefore:

    prefix_sum[i] = prefix_sum[j] - k


This means while calculating the current prefix sum, we can
ask:

    "Have I previously seen prefix_sum - k?"


Use a HashMap:

    prefix_sum -> frequency


Example:

    prefix_sum = 0

Store:

    {
        0: 1
    }


Read first 1:

    prefix_sum = 1

Check:

    1 - 2 = -1

Not found.

Store:

    {
        0: 1,
        1: 1
    }


Read second 1:

    prefix_sum = 2

Check:

    2 - 2 = 0

0 exists.

Therefore a valid subarray exists.


The HashMap allows us to count valid subarrays in O(n)
instead of O(n²).


============================================================
13. WHY DOES PREFIX SUM + HASHMAP WORK?
============================================================

Suppose:

    prefix[j] = sum from 0 to j

and:

    prefix[i] = sum from 0 to i


Then:

    prefix[j] - prefix[i]

gives us:

    sum from i+1 to j


If that equals k:

    prefix[j] - prefix[i] = k

Rearrange:

    prefix[i] = prefix[j] - k


So when we are at prefix[j], we only need to ask:

    "How many times have I seen prefix[j] - k?"

That question can be answered in O(1) using a HashMap.


============================================================
14. HASHMAP FOR GROUPING
============================================================

HashMaps can also group objects that share a property.

Classic problem:

    Group Anagrams


Input:

    ["eat", "tea", "tan", "ate", "nat", "bat"]


The key idea:

    Words that are anagrams have the same character
    frequency/signature.


For example:

    "eat"

frequency:

    a -> 1
    e -> 1
    t -> 1


"tea":

    a -> 1
    e -> 1
    t -> 1


Therefore they can share the same HashMap key.

Conceptually:

    signature -> list of words


    ("a": 1, "e": 1, "t": 1)
        |
        +-- eat
        +-- tea
        +-- ate


This is another important HashMap pattern:

    COMPUTE A SIGNATURE
        |
        v
    USE SIGNATURE AS KEY
        |
        v
    GROUP ITEMS


============================================================
15. HASHMAP FOR COUNTING PAIRS
============================================================

Suppose:

    nums = [1, 5, 7, -1]
    target = 6


We want pairs whose sum is 6.

For every number:

    complement = target - num


For 1:

    complement = 5

Have we seen 5?

    No.

Store 1.


For 5:

    complement = 1

Have we seen 1?

    Yes.

Therefore:

    (1, 5)


Again:

    "What do I need to complete the current value?"

becomes:

    complement = target - current


This is one of the strongest HashMap recognition patterns.


============================================================
16. HASHMAP FOR FREQUENCY + CONDITION
============================================================

Example:

    Find the first character that appears only once.


Input:

    "leetcode"


First calculate:

    frequency:

    {
        "l": 1,
        "e": 3,
        "t": 1,
        "c": 1,
        "o": 1,
        "d": 1
    }


Then scan the string again:

    l -> frequency 1

Therefore:

    l is the first non-repeating character.


This uses:

    Pass 1 -> build information
    Pass 2 -> use information


Time:

    O(n)

Space:

    O(k)

where k is the number of distinct characters.


============================================================
17. TWO-PASS HASHMAP PATTERN
============================================================

A very common strategy is:

    PASS 1:
        Build the HashMap.

    PASS 2:
        Use the HashMap to answer the question.


Example:

    Find majority element.


First:

    count frequencies.


Then:

    find the element whose frequency > n / 2.


However, sometimes we can combine the two passes into one.


============================================================
18. ONE-PASS HASHMAP PATTERN
============================================================

If the information needed for the current element can be
determined using previously seen elements, we can often do
everything in one pass.

Example:

    Two Sum


Instead of:

    Pass 1 -> store everything
    Pass 2 -> search everything

we do:

    for each element:

        check HashMap
        then store element


This gives:

    O(n)


This is generally preferable when possible.


============================================================
19. HASHMAP AS "MEMORY"
============================================================

A useful mental model:

    HashMap = MEMORY


Imagine processing:

    [4, 7, 2, 9, 7]


As you scan:

    4
        "I have seen 4."

    7
        "I have seen 4 and 7."

    2
        "I have seen 4, 7 and 2."

    9
        "I have seen 4, 7, 2 and 9."

    7
        "I have seen 7 before."


The HashMap remembers information about previous elements.


============================================================
20. HOW TO RECOGNIZE A HASHMAP PROBLEM
============================================================

Ask yourself these questions.


QUESTION 1:

    "Do I need to quickly check whether something exists?"

If YES:

    Think HashMap / Set.


QUESTION 2:

    "Do I need to count occurrences?"

If YES:

    Think HashMap frequency.


QUESTION 3:

    "Do I need to find a pair/complement?"

If YES:

    Think HashMap.


QUESTION 4:

    "Do I need information about a previous occurrence?"

If YES:

    Think HashMap.


QUESTION 5:

    "Am I repeatedly searching an array?"

If YES:

    Ask:

        Can I store the information in a HashMap?


QUESTION 6:

    "Do I need to count subarrays satisfying a sum condition?"

If YES:

    Think:

        Prefix Sum + HashMap.


QUESTION 7:

    "Do I need to group elements based on some property?"

If YES:

    Think:

        HashMap + Signature.


============================================================
21. HOW TO KNOW IF HASHMAP IS OPTIMAL
============================================================

Don't automatically use a HashMap just because it is fast.

First determine the bottleneck.

Suppose:

    nums = [1, 2, 3, 4, 5]


You repeatedly ask:

    "Does x exist?"

Brute force:

    O(n) per lookup


If you perform n lookups:

    O(n²)


HashMap:

    O(1) average lookup


n lookups:

    O(n)


Therefore HashMap is a strong optimization.


The general transformation is:

    REPEATED SEARCH
          |
          v
    STORE INFORMATION
          |
          v
    FAST LOOKUP


This is one of the most important optimization ideas in DSA.


============================================================
22. THE SPACE-TIME TRADEOFF
============================================================

HashMaps are often an example of:

    TIME <-> SPACE TRADEOFF


Brute force:

    Time:  O(n²)
    Space: O(1)


HashMap:

    Time:  O(n)
    Space: O(n)


We spend memory to save computation.


This is extremely common in algorithm design.


============================================================
23. WHEN HASHMAP IS NOT THE BEST APPROACH
============================================================

A HashMap is not automatically optimal.

Sometimes another pattern is better.


Example:

    Sorted array + Two Pointers


If:

    nums = [1, 2, 3, 4, 6]
    target = 6


We could use HashMap.

But if the array is already sorted, two pointers can solve
the pair-sum problem in:

    O(n)

with:

    O(1)

extra space.


Therefore:

    HashMap:
        O(n) time
        O(n) space


    Two pointers:
        O(n) time
        O(1) space


If the input is sorted and we only need a pair relationship,
Two Pointers may be better.


============================================================
24. HASHMAP VS SORTING
============================================================

Suppose we need to detect duplicates.

HashMap / Set:

    Time:  O(n) average
    Space: O(n)


Sorting:

    Time:  O(n log n)
    Space: depends on sorting algorithm


HashMap is usually faster asymptotically.

But if:

    - extra memory is expensive
    - sorting is already required
    - ordering is useful later

then sorting may be preferable.


Always consider the entire problem.


============================================================
25. HASHMAP VS SET
============================================================

Use:

    SET

when you only care about:

    "Does this exist?"


Example:

    seen = set()


Use:

    DICT / HASHMAP

when you need:

    key -> information


Examples:

    number -> index

    character -> frequency

    prefix_sum -> count

    character -> last_seen_index

    value -> object


Mental rule:

    Need ONLY existence?
        -> Set

    Need information associated with it?
        -> Dictionary


============================================================
26. COMMON PYTHON HASHMAP OPERATIONS
============================================================

Create:

    freq = {}


Insert:

    freq["a"] = 1


Update:

    freq["a"] += 1


Safe update:

    freq["a"] = freq.get("a", 0) + 1


Check existence:

    if "a" in freq:
        ...


Get value:

    value = freq.get("a")


Get with default:

    value = freq.get("a", 0)


Delete:

    del freq["a"]


Iterate over keys:

    for key in freq:
        ...


Iterate over key-value pairs:

    for key, value in freq.items():
        ...


Get all keys:

    freq.keys()


Get all values:

    freq.values()


Get all key-value pairs:

    freq.items()


============================================================
27. IMPORTANT PYTHON PATTERN: GET()
============================================================

Instead of:

    if num in freq:
        freq[num] += 1
    else:
        freq[num] = 1


We can write:

    freq[num] = freq.get(num, 0) + 1


Meaning:

    freq.get(num, 0)

says:

    "Give me the value associated with num.
     If num does not exist, give me 0."


Then:

    + 1


increments the frequency.


============================================================
28. HASHMAP WITH INDEX
============================================================

A very common structure:

    seen = {}

    for i, num in enumerate(nums):

        seen[num] = i


This creates:

    value -> latest index


Example:

    nums = [10, 20, 30]

    {
        10: 0,
        20: 1,
        30: 2
    }


This is useful for:

    - Two Sum
    - Longest substring
    - Duplicate detection
    - Distance between occurrences
    - Previous/next occurrence problems


============================================================
29. HASHMAP WITH FREQUENCY
============================================================

Structure:

    freq = {}

    for num in nums:
        freq[num] = freq.get(num, 0) + 1


Creates:

    value -> count


Useful for:

    - Frequency problems
    - Majority Element
    - Anagrams
    - Top K Frequent Elements
    - Duplicate problems
    - Counting pairs


============================================================
30. HASHMAP WITH PREFIX SUM
============================================================

Structure:

    prefix_count = {0: 1}
    prefix_sum = 0

    for num in nums:

        prefix_sum += num

        required = prefix_sum - k

        if required in prefix_count:
            count += prefix_count[required]

        prefix_count[prefix_sum] = (
            prefix_count.get(prefix_sum, 0) + 1
        )


The initialization:

    {0: 1}

is extremely important.

It represents:

    "Before processing any elements,
     prefix sum 0 has occurred once."


This allows subarrays starting at index 0 to be counted.


============================================================
31. THE "COMPLEMENT" PATTERN
============================================================

Whenever the problem says:

    "Find two values that satisfy some target"

try asking:

    "What value do I need to complete the current value?"


For sum:

    a + b = target

Therefore:

    b = target - a


Store previously seen values in a HashMap.


This general idea appears in many pair problems.


============================================================
32. THE "PREVIOUS OCCURRENCE" PATTERN
============================================================

When you see:

    "previous"
    "last occurrence"
    "distance between same values"
    "longest range without duplicates"

think:

    value -> previous index


Example:

    last_seen = {}

    for i, value in enumerate(nums):

        if value in last_seen:
            previous_index = last_seen[value]

        last_seen[value] = i


The HashMap gives immediate access to historical information.


============================================================
33. THE "FREQUENCY" PATTERN
============================================================

When you see:

    "how many times"
    "most frequent"
    "least frequent"
    "unique"
    "duplicates"
    "frequency"

think:

    value -> count


Example:

    freq = {}

    for value in nums:
        freq[value] = freq.get(value, 0) + 1


Then:

    for value, count in freq.items():
        ...


============================================================
34. THE "GROUP BY KEY" PATTERN
============================================================

When you see:

    "group"
    "categorize"
    "same property"
    "anagrams"
    "equivalent"

think:

    computed_key -> group


Example:

    groups = {}

    key = create_signature(value)

    if key not in groups:
        groups[key] = []

    groups[key].append(value)


The hard part is often finding the correct key/signature.


============================================================
35. HASHMAP + MONOTONIC STACK
============================================================

HashMaps can also be combined with other DSA patterns.

For example:

    Monotonic Stack + HashMap


You might store:

    value -> index

while a stack maintains:

    increasing/decreasing order


This happens when a problem requires both:

    fast lookup

and:

    next greater/smaller element


The important lesson is:

    DSA patterns are not isolated.

They can be combined.


============================================================
36. HASHMAP + HEAP
============================================================

Example:

    Top K Frequent Elements


First:

    HashMap

to calculate:

    value -> frequency


Then:

    Heap

to efficiently find the top K frequencies.


Pipeline:

    Input
      |
      v
    HashMap
      |
      v
    Frequencies
      |
      v
    Heap
      |
      v
    Top K


This is another example of combining patterns.


============================================================
37. COMMON HASHMAP PROBLEMS
============================================================

You should recognize HashMap as a possible solution for:

    Two Sum

    Contains Duplicate

    Valid Anagram

    Group Anagrams

    First Unique Character

    Majority Element

    Top K Frequent Elements

    Longest Consecutive Sequence

    Subarray Sum Equals K

    Continuous Subarray Sum

    Longest Substring Without Repeating Characters

    Longest Substring with K Distinct Characters

    Minimum Window Substring

    4Sum / 3Sum variants involving counting

    Count Number of Pairs

    Count Subarrays with a Given Sum

    Isomorphic Strings

    Word Pattern

    Ransom Note

    Happy Number

    Longest Arithmetic Subsequence

    Frequency-based problems


The exact implementation differs, but the underlying idea is
usually:

    STORE INFORMATION
        +
    FAST LOOKUP


============================================================
38. HASHMAP COMPLEXITY
============================================================

For Python dictionaries, average-case complexity is:

    Lookup:   O(1)
    Insert:   O(1)
    Delete:   O(1)


But technically these are average-case complexities.

Worst-case behavior can degrade because of hash collisions.

For normal DSA analysis, you generally write:

    Dictionary lookup -> O(1) average


Memory:

    If we store n elements:

    Space = O(n)


If the number of distinct values is k:

    Space = O(k)


For example:

    nums = [1, 1, 1, 1, 1]

There are n = 5 elements but only:

    k = 1

distinct value.

A frequency dictionary therefore uses:

    O(k)


============================================================
39. THE BIGGEST HASHMAP MISTAKE
============================================================

Don't use a HashMap blindly.

Ask:

    "What information am I storing?"

If you cannot clearly answer that question,
you probably haven't identified the pattern yet.


Good:

    value -> index

    value -> frequency

    prefix_sum -> frequency

    character -> last index


Bad thinking:

    "I'll just use a dictionary."


The HashMap is a TOOL.

You still need to determine what information the key and value
represent.


============================================================
40. THE HASHMAP DESIGN QUESTION
============================================================

Whenever you decide to use a HashMap, explicitly ask:

    What should the KEY represent?

and:

    What should the VALUE represent?


Example:

    Two Sum:

        key   = number
        value = index


Frequency:

        key   = number
        value = count


Longest substring:

        key   = character
        value = last index


Subarray sum:

        key   = prefix sum
        value = frequency


Group anagrams:

        key   = signature
        value = list of words


This is probably the most important HashMap design skill.


============================================================
41. HASHMAP DECISION TREE
============================================================

When solving a problem:

                    Start
                      |
                      v
            Need fast lookup?
                 /        \
               YES         NO
                |           |
                v           v
          What information? Other pattern
                |
       +--------+---------+
       |        |         |
       v        v         v
    Exists?  Count?   Previous info?
       |        |         |
       v        v         v
      Set     Dict    Dict
               |
               |
         +-----+------+
         |            |
         v            v
    Pair/target   Prefix sum?
         |            |
         v            v
    Complement   Prefix Sum
      lookup     + HashMap


============================================================
42. HOW TO TRANSFORM BRUTE FORCE INTO HASHMAP
============================================================

This is one of the most useful DSA skills.

Suppose brute force does:

    for i in range(n):

        for j in range(n):

            search/check something


Ask:

    "What is the inner loop actually searching for?"


If the inner loop is searching for:

    - an existing value
    - a frequency
    - an index
    - a previous prefix sum
    - a matching object

then you may be able to replace the inner loop with a
HashMap lookup.


Transformation:

    O(n²)

        becomes

    O(n)


by replacing:

    SEARCH

with:

    LOOKUP


============================================================
43. EXAMPLE: BRUTE FORCE -> HASHMAP
============================================================

Problem:

    Find whether two numbers sum to target.


Brute force:

    for i in range(n):

        for j in range(i + 1, n):

            if nums[i] + nums[j] == target:
                return True


Complexity:

    O(n²)


Ask:

    "What is the inner loop searching for?"


For nums[i], we need:

    target - nums[i]


Therefore:

    Store previously seen values.


Optimized:

    seen = set()

    for num in nums:

        complement = target - num

        if complement in seen:
            return True

        seen.add(num)


Complexity:

    O(n)


The optimization came from recognizing the repeated search.


============================================================
44. HASHMAP'S CORE SUPERPOWER
============================================================

HashMap does NOT magically make every problem O(n).

Its real superpower is:

    TURNING SEARCH INTO LOOKUP


Brute force:

    "Search through all previous elements."

HashMap:

    "Jump directly to the information."


This is the fundamental reason HashMaps are so powerful.


============================================================
45. HASHMAP PATTERN CHEAT SHEET
============================================================

Problem wording:

    "Have I seen this?"
        -> Set / HashMap


    "How many times?"
        -> Frequency HashMap


    "Where did I see it?"
        -> value -> index


    "When did I last see it?"
        -> value -> last index


    "What completes this value?"
        -> Complement HashMap


    "How many subarrays sum to K?"
        -> Prefix Sum + HashMap


    "Group equivalent items."
        -> HashMap + Signature


    "Top K frequent."
        -> HashMap + Heap/Bucket Sort


    "Longest substring with constraints."
        -> Sliding Window + HashMap


    "Repeated expensive search."
        -> Consider HashMap


============================================================
46. MOST IMPORTANT MENTAL MODEL
============================================================

When solving a new problem, think:

    1. What information do I need?

    2. Have I seen this information before?

    3. If yes, can I store it?

    4. What should my key be?

    5. What should my value be?

    6. Can I replace a repeated search with O(1) lookup?

    7. Does the extra O(n) memory give me a better time
       complexity?

If the answer is yes, HashMap is probably part of the solution.


============================================================
47. FINAL HASHMAP TEMPLATE
============================================================

The generic pattern is:

    memory = {}

    for i, value in enumerate(data):

        # 1. Ask something about previously seen data.
        if value in memory:
            ...

        # 2. Use previously stored information.
        previous = memory.get(value)

        # 3. Update memory.
        memory[value] = i


The exact operation changes from problem to problem.

But the philosophy remains:

    SEE
      |
      v
    LOOKUP
      |
      v
    USE
      |
      v
    STORE / UPDATE
      |
      v
    MOVE ON


============================================================
48. FINAL TAKEAWAY
============================================================

HashMap is not just a data structure.

It is a DSA problem-solving pattern based on:

    "Remember useful information about the past so that
     future operations can be performed quickly."


The most important patterns to master are:

    1. Frequency Counting
           value -> count

    2. Seen / Existence
           value -> exists

    3. Index Mapping
           value -> index

    4. Last Seen
           value -> latest index

    5. Complement Lookup
           required_value -> previous occurrence

    6. Prefix Sum + HashMap
           prefix_sum -> frequency

    7. Grouping
           signature -> group

    8. Sliding Window + HashMap
           character/value -> window information

    9. HashMap + Heap
           frequency -> top K

    10. HashMap + Other Patterns
           Combine fast lookup with another algorithmic pattern.


The single sentence to remember:

    HASHMAP = STORE THE PAST SO YOU CAN ANSWER QUESTIONS
              ABOUT THE PRESENT IN O(1) AVERAGE TIME.


And the most important recognition rule:

    If your brute-force solution repeatedly searches for
    information that you have already encountered,

    ASK:

        "Can I store that information in a HashMap?"

    If yes, you may be able to turn:

        O(n²) -> O(n)

    by replacing repeated SEARCH with fast LOOKUP.
"""

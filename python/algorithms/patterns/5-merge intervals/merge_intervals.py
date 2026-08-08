"""

================================================================================
                            MERGE INTERVALS PATTERN
================================================================================

DEFINITION
--------------------------------------------------------------------------------
The Merge Intervals pattern is used whenever the input consists of intervals
(ranges) and the goal is to combine, compare, insert, remove, or analyze
overlapping intervals efficiently.

An interval is simply a range represented as:

    [start, end]

where

    start <= end

Examples:

    [1, 5]      Numbers from 1 to 5
    [9, 11]     Time from 9AM to 11AM
    [20, 40]    Distance from 20km to 40km

Instead of treating each number individually, we treat the entire range as one
object.

--------------------------------------------------------------------------------
REAL WORLD EXAMPLES
--------------------------------------------------------------------------------

Imagine booking meeting rooms.

Meeting A:
    9:00 ---- 11:00

Meeting B:
           10:30 -------- 1:00

These meetings overlap.

Instead of keeping both separately, they represent one busy period:

    9:00 ----------------- 1:00

--------------------------------------------------------

Imagine painting a wall.

Painter A paints:

    1m -------- 5m

Painter B paints:

          4m -------- 8m

The painted wall is actually

    1m ------------------- 8m

--------------------------------------------------------

Imagine roads.

Road Repair A

0km ----------------- 10km

Road Repair B

             8km ----------------- 20km

Instead of two repairs, the road under repair becomes

0km ---------------------------20km

These are all Merge Interval problems.

================================================================================
CORE CONCEPT
================================================================================

Instead of comparing every interval with every other interval,

we first SORT them.

After sorting,

we only need to compare the CURRENT interval with the LAST merged interval.

This is the entire magic behind this pattern.

Without sorting:

Need many comparisons.

With sorting:

Only one comparison per interval.

================================================================================
WHY SORTING IS SO IMPORTANT
================================================================================

Suppose we have

[8,10]
[1,3]
[2,6]
[15,18]

Without sorting,

there is no predictable order.

The interval [2,6] could overlap with something before or after.

Now sort by start.

[1,3]
[2,6]
[8,10]
[15,18]

Everything is ordered.

Now while scanning left to right,

we know every future interval starts AFTER previous intervals.

This allows a greedy solution.

Sorting transforms a complicated O(n²) comparison problem into a simple
linear scan after sorting.

================================================================================
WHY DOES THE GREEDY APPROACH WORK?
================================================================================

Suppose we already merged

[1,6]

Now the next interval is

[8,10]

Since

8 > 6

there is no overlap.

Because intervals are sorted,

every future interval starts AFTER 8.

Meaning

none of the remaining intervals can ever overlap with [1,6].

Therefore

we safely finalize [1,6].

This is why sorting makes the greedy solution correct.

================================================================================
HOW TO RECOGNIZE A MERGE INTERVALS PROBLEM
================================================================================

Whenever you see words like

    interval
    ranges
    meeting
    calendar
    schedule
    booking
    event
    appointment
    time slot
    shift
    start
    end
    overlapping
    merge
    insert interval
    remove overlap
    free time

Immediately think

"Can I sort these intervals first?"

This is usually the biggest clue.

================================================================================
QUESTIONS TO ASK YOURSELF
================================================================================

Question 1

Does every element look like

[start, end] ?

If yes,
Merge Intervals might apply.

--------------------------------------------------

Question 2

Am I asked to merge or combine ranges?

Example

Input

[[1,3],[2,6]]

Output

[[1,6]]

Definitely Merge Intervals.

--------------------------------------------------

Question 3

Am I checking overlap?

If yes,

Merge Intervals is probably involved.

--------------------------------------------------

Question 4

Can sorting simplify comparisons?

If yes,

Sorting + Merge Intervals is usually optimal.

================================================================================
WHAT IS AN OVERLAP?
================================================================================

Suppose

Interval A

[a, b]

Interval B

[c, d]

They overlap if

    c <= b

Meaning

the second interval starts before the first interval finishes.

Example

[2,7]

[5,9]

Since

5 <= 7

they overlap.

Merged interval becomes

start = min(2,5) = 2

end = max(7,9) = 9

Result

[2,9]

--------------------------------------------------------

Example

[1,4]

[5,8]

Since

5 > 4

No overlap.

Keep both separately.

================================================================================
VISUAL EXAMPLES
================================================================================

Example 1

Intervals

[1,3]
[2,6]
[8,10]
[15,18]

Visualization

1-----3
   2--------6

Merge

1------------6

Remaining

8------10

15------18

Final

[1,6]
[8,10]
[15,18]

--------------------------------------------------------

Example 2

Intervals

[1,4]
[4,5]

Notice

4 == 4

Still overlap.

Merged

[1,5]

================================================================================
GENERAL ALGORITHM
================================================================================

Step 1

Sort intervals by starting value.

----------------------------------------

Step 2

Put first interval into result.

----------------------------------------

Step 3

For every remaining interval

Compare with last interval inside result.

----------------------------------------

Case 1

Overlap

Merge them.

----------------------------------------

Case 2

No overlap

Append new interval.

----------------------------------------

Step 4

Return result.

================================================================================
MENTAL MODEL
================================================================================

Imagine dragging a marker from left to right.

Whenever intervals touch,

keep extending the marker.

Whenever there is a gap,

finish the previous interval

and start a new marker.

This visualization makes the algorithm very intuitive.

================================================================================
WHY IS BRUTE FORCE BAD?
================================================================================

Suppose

n = 10000 intervals.

Brute force

Compare every interval with every other interval.

Total comparisons

n²

10000²

100 million comparisons.

Very slow.

--------------------------------------------------------

Merge Interval Solution

Sort

O(n log n)

Scan once

O(n)

Total

O(n log n)

Huge improvement.

================================================================================
COMMON PROBLEMS USING THIS PATTERN
================================================================================

1.
Merge Overlapping Intervals

Input

[[1,3],[2,6],[8,10]]

Output

[[1,6],[8,10]]

--------------------------------------------------

2.
Insert Interval

Insert

[4,8]

into

[[1,2],[3,5],[6,7],[9,10]]

Merge where needed.

--------------------------------------------------

3.
Meeting Rooms

Determine if any meetings overlap.

--------------------------------------------------

4.
Meeting Rooms II

Find minimum meeting rooms required.

(Solved using intervals + min heap.)

--------------------------------------------------

5.
Employee Free Time

Find free time among many employees.

--------------------------------------------------

6.
Interval List Intersections

Find common portions of two interval lists.

--------------------------------------------------

7.
Non-overlapping Intervals

Remove minimum intervals.

--------------------------------------------------

8.
Remove Covered Intervals

Remove intervals completely inside others.

--------------------------------------------------

9.
Calendar Booking Problems

--------------------------------------------------

10.
CPU Scheduling

--------------------------------------------------

11.
Memory Allocation

--------------------------------------------------

12.
Range Compression

================================================================================
COMMON VARIATIONS
================================================================================

Variation 1

Merge intervals.

----------------------------------------

Variation 2

Insert interval.

----------------------------------------

Variation 3

Find intersections.

----------------------------------------

Variation 4

Find gaps.

----------------------------------------

Variation 5

Count overlaps.

----------------------------------------

Variation 6

Minimum removals.

----------------------------------------

Variation 7

Meeting scheduling.

================================================================================
PATTERN IDENTIFICATION CHEAT SHEET
================================================================================

Question                               Pattern?

Input contains [start,end]?            YES

Need merge?                            YES

Need overlap detection?                YES

Need insert interval?                  YES

Need remove overlap?                   YES

Need find free slots?                  YES

Need compare ranges?                   YES

================================================================================
COMMON MISTAKES
================================================================================

Mistake 1

Not sorting first.

The algorithm depends on sorted intervals.

--------------------------------------------------------

Mistake 2

Using

current.start < previous.end

instead of

current.start <= previous.end

Touching intervals also overlap in most problems.

--------------------------------------------------------

Mistake 3

Merging with the previous input interval instead of the LAST MERGED interval.

Always compare against

result[-1]

not

intervals[i-1]

--------------------------------------------------------

Mistake 4

Updating start incorrectly.

Merged interval

start = previous.start

end = max(previous.end, current.end)

================================================================================
WHY THIS IS OFTEN THE OPTIMAL SOLUTION
================================================================================

Without sorting,

every interval might overlap with any other interval.

Need O(n²).

Sorting organizes intervals so that only adjacent comparisons matter.

Therefore

Sorting      O(n log n)

Linear Scan  O(n)

Overall

O(n log n)

For comparison-based interval problems,

this is almost always the optimal solution.

================================================================================
TIME COMPLEXITY
================================================================================

Sorting

O(n log n)

Scanning

O(n)

Overall

O(n log n)

================================================================================
SPACE COMPLEXITY
================================================================================

Output list

O(n)

Extra working space

O(1)

(Some sorting algorithms may internally use extra memory.)

================================================================================
ONE-LINE MEMORY TRICK
================================================================================

"Whenever the input consists of ranges [start, end], sort by start, compare only
with the last merged interval, merge if they overlap, otherwise start a new
interval."

This single sentence solves the majority of Merge Intervals problems.

================================================================================


"""

##! Question 1: Merge Intervals

"""

Given an array of intervals where intervals[i] = [starti, endi], merge all overlapping intervals, and return an array of the non-overlapping intervals that cover all the intervals in the input.

 

Example 1:

Input: intervals = [[1,3],[2,6],[8,10],[15,18]]
Output: [[1,6],[8,10],[15,18]]
Explanation: Since intervals [1,3] and [2,6] overlap, merge them into [1,6].
Example 2:

Input: intervals = [[1,4],[4,5]]
Output: [[1,5]]
Explanation: Intervals [1,4] and [4,5] are considered overlapping.
Example 3:

Input: intervals = [[4,7],[1,4]]
Output: [[1,7]]
Explanation: Intervals [1,4] and [4,7] are considered overlapping.
 

Constraints:

1 <= intervals.length <= 104
intervals[i].length == 2
0 <= starti <= endi <= 104

"""


##! Question 2: Insert Interval

"""

You are given an array of non-overlapping intervals where intervals[i] = [starti, endi] represent the start and the end of the ith interval and intervals is sorted in ascending order by starti. You are also given an interval newInterval = [start, end] that represents the start and end of another interval.

Two intervals are considered overlapping if they share at least one point.

Insert newInterval into intervals such that intervals is still sorted in ascending order by starti and intervals still does not have any overlapping intervals (merge overlapping intervals if necessary).

Return intervals after the insertion.

Note that you don't need to modify intervals in-place. You can make a new array and return it.

 

Example 1:

Input: intervals = [[1,3],[6,9]], newInterval = [2,5]
Output: [[1,5],[6,9]]
Example 2:

Input: intervals = [[1,2],[3,5],[6,7],[8,10],[12,16]], newInterval = [4,8]
Output: [[1,2],[3,10],[12,16]]
Explanation: Because the new interval [4,8] overlaps with [3,5],[6,7],[8,10].
 

Constraints:

0 <= intervals.length <= 104
intervals[i].length == 2
0 <= starti <= endi <= 105
intervals is sorted by starti in ascending order.
newInterval.length == 2
0 <= start <= end <= 105


"""


##! Question 3: Interval List Intersections

"""

You are given two lists of closed intervals, firstList and secondList, where firstList[i] = [starti, endi] and secondList[j] = [startj, endj]. Each list of intervals is pairwise disjoint and in sorted order.

Return the intersection of these two interval lists.

A closed interval [a, b] (with a <= b) denotes the set of real numbers x with a <= x <= b.

The intersection of two closed intervals is a set of real numbers that are either empty or represented as a closed interval. For example, the intersection of [1, 3] and [2, 4] is [2, 3].

 

Example 1:
Input: firstList = [[0,2],[5,10],[13,23],[24,25]], secondList = [[1,5],[8,12],[15,24],[25,26]]
Output: [[1,2],[5,5],[8,10],[15,23],[24,24],[25,25]]

Example 2:

Input: firstList = [[1,3],[5,9]], secondList = []
Output: []
 

Constraints:

0 <= firstList.length, secondList.length <= 1000
firstList.length + secondList.length >= 1
0 <= starti < endi <= 109
endi < starti+1
0 <= startj < endj <= 109 
endj < startj+1

"""


##! Question 4: Check if any two intervals intersect in a given set


"""

An interval is represented as a combination of start time and end time. Given a set of intervals, check if any two intervals intersect. 

Examples: 

Input:  arr[] = [[1, 3], [5, 7], [2, 4], [6, 8]]
Output: True
Explanation: The intervals {1, 3} and {2, 4} overlap

Input:  arr[] = [[1, 3], [7, 9], [4, 6], [10, 13]]
Output: False
Explanation: No pair of intervals overlap. 


"""


##! Question 5: Meeting Rooms II


"""

Given two arrays start[] and end[] such that start[i] is the starting time of ith meeting and end[i] is the ending time of ith meeting. Return the minimum number of rooms required to attend all meetings.

Note: A person can also attend a meeting if it's starting time is same as the previous meeting's ending time.

Examples:

Input: start[] = [1, 10, 7], end[] = [4, 15, 10]
Output: 1
Explanation: Since all the meetings are held at different times, it is possible to attend all the meetings in a single room.
Input: start[] = [2, 9, 6], end[] = [4, 12, 10]
Output: 2
Explanation: 1st and 2nd meetings at one room but for 3rd meeting one another room required.
Constraints:
1 ≤ start.size() = end.size() ≤ 105
0 ≤ start[i] < end[i] ≤ 106

"""


##! Question 6: Maximum CPU Load from the given list of jobs

"""

Given an array of jobs with different time requirements, where each job consists of start time, end time and CPU load. 

The task is to find the maximum CPU load at any time if all jobs are running on the same machine.

Examples: 

Input: jobs[] = {{1, 4, 3}, {2, 5, 4}, {7, 9, 6}} 
Output: 7 
Explanation: 
In the above-given jobs, there are two jobs which overlaps. 
That is, Job [1, 4, 3] and [2, 5, 4] overlaps for the time period in [2, 4] 
Hence, the maximum CPU Load at this instant will be maximum (3 + 4 = 7).


Input: jobs[] = {{6, 7, 10}, {2, 4, 11}, {8, 12, 15}} 
Output: 15 
Explanation: 
Since, There are no jobs that overlaps. 
Maximum CPU Load will be - max(10, 11, 15) = 15 

"""


##! Question 7: Employee Free Time


"""

Given a list of employee work schedules with each employee having a list of non-overlapping intervals representing their working hours, we are tasked with finding the common free time for all employees, or in other words, the times when all employees are not working.

The input is a nested list of intervals, each interval as [start, end], with start < end. The intervals are non-overlapping and are already sorted in ascending order. The output should also be a list of sorted intervals.

For example, consider schedule = [[[1,3],[6,7]],[[2,4]],[[2,5],[9,12]]]. Here, Employee 1 works from 1 to 3 and 6 to 7. Employee 2 works from 2 to 4 and Employee 3 works from 2 to 5 and 9 to 12. The common free time for all employees is [5,6] and [7,9] as these are the intervals when all employees are free.

"""

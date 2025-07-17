# Given two integer lists, num1 and num2, of size m and n, respectively , sorted in nondecreasing order.Merge nums1 and nums2 into a single list sorted in nondecreasing order.

def merge_lists(nums1, nums2):
    result = [None] * (len(nums1)+len(nums2))
    p1 = 0
    p2 = 0
    p3 = 0

    # Traverse both lists until the end of either list is reached
    while (p1 < len(nums1)) and (p2 < len(nums2)):
        # If the value at p1 is smaller than the value at p2, store the value at p3 and increment p1 and p3
        if (nums1[p1] < nums2[p2]):
            result[p3] = nums1[p1]
            p1 += 1
            p3 += 1
        # Otherwise, store the value at p2 into p3 and increment p2 and p3
        else:
            result[p3] = nums2[p2]
            p2 += 1
            p3 += 1
    # If elements remain in nums1, store them in result
    while (p1 < len(nums1)):
        result[p3] = nums1[p1]
        p1 += 1
        p3 += 1
    # If elements remain in nums2, store them in result
    while (p2 < len(nums2)):
        result[p3] = nums2[p2]
        p2 += 1
        p3 += 1
    return result

nums1 = [[23, 33, 35, 41, 44, 47, 56, 91, 105], [1, 2], [1, 1, 1], [6], [12, 34, 45, 56, 67, 78, 89, 99]]
nums2 = [[32, 49, 50, 51, 61, 99], [7], [1, 2, 3, 4], [-99, -45], [100]]

for i in range(len(nums1)):
    print(i + 1, ".\tFirst list: ", nums1[i])
    print("\tSecond list: ", nums2[i])
    print("\tMerged list: ", merge_lists(nums1[i], nums2[i]))
    print("-" * 100)
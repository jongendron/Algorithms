def merge(nums1: list, nums2: list) -> None:
    """
    Do not return anything, modify nums1 in-place instead.
    """

    # Get lengths of each array (merge length and total)
    m = len(nums2)  # length nums2 (merge and total length)
    n_ = len(nums1)  # length of nums1 (total length)
    n = n_ - m  # length of nums1 to be sorted (merge length)

    # Set pointers for traversal
    p2 = m - 1  # nums2 pointer initial condition
    p1 = n - 1  # nums1 pointer initial condition
    p1_ = n_ - 1  # nums1 second pointer (fill position)

    # Traversal
    while p1_ >= 0:
        print(p1,p2)
        if p1 < 0:
            nums1[p1_] = nums2[p2]
            p2 -= 1
        elif p2 < 0:
            nums1[p1_] = nums1[p1]
            p1 -= 1
        elif nums2[p2] >= nums1[p1]:
            nums1[p1_] = nums2[p2]
            p2 -= 1
        else:
            nums1[p1_] = nums1[p1]
            p1 -= 1
        p1_ -= 1
        


# a2 = [2,4,6,8]
# n = 4
# a1 = [1,3,5,7] + [0 for x in range(len(a2))]
# m = 4

a2 = [0]
a1 = [1,0]

merge(a1,a2)
print(a1)
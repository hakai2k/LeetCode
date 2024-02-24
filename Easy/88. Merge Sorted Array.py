def merge(nums1, nums2):
    nums1 = list(set(nums1))
    nums2 = list(set(nums2))
    for element in nums1:
        if element == 0:
            nums1.remove(element)
    for element in nums2:
        if element == 0:
            nums2.remove(element)
    nums1.extend(nums2)
    nums1.sort()
    return nums1


nums1 = [1,2,3,0,0,0,]
nums2 =  [2,5,6]
print(merge(nums1, nums2))
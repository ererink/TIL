def findMedianSortedArrays(nums1, nums2):
    nums = sorted(nums1 + nums2)
    idx = len(nums1) + len(nums2)
    if idx % 2 == 0:
        idx = idx // 2
        answer = (nums[idx] + nums[idx-1]) / 2
        return answer
    else:
        idx = idx // 2
        answer = nums[idx]
        return answer
    

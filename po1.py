nums1 = [x for x in range(1000000) if x % 3 == 0]
nums2 = [x for x in range(1000000) if x % 5 == 0]
nums3 = [x for x in range(1000000) if x % 15 == 0]

print(sum(nums1) + sum(nums2) - sum(nums3))

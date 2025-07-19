class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # 2025-07-19
        # find first decreasing value moving from left to right 
        # (this should be replaced with the next bigger number in subarray to the right)
        # subarrray to the right of the change should be sorted small to big
        # if array is reverse sorted, return sorted array
        sorted_nums = nums[::]
        sorted_nums.sort()
        sorted_nums.reverse()
        if sorted_nums == nums: # return sorted 
            nums.sort()
            return 
        prev = nums[-1]
        i = len(nums) -2
        while i > 0:
            if nums[i] < prev:
                break
            else:
                prev = nums[i]
                i-=1
        # now find value to switch with
        closest_larger = float('inf')
        i2 = -1 # index of number to switch
        difference = float('inf')
        for j in range(i+1, len(nums)):
            if nums[j] > nums[i]: # bigger than num to switch
                if (nums[j]-nums[i]) < difference: # closest largest number to the number being swapped, smaller difference
                    closest_larger = nums[j]
                    difference = nums[j] - nums[i]
                    i2 = j
        nums[i], nums[i2] = nums[i2], nums[i] # make swap 
        # sort subarray from nums[i+1] to end
        subarray = nums[i+1:]
        subarray.sort()
        for j, k in zip(range(0,len(subarray)), range(i+1,len(nums))):
            nums[k] = subarray[j]



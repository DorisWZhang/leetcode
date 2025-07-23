class NumArray:
    # 2025 -07-22


    def __init__(self, nums: List[int]):

        self.nums = nums
        # prefixSum[i] is sum of everything in nums from 0 to i-1
        self.prefixSum = [0] * (len(nums) +1)


        currSum = 0
        for i in range(len(nums)):
            currSum += nums[i]
            self.prefixSum[i+1] = currSum

    def sumRange(self, left: int, right: int) -> int:

        return self.prefixSum[right+1] - self.prefixSum[left]
        


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)
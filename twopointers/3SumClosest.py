class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        # 2025-07-17
        nums.sort()
        closest = float('inf')

        for i in range(len(nums)-2):
            left = i + 1
            right = len(nums) -1
            while left < right:
                currSum = nums[i] + nums[left] + nums[right]
                
                if currSum == target:
                    return target

                # if closer, update closest
                if abs(target - currSum) < abs(closest-target):
                    closest = currSum
                
                # check which way to move 
                # if we want a bigger number, move left towards right
                # if we want a smaller number, move right towards left
                if currSum < target:
                    left += 1
                else:
                    right -=1   
        return closest
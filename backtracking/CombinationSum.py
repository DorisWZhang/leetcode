class Solution:
    #2025-07-08
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        result = []
        def backtrack(nums, start):
            if sum(nums) == target:
                result.append(nums[:])
                return
            elif sum(nums) > target:
                return
            else:
                for i in range(start,len(candidates)):
                    nums.append(candidates[i])
                    backtrack(nums, i)  # not i + 1 because you can reuse the same number
                    nums.pop()
        
        backtrack([],0)
        return result

        
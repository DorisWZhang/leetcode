class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        # 2025-09-17

        subsets = []

        def backtrack(start, path):
            subsets.append(path[:])

            # loop and try explore every other path for subsets i-th element
            for i in range(start, len(nums)):
                path.append(nums[i])
                backtrack(i+1, path)
                path.pop() # backtrack, undo and try other path
        
        backtrack(0,[])
        return subsets


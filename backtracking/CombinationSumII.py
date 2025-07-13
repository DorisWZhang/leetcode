class Solution:
    # 2025-07-08
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        
        res = []
        candidates.sort() # sort at the start 
        def backtrack(start, curr):
            if sum(curr) == target:
                res.append(curr[:])
                return
            elif sum(curr) > target:
                return
            else:
                for i in range(start, len(candidates)):
                    if i > start and candidates[i] == candidates[i-1]: # prevent dupes
                        continue
                    else:
                        curr.append(candidates[i])
                        backtrack(i+1, curr) # +1 to prevent reusing number
                        curr.pop()
        backtrack(0, [])
        return res
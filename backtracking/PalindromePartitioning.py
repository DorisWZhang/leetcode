class Solution:
    def partition(self, s: str) -> List[List[str]]:
        # 2025-08-03

        n = len(s)
        result = []
        def backtrack(i, curr):
            if i >= n:
                result.append(curr)
                return
            for j in range(i+1, n+1):
                string = s[i:j] 
                if string == string[::-1]:
                    curr_copy = curr[::]
                    curr_copy.append(string)
                    backtrack(j, curr_copy)
        
        backtrack(0, [])
        return result

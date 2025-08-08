class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        # 2025-08-08

        # Monotonic stack
        # stack holds the days that are still looking for a warmer future day
        
        n = len(temperatures)
        result = [0]*n
        stack = []
        for curr_day, curr_temp in enumerate(temperatures):
            # go through stack, popping if the temperature is warmer than 
            # previous temperatures on days still looking for a future warmer day
            while stack and temperatures[stack[-1]] < curr_temp:
                prev_day = stack.pop()
                result[prev_day] = curr_day - prev_day
            stack.append(curr_day) # append
        
        return result

        
class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:

        # loop through and try each station as a starting point if its a valid starting point (gas[i] >= cost[i])
        # loop through starting at "start", tracking steps to calculate idx (accounting for wrap around)
        # if currgas goes under 0, exit loop and skip the next starting station to start += steps +1
        # this is because the failure at previous "start" means all stations from [start: start+step] will ALSO fail

        n = len(gas)
        if sum(gas) < sum(cost): # quick check for possibility
            return -1
        start = 0
        while start < n:
            if gas[start] < cost[start]: # cannot start here 
                start += 1
                continue
            curr_gas = 0
            steps = 0
            while steps < n:
                idx = (start + steps) % n # deal with wrap around
                curr_gas += gas[idx] - cost[idx]
                if curr_gas < 0:          # failed at idx
                    break
                steps += 1
            
            if steps == n:
                return start
            
            start += steps + 1 # start after latest fail point
        return -1

                

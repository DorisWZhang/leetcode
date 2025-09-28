class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # 2025-09-28
        # topological sort on directed map
        # process nodes with indegree 0
        inDegree = [0] * numCourses
        taken = set()
        availCourses = []
        for i in range(numCourses):
            for p in prerequisites:
                if p[0] == i:
                    inDegree[i] += 1

        if 0 not in inDegree: # cannot start any courses
            return False
        for i in range(len(inDegree)):
            degree = inDegree[i]
            if degree == 0:
                availCourses.append(i)
        
        while availCourses:
            course = availCourses.pop()
            taken.add(course)
            # update indegrees
            for p in prerequisites:
                if p[1] == course:
                    if inDegree[p[0]] > 0:
                        inDegree[p[0]] -=1
                        if inDegree[p[0]] == 0:
                            availCourses.append(p[0])
        return len(taken) == numCourses   
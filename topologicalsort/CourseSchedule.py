from collections import deque
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # 2025-07-06

        # topological sort/ direct acyclic graph
        # if a course is in prereq[i][0] -> then it has a prereq
        # loop through courses, labelled 0 to numCourses-1 and check for courses with in-degree of 0
        # process courses in queue and then remove any prereq relationships with that course as a prereq
        
        
        queue = deque()

        # enqueue all courses with no prereqs
        def findNoPrereq():
            for num in range(numCourses):
                no_prereq = True
                for prereq in prerequisites:
                    if prereq[0] == num: # has a prereq
                        no_prereq = False
                        break
                if no_prereq: # if there are no prereqs
                    queue.append(num)
        
        findNoPrereq()

        while queue:
            curr = queue.popleft()
            old_prerequisites = prerequisites.copy()
            for prereq in old_prerequisites:
                if prereq[1] == curr: # completed prereq, then remove it from prerequisites
                    prerequisites.remove(prereq)

                    # check if now a course has no other required prereqs..
                    prereq_needed = False
                    for updated_prereq in prerequisites:
                        if prereq[0] == updated_prereq[0]:
                            prereq_needed = True
                            break # break early, still has at least one prereq

                    if prereq_needed == False: # if no other prereqs required
                        # append to queue of courses to complete
                        queue.append(prereq[0])
        return len(prerequisites) == 0



                
        
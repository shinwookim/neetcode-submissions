class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        prereqs = {course: [] for course in range(numCourses)}
        for course, prereq in prerequisites:
            prereqs[course].append(prereq)

        visiting = set()
        def cycle_exists(course):
            if course in visiting:
                return True
            if prereqs[course] == []:
                return False
            
            visiting.add(course)
            for prereq in prereqs[course]:
                if cycle_exists(prereq):
                    return True
            visiting.remove(course)
            prereqs[course] = []
            return False

        for course in range(numCourses):
            if cycle_exists(course):
                return False
        return True
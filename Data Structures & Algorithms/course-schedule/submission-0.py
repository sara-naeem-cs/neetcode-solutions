class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        prerequisiteMap = {}
        for i in range(numCourses):
            prerequisiteMap[i] = []
        
        for course, prereq in prerequisites:
            prerequisiteMap[course].append(prereq)
        
        visited = set()

        def dfs(course):
            if course in visited:
                return False
            if prerequisiteMap[course] == []:
                return True
            
            #Update to add current course to visited
            visited.add(course)
            for prereq in prerequisiteMap[course]:
                if not dfs(prereq):
                    return False
            visited.remove(course)

            prerequisiteMap[course]=[]
            return True
        
        for courses in range(numCourses):
            if not dfs(course):
                return False
        return True
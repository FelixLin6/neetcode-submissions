class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = {}
        for i in range(len(prerequisites)):
            course, prereq = prerequisites[i][0], prerequisites[i][1]
            graph[course] = graph.get(course, []) + [prereq]

        for n in range(numCourses):
            path = [n]
            in_path = {n}
            while path:
                curr = path[-1]
                if graph.get(curr):
                    pre = graph[curr].pop()
                    if pre in in_path: return False
                    path.append(pre)
                    in_path.add(pre)
                else:
                    in_path.remove(path.pop())


        return True


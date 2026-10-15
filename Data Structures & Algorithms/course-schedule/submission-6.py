class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # Given a adjacency list basically
        # Form Adjacency list
        # Use adjacency List to BFS if theres a path through..

        adjList = {}
        for src, dst in prerequisites:
            if src not in adjList:
                adjList[src] = []
            if dst not in adjList:
                adjList[dst] = []
            adjList[src].append(dst)

        for key,value in adjList.items():
            print(f"key: {key}, values: {value}")

        # # Check if num courses <= prerequisites.count
        # if numCourses > len(prerequisites):
        #     return False

    # Do DFS, at each point add the course to visited then do DFS on neighbors. at end remove from visisted.
    # If a course seen again is ever in visited, we're looping..
        visited = set()
        def dfs(node):
            if node in visited:
                return False
            if adjList[node] == []:
                return True
            
            visited.add(node)
            for prereq in adjList[node]:
                if not dfs(prereq):
                    return False
            visited.remove(node)
            adjList[node] = []
            return True


        for node in adjList:
            if not dfs(node):
                return False
        return True

        


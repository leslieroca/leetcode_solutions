https://leetcode.com/problems/number-of-islands


from collections import deque

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        count = 0  
        visited = set()
  
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == "1" and (i,j) not in visited:
                    count += 1
                    # BFS algorithm
                    q = deque() 
                    q.append((i,j))
                    visited.add((i,j))
                    while q:
                        p = q.popleft()
                        p_i,p_j = p
                        adjacents = [(p_i-1, p_j), (p_i, p_j+1), (p_i+1, p_j), (p_i, p_j-1)]
                        for adj in adjacents:
                            adj_i, adj_j = adj
                            if 0 <= adj_i < len(grid) and 0 <= adj_j < len(grid[0]):
                                if grid[adj_i][adj_j] == "1" and adj not in visited:
                                    q.append(adj)
                                    visited.add(adj)

        return count       
                

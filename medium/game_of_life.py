https://leetcode.com/problems/game-of-life

class Solution:

    def nextState(self, current_state, count_live):
        if current_state == 1 and (count_live == 2 or count_live == 3):
            return 1
        elif current_state == 0 and count_live == 3:
            return 1
        else:
            return 0

    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        rows, cols = len(board), len(board[0])
        prev = None

        for i in range(rows):
            current = board[i].copy()
            for j in range(cols):
                count_live = 0

                # above row
                if i > 0:
                    for k in range(j - 1, j + 2):
                        if 0 <= k < cols:
                            count_live += prev[k]

                # same row
                if j - 1 >= 0:
                    count_live += current[j - 1]
                if j + 1 < cols:
                    count_live += current[j + 1]

                # below row
                if i < rows - 1:
                    for k in range(j - 1, j + 2):
                        if 0 <= k < cols:
                            count_live += board[i + 1][k]

                board[i][j] = self.nextState(board[i][j], count_live)

            prev = current
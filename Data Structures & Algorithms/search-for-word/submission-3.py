class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        """
        TODO:
        should not go back to where it came from"""

        def search(i: int, j: int, l: int, curr_path: set[(int,int)]) -> bool:
            
            
            if (i, j) in curr_path:
                return False

            if l == len(word) - 1 and board[i][j] == word[l]:
                return True
            
            if board[i][j] != word[l]:
                return False

            curr_path.add((i, j))
            if i > 0 and search(i - 1, j, l + 1, set(curr_path)):
                return True
            if i < len(board) - 1 and search(i + 1, j, l + 1, set(curr_path)):
                return True
            if j > 0 and search(i, j - 1, l + 1, set(curr_path)):
                return True
            if j < len(board[0]) - 1 and search(i, j + 1, l + 1, set(curr_path)):
                return True
            return False




        for i in range(len(board)):
            for j in range(len(board[0])):
                if search(i, j, 0, set()):
                    return True
        return False


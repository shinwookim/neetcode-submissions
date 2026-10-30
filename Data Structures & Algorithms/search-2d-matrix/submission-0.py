class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        lo, hi = 0, len(matrix)
        while lo < hi:
            mid = lo + (hi - lo) // 2
            if matrix[mid][0] == target:
                return True
            elif matrix[mid][0] < target:
                lo = mid + 1
            else:
                hi = mid
        row = lo - 1
        lo, hi = 0, len(matrix[0])
        while lo < hi:
            mid = lo + (hi - lo) // 2
            if matrix[row][mid] == target:
                return True
            elif matrix[row][mid] < target:
                lo = mid + 1
            else:
                hi = mid
        return False
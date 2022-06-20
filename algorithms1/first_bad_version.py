# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        left, right = 1, n
        
        while left <= right:
            pivot = (left + right) // 2            
            if isBadVersion(pivot) and pivot == 1:
                return 1
            if isBadVersion(pivot) and not isBadVersion(pivot - 1):
                return pivot
            if isBadVersion(pivot):
                right = pivot - 1
            else:
                left = pivot + 1
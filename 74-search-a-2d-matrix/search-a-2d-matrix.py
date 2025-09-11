class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        for i in range(len(matrix)):
            l=0
            r= len(matrix[l])-1
            while l<=r:
                middle = l+((r-l)//2)
                if matrix[i][middle]==target:
                    return(True)
                elif matrix[i][middle]<target:
                    l=middle+1
                else:
                    r=middle-1

        return False
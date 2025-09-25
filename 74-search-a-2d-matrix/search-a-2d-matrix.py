class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        for i in range(len(matrix)):
            l=0
            r= len(matrix[i])-1
            while l<=r:
                middle = l+(r-l)//2
                if matrix[i][middle] ==target:
                    return True

                elif matrix[i][middle] >target:
                    r=middle-1

                else:
                    l=middle+1


        return False

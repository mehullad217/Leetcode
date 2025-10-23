class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        points.sort()
        overlapping = points[0][1]
   
        min_arrows=1
        for i in range(1,len(points)):
            if points[i][0]<=overlapping:
                overlapping = min(points[i][1],overlapping)
                continue

            else:
                overlapping = points[i][1]
                min_arrows+=1
     


        return min_arrows
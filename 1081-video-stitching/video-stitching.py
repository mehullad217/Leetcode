class Solution:
    def videoStitching(self, clips: List[List[int]], time: int) -> int:
        clips.sort()
        n=len(clips)
        max_end = 0
        furthest_end = 0
        used=0
        i=0
        while max_end<time:

            while i<n and clips[i][0]<= max_end:
                furthest_end = max(furthest_end , clips[i][1])

                i+=1
                
            if furthest_end == max_end:
                return -1 
            used+=1
            max_end = furthest_end
     

        return used

                
                



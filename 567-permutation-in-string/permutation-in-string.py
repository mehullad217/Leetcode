class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        have = [0]*26
        need=[0] *26
        m,n = len(s1) , len(s2)
        l=0
        r= 0

        for i in s1:
            need[ord(i)-ord('a')]+=1

        while r<n:
            have[ord(s2[r]) -ord('a')]+=1

            if r-l+1> m:
                have[ord(s2[l]) - ord('a')]-=1
                l+=1
            if r-l+1 ==m  and  have ==need:
                return True
            r+=1
        
        return False
        
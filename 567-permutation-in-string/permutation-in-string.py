class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        from collections import Counter
        h1=Counter(s1)
        l=0
        for r in range(len(s2)):
            r= l+len(s1)
            h2 = Counter(s2[l:r])
            if h1==h2:
                return True
            l+=1
        
        return False
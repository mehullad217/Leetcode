class Solution:
    def countGoodSubstrings(self, s: str) -> int:
        from collections import Counter
        a={}
        l=0

        count=0
        while l<len(s):
            r=l+3
            window = s[l:r]
            a = Counter(window)
        #print(a)
        #print(len(set(a)))
            if len(set(a)) ==3:
        
                count+=1


            l+=1
        return count
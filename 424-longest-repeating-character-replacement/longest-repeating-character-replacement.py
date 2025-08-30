class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l=0
        r=0
        n=len(s)
        count={}
        max_count =0
        
        while r<len(s):
            count[s[r]] = count.get(s[r],0)+1
            max_count = max(max_count, count[s[r]])

            while (r-l+1) - max_count> k:
                count[s[l]]-=1
                l+=1
            longest  = max( r-l+1 , max_count)
            r+=1

        return longest
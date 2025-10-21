class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        n= len(s)
        l=0
        r=0
        sett = set()
        longest = 0
        for r in range(n):
            while s[r] in sett:
                sett.remove(s[l])
                l+=1
            
            sett.add(s[r])
            w = r-l+1
            longest = max(w , longest)

            




        return longest
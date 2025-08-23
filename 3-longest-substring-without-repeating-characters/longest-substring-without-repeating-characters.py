class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l=0
        r=0
        sub = ""
        max_length =len(sub)
        while r<len(s):
            #print('R:',r)
            #print('initial_sub:',sub)
            #print('new_element',s[r])
            if s[r] not in sub:
                r+=1
                sub = s[l:r]
                max_length = max(max_length,len(sub))
            else:
                l+=1
                r=l
                print('final_sub',sub)
                sub= s[l:r]
        return max_length
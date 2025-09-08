class Solution:
    def minWindow(self, s: str, t: str) -> str:
        from collections import Counter

        a= Counter(t)
        b= Counter()
        l=0 
        r=0 
        min_substring = ""
        if len(s)<len(t):
            return ""
        while r< len(s):
            if s[r] in t:
                b[s[r]]+=1
                #print(b)

            while b>=a:
                # print('Current Min_string is ' , min_substring)
                # print('updated window is ' ,s[l:r+1] )
                if not min_substring or len(s[l:r+1]) < len(min_substring):
                    min_substring = s[l:r+1]
                #print('updated Min_string is' , min_substring)
                if s[l] in b.keys():
                    b[s[l]]-=1
                if s[l] in b and b[s[l]]==0:
                    del b[s[l]]

                l+=1
            
            r+=1
        return min_substring
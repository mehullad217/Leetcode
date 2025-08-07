class Solution:
    def shortestBeautifulSubstring(self, s: str, k: int) -> str:
        r= 0
        l=0
        count_1 =0
        k=k
        best = ""

        for r in range(len(s)):
            if s[r]=='1':
                count_1+=1
            

            while count_1>k:
                if s[l]=='1':
                    count_1-=1
                    l+=1

            while count_1==k:
                candidate = s[l:r+1]
                if best == "" or len(candidate) < len(best):
                    best = candidate
                elif len(candidate) == len(best) and candidate < best:
                    best = candidate

                if s[l] == '1':
                    count_1 -= 1
                l += 1

        return best
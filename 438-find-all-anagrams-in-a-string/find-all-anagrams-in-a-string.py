class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        from collections import Counter
        a={}
        b ={}
        output=[]
        k= len(p)
        anag = Counter(p)
        window = Counter(s[:k])

        if anag == window:
            output.append(0)

        for i in range(k,len(s)):
            window[s[i]]+=1
            window[s[i-k]]-=1

            if window[s[i-k]]==0:
                del window[s[i-k]]
            if window == anag:
                output.append(i-k+1)

        return output        
class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = "".join(char.lower() for char in s if char.isalnum())
        l=0
        r=len(s)-1
        while l<r:
            if s[l] ==s[r]:
                l+=1
                r-=1
                continue
            else:
                return False

        return True
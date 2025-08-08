class Solution:
    def isPalindrome(self, s: str) -> bool:
        cleaned_chars = [char for char in s if char.isalnum()]
        s = "".join(cleaned_chars).lower()
        l=0
        r= len(s)-1
        flag=True
        while l<=r:
            if s[l]==s[r]:
                l+=1
                r-=1
            else:
                flag = False
                break
        return flag

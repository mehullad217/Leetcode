class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        have = [0]*26
        need = [0]*26
        l=0
        for i in s1:
             have[(ord(i)- ord('a'))] +=1

        for r in range(len(s2)):
            need[(ord(s2[r])- ord('a'))] +=1
            if r-l+1> len(s1):
                need[(ord(s2[l])- ord('a'))] -=1
                l+=1
            if have == need:
                return True


        return False 


        
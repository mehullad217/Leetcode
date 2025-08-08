class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        l=0
        r= len(nums)-1
        if len(nums)>0 and val in nums:
            while l<=r:
                if nums[l] == val:
                    temp=nums[l]
                    #print(temp)
                    nums[l]= nums[r]
                    nums[r]=temp
                    #print(s[r])
                    r-=1
                else:
                    l+=1

            for i in range(len(nums)):
                if nums[i]== val:
                    break
            return i
        else:
            return len(nums)
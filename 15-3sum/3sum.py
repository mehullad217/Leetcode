class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        output=[]
        i=0
        nums.sort()
        for i in range(len(nums)):
            if i>0 and nums[i-1] == nums[i]:
                continue
            l=i+1
            r = len(nums)-1
            while l<r:
                sum1 = nums[i] +nums[l]+ nums[r]
                if sum1 <0:
                    l+=1
                elif sum1>0:
                    r-=1
                else:
                    output.append([nums[i] , nums[l] ,nums[r]])
                    while l<r and nums[l] ==nums[l+1]:
                        l+=1
                    while l<r and nums[r] ==nums[r-1]:
                        r-=1

                    l+=1
                    r-=1
        return output
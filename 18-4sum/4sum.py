class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        output = []

        i=0

        nums.sort()
        for i in range(len(nums)):
            if i>0 and nums[i] ==nums[i-1]:
                continue
            j=i+1
            for j in range(j,len(nums)):
                if j>i+1 and nums[j] ==nums[j-1]:
                    continue    
                l= j+1
                r = len(nums)-1
                while l<r:

                    sum1= nums[i]+ nums[j] + nums[l]+nums[r]
                    # print('This is nums[i]',nums[i])
                    # print('This is nums[j]' ,  nums[j])
                    # print('This is nums[l]',nums[l])
                    # print('This is nums[r]',nums[r])
                    # print('This is sum1',sum1)
                    if sum1 < target:
                        l+=1
                    elif sum1 > target:
                        r-=1
                    else:
                        output.append([nums[i],nums[j],nums[l],nums[r]])
                        while l<r and nums[l]==nums[l+1] :
                            l+=1
                        while l<r and nums[r]==nums[r-1] :
                            r-=1
                        l+=1
                        r-=1
        return output
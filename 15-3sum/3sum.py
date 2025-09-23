class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        i=0
        nums.sort()
        output_set=set()
        output=[]
        
        for i in range(len(nums)-1):
            if i>0 and nums[i-1] == nums[i]:
                continue
            l=i+1
            r= len(nums)-1

        
            while l<r:
                sum1 = nums[i]+ nums[l]+ nums[r]
                if sum1 == 0:
                    output_set.add((nums[i],nums[l],nums[r]))
                    l+=1
                    continue

                elif sum1> 0:
                    r-=1
                else:
                    l+=1

        for i in output_set:
            output.append(list(i))

        return output

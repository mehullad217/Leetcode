class Solution:
    def trap(self, height: List[int]) -> int:
        nums= height
        leftmax=0
        rightmax=0
        l=0
        n= len(nums)
        r=n-1
        total_water =0

        for i in range(n):
            if leftmax <=rightmax:
                leftmax = max(leftmax,nums[l])
                # print("leftmaxis" , leftmax )
                water = max(0,leftmax- nums[l])
                # print('currentwater', water)
                # print("l was",l)
                l+=1
                # print("l increased to",l)
            else:
                rightmax = max(rightmax,nums[r])
                # print("rightmaxis" , rightmax)
                water = max(0,rightmax- nums[r])
                # print('currentwaterfromright', water)
                # print("r was",r)
                r-=1

            total_water+=water
        return total_water
class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        output_array =[0]*len(nums)
        l=0
        r=len(nums)-1
        w =len(nums)-1
        while l<=r:
            if abs(nums[l]) <=abs(nums[r]):
                print(nums[r]**2)
                output_array[w]=nums[r]**2
                r-=1
                w-=1
            else:
                print(nums[l]**2)
                output_array[w]=nums[l]**2
                l+=1
                w-=1

        return output_array
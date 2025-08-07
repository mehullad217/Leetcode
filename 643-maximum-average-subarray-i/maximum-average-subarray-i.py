class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        #nums = [1,12,-5,-6,50,3]
        curr_sum=0
        window_sum= float('-inf')
        k=k
        for i in range(len(nums)):
            curr_sum = curr_sum+ nums[i]
            
            #print("this is i :" ,i)
            #print(curr_sum)
            if i>=k-1:
                window_sum = max(window_sum, curr_sum)
                #print(window_sum)
                curr_sum = curr_sum - nums[i-k+1]

        return (window_sum/k)

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        if k<=0:
            return []


        n=len(nums)
        if k==1 or n==0:
            return nums[:]

        dq = deque()
        out =[]
        for i, ch in enumerate(nums):
            while dq and nums[dq[-1]]<= ch:
                dq.pop()

        
            dq.append(i)


            if i-k >=dq[0]:
                dq.popleft()
  
        
            if i>=k-1:
                out.append(nums[dq[0]])


        return out
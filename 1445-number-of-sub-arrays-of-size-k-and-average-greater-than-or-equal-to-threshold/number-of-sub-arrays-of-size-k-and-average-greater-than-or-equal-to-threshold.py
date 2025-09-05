class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:



        curr_sum=0
        count=0
        for i in range(k):
            curr_sum+= arr[i]

        avg = curr_sum/k
        if avg>=threshold:
            count+=1

        for i in range(k,len(arr)):
            curr_sum+= arr[i]
            curr_sum-= arr[i-k]

            avg = curr_sum/k
            if avg>=threshold:
                count+=1

        return (count)
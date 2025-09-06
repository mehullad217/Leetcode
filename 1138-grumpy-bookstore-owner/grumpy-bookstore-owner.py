class Solution:
    def maxSatisfied(self, customers: List[int], grumpy: List[int], minutes: int) -> int:
        max_cust=0
        extra = 0 
        og_cust=0
        for i in range(minutes):
            if grumpy[i]==1:
                extra+=customers[i]

        max_cust = max(max_cust, extra)
        for i in range(minutes, len(grumpy)):
            if grumpy[i]==1:
                extra+=customers[i] 
            if grumpy[i-minutes]==1:
                extra-=customers[i-minutes]

            max_cust = max(max_cust,extra)

        

        for i in range (len(grumpy)):
            if grumpy[i]==0:
                og_cust+=customers[i]

        return og_cust + max_cust
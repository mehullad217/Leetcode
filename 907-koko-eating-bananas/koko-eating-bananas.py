class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        min_eating=1
        max_eating = max(piles)
        output = max_eating
        while min_eating<=max_eating:
            middle = min_eating +((max_eating-min_eating)//2)
            hours = 0
            for i in range (len(piles)):
                hours += math.ceil(piles[i]/middle)

            if hours<=h:
                output = min(output,middle)

                max_eating = middle-1

            if hours>h:
                min_eating  = middle+1

        return output
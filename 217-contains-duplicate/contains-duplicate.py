class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        from collections import Counter
        c = Counter(nums)
        for i in c:
            if c[i]>1:
                return True

        return False
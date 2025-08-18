class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        pairs = list(zip(position,speed))
        pairs.sort(key = lambda x:x[0],reverse=True)
        stack =[]
        for i in (pairs):
            time = ((target- i[0])/i[1])
            if not stack:
                stack.append(time)
            elif stack[-1]>=time:
                continue
            else:
                stack.append(time)
        return len(stack)
        
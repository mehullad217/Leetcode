class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        ans = [0]*len(temperatures)
        stack1 =[]
        for i in range(len(temperatures)):
            if not stack1:
                stack1.append(i)
            elif temperatures[i] > temperatures[stack1[-1]]:
                while stack1 and temperatures[i]>temperatures[stack1[-1]]:
                    pop = stack1.pop()
                    ans[pop] = i - pop
                stack1.append(i)
            else:
                stack1.append(i)

        return ans
        
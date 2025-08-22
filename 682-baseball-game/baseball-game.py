class Solution:
    def calPoints(self, operations: List[str]) -> int:
        stk = []
        for  i in operations:
            if i.lstrip('-').isdigit():
                stk.append(int(i))
            elif i =="D":
                stk.append(stk[-1]*2)

            elif i=="C":
                stk.pop()
            else:
                sum1 = stk[-1]+stk[-2]
                stk.append(sum1)
        return sum(stk)
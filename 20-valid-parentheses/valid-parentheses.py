class Solution:
    def isValid(self, s: str) -> bool:
        stack1= []
        dict1 = {')': '(',
        '}':'{',']':'['}
        if len(s)>1:
            for i in s:
                if i in ['(' ,'{' ,"["]:
                    stack1.append(i)
                elif i in [')' ,'}',']']:
                    if len(stack1):
                        if stack1[-1] ==dict1[i]:
                            stack1.pop()
                        else:
                            return False
                    else:
                        return False
        else:
            return False                
        if stack1:
            return False
        else:
            return True
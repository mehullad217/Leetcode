class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        #tokens = ["2","1","+","3","*"]
        stack1 =[ ]
        operations = {"+" ,"-" ,"/" ,"*"}
        
        for i in tokens:
            if i not in operations:
                    stack1.append(int(i))
            else:
                if i =='+':
                        pop1 =stack1.pop()
                        pop2 = stack1.pop()
                        result =(pop2)+(pop1)
                        stack1.append(result)
                        #print(stack1)
                elif i =='*':
                        pop1 =stack1.pop()
                        pop2 = stack1.pop()
                        result =(pop2)*(pop1)
                        stack1.append(result)
                        #print(stack1)
                elif i =='/':
                        pop1 =stack1.pop()
                        pop2 = stack1.pop()
                        result =(pop2)/(pop1)
                        stack1.append(int(result))
                        #print(stack1)

                elif i =='-':
                        pop1 =stack1.pop()
                        pop2 = stack1.pop()
                        result =(pop2)-(pop1)
                        stack1.append(result)
                        #print(stack1)
        return stack1[-1]
class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stk=[]
        for i in asteroids:
            alive=True
            if i>0:
                stk.append(i)
            else:
                if not stk or stk[-1]<0:
                    stk.append(i)
                    continue
                while  stk and (stk[-1]>0 and i<0):
                    if abs(stk[-1])<abs(i):
                        stk.pop()
                    elif abs(stk[-1]) == abs(i):
                        stk.pop()
                        alive= False
                        break
                    else:
                        alive =False
                        break
                if alive:
                    stk.append(i)
        return stk
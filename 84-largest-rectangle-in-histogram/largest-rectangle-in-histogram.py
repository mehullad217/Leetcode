class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stk = []
        max_area =0 
        n= len(heights)
        for i , height in enumerate(heights):
            start =i
            while stk and height< stk[-1][1]:
                j, h = stk.pop() 
                area = h *(i-j)
                max_area = max(max_area,area)
                start = j
            stk.append((start, height))

        while stk:
            j,h= stk.pop()
            w =n-j
            max_area =max(max_area ,  h*(n-j))
        return max_area


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        #a= ['eat', 'tea', 'tan', 'ate', 'nat', 'bat']
        dict1 ={}
        output=[]
        for i in strs:
            sorted_i = sorted(i)
            sor = "".join(sorted_i)
            if sor in dict1.keys():
                dict1[sor].append(i)
            else:
                dict1[sor]=[]
                dict1[sor].append(i) 

        for i in dict1.keys():
            output.append(dict1[i])

        return (output)
        
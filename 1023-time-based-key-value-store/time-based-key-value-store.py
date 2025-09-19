class TimeMap:

    def __init__(self):
        self.store= {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.store:
            self.store[key] = []
        self.store[key].append([value,timestamp])

    def get(self, key: str, timestamp: int) -> str:
        res = ""
        val = self.store.get(key,[])
        l=0
        r= len(val)-1
        while l<=r:
            middle = l+(r-l)//2
            if val[middle][-1] <=timestamp:
                l=middle+1
                res = val[middle][0]
            elif val[middle][-1] >timestamp:
                r=middle-1

        return res


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)
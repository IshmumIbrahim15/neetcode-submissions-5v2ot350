class TimeMap:

    def __init__(self):
        self.hashMap = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.hashMap:
            self.hashMap[key] = []
        self.hashMap[key].append([value, timestamp])

    def get(self, key: str, timestamp: int) -> str:
        i = 0
        j = len(self.hashMap.get(key, [])) - 1

        res = ""

        while(i <= j):
            m = (i + j) // 2
            if(self.hashMap.get(key,[])[m][1] <= timestamp):
                res = self.hashMap.get(key,[])[m][0]
                i = m + 1
            else:
                j = m - 1
            
        return res
                
        
class TimeMap:

    def __init__(self):
        #Hashmap key = person, value = list with index representing time
        self.time_hash = {}


    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.time_hash:
            self.time_hash[key] = []
        self.time_hash[key].append((value, timestamp))


    def get(self, key: str, timestamp: int) -> str:
        if key not in self.time_hash:
            return -1
        else:
            l = 0
            r = len(self.time_hash[key])-1

            while l<=r: #Check when there's one element left too
                mid = (l+r)//2
                if self.time_hash[key][mid][1] == timestamp:
                    return self.time_hash[key][mid][0]
                elif self.time_hash[key][mid][1] > timestamp:
                    r = mid-1
                else:
                    l = mid + 1
                

        return self.time_hash[key][0][0]
        

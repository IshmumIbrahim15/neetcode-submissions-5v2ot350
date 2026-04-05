class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        posSpeed = []
        
        for i in range(len(position)):
            posSpeed.append([position[i], speed[i]])
        
        posSpeed.sort()
        time = []
        time.append((target - posSpeed[-1][0])/posSpeed[-1][1])

        for i in range(len(posSpeed) - 2, -1, -1):
            currTime = (target - posSpeed[i][0])/posSpeed[i][1]
            if currTime > time[-1]:
                time.append(currTime)

        return len(time)



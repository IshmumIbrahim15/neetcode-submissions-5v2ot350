class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        posSpeed = []

        for i in range(len(position)):
            posSpeed.append([position[i],speed[i]])
        
        posSpeed.sort()
        posSpeed.reverse()

        stack = []
        fleet = 0
        for i in range(len(posSpeed)):
            time = (target - posSpeed[i][0]) / posSpeed[i][1]
            if not stack:
                stack.append(time)
            elif time <= stack[-1]:
                fleet += 1
            else:
                stack.append(time)
        
        return len(stack)
        

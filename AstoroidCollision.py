#using stack
class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stck = []
        for x in asteroids:
            if x > 0:
                stck.append(x)
            else:
                while stck and stck[-1] > 0 and stck[-1] < -x:
                    stck.pop()
                if stck and stck[-1] == -x:
                    stck.pop()
                elif not stck or stck[-1] < 0:
                    stck.append(x)
        return stck

class Solution:
    def asteroidCollision(self, asteroids):
        stack = []

        for asteroid in asteroids:
            alive = True

            while alive and asteroid < 0 and stack and stack[-1] > 0:

                if stack[-1] < -asteroid:
                    # Top asteroid is smaller
                    stack.pop()

                elif stack[-1] == -asteroid:
                    # Both destroy each other
                    stack.pop()
                    alive = False

                else:
                    # Current asteroid is smaller
                    alive = False

            if alive:
                stack.append(asteroid)

        return stack
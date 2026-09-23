from collections import deque
class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        dead = set(deadends)
        if "0000" in dead:
            return -1
        queue = deque()
        queue.append(("0000",0))
        visited = set()
        visited.add("0000")
        while queue:
            current , moves = queue.popleft()
            if current == target:
                return moves
            for i in range(4):
                digit = int(current[i])
            #now i move the digit forward and backword
                for change in [-1,1]:
                    new_digit = (digit + change) % 10 
                    next_state = (current[:i] + str(new_digit) + current[i + 1:])
                    if next_state not in dead and next_state not in visited:
                        visited.add(next_state)
                        queue.append((next_state,moves + 1))
        return -1

        
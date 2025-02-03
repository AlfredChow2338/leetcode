class Solution:
    def maxDistance(self, s: str, k: int) -> int:
        x, y = 0, 0  
        maxi = 0  
        move_count = 1  
        
        for direction in s:
            if direction == 'N':
                y += 1
            elif direction == 'W':
                x -= 1
            elif direction == 'S':
                y -= 1
            else:
                x += 1
            
            curr_distance = abs(x) + abs(y)
            
            # Update the maximum distance considering:
            # - The current distance
            # - The potential extra distance that can be covered using 'k' extra moves
            maxi = max(maxi, curr_distance, min(move_count, curr_distance + (k * 2)))
            
            move_count += 1  
        return maxi
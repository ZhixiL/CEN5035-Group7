Here is the implementation of the `numberOfPoints` function in Python:


class Solution:
    def numberOfPoints(self, nums: List[List[int]]) -> int:
        start_points = []
        end_points = []
        
        # Store all the start and end points separately
        for car in nums:
            start_points.append(car[0])
            end_points.append(car[1])
        
        # Find the minimum start point and maximum end point
        min_start = min(start_points)
        max_end = max(end_points)
        
        # Count the number of points between the minimum start and maximum end points
        count = 0
        for i in range(min_start, max_end + 1):
            count += 1
        
        return count


Note: This implementation assumes that the given `nums` array is valid and non-empty.
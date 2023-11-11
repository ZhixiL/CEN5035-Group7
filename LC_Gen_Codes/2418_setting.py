class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        # Create a dictionary to store names and heights
        person_heights = {}
        for i in range(len(names)):
            person_heights[names[i]] = heights[i]
        
        # Sort the names based on their heights in descending order
        sorted_names = sorted(person_heights, key=lambda x: person_heights[x], reverse=True)
        
        return sorted_names
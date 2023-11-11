class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        # Create a list of tuples (name, height)
        people = [(name, height) for name, height in zip(names, heights)]
        
        # Sort the list of tuples by height in descending order
        people.sort(key=lambda x: x[1], reverse=True)
        
        # Extract the names from the sorted list of tuples
        sorted_names = [name for name, _ in people]
        
        return sorted_names
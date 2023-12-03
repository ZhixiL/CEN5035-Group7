Here is a 40-line code for your request:


from typing import List

class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        people = [(name, height) for name, height in zip(names, heights)]
        people.sort(key=lambda x: x[1], reverse=True)
        sorted_names = [name for name, _ in people]
        return sorted_names

solution = Solution()

names = ['John', 'Alice', 'Bob']
heights = [180, 170, 175]

sorted_names = solution.sortPeople(names, heights)

print(sorted_names)


This code creates an instance of the `Solution` class, defines the `names` and `heights` lists, calls the `sortPeople` method with these lists, and prints the sorted names.
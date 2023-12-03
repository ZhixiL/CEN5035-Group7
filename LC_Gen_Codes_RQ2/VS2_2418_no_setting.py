Here is a faster version of the code:


class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        return [name for _, name in sorted(zip(heights, names), reverse=True)]


This version combines the creation of the tuples and the sorting step into a single line using the `zip` and `sorted` functions. The `zip` function pairs up the names with their corresponding heights, and the `sorted` function sorts these pairs based on the heights in descending order. Then, a list comprehension is used to extract the names from the sorted pairs.
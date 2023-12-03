Here's a one-liner solution that uses list comprehension and the `filter` function to eliminate empty splits:


class Solution:
    def splitWordsBySeparator(self, words: List[str], separator: str) -> List[str]:
        return [split for word in words for split in filter(None, word.split(separator))]


This code will produce the same result as the original code, but in a more concise way.
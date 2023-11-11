Here's the implementation of the `splitWordsBySeparator()` function in Python:


class Solution:
    def splitWordsBySeparator(self, words: List[str], separator: str) -> List[str]:
        result = []
        for word in words:
            splits = word.split(separator)
            for split in splits:
                if split != "":
                    result.append(split)
        return result


This function takes in a list of strings `words` and a separator `separator` as input. It initializes an empty list `result` to store the new strings formed after the splits.

It then iterates through each string `word` in the `words` list. For each word, it splits the word using the `split()` method with the `separator` as the delimiter. The resulting splits are stored in the `splits` list.

Next, it iterates through each split in the `splits` list. If the split is not an empty string, it appends it to the `result` list.

Finally, it returns the `result` list containing the new strings formed after the splits.

Note that the implementation checks for empty strings and excludes them from the resulting list, as mentioned in the prompt.
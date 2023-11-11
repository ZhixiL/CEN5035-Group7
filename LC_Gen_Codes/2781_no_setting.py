class Solution:
    def is_valid(self, substr: str, forbidden: List[str]) -> bool:
        # check if a substring is valid
        for f in forbidden:
            if f in substr:
                return False
        return True
    
    def longestValidSubstring(self, word: str, forbidden: List[str]) -> int:
        longest_length = 0
        n = len(word)
        
        # generate all possible substrings of word
        for i in range(n):
            for j in range(i+1, n+1):
                substr = word[i:j]
                if self.is_valid(substr, forbidden) and len(substr) > longest_length:
                    longest_length = len(substr)
                    
        return longest_length

The above code defines a class Solution and a method longestValidSubstring. The method takes a string word and an array of strings forbidden as input and returns the length of the longest valid substring.

The method first defines a helper function is_valid to check if a given substring is valid. It iterates over the forbidden list and checks if any substring in forbidden is present in the given substring. If a forbidden substring is found, the function returns False. If none of the forbidden substrings are found, the function returns True.

The method then initializes the longest_length variable to 0 and the n variable to the length of the word string.

It uses nested loops to generate all possible substrings of the word string. The outer loop iterates from 0 to n-1 and the inner loop iterates from i+1 to n. This generates all possible substrings of word starting from index i.

For each generated substring, it calls the is_valid function to check if it is valid. If the substring is valid and its length is greater than the current longest_length, it updates longest_length to the length of the current substring.

Finally, it returns the longest_length as the output.
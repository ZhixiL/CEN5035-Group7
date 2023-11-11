class Solution:
    def longestValidSubstring(self, word: str, forbidden: List[str]) -> int:
        forbidden_set = set(forbidden)  # Convert the forbidden list into a set for efficient substring checking
        
        longest_substring_length = 0  # Initialize the length of the longest valid substring as 0
        
        for i in range(len(word)):
            for j in range(i+1, len(word)+1):
                substring = word[i:j]  # Get the substring starting from index i and ending at index j
                
                # Check if the substring is valid by iterating through each substring of the substring
                is_valid = True
                for k in range(len(substring)):
                    for l in range(k+1, len(substring)+1):
                        subsubstring = substring[k:l]  # Get the subsubstring starting from index k and ending at index l
                        
                        if subsubstring in forbidden_set:
                            is_valid = False
                            break
                    if not is_valid:
                        break
                
                # If the substring is valid and longer than the current longest valid substring, update the length
                if is_valid and len(substring) > longest_substring_length:
                    longest_substring_length = len(substring)
        
        return longest_substring_length
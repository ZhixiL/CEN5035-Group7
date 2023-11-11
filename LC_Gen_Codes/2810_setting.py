class Solution:
    def finalString(self, s: str) -> str:
        reversed_string = ''
        for char in s:
            if char == 'i':
                reversed_string = char + reversed_string
            else:
                reversed_string += char
        
        return reversed_string
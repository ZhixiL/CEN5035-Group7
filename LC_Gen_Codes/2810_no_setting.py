class Solution:
    def finalString(self, s: str) -> str:
        result = ""
        stack = []
        for c in s:
            if c == 'i':
                stack.reverse()
            else:
                stack.append(c)
        result += ''.join(stack)
        return result

# Testing the code
solution = Solution()
print(solution.finalString("string"))  # Output: "rtsng"
print(solution.finalString("poiinter"))  # Output: "ponter"
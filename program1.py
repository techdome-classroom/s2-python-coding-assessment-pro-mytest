class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack = []
        # Dictionary to map closing brackets to their corresponding opening ones
        mapping = {')': '(', '}': '{', ']': '['}

        for char in s:
            if char in mapping:
                # Pop the top element from the stack if it is not empty, otherwise assign a dummy value
                top_element = stack.pop() if stack else '#'

                # If the top element doesn't match the corresponding opening bracket, return False
                if mapping[char] != top_element:
                    return False
            else:
                # If it's an opening bracket, push it onto the stack
                stack.append(char)

        # If the stack is empty at the end, then the string is valid
        return not stack

# Example usage:
solution = Solution()
print(solution.isValid("()"))        # Output: True
print(solution.isValid("()[]{}"))    # Output: True
print(solution.isValid("(]"))        # Output: False

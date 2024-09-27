class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        # Mapping of Roman numerals to integers
        roman_to_int = {
            'I': 1, 'V': 5, 'X': 10, 'L': 50,
            'C': 100, 'D': 500, 'M': 1000
        }
        
        total = 0
        prev_value = 0
        
        # Traverse the Roman numeral string from left to right
        for char in s:
            current_value = roman_to_int[char]
            
            # If the previous value is smaller, it means we should subtract it (special case like IV, IX, etc.)
            if prev_value < current_value:
                total += current_value - 2 * prev_value
            else:
                total += current_value
            
            prev_value = current_value
        
        return total

# Example usage:
solution = Solution()
print(solution.romanToInt("III"))        # Output: 3
print(solution.romanToInt("LVIII"))      # Output: 58
print(solution.romanToInt("MCMXCIV"))    # Output: 1994



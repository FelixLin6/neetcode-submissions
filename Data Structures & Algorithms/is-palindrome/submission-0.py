class Solution:
    def isPalindrome(self, s: str) -> bool:
        i, j = 0, len(s) - 1
        while i < j:
            a, b = s[i].lower(), s[j].lower()

            if not a.isalnum():
                i += 1
                continue
            if not b.isalnum():
                j -= 1
                continue

            if a != b:
                return False
            i += 1
            j -= 1
        
        return True
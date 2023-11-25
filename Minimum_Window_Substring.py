class Solution:
    def checker(self, substr: str, tester: str) -> bool:
        for char, count in tester.items():
            if substr.get(char, 0) < count:
                return False
        return True
        
    def minWindow(self, s: str, t: str) -> str:
        if not s or not t:
            return ""

        tester_counts = {}
        for char in t:
            tester_counts[char] = tester_counts.get(char, 0) + 1

        substr_counts = {}
        left, right = 0, 0
        minLength = float('inf')
        minStr = ""

        while right < len(s):
            substr_counts[s[right]] = substr_counts.get(s[right], 0) + 1
            right += 1

            while self.checker(substr_counts, tester_counts):
                if right - left < minLength:
                    minLength = right - left
                    minStr = s[left:right]

                substr_counts[s[left]] -= 1
                if substr_counts[s[left]] == 0:
                    del substr_counts[s[left]]

                left += 1

        return minStr

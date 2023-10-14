class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        #can check by checking the count of the element is zero if it is append
        subStr = ''
        currentLength = 0
        for element in range(0, len(s)):
            subStr = subStr + s[element];
            if (element + 1) == len(s):
                if len(subStr) > currentLength:
                    currentLength = len(subStr)
                break;
            else:
                for newChar in range((element + 1), len(s)):
                    if subStr.count(s[newChar]) == 0:
                        subStr = subStr + s[newChar]
                        if newChar == (len(s) - 1):
                            if len(subStr) > currentLength:
                        
                                currentLength = len(subStr)
                            subStr = ''
                            break;
                        else:
                            continue;
                    else:
                        if len(subStr) > currentLength:
                            currentLength = len(subStr)
                        subStr = ''
                        break;
        return currentLength;

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        result = ""
        _max = 0
        for i in range(len(s)):
            result = ""
            count=1
            result+=s[i]
            for j in range(i+1, len(s)):
                if s[j] not in result:
                    result+=s[j]
                    count+=1
                    # print(result)
                else:
                    _max = max(_max, count) 
                    break
            _max = max(_max, count)
        return _max
    
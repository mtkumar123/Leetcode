class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: bool
        """
        """
        catsandog
        cats, cat, and, dog
        """
        computed_values = {}
        def word_check(index):
            if index == len(s):
                return True
            for word in wordDict:
                if word == s[index:index+len(word)]:
                    index += len(word)
                    if index in computed_values:
                        if computed_values[index]:
                            return True
                        else:
                            index -= len(word)
                            continue
                    else:
                        result = word_check(index)
                        computed_values[index] = result
                        if result:
                            return True
                        else:
                            index -= len(word)
                            continue
            return False
        result = word_check(0)
        return result

word_break = Solution()
word_dict = ["apple","pen"]
s = "applepenapple"
result = word_break.wordBreak(s, word_dict)
            

        
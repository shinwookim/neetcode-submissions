class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if len(digits) == 0:
            return []
        ans = []
        digitMap = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "qprs",
            "8": "tuv",
            "9": "wxyz",
        }
        def generate(prefix, i):
            if i == len(digits):
                ans.append(prefix)
            else:
                for c in digitMap[digits[i]]:
                    generate(prefix + c, i + 1)

        generate("", 0)
        return ans
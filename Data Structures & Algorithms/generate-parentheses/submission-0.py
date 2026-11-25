class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        ans = []

        def generate(s, n, closing):
            if n == 0:
                while closing > 0:
                    s += ")"
                    closing -= 1
                ans.append(s)
            else:
                generate(s + "(", n - 1, closing + 1)
                if closing > 0:
                    generate(s + ")", n, closing - 1)
        generate("", n, 0)
            
        return ans
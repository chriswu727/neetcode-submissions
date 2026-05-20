class Solution:
    def isPalindrome(self, s: str) -> bool:
        ns = ""
        for c in s:
            if c.isalnum():
                ns += c.lower()
        return ns == ns[::-1]


        # l, r = 0, len(s) - 1
        # while l < r:
        #     if s[l] == " ":
        #         l += 1
        #     if s[r] == " ":
        #         r -= 1
        #     if s[l] != s[r]:
        #         return False
        # return True
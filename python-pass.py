# defined class name solution
class Solution:
 #  defined function name longestPalindrome to  give string  and the give one  parameter s to refrence to string and keyword self refers to the function in same class
    def longestPalindrome(self, s):
        # defined function to give three parameters s,l,r by it specific index character the function is odd or even
        def getPalindrome(s, l, r):
            # this loop working on every character on string and check the number is even and return character
            while l >= 0 and r < len(s) and s[l] == s[r]:
                l -= 1
                r += 1
            return s[l+1:r]
        # defined variable res to save character
        res = ''
        # this loop to length string by using range method and call function getPalindrome and chicken the length sub is > res save in res
        for i in range(len(s)):
            # odd case 'aba'
            sub = getPalindrome(s, i, i)
            if len(sub) > len(res):
                res = sub
            # even case 'abba'
            sub = getPalindrome(s, i, i+1)
            if len(sub) > len(res):
                res = sub
        return res

        # defined object to class Solution
        s1 = Solution()

        # print by calling function longestPalindrome with give string  using object s1
        print(s1.longestPalindrome('babad'))
        print(s1.longestPalindrome('cbbd'))
        print(s1.longestPalindrome('a'))
        print(s1.longestPalindrome('ac'))

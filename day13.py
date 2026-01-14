"""Given a string s, reverse only all the vowels in the string and return it.

The vowels are 'a', 'e', 'i', 'o', and 'u', and they can appear in both lower and upper cases, more than once."""
class Solution:
    def reverseVowels(self, s: str) -> str:
        vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
        n = len(s)
        s_list = list(s)
        i=0
        while i < n-1:
            if s_list[i] in vowels and s_list[n-1] in vowels:
                tmp = s_list[i]
                s_list[i] = s_list[n-1]
                s_list[n-1] = tmp
                i = i+1
                n = n-1
            elif s_list[i] not in vowels:
                i = i + 1
            elif s_list[n-1] not in vowels:
                n = n - 1
        return "".join(s_list)

s = Solution()
print(s.reverseVowels("heldhkfjcqofhqowhfsajbsdalo"))

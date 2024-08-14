"""

Given a string s, reverse only all the vowels in the string and return it.

The vowels are 'a', 'e', 'i', 'o', and 'u', and they can appear in both lower and upper cases, more than once.

 

Example 1:

Input: s = "hello"
Output: "holle"
Example 2:

Input: s = "leetcode"
Output: "leotcede"
 

Constraints:

1 <= s.length <= 3 * 105
s consist of printable ASCII characters.

"""

class Solution:
    def reverseVowels(self, s: str) -> str:
        vowel = lambda x : True if x in ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'] else False
        vowels = []
        new_s = []
        c = 0

        for i in s:
            if vowel(i):
                if i.islower():
                    vowels.append(i)
                else:
                    vowels.append(i.upper())
        vowels = vowels[::-1]

        for j in s:
            if vowel(j):
                new_s.append(vowels[c])
                c += 1
            else:
                new_s.append(j)

        return ''.join(new_s)
        
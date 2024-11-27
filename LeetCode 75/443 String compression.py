"""
Given an array of characters chars, compress it using the following algorithm:

Begin with an empty string s. For each group of consecutive repeating characters in chars:

If the group's length is 1, append the character to s.
Otherwise, append the character followed by the group's length.
The compressed string s should not be returned separately, but instead, 
be stored in the input character array chars. Note that group lengths that 
are 10 or longer will be split into multiple characters in chars.

After you are done modifying the input array, return the new length of the array.

You must write an algorithm that uses only constant extra space.
"""

class Solution:
    def compress(self, chars: List[str]) -> int:
        l, r = 0, 0
        s = len(chars)

        while l < s:
            n = 0
            r = l
            while r < s and chars[l] == chars[r]:
                if chars[l] == chars[r]:
                    n += 1
                r += 1

            if n > 1:
                for k in range(l + 1, r):
                    chars.pop(l + 1)
                    s -= 1
                for k in range(len(str(n))):
                    l = l + 1
                    chars.insert(l, str(n)[k])
                    s += 1

            l += 1
            r = l

        return len(chars)


class Solution:
    def compress(self, chars: List[str]) -> int:
        d = {}
        
        # Count chars 
        for i in range(0, len(chars)):
            if chars[i] not in d:
                d[chars[i]] = int(1)
                print(d)
            else:
                d[chars[i]] = int(d[chars[i]]) + 1
                print(d)

        # built list
        val = []
        for i,j in d.items():
            if int(j) == 1:
                val.append(str(i))
            else:
                val.append(str(i))
                val.append(str(j))
        chars = list("".join(val))

        return len(val)
    

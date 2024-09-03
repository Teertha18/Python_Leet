# Merge Strings Alternately 
# You are given two strings word1 and word2. Merge the strings by adding letters in alternating order, starting with word1. If a string is longer than the other, append the additional letters onto the end of the merged string.

# Return the merged string.

# Example 1:

# Input: word1 = "abc", word2 = "pqr"
# Output: "apbqcr"
# Explanation: The merged string will be merged as so:
# word1:  a   b   c
# word2:    p   q   r
# merged: a p b q c r
# Example 2:

# Input: word1 = "ab", word2 = "pqrs"
# Output: "apbqrs"
# Explanation: Notice that as word2 is longer, "rs" is appended to the end.
# word1:  a   b 
# word2:    p   q   r   s
# merged: a p b q   r   s
# Example 3:

# Input: word1 = "abcd", word2 = "pq"
# Output: "apbqcd"
# Explanation: Notice that as word1 is longer, "cd" is appended to the end.
# word1:  a   b   c   d
# word2:    p   q 
# merged: a p b q c   d

class Solution(object):
    def mergeAlternately(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: str
        """
        value = ''
        i =0
        if len(word1) == len(word2):
            while i < len(word1):
                value += word1[i] + word2[i]
                i += 1
        elif len(word1)>len(word2):
            while i<len(word1) and i<len(word2):
                value += word1[i] + word2[i]
                i += 1
            value = value + word1[i:len(word1)] 
        elif len(word1)<len(word2):
            while i<len(word1) and i<len(word2):
                value += word1[i] + word2[i]
                i += 1
            value = value + word2[i:len(word2)] 
                

        return value

if __name__ == "__main__":
    S = Solution()
    s1 = S.mergeAlternately("abc","pqr")
    print(s1)
    s2 = S.mergeAlternately("ab","pqrs")
    print(s2)
    s3 = S.mergeAlternately("abcdefghr","pqrs")
    print(s3)
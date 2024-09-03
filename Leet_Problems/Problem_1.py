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
    #  My code 
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
    
    def otherMergeAlternately(self, word1: str, word2: str) -> str:
        # Initialize pointers for both words
        i, j = 0, 0
        result = []
        
        # Iterate while both pointers are within bounds
        while i < len(word1) and j < len(word2):
            result.append(word1[i])
            result.append(word2[j])
            i += 1
            j += 1
        
        # Append remaining characters of word1, if any
        if i < len(word1):
            result.extend(word1[i:])
        
        # Append remaining characters of word2, if any
        if j < len(word2):
            result.extend(word2[j:])
        
        # Join the result list into a string and return
        return ''.join(result)

if __name__ == "__main__":
    S = Solution()
    l = [("abc","pqr"),("ab","pqrs"),("abcdefghr","pqrs")]

    for data in l:
        print(S.mergeAlternately(data[0],data[1]))

    for data in l:
        print(S.otherMergeAlternately(data[0],data[1]))

    
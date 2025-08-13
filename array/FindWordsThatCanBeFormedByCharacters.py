from collections import Counter
class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        result = 0
        chars_count = Counter(chars)
        
        for word in words: # loopthrough and check if the words set of chars is in chars
            word_count = Counter(word)
            # Check if word_count is <= chars_count for all chars
            if all(word_count[c] <= chars_count.get(c, 0) for c in word_count):
                result += len(word)
        return result
        
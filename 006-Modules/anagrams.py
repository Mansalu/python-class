def AreAnagrams(word1, word2):
    """
    A function for determining if two words are anagrams. Returns true if the
    words contain the same letters, false otherwise.
    """
    word1Chars = []
    word2Chars = []

    for letter in word1:
        word1Chars.append(letter)
    for letter in word2:
        word2Chars.append(letter)

    word1Chars.sort()
    word2Chars.sort()

    result = word1Chars == word2Chars
    return result


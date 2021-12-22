# Given a pattern and a string
# map the pattern to the string where a letter[i] in the pattern corresponds to word[i] in the string
# all lowercase letters for both
# words in the string are seperated by a single space with no leading or trailing whitespace

def string_patter(pattern, a):
    # split a into a list
    word_list = a.split()
    # if length of the pattern and length of the list aren't equal, return False
    if len(pattern) != len(word_list):
        return False

    # create a dict with pattern letters as keys and corresponding words from the list as values
    pattern_dict = {pattern[i]: word_list[i] for i in range(len(pattern))}
    # create a mirror dict where list words are keys and corresponding pattern letters are values
    pattern_a_dict = {word_list[i]: pattern[i] for i in range(len(pattern))}

    # loop through range(len(pattern))
    for i in range(len(pattern)):
        # if word from list at i doesn't equal the dictionary[pattern[i]]
        if word_list[i] != pattern_dict[pattern[i]]:
            return False
        # or if pattern letter at i doesn't the reverse dict, rules out edge case where the same word is used for multiple pattern letters
        elif pattern[i] != pattern_a_dict[word_list[i]]:
            return False
    # made it through the loop, pattern matches, return True
    return True

print(string_patter("abba", "lambda school school lambda")) #--> True
print(string_patter("abba", "lambda school school coding")) #--> False
print(string_patter("aaaa", "lambda school school lambda")) #--> False
print(string_patter("abba", "lambda lambda lambda lambda")) #--> False
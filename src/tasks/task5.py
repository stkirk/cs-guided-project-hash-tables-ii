# given an array of strings
# all strings are words consisting of lowercase letters
# group strings that are anagrams of each other and return them as a list that is an item in a larger list
# order the groups in descending order of number of words in a group

def anagram(strs):
    # create a dictionary with a sorted list of letters from each word in strs as key and a list of corresponding words as values
    anagram_dict = {tuple(sorted(word)): [] for word in strs}

    # loop through strs
    for word in strs:
        # sort the word into a tuple of letters in alphabetical order
        word_tuple = tuple(sorted(word))
        # append the word to anagram_dict[word_tuple], they should all exist?
        anagram_dict[word_tuple].append(word)
    
    # list comprehension to loop through the dictionary and return all values
    anagram_list = [anagrams for anagrams in anagram_dict.values()]
    # sort list by len(i) in descending order and return
    return sorted(anagram_list, key=lambda anagram: -len(anagram))

print(anagram(["apt","pat","ear","tap","are","arm"])) #--> [["apt","pat","tap"],["ear","are"],["arm"]]
print(anagram([""])) #--> [[""]]
print(anagram(["a"])) #--> [["a"]]

# print(sorted("apt"))
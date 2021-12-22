"""
You are given a non-empty list of words.

Write a function that returns the *k* most frequent elements.

The list that you return should be sorted by frequency from highest to lowest.
If two words have the same frequency, then the word with the lower alphabetical
order should come first.

Example 1:

```plaintext
Input:
words = ["lambda", "school", "rules", "lambda", "school", "rocks"]
k = 2

Output:
["lambda", "school"]

Explanation:
"lambda" and "school" are the two most frequent words.
```

Example 2:

```plaintext
Input:
words = ["the", "sky", "is", "cloudy", "the", "the", "the", "cloudy", "is", "is"]
k = 4

Output:
["the", "is", "cloudy", "sky"]

Explanation:
"the", "is", "cloudy", and "sky" are the four most frequent words. The words
are sorted from highest frequency to lowest.
```

Notes:

- `k` is always valid: `1 <= k <= number of unique elements.
- words in the input list only contain lowercase letters.
```
"""
"""
Input:
words -> List[str]
k -> int

Output:
List[str]
"""
# The word "frequency" in the prompt should tip off to this strategy
# return the first k words in the sorted list
def top_k_frequent(words, k):
    # build a dictionary: word is key, count is value
    frequency_dict = {}
    # loop through all words
    for word in words:
        # if word is already in frequency_dict
        if word in frequency_dict:
            # increment its value
            frequency_dict[word] += 1
        # otherwise, add it to the dictionary
        else: 
            frequency_dict[word] = 1

    # sort the dictionary by its values
    # sorted will return the keys in a list
    # we want to sort each item in the dictionary as a tuple with occurence first and word second, this way it will sort first by occurence and then if there is a tie move on to alphabetical order of the keys - (2, "lambda")
    # do this by making the return value of the lambda function sort key the tuple
    # tuples help with a second level of comparison
    # default behavior is to sort large-->small, if we want to sort in descending order, throw a negative on the integer
    frequency_list = sorted(frequency_dict, key=lambda word: (-frequency_dict[word], word))

    # now that the list is sorted, we can send back the k most frequently used words
    k_items = frequency_list[0:k]

    return k_items
    

print(top_k_frequent(["lambda", "school", "rules", "lambda", "school", "rocks"], 2))
#--> ["lambda", "school"]
print(top_k_frequent(["the", "sky", "is", "cloudy", "the", "the", "the", "cloudy", "is", "is"], 4)) #--> ["the", "is", "cloudy", "sky"]


# sorted, will sort tuples by the 0 index, then if there is a tie move to the second, and so on
arr = [('b', 2), ('b', 1)]
print(sorted(arr))

# Look up set in docs
unique = set(["the", "sky", "is", "cloudy", "the", "the", "the", "cloudy", "is", "is"])
print("set of unique words in the list", unique)
"""
Given a string, sort it in decreasing order based on the frequency of characters.

Example 1:

```plaintext
Input:
"free"

Output:
"eefr"

Explanation:
'e' appears twice while 'f' and 'r' appear once.
So 'e' must appear before 'f' and 'r'. Therefore, "eerf" is also a valid answer.
```

Example 2:

```plaintext
Input:
"dddbbb"

Output:
"dddbbb"

Explanation:
Both 'd' and 'b' appear three times, so "bbbddd" is also a valid answer.
Note that "dbdbdb" is incorrect, as the same characters must be together.
```

Example 3:

```plaintext
Input:
"Bbcc"

Output:
"ccBb"

Explanation:
"ccbB" is also a valid answer, but "Bbcc" is incorrect.
Note that 'B' and 'b' are treated as two different characters.
```
"""
# gives access to Counter()
# Counter is for rapid tallying
import collections

def frequency_sort(s: str) -> str:
    # Counter() returns a dictionary with items as keys and their counts as values
    counter_dict = collections.Counter(s)

    # Construct a new string with all the chars from the original, sorted in order of most frequently occuring chars first
    string_list = []
    # iterate over the dictionary using the most_common() Counter method
    # it returns a list of tuples, the first index is the letter and second is the count
    for (letter, frequency_count) in counter_dict.most_common():
        # append these letters to the string_list the amount of times they occur
        string_list.append(letter * frequency_count)
    return "".join(string_list)

print(frequency_sort("free")) #--> "eerf"  
print(frequency_sort("dddbbb")) #--> "dddbbb"
print(frequency_sort("Bbcc")) #--> "Bbcc"
print(frequency_sort("lambndaschool")) #--> "aaoollmbdsch"
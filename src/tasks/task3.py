# given two input strings "a" and "b"
# determine if the two strings can be mapped to each other such that the characters from "a" have a consistent relationship to the characters in "b"
# example: "odd" and "egg" are isomorphic
# o-->e AND d-->g
# assuming both strings are the same length?

def is_isomorph(a, b):
    # return false if string lengths are different
    if len(a) != len(b):
        return False
    # create a dictionary with keys as letters from string a and values as corresponding letters from str_b
    mapped_dict_a = {a[i]: b[i] for i in range(len(a))}

    # mapped_dict_b = {b[i]: a[i] for i in range(len(b))}
    
    # loop through string a
    for i in range(len(a)):
        # letter in string a at this index as a key to the dictionary which should return the value string b[i], if it doesn't: return False
        if mapped_dict_a[a[i]] != b[i]:
            return False

    # for i in range(len(b)):
    #     # letter in string b at this index as a key to the dictionary which should return the value string a[i], if it doesn't: return False
    #     if mapped_dict_b[b[i]] != a[i]:
    #         return False

    # loop finishes without return out, must be an isomorph
    return True

print(is_isomorph("odd", "egg")) #--> True
print(is_isomorph("foo", "bar")) #--> False
print(is_isomorph("abca", "zbxz")) #--> True
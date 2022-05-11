from collections import Counter

# Returns a new dictionary without dictionary words that are potential anagram words
def remove_non_anagrams(w_counter, dictionary):
    new_dict = []

    # For each word in the dictionary, if it is contained in the original word, add it to the new dictionary
    for word in dictionary:
        if Counter(word) & w_counter == Counter(word):
            new_dict.append(word)

    new_dict.sort()  # sort by alphabetical order
    new_dict.sort(key=len, reverse=True)  # sort by length of word

    return new_dict

# Recursive function that checks for anagrams of a word
def check_anagram(pointer, dictionary, y):
    for j in range(y, len(dictionary)):
        count = Counter(dictionary[j])
        if count == pointer:
            a = [dictionary[j]]
            return a
        if count & pointer == count:
            leftover = pointer - count
            z = check_anagram(leftover, dictionary, j)
            if z is not None:
                z.insert(0, dictionary[j])
                return z
    return None

# This function finds anagrams for a word 
def find_anagram(word, dictionary):
    if word == Counter(dictionary[0]):
        anagram = [dictionary[0]]
        return anagram
        
    for i in range(len(dictionary)):
        p = word - Counter(dictionary[i])
        anagram = check_anagram(p, dictionary, i)
        if anagram is not None:
            anagram.insert(0, dictionary[i])
            return anagram
    
    return []

if __name__ == "__main__":
    words = []
    dictionary = []
    current_line = "words"

    # Read lines from input into list of words and dictionary
    while True:
        try:
            line = input()
        except EOFError:
            break

        if line == "":
            current_line = "dictionary"
        else:
            if current_line == "words":
                words.append(line)
            elif current_line == "dictionary":
                dictionary.append(line)
   
    for word in words:
        anagram = []
        w_count = Counter(word)
        new_dict = remove_non_anagrams(w_count, dictionary)
        if len(new_dict) > 0:
            anagram = find_anagram(w_count, new_dict)
            
        anagram = " ".join(str(i) for i in anagram)
        print(word + ": " + anagram)
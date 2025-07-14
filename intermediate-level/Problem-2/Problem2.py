# Problem-2: Group Anagrams Together
def Anagrams(words):
    anagrams_dict = {}
    for word in words:
        key = ''.join(sorted(word))
        if key in anagrams_dict:
            anagrams_dict[key].append(word)
        else:
            anagrams_dict[key] = [word]
    return list(anagrams_dict.values())


input_words = ["bat", "tab", "cat", "act"]
print(Anagrams(input_words))

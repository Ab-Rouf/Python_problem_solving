# Problem-1: Longest Word in a Sentence
def longest_word(string):
  words=string.split()
  longest_word=max(words,key=len)
  return longest_word


s=input("Enter your sentences:")

print(longest_word(s))



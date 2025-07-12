def capitalization(text):
  words=text.split()
  capitalization_words=[]
  for word in words:
    capitalization_words.append(word.capitalize())
  return ' '.join(capitalization_words)
  

text=input("Enter your sentences:")
print(capitalization(text))

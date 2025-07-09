#count vowel in a sentence.

s="Data Science is awesome"
l=s.lower()
v=['a','e','i','o','u']
c=0
for i in range(len(l)):
    if l[i] in v:
        c=c+1

print(c)

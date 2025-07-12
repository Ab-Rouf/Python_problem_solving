string=input("Enter your string:")

s=string.lower()

reverse=s[: : -1]

if s==reverse:
  print("True")
else:
  print("False")
  


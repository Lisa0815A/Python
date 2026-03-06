import random
import string

def generate_password(min_len,numbers=True,special_characters=True):
  letters = string.ascii_letters
  digits = string.digits
  special = string.punctuation
  print(letters,digits,special)

  characters = letters
  if numbers:
    characters += digits
    if special_characters:
      characters += special

    pwd = ""
    meet_criteria = False
    has_number = False
    has_special = False
    while not meet_criteria or len(pwd) < min_len:
      new_char = random.choice(characters)
      pwd += new_char
      if new_char in digits:
        has_number = True
      elif new_char in special:
        has_special = True

      meet_criteria = True
      if numbers:
        meet_criteria = has_number
      if special_characters:
        meet_criteria = meet_criteria and has_special

  return pwd 
        
min_length = int(input("Enter the minimum length :"))
has_numbers = input("Include numbers? (y/n) :").lower() == "y"
has_special = input("Include special characters? (y/n):").lower() == "y"       
pwd = generate_password(min_length,has_numbers,has_special)
print("The generated password is:",pwd)

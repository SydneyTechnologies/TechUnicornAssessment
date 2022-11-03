# Run this code, 

def vowelCount(word):
    # this function takes a word 
  vowels = ["a", "e", "i", "o", "u"]  # vowel reference
  count = 0 # start counter
  for char in word:
    if char in vowels:
      count +=1 # increase count when a character matches a vowel
  return count 


print("This program calculates the number of vowels in a string")
user_input = input("please enter a string: ")
print(f"The string {user_input} has: {vowelCount(user_input)} vowels")
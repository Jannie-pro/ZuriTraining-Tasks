# Check if two words are anagrams 
# Example:
# find_anagrams("hello", "check") --> False
# find_anagrams("below", "elbow") --> True


def find_anagram(word, anagram):
    # [assignment] Add your code here

    if(sorted(word) == sorted(anagram)):
      print("The words are anagrams")
    else:
          print("The words aren't anagrams")

word = input("Enter first word: ")
anagram = input("Enter second word: ")
find_anagram(word, anagram)


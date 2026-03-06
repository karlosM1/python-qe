text: str = "racecar"



def find_character(text:str, character:str) -> str:
  for char in text:
    if char == character:
      return f"Character '{character}' found ."
  return f"Character '{character}' not found in the text."

result = find_character(text, 'o')
# print(result)


def count_vowels(text:str)-> int:
  vowels = 'aeiouAEIOU'
  count = 0
  for char in text:
    if char in vowels:
      count +=1
  return count

vowel_count = count_vowels(text)
# print(f"Number of vowels in the text: {vowel_count}")


def is_palindrome(text:str) -> bool:
  string = text.lower().replace(" ", "")
  return string == string[::-1]

palindrome_result = is_palindrome(text)
# print(f"Is the text a palindrome? {palindrome_result}")

def is_number_palindrome(num:int) -> bool:
  string = str(num)
  return string == string[::-1]

number_palindrome_result = is_number_palindrome(12321)
# print(f"Is the number a palindrome? {number_palindrome_result}")

def first_unique_char(s:str) -> str:
  char_count = []
  for char in s:
    if char in char_count:
      char_count.remove(char)
    else:
      char_count.append(char)
  return char_count[0] if char_count else None

unique_char = first_unique_char("swiss")
# print(f"The first unique character is: {unique_char}")

def is_anagram(s1:str, s2:str) -> bool:
  return sorted(s1) == sorted(s2)
anagram_result = is_anagram("listen", "silent")
  # print(f"Are the two strings anagrams? {anagram_result}")

def prc(s: str) -> str:
  splited_text = s.split()
  longest = ""
  for text in splited_text:
    if len(text) > len(longest):
      longest = text
  return longest

# print(prc("The quick brown fox jumpsss over the lazy dog"))


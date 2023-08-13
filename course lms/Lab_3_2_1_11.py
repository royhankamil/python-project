word_without_vowels = ""

# Prompt the user to enter a word
# and assign it to the user_word variable.
user_word = input("input a word: ")
user_word = user_word.upper()

for letter in user_word:
    # Complete the body of the loop.
    if letter == 'A' or letter == 'I'or letter == 'U'or letter =='E'or letter == 'O':
        continue
    word_without_vowels += letter

# Print the word assigned to word_without_vowels.
print(word_without_vowels)


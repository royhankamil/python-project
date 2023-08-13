# Prompt the user to enter a word
# and assign it to the user_word variable.
user_word = input("input the word: ")
user_word = user_word.upper()


for letter in user_word:
    # Complete the body of the for loop.
    if letter == 'A' or letter == 'I'or letter == 'U'or letter =='E'or letter == 'O':
        continue
    print(letter)
  
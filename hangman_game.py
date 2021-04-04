import random
from words import word_list

stages = [
          """
            --------
            |      |
            |      O
            |     \\|/
            |      |
            |     / \\
            -
          """,
          """
            --------
            |      |
            |      O
            |     \\|/
            |      |
            |     / 
            -
          """,
          """
            --------
            |      |
            |      O
            |     \\|/
            |      |
            |      
            -
          """,
          """
            --------
            |      |
            |      O
            |     \\|/
            |      
            |     
            -
          """,
          """
            --------
            |      |
            |      O
            |     \\|
            |      
            |     
            -
          """,
          """
            --------
            |      |
            |      O
            |      |
            |      
            | 
            -
          """,
          """
            --------
            |      |
            |      O
            |     
            |      
            |     
            -
          """,
          """
            --------
            |      |
            |      
            |     
            |      
            |     
            -
          """]

play = True

while play:
  word = random.choice(word_list).upper()
  word_completion = "_ " * len(word)
  guessed = False
  guessed_letters = []
  guessed_words = []
  tries = 7
  print("\nLet's play Hangman!")
  print(stages[tries])
  print(word_completion)
  while not guessed and tries > 0:
    guess = input("Please guess a letter or word: ").upper()
    if len(guess) == 1 and guess.isalpha():
      if guess in guessed_letters:
        print("\nYou already guess the letter {}.".format(guess))
      elif guess not in word:
        guessed_letters.append(guess)
        print("\nThe letter {} is not in the word.".format(guess))
        tries -= 1
      else:
        guessed_letters.append(guess)
        print("\nGood job, the letter {} is in the word.".format(guess))
        word_completion_as_list = list(word_completion)
        i = 0
        for character in word:
          if character == guess:
            word_completion_as_list[i * 2] = guess
          i += 1
        word_completion = "".join(word_completion_as_list)
        if "_" not in word_completion:
          guessed = True
    elif len(guess) == len(word) and guess.isalpha():
      if guess in guessed_words:
        print("\nYou already guess the word {}.".format(guess))
      elif guess != word:
        guessed_words.append(guess)
        print("\n{} is not the word.".format(guess))
        tries -= 1
      else:
        word_completion_as_list = list(word_completion)
        i = 0
        for character in word:
          word_completion_as_list[i * 2] = character
          i += 1
        word_completion = "".join(word_completion_as_list)
        guessed = True
    else:
      print("\nNot a valid guess.")
    print(stages[tries])
    print(word_completion)
  if guessed:
    print("\nYou guessed the word! You win!")
  else:
    print("\nYou ran out of tries. The word was {}. Maybe next time!".format(word))
  play_again = input("\nPlay again? (y/n): ").upper()
  if play_again == 'N':
    play = False




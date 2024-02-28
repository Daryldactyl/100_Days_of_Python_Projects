import random
import hangman_art
import hangman_words
from replit import clear

chosen_word = random.choice(hangman_words.word_list)
word_length = len(chosen_word)
already_guessed = []
end_of_game = False
lives = 6

print(hangman_art.logo)

display = []
for _ in range(word_length):
    display += "_"

while not end_of_game:
    guess = input("Guess a letter: ").lower()
    clear()
  
    if guess in already_guessed:
          print(f"You've already guessed {guess}. Try another letter")
    
    
    for position in range(word_length):
        letter = chosen_word[position]
        if letter == guess:
            display[position] = letter
          
    if guess not in chosen_word:

        if guess not in already_guessed:
            lives -= 1
            print(f"{guess} is not in this word!")
        if lives == 0:
            end_of_game = True
            print("You lose.")
            print(f"The word was {chosen_word}")
    already_guessed += guess
    printed_guess = " ".join(already_guessed)
    print(f"Guesses this round: {printed_guess}")

    print(f"{' '.join(display)}")

    if "_" not in display:
        end_of_game = True
        print("You win.")

    print(hangman_art.stages[lives])
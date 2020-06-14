import random
from words import word_list

def get_word():
    # the word in the wordlist choice will be random
    word = random.choice(word_list)
    # returning all words to be uppercase
    return word.upper()

# function for interactive gameplay
# will update variable each time a player take
def play(word):
    word_completion = "_" * len(word)
    guessed = False
    guessed_letters = [] # a list to hold the letters the user guesses
    guessed_words = [] # a list to hold the words the user guess
    tries = 6 #number of body parts to draw on the hangman
    print("Let's PLay Hangman!")
    print(display_hangman(tries))
    print(word_completion)
    print("\n")
    #The condition
    while not guessed and tries > 0:
        guess = input("Please guess a letter or word: ").upper()
        # guessing a letter means guess has a length of 1 and is a letter from the alphabet
        if len(guess) == 1 and guess.isalpha():
            if guess in guessed_letters:
                print("You already guessed the letter", guess)
            elif guess not in word:
                print(guess, "is not in the word")
                tries -= 1
                guessed_letters.append(guess)
            else:
                print("Good job", guess, "is in the word")
                guessed_letters.append(guess)
                # update variable word_completion to reveal all occurance of guess
                # convert word_completion to a list so we can index into it and store this 
                # in a new variable called word_as_list
                # need to find all the indice that guess occurs in word and we would use a lsit comprehension
                word_as_list = list(word_completion)
                # here in enumerate will call index of i, and letter at the index of each iteration
                # appending i to this list if corresponding letter equals guess
                indices = [i for i, letter in enumerate(word) if letter == guess]
                # for loop over indice to replace "_" at index with guess
                for index in indices:
                    word_as_list[index] = guess
                # update word_completion with new changes by calling "_" .join on word_as_list
                # to convert it back to a string. It's also a possibility that guess completes the word
                word_completion = "".join(word_as_list)
                # if statement to check this
                if "_" not in word_completion:
                    guessed = True
        # guessing a word is length of a word from word_list and is a letter in alphabet
        elif len(guess) == len(word) and guess.isalpha():
            if guess in guessed_words:
                print("You already guessed this word", guess)
            elif guess != word:
                print(guess, "is not the word")
                tries -= 1
                guessed_words.append(guess)
        else: 
            print("Not a valid guess")
        print(display_hangman(tries))
        print(word_completion)
        print("\n")
    if guessed: 
        print("Congrats, you guessed the word! You win!")
    else: 
        print("Sorry, you ran out of tries. The word was " + word + ". Maybe next time.")


def display_hangman(tries):
    stages = [  # final state: head, torso, both arms, and both legs
                """
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |     / \\
                   -
                """,
                # head, torso, both arms, and one leg
                """
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |     / 
                   -
                """,
                # head, torso, and both arms
                """
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |      
                   -
                """,
                # head, torso, and one arm
                """
                   --------
                   |      |
                   |      O
                   |     \\|
                   |      |
                   |     
                   -
                """,
                # head and torso
                """
                   --------
                   |      |
                   |      O
                   |      |
                   |      |
                   |     
                   -
                """,
                # head
                """
                   --------
                   |      |
                   |      O
                   |    
                   |      
                   |     
                   -
                """,
                # initial empty state
                """
                   --------
                   |      |
                   |      
                   |    
                   |      
                   |     
                   -
                """
    ]
    return stages[tries]

# Main function to put everything together
def main():
    word = get_word()
    play(word)
# options for user to play again
    while input("Play Again? (Y/N) ").upper() == "Y":
        word = get_word()
        play(word)

if __name__ == "__main__":
    main()
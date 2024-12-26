import random

words = ["python", "programming", "computer", "code", "algorithm", "variable", "function", "loop"]

word = random.choice(words)

guessed_letters = set()
incorrect_guesses = 0

hidden_word = ["_" for _ in word]
print(" ".join(hidden_word))

while "_" in hidden_word and incorrect_guesses < 6:
    guess = input("Guess a letter: ").lower()
    if guess in guessed_letters:
        print("You already guessed that letter.")
    elif guess in word:
        print("Correct!")
        for i in range(len(word)):
            if word[i] == guess:
                hidden_word[i] = guess
        print(" ".join(hidden_word))
    else:
        print("Incorrect.")
        incorrect_guesses += 1
        print(f"You have {6 - incorrect_guesses} guesses left.")
    guessed_letters.add(guess)

if "_" not in hidden_word:
    print("Congratulations, you guessed the word!")
else:
    print(f"Sorry, the word was {word}. Better luck next time!")

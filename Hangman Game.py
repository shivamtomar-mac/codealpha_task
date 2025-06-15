import random

words = ['apple', 'banana', 'cherry', 'mango', 'peach']

def hangman():
    word = random.choice(words)
    guessed = ['_'] * len(word)
    attempts = 6
    guessed_letters = set()
    while attempts > 0 and '_' in guessed:
        print('Word:', ' '.join(guessed))
        print('Attempts left:', attempts)
        letter = input('Guess a letter: ').lower()
        if letter in guessed_letters:
            print('You already guessed it.')
            continue
        guessed_letters.add(letter)
        if letter in word:
            for i, char in enumerate(word):
                if char == letter:
                    guessed[i] = letter
        else:
            attempts -= 1
        if '_' not in guessed:
            print('Congratulations! You guessed it!', word)
            return
    print('Sorry, you lose. The word was', word)

if __name__ == '__main__':
    hangman()

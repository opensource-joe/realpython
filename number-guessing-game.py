# Number guessing game - human input, computer generated number

import random
print('Guess a number between 1 and 10')
number = random.randint(1, 10)
guess = int(input())
print(f'Number: {number}, Guess: {guess}')
if guess == number:
    print(f'Correct - the number was {number}')
else:
    print(f'Sorry, the number was {number}, not {guess}')
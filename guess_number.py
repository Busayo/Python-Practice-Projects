import random


def game(stop):
  start = 0
  number_guessed = 0
  guess = random.randint(start, stop)
  while number_guessed != guess:
    number_guessed = int(input(f'Guess a number between 1 and {stop}: '))
    if number_guessed < guess:
      print(f'Number was too low, please try a higher value')
    elif number_guessed > guess:
      print(f'Number was too high, please try a higher value')

  print(f"Guessed number was correct, it is {guess}!!")


game(20)

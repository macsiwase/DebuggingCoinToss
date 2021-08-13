import random
import logging
logging.basicConfig(level=logging.DEBUG, format=' %(asctime)s -  %(levelname)s -  %(message)s')


guess = ''

while guess not in ('heads', 'tails'):
    print('Guess the coin toss! Enter heads or tails:')
    guess = input()

    if guess == "heads" or guess == "tails":
        continue
    else:
        logging.debug("Our guess does not give an error message if we enter any guesses other than heads or tails. Even if there is a capital letter included.")

toss = random.randint(0, 1) # 0 is tails, 1 is heads
logging.debug("The correct answer is " + str(toss))

if toss == guess:
    print('You got it!')
else:
    print('Nope! Guess again!')
    guesss = input()
    if toss == guess:
        print('You got it!')
    else:
        print('Nope. You are really bad at this game.')
        logging.debug("Even if you enter 0 or 1, it is incorrect because our guess is "+ str(type(guess)) + "and the correct answer is " + str(type(toss)))

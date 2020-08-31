# guess the number game
# By: Kyuudere

import random

number_lists = list(range(0, 1001))      # - creates number list
random_number_list = []     # - area to store generated number

# picks random number from number_list and "STARTS THE GAME"
def pick_random():
    print("Random Number Generated")
    random_number = random.choice(number_lists)
    random_number_list.append(random_number)
    guess_number()


# guess the random number
def guess_number():
    correct_answer_status = 'false'
    the_number = int(random_number_list.pop())
    while correct_answer_status == 'false':
        answer = input("Guess the random number in between 0 and 1000: ")
        try:
            if int(answer) == the_number:
                print("Correct")
                correct_answer_status = 'true'
                play_again()
            elif int(answer) < int(the_number):
                print("HIGHER! FOOL! HIGHER!")
            elif int(answer) > int(the_number):
                print("LOWER! FOOL! LOWER!")
        except ValueError:
                print("THAT'S NOT A NUMBER!!!")


# asks to play again or quit
def play_again():
    random_number_list.clear()
    play_again_answer = input("Would you like to play again y/any other key to 'quit': ")
    if play_again_answer == 'y':
        pick_random()
    elif play_again_answer != 'y':
        return


pick_random()

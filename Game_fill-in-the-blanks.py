
ATTEMPT_LIMIT = 3

# Reference to make the text displayed to user change

class bcolors:
    FAIL = '\033[91m'
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'

def play_game():
    # Function Purpose: to allow the user to make a difficulty choice with regards to which fill in the blanks game they wish to play.
    # whlist playing the game the user will be prompted to guess the answer to each unique blank space. Should the user fail to answer incorrectly
    # 3 times they will fail the quiz and the game will exit.
    #
    # Inputs: Only user input to prompts
    # Outputs: Only Print statements prompting the users and the execution of the following functions: level_check(level_choice) and test_user_answers(quiz_str_split2, answer)

	print "\n"
	print bcolors.HEADER +"WELCOME TO THE GAME OF FILL IN THE STRING."
	print bcolors.OKGREEN + "\n"
        current_level= level_check()

	print bcolors.OKBLUE + "To play you will be prompted to fill the spaces of the below sentence"
	print bcolors.OKBLUE + 'You will get 3 guesses per problem'
        quiz_str_split = levels_quiz_string[current_level]
        quiz_str_split2 = quiz_str_split.split()
        answer = levels_ans[current_level]
	print bcolors.OKGREEN + "The current paragraph reads as such:"
        test_user_answers(quiz_str_split2, answer)

def level_check():
    #  Purpose: to check that the users input for difficulty level is validates
    # input: level choice
    # output: the list positition of the chosen difficulty level.
    current_level = 0
    level_choice = raw_input("Which level do you want to play? Please enter easy, medium or hard then press Enter) \n")

    while level_choice not in difficulty:
		print bcolors.FAIL + ""
		level_choice = raw_input('Your input was invalid.your only choices are easy, medium or hard. \n')
    current_level = difficulty.index(level_choice)
    print bcolors.OKGREEN + '\n You have selected '+ level_choice +' mode.'
    return current_level


# STEP 2


def test_user_answers(quiz_str_split2, answer):
    # Purpose: Scans through the Quiz string for blanks and validates whether they are answered correctly
    # When the answers are correct the blanks are filled in.
    # Input: The selected quiz string split into a list of words and the answer list to the quiz.

    blank_num = 1
    for word in quiz_str_split2:
        if is_blank(word) == True and blank_num <= len(answer):
            print_question(quiz_str_split2)
            user_input = raw_input('\n\nWhat should go in blank space ___'+str(blank_num)+'___ ?\n')
            #user_input = user_input.capitalize()
            response = is_correct(user_input, blank_num, answer)
            full_blank = '___'+str(blank_num)+'___'
            quiz_str_split2 = fill_blank(quiz_str_split2,full_blank, response)
            #quiz_str_split2 = quiz_str_split_new
            blank_num += 1
    print bcolors.HEADER + 'Congratulations!!! You''ve successfully completed the quiz.'
    print bcolors.OKBLUE + '\n Here is the completed sentence'
    print print_question(quiz_str_split2)


def is_blank(word):
    # Purpose: Identifies if the current word from quiz_str_split is a blank to be filled.
    # Input: the the current word from quiz_str_split
    # Output: A boolean True or False value
    if word.find('___') != -1:
        return True
    return False


def print_question(quiz_str_split2):
    # Purpse: Prints out the question for the level as it currently exists. Will print with blanks filled as quiz progresses
    # Input: the split list of quiz words + answers currently completed
    # Output: concatenates all of the individual words from the split word list to a single string.
    print '\n'+' '.join(quiz_str_split2)



def is_correct(user_input, blank_num, answer):
    # Purpose: Determines if the user's answer was correct for the given blank.  If incorrect prompts user to try again. Runs until the correct answer is entered.
    # Input: the users answer to the blank number that the user is currently being asked to guess (ie blank_num) and the answer list
    # Output: True if user is correct.
	attempt = 1

	while attempt < ATTEMPT_LIMIT:
            if user_input == answer[blank_num-1]:
                print bcolors.OKBLUE + 'Correct!'
                print bcolors.OKGREEN + ""
                return user_input

            else:
                print bcolors.WARNING + "Incorrect. Try again!\n You have made " +str(attempt)+" of " + str(ATTEMPT_LIMIT) + " attempts\n"
                user_input = raw_input('What should go in blank ___'+str(blank_num)+'___?\n')
                #user_input = user_input.capitalize()
                if user_input == answer[blank_num-1]:
                    print bcolors.OKBLUE + 'Correct!'
                    print bcolors.OKGREEN + ""
                    print answer[blank_num-1]
                    return user_input
                attempt = attempt + 1

        print bcolors.FAIL + "you've made 3 out of 3 attempts. Goodbye\n"
        exit()


def fill_blank(quiz_str_split2,full_blank, user_input):
    # PURPOSE: Will replace the blank value with the user input if it is the correct value
    # INPUT: the splt quiz word list, the blank value that must be replaced by the user input, the user input/answer
    # OUTPUT: The full quiz with all of the blank spaces of the same number filled with the answer provided by the user.
    #quiz_str_split2.replace(full_blank, user_input)
    quiz_str_split2 = [word.replace(full_blank,user_input) for word in quiz_str_split2]
    return quiz_str_split2


# This section list all of the starting lists and their values called by the Game

difficulty = ['easy', 'medium', 'hard']

levels_quiz_string = [
# easy Quiz
("""'Hello ___1___!'  In ___2___ this is particularly easy; all you have to do
is type in: ___3___ "Hello ___1___ !"
Of course, that isn't a very useful thing to do. However, it is an
example of how to output to the user using the ___3___ command, and
produces a program which does something, so it is useful in that capacity.

It may seem a bit odd to do something in a Turing complete language that
can be done even more easily with an ___4___ file in a browser, but it's
a step in learning ___2___ syntax, and that's really its purpose.'"""),
# Medium Quiz
("""'A ___1___ is created with the def keyword.  You specify the inputs a
  ___1___ takes by adding ___2___ separated by commas between the parentheses.
___1___ by default returns ___3___ if you don't specify the value to retrun.
___2___ can be standard data types such as string, integer, dictionary, tuple,
and ___4___ or can be more complicated such as objects and lambda functions."""),

#Hard Quiz
(""""'When you create a ___1___, certain ___2___s are automatically
generated for you if you don't make them manually. These contain multiple
underscores before and after the word defining them.  When you write
a ___1___, you almost always include at least the ___3___ ___2___, defining
variables for when ___4___s of the ___1___ get made.  Additionally, you generally
want to create a ___5___ ___2___, which will allow a string representation
of the method to be viewed by other developers.
You can also create binary operators, like ___6___ and ___7___, which
allow + and - to be used by ___4___s of the ___1___.  Similarly, ___8___,
___9___, and ___10___ allow ___4___s of the ___1___ to be compared
(with <, >, and ==).'""")]

levels_ans = [["world", "programming", "print", "HTML"],
            ["Procedure", "parameter", "None", "List"],
            ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10"]]


play_game()

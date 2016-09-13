# Write code for the function play_game, which takes in as inputs parts_of_speech
# (a list of acceptable replacement words) and ml_string (a string that
# can contain replacement words that are found in parts_of_speech). Your play_game
# function should return the joined list replaced, which will have the same structure
# as ml_string, only that replacement words are swapped out with "corgi", since this
# program cannot replace those words with user input.

parts_of_speech  = ["___1___", "___2___", "___3___", "___4___"]
parts_of_speech_hard  = ["___1___", "___2___", "___3___", "___4___", "___5___", "___6___", "___7___", "___8___", "___9___", "___10___"]

test_string = """A ___1___ is created with the def keyword. You specify the inputs a ___1___ takes by
adding ___2___ separated by commas between the parentheses. ___1___s by default return ___3___ if you
don't specify the value to return. ___2___ can be standard data types such as string, number, dictionary,
tuple, and ___4___ or can be more complicated such as objects and lambda functions."""

answers = ["Function", "Parameters", "None", "List"]
answers_easy = ["World", "Programming", "Print", "HTML"]
answers_medium = ["Procedure", "parameter", "None", "List"]
answers_hard = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10"]


easy_string = """You've chosen easy!

You will get 3 guesses per problem

The current paragraph reads as such:

A common first thing to do in a language is display
'Hello ___1___!'  In ___2___ this is particularly easy; all you have to do
is type in: ___3___ "Hello ___1___!"
Of course, that isn't a very useful thing to do. However, it is an
example of how to output to the user using the ___3___ command, and
produces a program which does something, so it is useful in that capacity.

It may seem a bit odd to do something in a Turing complete language that
can be done even more easily with an ___4___ file in a browser, but it's
a step in learning ___2___ syntax, and that's really its purpose."""

medium_string = """You've chosen medium!

You will get 3 guesses per problem

The current paragraph reads as such:

A ___1___ is created with the def keyword.  You specify the inputs a
___1___ takes by adding ___2___ separated by commas between the parentheses.
___1___ by default returns ___3___ if you don't specify the value to retrun.
___2___ can be standard data types such as string, integer, dictionary, tuple,
and ___4___ or can be more complicated such as objects and lambda functions."""

hard_string = """You've chosen hard!

You will get 3 guesses per problem

The current paragraph reads as such:
When you create a ___1___, certain ___2___s are automatically
generated for you if you don't make them manually. These contain multiple
underscores before and after the word defining them.  When you write
a ___1___, you almost always include at least the ___3___ ___2___, defining
variables for when ___4___s of the ___1___ get made.  Additionally, you generally
want to create a ___5___ ___2___, which will allow a string representation
of the method to be viewed by other developers.

You can also create binary operators, like ___6___ and ___7___, which
allow + and - to be used by ___4___s of the ___1___.  Similarly, ___8___,
___9___, and ___10___ allow ___4___s of the ___1___ to be compared
(with <, >, and ==)."""



class bcolors:
    FAIL = '\033[91m'
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'


def word_in_pos(word, parts_of_speech):
    for pos in parts_of_speech:
        if pos in word:
            return pos
    return None

def answer_match(user_input, answers):
    for position in answers:
        if position in user_input:
            return position
    return False



#ml_string = "PLACE is really an ADJECTIVE"
#parts_of_speech = ["PLACE","ADJECTIVE"]

def play_game(ml_string, parts_of_speech, answers):
    replaced = []
    ml_string = ml_string.split()
    for word in ml_string:
        replacement = word_in_pos(word, parts_of_speech)
        if replacement != None:
            user_input = raw_input("Type in missing word for: " + replacement + " ")
            user_input = user_input.capitalize()
            result = answer_match(user_input, answers)

            counter = 1

            if result != False:
                word = word.replace(replacement, result)

                replaced.append(word)

            while result == False and counter < 3:
                print 'Wrong Answer - Try again'
                print ""
                counter = counter + 1

                user_input = raw_input("Type in missing word for: " + replacement + " ")
                user_input = user_input.capitalize()
                result = answer_match(user_input, answers)
            if result == False and counter == 3:
                print bcolors.FAIL + 'You answered incorrectly 3 times - Goodbye'
                print ""
                exit()
        else:
            replaced.append(word)

        replaced_string = " ".join(replaced)
    return replaced_string

print ""
print ""
print bcolors.HEADER + "WELCOME TO THE GAME OF FILL IN THE STRING"
print ""
level = raw_input("Which level do you want to play? (easy, medium or hard)")
print level
if level == "easy":
    print bcolors.OKBLUE + "To play you will be prompted to fill the spaces of the below sentence"
    print ""
    print bcolors.OKGREEN + easy_string
    print play_game(easy_string, parts_of_speech, answers_easy)
elif level == "medium":
    print bcolors.OKBLUE + "To play you will be prompted to fill the spaces of the below sentence"
    print ""
    print bcolors.OKGREEN + medium_string
    print play_game(medium_string, parts_of_speech, answers_medium)
elif level == "hard":
    print bcolors.OKBLUE + "To play you will be prompted to fill the spaces of the below sentence"
    print ""
    print bcolors.OKGREEN + hard_string
    print play_game(hard_string, parts_of_speech_hard, answers_hard)
else:
     print "That is not an option - good bye"
     print ""


#------------------------ START OF REVISED CODE	-----------------------------

print fill_in_blanks_game()

def fill_in_blanks_game():	
	print "\n"
	print bcolors.HEADER + "WELCOME TO THE GAME OF FILL IN THE STRING. \n"
	level_choice = raw_input("Which level do you want to play? Please enter easy, medium or hard then press Enter) \n")
	current_level = level_check(level_choice)  					#current_level will hold the list position of choice 
	quiz_str_split = levels_quiz_string[current_level].split()  #use this to split the Levels_quiz string for difficulty level selected into a word list called Level[]
	answer = levels_ans[current_level]  						#retrieves the system answers for the difficulty index position selected. 
	test_user_answers(quiz_str_split, answer)

	 

# STEP 1
# Returns the level index of the value entered by the user ie Easy =0, Medium=1, Hard =2  
# if the user enters correct values. 
# If incorrect values are entered it will run until correct input is given. 

def level_check(level_choice):
    while level_choice not in difficulty:
        level_choice = raw_input('Your input was invalid.'
                               'your only choices are easy, medium or hard. \n')
    current_level = difficulty.index(level_choice)
    print '\n You have selected '+ level_choice +' mode.'
    return current_level

# STEP 2
# Scans through the Quiz string for blanks and validates whether they are answered correctly
# When the answers are correct the blanks are filled in. 
	
def test_user_answers(quiz_str_split, answer):
    index = 0
    blank_num = 1
    for word in quiz_str_split:
        if is_blank(word):
            print_question(quiz_str_split)
            user_input = raw_input('\nWhat should go in blank '+str(blank_num)+'?\n')
            if is_correct(user_input, blank_num, answer):
                quiz_str_split[index] = answer[blank_num-1]
                blank_num += 1
        index += 1	

# STEP 2a
# Identifies if the current word from quiz_str_split is a blank to be filled. 

def is_blank(word):
    if word.find('_____') != -1:
        return True
    return False

# STEP 2b
# Prints out the question for the level as it currently exists. 
# Will print with blanks filled as quiz progresses
def print_question(quiz_str_split):
    print '\n'+' '.join(quiz_str_split)		
	
	
# Step 2c
# Determines if the user's answer was correct for the given blank.
# If incorrect prompts user to try again. Runs until the correct answer is entered.
# Returns True if user is correct.
def is_correct(user_input, blank_num, answer):
    while user_input != answer[blank_num-1]:
        print "Incorrect. Try again!\n"
        user_input = raw_input('What should go in blank '+str(blank_num)+'?\n')
    if user_input == answer[blank_num-1]:
        print 'Correct!\n'
    return True
	

# This section list all of the starting lists and their values called by the Game		

difficulty = ['easy', 'medium', 'hard']

levels_quiz_string = [
			# Easy Quiz
			("""'Hello ___1___!'  In ___2___ this is particularly easy; all you have to do
			is type in: ___3___ "Hello ___1___!"
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
levels_ans = [["World", "Programming", "Print", "HTML"],
            ["Procedure", "parameter", "None", "List"],
            ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10"]]
			

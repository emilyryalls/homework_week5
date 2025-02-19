from rock_paper_scissors import user_answer, computer_answer, comparison

user = user_answer()
# the functions are assigned to a variable
comp = computer_answer()
# the functions are assigned to a variable
comparison(user, comp)
# # the functions are assigned to a variable
# the parameters are passed in to the function comparison when it is called

repeat = input("Do you want to play again?:Y/N").upper()
# user input is taken to see the if the game has to be run again
if repeat == "N":
    print("Game ends, Thanks for Playing")
else:
    user = user_answer()
    comp = computer_answer()
    comparison(user, comp)
#  kept the game on repeat if user want to play again
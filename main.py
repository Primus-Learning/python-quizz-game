from models.answer import Answer
from models.question import Question
from dictionary import dictionary

# Variable scopes
# Functions
# Loops (for, while)
# Conditions (if, else)
# Exceptions handling
# Exceptions making
# Classes 
# imports (modules)
# Virtual environments
# PIP install packages
# PIP requirements.txt

questions = []
continuePlaying = True

for item in dictionary:
    answers = []
    for answer in item["answers"]:
        answers.append(Answer(answer["label"], answer["correct"]))
    questions.append(Question(item["label"], answers))

while continuePlaying:
    score = 0

    for question in questions:
        question.printQuestion()
        stopAsking = False
        while stopAsking is False:
            try:
                userResponse = int(input("Enter the correct answer : "))
                if question.check(userResponse):
                    print("Correct answer !")
                    score += 1
                else:
                    print("Sorry this is not the correct answer")
                stopAsking = True
            except IndexError:
                print(f"Sorry but {userResponse} is not a correct input.")
                print(f"Select a number between 1 and {len(question.answers)}")
        print("-----------------------------------")
    
    # Printing the user's score
    print("---")
    print(f"--- You have finished this turn with a score of {score}/{len(questions)}")
    print("---")
    
    userEnteredACorrectAnswer = False
    while userEnteredACorrectAnswer is False:
        userWantsToPlayAgain = input("Do you want to play again ([Y]es/[N]o) : ")
        if userWantsToPlayAgain == "Y" or userWantsToPlayAgain == "y":
            continuePlaying = True
            userEnteredACorrectAnswer = True
        elif userWantsToPlayAgain == "N" or userWantsToPlayAgain == "n":
            continuePlaying = False
            userEnteredACorrectAnswer = True
        else:
            print("Unknown answer. The only possible responses are `Y` or `N`")

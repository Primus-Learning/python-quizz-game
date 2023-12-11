from camelcase import CamelCase

c = CamelCase()

class Question:
    label = ""
    answers = []

    def __init__(self, label, answers) -> None:
        self.label = c.hump(label)
        numberOfCorrectAnswers = 0

        if len(answers) < 3:
            raise Exception("You should provide more than 2 answers")
        
        for answer in answers:
            if answer.isCorrectAnswer:
                numberOfCorrectAnswers += 1
        if numberOfCorrectAnswers > 1:
            raise Exception("You cannot provide more than one correct answer")
        self.answers = answers

    def check(self, userInput):
        if self.answers[userInput - 1].isCorrectAnswer:
            return True
        return False

    def printQuestion(self):
        print(f"==[ {self.label} ]==")
        index = 1
        for answer in self.answers:
            print(f"    {index} - {answer.label}")
            index += 1

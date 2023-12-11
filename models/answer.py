from camelcase import CamelCase

c = CamelCase()

class Answer:
    label = ""
    isCorrectAnswer = False

    def __init__(self, label, isCorrect) -> None:
        self.label = c.hump(label)
        self.isCorrectAnswer = isCorrect

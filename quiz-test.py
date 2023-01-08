# Question
class Question:
    def __init__(self, text, choices, answer):
        self.text = text
        self.choices = choices
        self.answer = answer

    def checkAnswer(self, answer):
        return self.answer == answer


# Quiz
class Quiz:
    def __init__(self, questions):
        self.questions = questions
        self.score = 0
        self.questionIndex = 0

    def getQuestion(self):
        return quiz.questions[self.questionIndex]

    def displayQuestion(self):
        question = self.getQuestion()
        print(f"Soru {self.questionIndex + 1}: {question.text}")

        for q in question.choices:
            print("-", q)

        answer = input("cevap : ")
        self.guess(answer)
        self.loaadQuestion()

    def guess(self, answer):
        question = self.getQuestion()

        if question.checkAnswer(answer):
            self.score += 1
        self.questionIndex += 1

    def loaadQuestion(self):
        if len(self.questions) == self.questionIndex:
            self.showScore()
        else:
            self.displayProgress()
            self.displayQuestion()

    def showScore(self):
        print("score :", self.score)

    def displayProgress(self):
        totalQuestion = len(self.questions)
        questionNumber = self.questionIndex + 1

        if questionNumber > totalQuestion:
            print("quiz bitti")
        else:
            print(f"Question {questionNumber} of {totalQuestion}".center(100, "*"))


q1 = Question("en iyi proglamma dili hangisidir ?", ["C#", "python", "javascript", "java"], "python")
q2 = Question("en popüler proglamma dili hangisidir ?", ["python", "javascript", "C#", "java"], "python")
q3 = Question("en çok kazandıran proglamma dili hangisidir ?", ["C#", "javascript", "java", "python"], "python")
q4 = Question("en çok sevilen proglamma dili hangisidir ?", ["C#", "javascript", "java", "python"], "python")
q5 = Question("en kolay proglamma dili hangisidir ?", ["C#", "javascript", "java", "python"], "python")

questions = [q1, q2, q3, q4, q5]

quiz = Quiz(questions)

quiz.loaadQuestion()

# print(q1.checkAnswer("python"))
# print(q1.checkAnswer("C#"))

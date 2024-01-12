from data import question_data
from question_model import Question
from quiz_brain import QuizBrain

question_bank = []
for questions in question_data:
    questions_text = questions['question']
    questions_answer = questions['correct_answer']
    new_question = Question(questions_text, questions_answer)
    question_bank.append(new_question)

quiz = QuizBrain(question_bank)

while quiz.still_has_question():
    quiz.next_question()

print("You've completed the quiz")
print(f'Your final score was: {quiz.score}/{quiz.question_number}')



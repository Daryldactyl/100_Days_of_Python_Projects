from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

question_bank = []
for question in question_data:
    questions_text = question["text"]
    question_answer = question["answer"]
    new_question = Question(questions_text, question_answer)
    question_bank.append(new_question)

quiz = QuizBrain(question_bank)
while quiz.still_has_questions():
    quiz.next_question()

print("You've compelted the Quiz!")
print(f"Your final score was {quiz.score}/{len(question_bank)}")

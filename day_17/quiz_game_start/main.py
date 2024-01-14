from day_17.quiz_game_start.data import question_data
from day_17.quiz_game_start.question_model import Question
from day_17.quiz_game_start.quiz_brain import QuizBrain

question_bank = []

for question in question_data:
    new_question = Question(question['text'], question['answer'])
    question_bank.append(new_question)

new_quiz = QuizBrain(question_bank)

while new_quiz.still_has_questions():
    new_quiz.next_question()

print("You've completed the quiz!")
print(f"Your final score was {new_quiz.score}/{len(question_bank)}")


from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

question_list = []

for one_question in question_data:
    question_list.append(Question(one_question["question"], one_question["correct_answer"]))

quiz = QuizBrain(question_list)

while quiz.has_question():
    quiz.next_question()
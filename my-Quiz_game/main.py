from data import question_data as data
from question_model import Question
from quiz_brain import QuizBrain
import signal
import sys

def sigint_handler(signal, frame):
    print ('KeyboardInterrupt is caught')
    print("Bye!!")
    sys.exit(0)
signal.signal(signal.SIGINT, sigint_handler)

question_bank = []
# Make a list full of Question objects

for question in data:
    answer = question['answer']
    text = question['text']

    new_object = Question(text, answer)
    question_bank.append(new_object)


quiz = QuizBrain(data)

while quiz.still_has_questions():
    quiz.next_question()
    quiz.check_answer(quiz.choice, quiz.q_answer)

print("You've completed the quiz!")
print(f"Your final score was: {quiz.score}/{(len(question_bank))}")

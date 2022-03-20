class QuizBrain:

    def __init__(self, question_list):
        self.question_list = question_list
        self.question_num = 0
        self.score = 0

    def next_question(self):
        q_text = self.question_list[self.question_num]['text']
        self.q_answer = self.question_list[self.question_num]['answer']
        self.choice = input(f"Q.{self.question_num + 1}: {q_text} (true/false): ").title()
        self.question_num += 1

    def still_has_questions(self):
        list_lenght = len(self.question_list)
        if list_lenght == self.question_num:
            return False
        else:
            return True
    
    def check_answer(self, user_answer, correct_answer):
        if user_answer == correct_answer:
            print(f"You got it right!")
            self.score += 1
        else:
            print("That's wrong.")
        print(f"The correct answer was {correct_answer}")
        print(f"Your current score is {self.score}/{self.question_num}.")
        print('\n')

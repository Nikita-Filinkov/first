class Question:

    def __init__(self, question, diff, answer):
        self.question = question
        self.diff = diff
        self.answer = answer

        self.question_text = False
        self.user_answer = None
        self.points = int(self.diff) * 10

    def get_points(self):
        return self.points

    def is_correct(self):
        return self.user_answer == self.answer

    def build_question(self):
        question = f"Вопрос: {self.question}\nСложность {self.diff}/5"
        return question

    def build_feedback(self):
        if self.user_answer == self.answer:
            feedback_1 = f"Ответ верный, получено - {self.points} баллов"
            return feedback_1
        feedback_2 = f"Ответ неверный, верный ответ - {self.answer}"
        return feedback_2

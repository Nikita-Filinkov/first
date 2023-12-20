class Player:
    def __init__(self, name):
        self.name = name
        self.user_answer = None
        self.use_answer = []

    def count_user_answer(self):
        return int(len(self.use_answer))

    def exame_return_answer(self):
        return self.user_answer in self.use_answer

    def add_user_answer(self):
        self.use_answer.append(self.user_answer)
        return self.use_answer

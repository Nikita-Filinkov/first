class BasicWord:
    def __init__(self, word, subwords):
        self.word = word
        self.subwords = subwords

    def is_correct(self, user_answer):
        return user_answer in self.subwords

    def count_subwords(self):
        count_ = int(len(self.subwords))
        return count_

    def build_question(self):
        question = f"Составте {len(self.subwords)} слов из слова {self.word}"
        return question

    def min_len_subwords(self):
        b = []
        for i in self.subwords:
            b.append(len(i))
        return min(b)



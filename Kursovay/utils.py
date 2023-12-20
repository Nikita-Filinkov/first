import random
from Kursovay.Date import words
from Kursovay.BasicWord import BasicWord


def create_examples_class():
    examples = []
    for word in words:
        new_exampl = BasicWord(word.get('word'), word.get('subwords'))
        examples.append(new_exampl)
        random.shuffle(examples)
    return examples[0]




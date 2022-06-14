import string
from element import Element
from invalidassignmentexception import InvalidAssignmentException


class Hangman:

    def __init__(self):
        self.word = []
        self.lifes = 5

    def show(self):
        display = f'Lifes: {self.lifes} - Word: '
        for object in self.word:
            display += f'{object.display} '
        return display

    def set_word(self, word: string):
        for letter in word.lower():
            self.word.append(Element(value=letter))

    def assign(self, letter: string):
        assignable = False
        for object in self.word:
            if object.value == letter.lower():
                object.display = letter.lower()
                assignable = True
        if not assignable:
            self.lifes -= 1
            raise InvalidAssignmentException('No Válido')

    def winner(self):
        result = True
        for object in self.word:
            if object.display == '_':
                result = False
        return result

    def play(self):
        while self.lifes > 0 and not self.winner():
            print(self.show())
            letter = input('Ingrese letra: ')
            try:
                self.assign(letter)
            except InvalidAssignmentException as err:
                print(err.args[0])
        if self.lifes == 0:
            return 'Perdiste'
        print(self.show())
        return 'Ganaste'

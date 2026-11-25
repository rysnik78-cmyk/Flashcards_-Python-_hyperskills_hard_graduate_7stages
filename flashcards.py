# Write your code here

class FlashcardsBase:
    def __init__(self):
        self.flashcards = {}

    def add_flashcard(self, card, definition):
        self.flashcards[card] = definition

    def return_flashcard_data(self, card):
        return card, self.flashcards[card]

def main():
    flashcards_base = FlashcardsBase()

    # print('Card:')
    card = input()
    # print(card)
    # print('Definition:')
    definition = input()
    # print(definition)

    flashcards_base.add_flashcard(card, definition)

    actual_card = flashcards_base.return_flashcard_data(card)
    user_answer = input()
    if user_answer == actual_card[1]:
        print('Your answer is right!')
    else:
        print('Your answer is wrong...')


if __name__ == "__main__":
    main()

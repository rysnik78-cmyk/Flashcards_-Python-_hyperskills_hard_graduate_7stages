# Write your code here

class FlashcardsBase:
    def __init__(self):
        self.flashcards = {}

    def add_flashcard(self, card, definition):
        self.flashcards[card] = definition


def main():
    flashcards_base = FlashcardsBase()

    print('Card:')
    card = input()
    print(card)
    print('Definition:')
    definition = input()
    print(definition)

    flashcards_base.add_flashcard(card, definition)


if __name__ == "__main__":
    main()

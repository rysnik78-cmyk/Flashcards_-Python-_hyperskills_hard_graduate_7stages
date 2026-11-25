# Write your code here

class FlashcardsBase:
    def __init__(self):
        self.flashcards = {}
        self.card_limit = 10

    def add_flashcard(self, card, definition):
        self.flashcards[card] = definition

    def return_flashcard_data(self, card):
        return card, self.flashcards[card]

    def check_card(self, card):
        return card in self.flashcards

    def check_definition(self, definition):
        return definition in self.flashcards.values()

    def return_flashcard_card_from_definition(self, definition):
        for key,value in self.flashcards.items():
            if value == definition:
                return key
        return None

def main():
    flashcards_base = FlashcardsBase()

    number_of_cards = input('Input the number of cards:\n')
    flashcards_base.card_limit = int(number_of_cards)
    for i in range(flashcards_base.card_limit):
        print(f'The term for card #{i+1}:')
        while True:
            card = input()
            if flashcards_base.check_card(card):
                print(f'The term "{card}" already exists. Try again:')
                continue
            break

        print(f'The definition for card #{i + 1}:')
        while True:
            definition = input()
            if flashcards_base.check_definition(definition):
                print(f'The definition "{definition}" already exists. Try again:')
                continue
            break
        flashcards_base.add_flashcard(card, definition)

    for card in flashcards_base.flashcards.items():


        print(f'Print the definition of "{card[0]}":')
        user_answer = input()
        if user_answer == card[1]:
            print('Correct!')
        else:
            if flashcards_base.check_definition(user_answer):
                print(f'Wrong. The right answer is "{card[1]}"', end='')
                print(f' but your definition is correct for {flashcards_base.return_flashcard_card_from_definition(user_answer)}.')
            else:
                print(f'Wrong. The right answer is "{card[1]}"')

if __name__ == "__main__":
    main()

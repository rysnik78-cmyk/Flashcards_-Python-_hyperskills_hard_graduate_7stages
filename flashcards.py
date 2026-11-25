# Write your code here

class FlashcardsBase:
    def __init__(self):
        self.flashcards = {}
        self.card_limit = 10

    def add_flashcard(self, card, definition):
        self.flashcards[card] = definition

    def return_flashcard_data(self, card):
        return card, self.flashcards[card]

def main():
    flashcards_base = FlashcardsBase()

    number_of_cards = input('Input the number of cards:\n')
    flashcards_base.card_limit = int(number_of_cards)
    for i in range(flashcards_base.card_limit):
        print(f'The term for card #{i+1}:')
        card = input()
        print(f'The definition for card #{i + 1}:')
        definition = input()
        flashcards_base.add_flashcard(card, definition)

    for card in flashcards_base.flashcards.items():


        print(f'Print the definition of "{card[0]}":')
        user_answer = input()
        if user_answer == card[1]:
            print('Correct!')
        else:
            print(f'Wrong. The right answer is "{card[1]}".')



if __name__ == "__main__":
    main()

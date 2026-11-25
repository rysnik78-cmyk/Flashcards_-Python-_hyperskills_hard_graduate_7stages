# Write your code here
import random
import json
import os


class FlashcardsBase:
    def __init__(self):
        self.flashcards = {}
        self.card_limit = 10

    def add_flashcard(self, card, definition):
        self.flashcards[card] = definition
        print(f'The pair ("{card}":"{definition}") has been added.')

    def remove_flashcard(self, card):
        del self.flashcards[card]

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

    def return_random_flashcard_data(self):
        print('losowanie3')
        random_key = random.choice(list(self.flashcards.keys()))
        print('losowanie4')
        print(random_key)
        return random_key, self.flashcards[random_key]

    def export_to_json(self, file_name):
        with open(file_name, 'w') as file:
            json.dump(self.flashcards, file)
        print(f'{len(self.flashcards)} cards have been saved.')

    def import_from_json(self, file_name):
        with open(file_name, 'r') as file:
            flashcards_to_add = json.load(file)
            self.flashcards = self.flashcards | flashcards_to_add
        print(f'{len(flashcards_to_add)} cards have been loaded.')




def main():
    flashcards_base = FlashcardsBase()

    # number_of_cards = input('Input the number of cards:\n')
    # flashcards_base.card_limit = int(number_of_cards)
    while True:
        print('Input the action (add, remove, import, export, ask, exit):')
        action = input()
        match action.lower():
            case 'add':
                # add one card
                print(f'The card:')
                while True:
                    card = input()
                    if flashcards_base.check_card(card):
                        print(f'The term "{card}" already exists. Try again:')
                        continue
                    break
                print(f'The definition of the card:')
                while True:
                    definition = input()
                    if flashcards_base.check_definition(definition):
                        print(f'The definition "{definition}" already exists. Try again:')
                        continue
                    break
                flashcards_base.add_flashcard(card, definition)
                continue
            case 'remove':
                print(f'Which card?')
                while True:
                    card = input()
                    if flashcards_base.check_card(card):
                        flashcards_base.remove_flashcard(card)
                        print('The card has been removed.')
                        break
                    print(f'Can\'t remove "{card}": there is no such card.')
                    break
                continue
            case 'import':
                # TODO import from jason
                # If there is no file with such name, print the message File not found.
                file_name = input('File name:')
                if not os.path.exists(file_name):
                    print('File not found.')
                else:
                    flashcards_base.import_from_json(file_name)
                continue


            case 'export':
                # TODO export to json
                file_name = input('File name:')
                flashcards_base.export_to_json(file_name)
                continue

            case 'ask':
                print('How many times to ask?')
                number_of_questions = int(input())
                for i in range(number_of_questions):
                    print('losowanie1')
                    actual_flash_card = flashcards_base.return_random_flashcard_data()
                    print('losowanie2')
                    print(f'Print the definition of "{actual_flash_card}":')
                    user_answer = input()
                    if user_answer == actual_flash_card[1]:
                        print('Correct!')
                    else:
                        if flashcards_base.check_definition(user_answer):
                            print(f'Wrong. The right answer is "{actual_flash_card[1]}"', end='')
                            print(
                                f' but your definition is correct for {flashcards_base.return_flashcard_card_from_definition(user_answer)}.')
                        else:
                            print(f'Wrong. The right answer is "{actual_flash_card[1]}"')
                continue

            case 'exit':
                print('Bye bye!')
                break


if __name__ == "__main__":
    main()

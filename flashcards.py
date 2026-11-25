# Write your code here
import random
import json
import os
import io
import sys
import builtins

class LoggerIO():
    def __init__(self):
        self.log = io.StringIO()

    def logged_input(self, prompt=''):
        result = input(prompt)
        self.log.write(prompt)
        self.log.write(result + '\n')
        return result

    def logged_print(self, output):
        print(output)
        self.log.write(str(output) + '\n')

    def save_log(self, filename):
        with open(filename, 'w') as f:
            f.write(self.log.getvalue())

    def logg_close(self):
        self.log.close()

class FlashcardsBase:
    def __init__(self):
        self.flashcards = {}
        self.card_limit = 10

    def add_flashcard(self, card, definition):
        self.flashcards[card] = {'definition': definition, 'mistakes': 0}

    def remove_flashcard(self, card):
        del self.flashcards[card]

    def return_flashcard_data(self, card):
        return card, self.flashcards[card]['definition'], self.flashcards[card]['mistakes']

    def check_card(self, card):
        return card in self.flashcards

    def check_definition(self, definition):
        return definition in [x['definition'] for x in self.flashcards.values()]

    def return_flashcard_card_from_definition(self, definition):
        for key,value in self.flashcards.items():
            if value['definition'] == definition:
                return key
        return None

    def return_random_flashcard_data(self):
        random_key = random.choice(list(self.flashcards.keys()))
        return random_key, self.flashcards[random_key]

    def export_to_json(self, file_name):
        with open(file_name, 'w') as file:
            json.dump(self.flashcards, file)


    def import_from_json(self, file_name):
        with open(file_name, 'r') as file:
            flashcards_to_add = json.load(file)
            self.flashcards = self.flashcards | flashcards_to_add

        return len(flashcards_to_add)

    def reset_stats(self):
        for flashcard in self.flashcards.values():
            flashcard['mistakes'] = 0

    def return_hardest_card_tuple(self):
        list_of_hardest_cards = []
        hardest_card_score = None
        for flashcard_item in self.flashcards.items():
            if hardest_card_score is None or flashcard_item[1]['mistakes'] > hardest_card_score:
                hardest_card_score = flashcard_item[1]['mistakes']
                list_of_hardest_cards = [flashcard_item[0]]
            elif flashcard_item[1]['mistakes'] == hardest_card_score:
                list_of_hardest_cards.append(flashcard_item[0])
        return list_of_hardest_cards, hardest_card_score

def main():
    flashcards_base = FlashcardsBase()
    logg = LoggerIO()


    # number_of_cards = input('Input the number of cards:\n')
    # flashcards_base.card_limit = int(number_of_cards)
    while True:
        logg.logged_print('Input the action (add, remove, import, export, ask, exit, log, hardest card, reset stats):')
        action = logg.logged_input()
        match action.lower():
            case 'log':
                file_name = logg.logged_input('File name:')
                logg.save_log(file_name)
                logg.logged_print('The log has been saved.')
                continue

            case 'add':
                # add one card
                logg.logged_print(f'The card:')
                while True:
                    card = logg.logged_input()
                    if flashcards_base.check_card(card):
                        logg.logged_print(f'The term "{card}" already exists. Try again:')
                        continue
                    break
                logg.logged_print(f'The definition of the card:')
                while True:
                    definition = logg.logged_input()
                    if flashcards_base.check_definition(definition):
                        logg.logged_print(f'The definition "{definition}" already exists. Try again:')
                        continue
                    break
                flashcards_base.add_flashcard(card, definition)
                logg.logged_print(f'The pair ("{card}":"{definition}") has been added.')
                continue

            case 'remove':
                logg.logged_print(f'Which card?')
                while True:
                    card = logg.logged_input()
                    if flashcards_base.check_card(card):
                        flashcards_base.remove_flashcard(card)
                        logg.logged_print('The card has been removed.')
                        break
                    logg.logged_print(f'Can\'t remove "{card}": there is no such card.')
                    break
                continue
            case 'import':
                # TODO import from jason
                # If there is no file with such name, print the message File not found.
                file_name = logg.logged_input('File name:')
                if not os.path.exists(file_name):
                    logg.logged_print('File not found.')
                else:
                    load_cards_number = flashcards_base.import_from_json(file_name)
                    logg.logged_print(f'{load_cards_number} cards have been loaded.')
                continue


            case 'export':
                # TODO export to json
                file_name = logg.logged_input('File name:')
                flashcards_base.export_to_json(file_name)
                logg.logged_print(f'{len(flashcards_base.flashcards)} cards have been saved.')
                continue

            case 'ask':
                logg.logged_print('How many times to ask?')
                number_of_questions = int(logg.logged_input())
                for i in range(number_of_questions):
                    actual_flash_card = flashcards_base.return_random_flashcard_data()
                    logg.logged_print(f'Print the definition of "{actual_flash_card[0]}":')
                    user_answer = logg.logged_input()
                    if user_answer == actual_flash_card[1]['definition']:
                        logg.logged_print('Correct!')
                    else:
                        if flashcards_base.check_definition(user_answer):
                            logg.logged_print(f'Wrong. The right answer is "{actual_flash_card[1]['definition']} but your definition is correct for {flashcards_base.return_flashcard_card_from_definition(user_answer)}.')
                        else:
                            logg.logged_print(f'Wrong. The right answer is "{actual_flash_card[1]['definition']}"')
                        flashcards_base.flashcards[actual_flash_card[0]]['mistakes'] += 1
                continue

            case 'reset stats':
                flashcards_base.reset_stats()
                logg.logged_print('Card statistics have been reset.')
                continue

            case 'hardest card':
                list, score = flashcards_base.return_hardest_card_tuple()
                if not score:
                    logg.logged_print('There are no cards with errors.')
                else:
                    if len(list) == 1:
                        logg.logged_print(f'The hardest card is "{list[0]}". You have {score} errors answering it.')
                    elif len(list) > 1:
                        logg.logged_print(f'The hardest cards are "{", ".join(list)}". You have {score} errors answering them.')

                continue

            case 'exit':
                logg.logged_print('Bye bye!')
                break
    logg.logg_close()

if __name__ == "__main__":
    main()


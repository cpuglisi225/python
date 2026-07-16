"""
Diceware Passphrase Generator

A small tool to generate passphrases using Diceware wordlists.
Randomness is provided by Python's secrets module.

Wordlists used:
- EFF Large Wordlist (English)
- Tarin Gamberini Diceware Italian Wordlist (Italian)

Sources:
https://www.eff.org/files/2016/07/18/eff_large_wordlist.txt
https://www.taringamberini.com/downloads/diceware_it_IT/lista-di-parole-diceware-in-italiano/4/word_list_diceware_it-IT-4.txt

"""
import secrets
from pathlib import Path
import os


WIDTH = 40
LINE = '=' * WIDTH

WORDLIST_PATH = Path(__file__).resolve().parent /'wordlists'

MIN_WORDS = 2
MAX_WORDS = 20
DICE_ROLLS = 5

LANGUAGES = {
    "en": {
        "name": "English",
        "file": "eff_large_wordlist.txt"
    },
    "it": {
        "name": "Italian",
        "file": "it_tarin_gamberini.txt"
    }
}

def print_banner():
    print(LINE)
    print('D I C E W A R E'.center(WIDTH))
    print('Passphrase Generator'.center(WIDTH))

def print_menu_options():
    print(LINE)
    print('Available languages:')

    for lang_code, lang_info in LANGUAGES.items():
        print(f'  [{lang_code}] {lang_info["name"]}')

    print()
    print('Mixed:')
    print('  [en+it] English + Italian')

    print()
    print('Exit:')
    print('  [q] Quit')

    print(LINE)
    
def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def get_words_count():
    while True:
        words_number = input('Number of words: ').strip()

        try:
            words_number = int(words_number)

            if MIN_WORDS <= words_number <= MAX_WORDS:
                return words_number
            else:
                print(f'Please enter a number between {MIN_WORDS} and {MAX_WORDS}.')

        except ValueError:
            print('Invalid number, try again.')

def get_menu_option():

    print_menu_options()
    valid_options = set(LANGUAGES.keys()) | {'en+it', 'q'}
    while True:
        selected_option = input('Choice: ').strip().lower()
        if selected_option == 'it+en':
            selected_option = 'en+it'
        if selected_option in valid_options:
            return selected_option 
        else:
            print('Invalid choice, try again.') 

def get_separator():

    while True:
        separator = input("Separator (press Enter for none): ")

        if separator == "":
            return ""
        if len(separator) > 5:
            print("Separator too long (max 5 characters).")
            continue
        for char in separator:
            if char.isalnum():
                print("Separator cannot contain letters or digits.")
                break
        else:
            return separator

def load_wordlist(selected_lang: str) -> dict:

    wordlist_path = WORDLIST_PATH / LANGUAGES[selected_lang]["file"]

    wordlist_dict = {}

    try:
        with open(wordlist_path, 'r', encoding='utf-8') as f:
            for line in f:
                code, word = line.split()
                wordlist_dict[code] = word

    except FileNotFoundError:
        print(f'Wordlist not found: {wordlist_path}')

    except PermissionError:
        print(f'Permission denied: {wordlist_path}')

    except ValueError:
        print(f'Invalid wordlist format: {wordlist_path}')

    return wordlist_dict

def roll_dice_code ():
    dice_code = ''
    for _ in range(DICE_ROLLS):
        dice = secrets.randbelow(6)+1
        dice_code += str(dice)
    return dice_code

def get_word(code, wordlist_dict):
    return wordlist_dict.get(code, '[missing word]')

def generate_passphrase(wordlists, words_count, separator):
    passphrase = []

    for _ in range(words_count):
        wordlist = secrets.choice(wordlists)
        code = roll_dice_code()
        passphrase.append(get_word(code, wordlist))

    return separator.join(passphrase)
     
def print_passphrase(passphrase):
    print(LINE)
    print(f'\nPASSPHRASE: {passphrase}\n')
    print(LINE)


while True:
    print_banner()
    selected_option = get_menu_option()

    
    if selected_option == 'q':
        print('Goodbye!')
        break

    words_count = get_words_count()
    separator = get_separator()

    if selected_option == 'en+it':
            wordlists= [load_wordlist('en'), load_wordlist('it')]
    else:
        wordlists = [
            load_wordlist(selected_option)
        ]      
    passphrase = generate_passphrase(wordlists, words_count, separator)
    print_passphrase(passphrase)
    input('Press Enter to continue...')
    clear_screen()
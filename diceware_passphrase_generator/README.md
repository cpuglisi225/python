# Diceware Passphrase Generator

A simple Python program that generates passphrases using the Diceware method.

The program uses the Python `secrets` module to generate secure random dice rolls
and select words from Diceware wordlists.

## Features

- Generate passphrases with a custom number of words
- Choose between:
  - English wordlist
  - Italian wordlist
  - Mixed English + Italian wordlist
- Choose a custom separator between words
- Uses only Python standard library modules

## How it works

Each word is selected by generating a 5-digit dice code.

Example:

```text
35216 → corresponding word in the Diceware list
```

The generated words are then combined to create the final passphrase.

## Wordlists

The project uses the following wordlists:

- EFF Large Wordlist (English)  
  https://www.eff.org/files/2016/07/18/2/english.txt

- Tarin Gamberini Diceware Italian Wordlist  
  https://www.taringamberini.com/downloads/diceware_it_IT/lista-di-parole-diceware-in-italiano/4/word_list_diceware_it-IT-4.txt

## Project structure

```text
diceware/
│
├── main.py
├── wordlists/
│   ├── eff_large_wordlist.txt
│   └── it_tarin_gamberini.txt
├── README.md
└── requirements.txt
```
## Example

Example of generated passphrase:

```text
========================================
            D I C E W A R E             
          Passphrase Generator          
========================================
Select wordlist language:
1) English
2) Italian
3) Mixed (English + Italian)
0) Exit
========================================
Select an option: 1
Number of words: 6
Separator (press Enter for none): -
========================================
passphrase='badass-falsify-whimsical-pushing-counting-serotonin'
```

The output will be different every time because each word is selected using secure random generation.
## Security notes

The generator follows the Diceware method:

- Each word is selected using a 5-dice roll code (`6⁵ = 7776` possible combinations).
- Randomness is generated using Python's `secrets` module.
- The total entropy increases with the number of words used in the passphrase.

Example:

```text
5 words ≈ 64 bits of entropy
6 words ≈ 77 bits of entropy
```

Using multiple wordlists can further increase the number of possible combinations.


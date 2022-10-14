from colorama import Fore, Back, Style
import pandas

morse_dict = pandas.read_csv("morse.csv")
phonetic_dict = {row.letter: row.code for (index, row) in morse_dict.iterrows()}

def text_to_morse():
    word = input(Fore.RESET + 'Input Your Message: ').upper()
    try:
        output_list = [phonetic_dict[letter] for letter in word]
    except KeyError:
        print(Fore.RED + "Please only input english Alpha-Numeric Characters")
        text_to_morse()
    else:
        message = ' '.join(output_list)
        print(message)
if __name__ == '__main__':
    text_to_morse()


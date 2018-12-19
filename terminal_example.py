from src.BinConvert import binary_to_string, string_to_binary
from os import system as syscmd #Stands for 'system command', the library was renamed as the below would have raised errors.
from platform import system
from time import sleep
from pyperclip import copy

def clear_terminal():
    '''
    Checks the operating system and clears the terminal depending
    on your operating system.
    '''
    if system() == 'Windows':
        syscmd('cls')
    else: syscmd('clear')

def main():
    run = True
    logo = """
    ___  _      _____                      __
   / _ )(_)__  / ___/__  ___ _  _____ ____/ /_
  / _  / / _ \\/ /__/ _ \\/ _ \\ |/ / -_) __/ __/
 /____/_/_//_/\\___/\\___/_//_/___/\\__/_/  \\__/"""

    while run:
        print(logo, '\n\nText will automatically copy to your clipboard!\nASCII Art is not supported!', "\n\n1) Convert text to binary code\n2) Convert binary code to text\nq) Quit\n\n")
        user_input = input('Enter: ')

        if user_input == '1':
            clear_terminal()
            print("\nEnter the text you'd like to encode below.\n")
            text_string = input('Enter: ')
            clear_terminal()
            '''
            The BinConv functions will raise an error if the characters are not supported. If the
            BinConv funtions raise an error then it displays a message to the user letting them
            know the characters they have entered are not supported.
            '''
            try:
                encoded_string = string_to_binary(text_string)
                copy(encoded_string)
            except:
                print('Sorry, but an ASCII character or a binary byte you have given this program is not supported.')
            print(f"\nYour encoded message is:\n\n{encoded_string}")
            sleep(4)
            clear_terminal()

        elif user_input == '2':
            clear_terminal()
            print("\nEnter the binary code you'd like to decode below.\n")
            binary_string = input('Enter: ')
            clear_terminal()
            try:
                decoded_string = binary_to_string(binary_string)
                copy(decoded_string)
            except:
                print('Sorry, but an ASCII character or a binary byte you have given this program is not supported.')
            print(f"\nYour encoded message is:\n\n{decoded_string}")
            sleep(4)
            clear_terminal()

        elif user_input == 'q':
            clear_terminal()
            print('\n(¯`·._.·(¯`·._.· Goodbye ·._.·´¯)·._.·´¯)')
            sleep(1)
            run = False

        else:
            clear_terminal()
            print(f'{user_input} is not a valid entry.')
            sleep(2)
            clear_terminal()

if __name__ == '__main__':
    main()

#THIS IS THE PROTOTYPE VERSION

#Importing the the 'system' module from os and 'platform.system', for the 'ClearTerminal' function
from os import system as syscmd
from platform import system

CharList = []
BinList = []
def BinToDec(Bin):
    # The binary string is split into a list of string bits so they can be converted from string to integer.
    BinaryStr = list(Bin)
    BinaryStr = [int(bit) for bit in BinaryStr]

    Dec = 0
    Pow  = 7
    ''' Every bit is run through this simple little formula, adding all the sums of the bits returns
    the ASCII decimal. The decimal is then added to list so we can combine it later on to form a string. '''
    for bit in BinaryStr:
        Dec += bit*2**Pow
        Pow -= 1
    CharList.append(chr(Dec))

def DecToBin(Dec):

    Dec = int(Dec)
    BinaryStr = []
    ''' Here I run the decimal through modulus condition 8 times (for every bit in a 8-bit binary code),
    depending if the decimal returns a remainder or not I add '1' or '0' to a list respectivly.
    This list of bits is inverted in the list so it is reversed, the list is joined
    together to form an 8-bit binary string (e.g.'01000001') and added to another list so it can
    later be joined (seperated by a whitespace) and printed on screen.'''
    for bit in range(8):
        if Dec % 2 == 0:
            Dec /= 2
            BinaryStr.append('0')
        else:
            Dec //= 2
            BinaryStr.append('1')
    BinaryStr.reverse()
    BinList.append(''.join(BinaryStr))

def StrToDec(String):
    ''' The string is split into a list so I can run it through a for loop, the characters
    in the list are converted into its decimal counterpart so we can run it through a function.'''
    String = list(String)

    for char in String:
        Dec = ord(char)
        DecToBin(Dec)

def BinSnipper(BinStr):
    BinStr = BinStr.split(" ")

    for Bin in BinStr:
        BinToDec(Bin)

def ClearTerminal():
    if system() == 'Windows':
        syscmd('cls')
    else: syscmd('clear')

def main():

    while True:
        print("1) Convert Text to Binary\n2) Convert Binary to Text\nq) Quit\n")
        UserInput = input("Enter: ")

        if UserInput == '1':
            ClearTerminal()
            print("Enter the text you would like to encode.\n")
            StrToDec(input("Enter: "))
            print('\n', ' '.join(BinList), '\n')
            BinList.clear()

        elif UserInput == '2':
            ClearTerminal()
            print("Enter the binary code you would like to decode\n")
            BinSnipper(input("Enter: "))
            print('\n', ''.join(CharList), '\n')
            CharList.clear()

        elif UserInput == 'q':
            print("Exiting...")
            break
        else:
            print("{Uin} is not a valid option.".format(Uin=UserInput))


if __name__ == '__main__':
    main()

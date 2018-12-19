class BinaryConverter():
    def __init__(self, text=None, binary=None):
        self.text = text
        self.binary = binary

    def text_to_binary(self):
        binary_list = []
        self.text = list(self.text)

        '''
        The string is split into a list so I can run it through a for loop, the characters
        in the list are converted into its decimal counterpart so it can run through another
        for loop that requires integers.
        '''

        for character in self.text:
            decimal = ord(character)
            decimal = int(decimal)
            binary_string = []
            '''
            Here the decimal runs through a modulus condition 8 times (for every bit in a byte
            (8-bits)). Depending if the decimal returns a remainder or not, it will add '1' or
            '0' to a list respectivly. This list of bits is actually inverted in the list, so
            the list is reversed. The list is then joined together to form a byte (e.g.'01000001')
            and added to another list so it can later be joined (seperated by a whitespace).
            '''

            for bit in range(8):
                if decimal % 2 == 0:
                    decimal /= 2
                    binary_string.append('0')
                else:
                    decimal //= 2
                    binary_string.append('1')
            binary_string.reverse()
            binary_list.append(''.join(binary_string))
        return ' '.join(binary_list)
        binary_list.clear()

    def binary_to_text(self, *args):
        character_list = []
        self.binary = self.binary.split(" ")

        for byte in self.binary:
            byte = list(byte)
            byte = [int(string_bit) for string_bit in byte]

            decimal = 0
            power_of = 7

            '''
            Every bit is run through this simple little formula, adding all the sums of the bits returns
            the ASCII decimal. The decimal is then added to list so we can combine it to form a string.
            '''

            for bit in byte:
                decimal += bit*2**power_of
                power_of -= 1
            character_list.append(chr(decimal))
        return ''.join(character_list)
        character_list.clear()

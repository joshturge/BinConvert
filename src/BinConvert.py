def decimal_check(decimal):
    '''
    Checks the ASCII charcter decimal to make sure it's in the range of 32 to 126.
    This is done so there are no invalid characters in the output. This function
    should only be called by "text_to_binary()" and "binary_to_text()".
    '''
    if decimal < 32 or decimal > 126:
        raise Exception('ASCII character decimal is not supported')

def string_to_binary(string):
    binary_list = []
    string = list(string)
    '''
    The string is split into a list so I can run it through a for loop, the characters
    in the list are converted into its decimal counterpart so it can run through another
    for loop that requires integers.
    '''
    for character in string:
        decimal = ord(character)
        decimal_check(decimal)
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

def binary_to_string(binary_string):
    character_list = []
    binary_string = binary_string.split(" ")

    for byte in binary_string:
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
        decimal_check(decimal)
        character_list.append(chr(decimal))
    return ''.join(character_list)

from src.BinConv import binary_to_string, string_to_binary

binary_message = ("01010000 01100001 01101110 01100011 01100001 01101011 01100101 "
                  "01110011 00100000 01100001 01110010 01100101 00100000 01100001 "
                  "01101101 01100001 01111010 01101001 01101110 01100111 00101110")

text_string = 'Hello World!'


print('Binary to Text:\t' + BinConvert.binary_to_string(binary_message) + '\n')
print('Text to Binary:\t' + BinConvert.string_to_binary(text_string) + '\n')

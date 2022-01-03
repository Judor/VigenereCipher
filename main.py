import optparse


def encrypt(text, key):
    text = text.upper()
    key = key.upper()
    key_length = len(key)
    int_key = [ord(i) for i in key]
    int_text = [ord(i) for i in text]
    encoded_text = ''
    for i in range(len(int_text)):
        value = (int_text[i] + int_key[i % key_length]) % 26
        encoded_text += chr(value + 65)
    return encoded_text


def decrypt(encoded_text, key):
    encoded_text = encoded_text.upper()
    key = key.upper()
    key_length = len(key)
    int_key = [ord(i) for i in key]
    encoded_int_text = [ord(i) for i in encoded_text]
    text = ''
    for i in range(len(encoded_int_text)):
        value = (encoded_int_text[i] - int_key[i % key_length]) % 26
        text += chr(value + 65)
    return text


if __name__ == "__main__":
    # create OptionParser object
    parser = optparse.OptionParser()
    parser.add_option('-e', dest='encrypt', action='store_true',
                      help='Calls the encrypt function. usage : -e text key')
    parser.add_option('-d', dest='decrypt', action='store_true',
                      help='Calls the decrypt function. usage : -d text key')

    (options, args) = parser.parse_args()

    if options.encrypt:
        text = input("Please type the text to encrypt: ")
        key = input("Please type your encryption key: ")
        print('The encrypted text is : ' + encrypt(text, key))
    elif options.decrypt:
        text = input("Please type the text to encrypt: ")
        key = input("Please type your encryption key: ")
        print('The decrypted text is : ' + decrypt(text, key))
    else:
        raise Exception('One argument was needed. Type python main.py -h for more help about the usage')

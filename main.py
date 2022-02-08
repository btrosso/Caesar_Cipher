alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

#testing the functionality of the index method
# index = alphabet.index('d')
# print(index)

def encrypt(text, shift):
    text_list = list(text)
    i = 0
    for char in text_list:
        index = alphabet.index(char)
        shifted_index = index + shift
        if shifted_index > 25:
            index = shifted_index - 26
            text_list[i] = alphabet[index]
        else:
            text_list[i] = alphabet[index + shift]
        i += 1
    text_list = ''.join(text_list)      
    print(text_list)

encrypt(text=text, shift=shift)